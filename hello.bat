@echo off

7z a -tzip hello.zip hello.py
aws lambda update-function-code --function-name api-private-hello --zip-file fileb://hello.zip --output table
del hello.zip
