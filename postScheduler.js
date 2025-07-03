const fs = require('fs');
const config = require('./config.json');
const { getTrendingKeywords } = require('./trendScanner');

let messages = [];
try {
  const raw = fs.readFileSync('./shillMessages.json', 'utf8');
  messages = JSON.parse(raw);
} catch (err) {
  console.error('Error loading shill messages:', err);
}

function getRandomItem(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function buildMessage() {
  const template = getRandomItem(messages) || 'Buy {keyword} now!';
  const keywords = config.keywords.concat(getTrendingKeywords());
  const keyword = getRandomItem(keywords);
  return template.replace('{keyword}', keyword);
}

function startShilling(interval = config.defaultInterval) {
  const scheduleNext = () => {
    const randomOffset = Math.random() * interval * 1000;
    const delay = interval * 1000 + randomOffset;
    setTimeout(() => {
      const message = buildMessage();
      console.log(`\u{1F525} Shilling: ${message}`);
      scheduleNext();
    }, delay);
  };
  scheduleNext();
}

module.exports = { startShilling };
