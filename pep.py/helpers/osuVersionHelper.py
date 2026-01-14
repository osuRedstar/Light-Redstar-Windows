import re, datetime, requests

from constants import exceptions

OSU_VERSION = re.compile(
    r"^b(?P<date>\d{8})(?:\.(?P<revision>\d+))?"
    r"(?P<stream>beta|cuttingedge|dev|tourney|ce45)?$", #ce45 == cuttingedge
)

class OsuVersion:
    def __init__(self, date: datetime.date, revision: int, stream: str) -> None:
        self.date = date
        self.revision = revision
        self.stream = stream

def parse_osu_version_string(osu_version_string: str) -> OsuVersion:
    match = OSU_VERSION.match(osu_version_string)
    if match is None: return None

    return OsuVersion(
        date=datetime.date(
            year=int(match["date"][0:4]),
            month=int(match["date"][4:6]),
            day=int(match["date"][6:8]),
        ),
        revision=int(match["revision"]) if match["revision"] else None,
        stream=match["stream"] or "stable",
    )

def get_allowed_client_versions(osu_stream: str) -> set:
    """
    Return a list of acceptable client versions for the given stream.

    This is used to determine whether a client is too old to connect to the server.

    Returns None if the connection to the osu! api fails.
    """
    if osu_stream in ("stable", "beta"):  osu_stream += "40"  # i wonder why this exists

    osuallowver = set()
    for b in requests.get(f"https://osu.ppy.sh/api/v2/changelog?stream={osu_stream}").json()["builds"]:
        version = datetime.date(
            int(b["version"][0:4]),
            int(b["version"][4:6]),
            int(b["version"][6:8]),
        )
        osuallowver.add(version)
        if any(entry["major"] for entry in b["changelog_entries"]):
            # this build is a major iteration to the client
            # don't allow anything older than this
            break
    return osuallowver

def isNeedUpdate(osu_version_string: str) -> None:
    povs = parse_osu_version_string(osu_version_string)
    if not povs: raise exceptions.unknownClientException()
    gacv = get_allowed_client_versions(povs.stream)
    if not povs.date in gacv: raise exceptions.forceUpdateException()