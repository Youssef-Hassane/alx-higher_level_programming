#!/usr/bin/node
// code made by : youssef
const data = require('./100-data').list;
console.log(data);
console.log(data.map((e, idx) => e * idx));
