#!/usr/bin/env bash

echo "Building docker container"
docker build -t reido/climove .
echo "Finished building docker container"

echo "Adding +x perms"
chmod +x runclimove.sh

echo "Removing link if exists"
rm -f $HOME/bin/runclimove
rm -f $HOME/bin/climove
echo "Linking to $HOME/bin/runclimove"
ln -s `pwd`/runclimove.sh $HOME/bin/climove
echo "Finished install"
echo "usage: climove <src glob str> <dest dir>"