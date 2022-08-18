mkdir "%SRC_DIR%"
ROBOCOPY /E "%RECIPE_DIR%\..\src" "%SRC_DIR%"
copy "%RECIPE_DIR%\..\setup.py" "%SRC_DIR%\setup.py"
cd %SRC_DIR%

pip install .
if errorlevel 1 exit 1
