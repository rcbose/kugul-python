ex.js
const fs = require('fs');
const https = require('https');
const url = require('url');

function readFileFromUrl(fileUrl) {
  try {
    const parsedUrl = new URL(fileUrl);

    if (parsedUrl.protocol !== 'https:' && parsedUrl.protocol !== 'http:') {
      console.log('Error: Only HTTP(S) protocols are supported.');
      return;
    }

    https.get(parsedUrl, (response) => {
      let fileContent = '';

      response.on('data', (chunk) => {
        fileContent += chunk;
      });

      response.on('end', () => {
        console.log('File content:');
        console.log(fileContent);

      });

    }).on('error', (error) => {
      console.error('Error fetching the file from the URL:', error.message);
    });
  } catch (error) {
    console.error('Error parsing the URL:', error.message);
  }
}

if (require.main === module) {
  if (process.argv.length !== 3) {
    console.log('Usage: node read_file_from_url.js <file_url>');
  } else {
    const fileUrl = process.argv[2];
    readFileFromUrl(fileUrl);
  }
}
