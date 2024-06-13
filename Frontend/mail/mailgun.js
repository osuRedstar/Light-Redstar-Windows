const mailgun = require("mailgun-js");
const DOMAIN = 'pwreset.redstar.moe';

const api_key = '5fa329a705a1e375662911439a4f84c3-787e6567-79f33f63';

const mg = mailgun({apiKey: api_key, domain: DOMAIN});
const data = {
	from: 'RedstarOSU! <support@pwreset.redstar.moe>',
	to: 'jeonkangheun@gmail.com',
	subject: 'Hello',
	text: 'Testing some Mailgun awesomness!'
};
mg.messages().send(data, function (error, body) {
	console.log(body);
});