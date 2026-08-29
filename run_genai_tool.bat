@echo off
title NCERT Social Science GenAI Image Tool
echo ========================================================
echo   NCERT Social Science GenAI Image Automation Tool
echo ========================================================
echo.

if "%~1"=="" (
    echo Please enter the HTML file name (e.g. copy_master_hist4.html):
    set /p HTMLFILE=
) else (
    set HTMLFILE=%~1
)

echo Enter Subject (history / geography / civics / economics) [default: history]:
set /p SUBJECT=
if "%SUBJECT%"=="" set SUBJECT=history

echo Enter Chapter Number [default: 1]:
set /p CHAPTER=
if "%CHAPTER%"=="" set CHAPTER=1

echo.
echo Running GenAI Image Automation Tool...
python ncert_genai_automation_tool.py --html "%HTMLFILE%" --subject "%SUBJECT%" --chapter %CHAPTER%

echo.
echo ========================================================
echo Done! Open %HTMLFILE% in your browser to view the result.
echo ========================================================
pause
