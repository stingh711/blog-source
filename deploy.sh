#!/bin/bash
make publish
cd output
git add .
git commit -m "update"
git push
