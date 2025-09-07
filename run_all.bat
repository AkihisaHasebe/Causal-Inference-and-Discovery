@echo off
REM Run create_dataset.py
python create_dataset.py
IF ERRORLEVEL 1 (
    echo create_dataset.py failed.
    exit /b 1
)

REM Run lingam_example.py
python lingam_example.py
IF ERRORLEVEL 1 (
    echo lingam_example.py failed.
    exit /b 1
)

echo Both scripts executed successfully.