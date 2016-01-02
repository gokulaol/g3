#!/bin/bash


MONGODB="/usr/local/bin/mongod"
function start_mongo()
{
	cmd="$MONGODB --config /usr/local/etc/mongod.conf"
	echo $cmd
	$cmd
}

function start_server()
{
	./server.py -d 5
}

#start_server
start_mongo


