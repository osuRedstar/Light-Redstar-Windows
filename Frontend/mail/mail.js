//const btn = document.querySelector("#sendmail")
//const btn = document.querySelector("#sendmail")

//function getUser() {
//    const GETUSER = document.querySelector("#getuser")
//    //const email = 
//}

//btn.addEventListener("click", getUser)

const username = "INPUT username"
const beatmapID = "INPUT beatmapID"
const reason = "INPUT Reason for sending mail"

query = `a`

const nodemailer = require('nodemailer')

var transporter = nodemailer.createTransport({
    service: 'daum', // gmail, naver, nate 등
    host: 'smtp.daum.net',
    port: 465,
    auth: {
        user: 'support@redstar.moe',
        pass: 'skchqhdpdy0113'
    }
});
var mailOptions = {
    from: `'RedstarOSU! Team' <support@redstar.moe>`,
    to: 'jeonkangheun@gmail.com',
    subject: `${username} Nodejs sendMail Test`,
    //text: 'asdf'
    html: query
};

transporter.sendMail(mailOptions, function(error, info) {
    if (error) {
        console.log(error);
    } else {
        console.log('Email sent success! : ' + info.response);
    }

    //#4. 전송 후 결과 단순 출력
    for(let key in info){  
        console.log('키 : '+key + ', 값 : ' + info[key])
    }

    transporter.close();
});
