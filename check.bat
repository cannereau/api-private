@echo off

rem install requests package
pip install requests

rem use 7zip to build package
7z a -tzip check.zip check.py
7z a -tzip -r check.zip certifi
7z a -tzip -r check.zip chardet
7z a -tzip -r check.zip idna
7z a -tzip -r check.zip requests
7z a -tzip -r check.zip urllib3

rem update Lambda code with AWS CLI
aws lambda update-function-code --function-name api-private-check --zip-file fileb://check.zip --output table

rem remove package
del check.zip
