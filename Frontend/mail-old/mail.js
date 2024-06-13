//const btn = document.querySelector("#sendmail")
//const btn = document.querySelector("#sendmail")

//function getUser() {
//    const GETUSER = document.querySelector("#getuser")
//    //const email = 
//}

//btn.addEventListener("click", getUser)


const nodemailer = require('nodemailer')

var transporter = nodemailer.createTransport({
    service: 'daum', // gmail, naver, nate 등
    host: 'smtp.daum.net',
    port: 465,
    auth: {
        user: 'support@redstar.moe',
        pass: 'skchqhdpdy0113'
    },
    tls: {
        rejectUnauthorized: false
    }
});
var mailOptions = {
    from: `'RedstarOSU!' <support@redstar.moe>`,
    to: 'moudoc3921@gmail.com',
    subject: 'Nodejs sendMail Test',
    //text: 'asdf'
    html: '<h1>인증번호</h1><h2></h2>'
};

transporter.sendMail(mailOptions, function(error, info) {
    if (error) {
        console.log(error);
    } else {
        console.log('Email sent success! : ' + info.response);
    }
    transporter.close();
});