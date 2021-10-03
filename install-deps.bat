SET SUB_DIR_PATH=%1

IF "%SUB_DIR_PATH%" == "" (
    SET SUB_DIR_PATH=.
)


python -m pip install PIP SetUpTools --upgrade --user

python -m pip install -r %SUB_DIR_PATH%\requirements.txt --upgrade --user
