//Lab6 Assigment

//Importing required modules
const dns = require('dns');
const os = require("os");
const http = require('http');
const fs = require('fs');
const ip = require('ip');

//Creating server
http.createServer((req,res) => {
    if (req.url.match("/sysinfo")){
        myHostName = os.hostname();
        myIP = ip.address();

        serverUptime = os.uptime();
        days = parseInt(serverUptime/86400);
        serverUptime = (serverUptime - (days*86400));
        hours = parseInt(serverUptime/3600);
        serverUptime = (serverUptime - (hours*3600));
        minutes = parseInt(serverUptime/60);
        serverUptime = (serverUptime - (minutes*60));
        seconds = serverUptime;

        freeMem = os.freemem()/1000000;
        totalMem = os.totalmem()/1000000;
        cpus = os.cpus();
        countCPU = cpus.length;
        //HTML Page
        html=`
        <!DOCTYPE html>
        <html>
            <head>
                <title>Node JS Lab 6</title>
            </head>
            <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP Address: ${myIP}</p>
                <p>Server Uptime: ${days} days ${hours} hours ${minutes} minutes ${seconds} seconds</p>
                <p>Total Memory: ${totalMem} MB</p>
                <p>Free Memory: ${freeMem} MB</p>
                <p>CPUs: ${countCPU}</p>
            </body>
        </html>`
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server on port 3000. See /sysinfo for information");
