#!/bin/bash

while true;
  do clear;
  date;
  ps ax | grep python|grep test;
  echo;
  netstat -tulpan | grep 900;
  echo; 
  sleep 1;
done
