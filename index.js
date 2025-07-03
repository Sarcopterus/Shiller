require('dotenv').config();
const postScheduler = require('./postScheduler');
const config = require('./config.json');

function startBot() {
  console.log(`Modo del bot: ${process.env.BOT_MODE}`);
  postScheduler.startShilling(config.defaultInterval);
  console.log('✅ Shiller Bot listo para causar caos.');
}

startBot();
