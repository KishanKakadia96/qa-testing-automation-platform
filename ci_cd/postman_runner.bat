@echo off
cd /d "%~dp0..\testing\postman"
if not exist "..\..\api_automation\reports" mkdir "..\..\api_automation\reports"

echo Running Postman Collections...
newman run collections\QA-Testing.postman_collection.json 
-e environments\QA-Testing.postman_environment.json 
--reporters html,cli 
--reporter-html-export ..\..\api_automation\reports\postman_report.html

echo.
echo Report: api_automation\reports\postman_report.html
pause
