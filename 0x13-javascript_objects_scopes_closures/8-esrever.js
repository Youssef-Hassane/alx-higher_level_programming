#!/usr/bin/node
// code made by : youssef
exports.esrever = function (list) {
  const newArray = [];
  list.map(e => newArray.unshift(e));
  return newArray;
};
