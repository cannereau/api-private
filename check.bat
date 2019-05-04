@echo off

7z a -tzip check.zip check.py
7z a -tzip -r check.zip certifi
7z a -tzip -r check.zip chardet
7z a -tzip -r check.zip idna
7z a -tzip -r check.zip requests
7z a -tzip -r check.zip urllib3

aws lambda update-function-code --function-name api-private-check --zip-file fileb://check.zip --output table
del check.zip
