#!/usr/bin/node
// code made by : youssef
let count = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
