
mkdir "%SRC_DIR%"
ROBOCOPY /E "%RECIPE_DIR%\..\src" "%SRC_DIR%"
# ROBOCOPY /E "%RECIPE_DIR%\..\test" "%SRC_DIR%\test"
copy "%RECIPE_DIR%\..\setup.py" "%SRC_DIR%\setup.py"
cd %SRC_DIR%

%PYTHON% setup.py install --single-version-externally-managed --record record.txt
if errorlevel 1 exit 1
