const redstar_userid = document.getElementById("redstaruserid");
const bancho_userid = document.getElementById("banchouserid");
const bancho_username = document.getElementById("banchousername");

function RedstarUserId(arg) {
    //arg.preventDefault();
    const get_id = prompt("당신의 Redstar ID를 적어주세요! \nPlease write down your Redstar ID!")
    if (get_id === null) {
        alert("정확하게 입력하세요! \nPlease enter it correctly!");
        get_id = "";
        location.reload(true);
    }
    else if (isNaN(get_id) === true) {
        alert("당신의 ID(숫자)를 입력하세요! \nEnter your ID (number)!")
        location.reload(true);
    }
    redstar_userid.href = `https://a.redstar.moe/${get_id}`

}

function BanchoUserId(arg) {
    //arg.preventDefault();
    const get_id = prompt("당신의 Bancho ID를 적어주세요! \nPlease write down your Bancho ID!")
    if (get_id === null) {
        alert("정확하게 입력하세요! \nPlease enter it correctly!");
        get_id = "";
        location.reload(true);
    }
    else if (isNaN(get_id) === true) {
        alert("당신의 ID(숫자)를 입력하세요! \nEnter your ID (number)!")
        location.reload(true);
    }
    bancho_userid.href = `https://a.redstar.moe/bancho/id/${get_id}`

}

function BanchoUserName(arg) {
    //arg.preventDefault();
    const get_id = prompt("당신의 Bancho Name를 적어주세요! \nPlease write down your Bancho Name!")
    if (get_id === null) {
        alert("정확하게 입력하세요! \nPlease enter it correctly!");
        get_id = "";
        location.reload(true);
    }
    bancho_username.href = `https://a.redstar.moe/bancho/u/${get_id}`

}

redstar_userid.addEventListener("click", RedstarUserId);
bancho_userid.addEventListener("click", BanchoUserId);
bancho_username.addEventListener("click", BanchoUserName);