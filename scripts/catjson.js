var fs = require('fs');
var file = '/tmp/speedtest.json';
 
fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.log('Error: ' + err);
    return;
  }
 
  data = JSON.parse(data);

  data.sort(function(a,b){return a.timestamp-b.timestamp});
 
  console.log("timestamp, latency, download_speed, upload_speed");
  data.forEach(function(d) { console.log(d.timestamp + "," + d.latency + "," + d.download_speed + "," + d.upload_speed); });
});
