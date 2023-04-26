'''config.py'''

import os

BASE_DIR = os.path.dirname(__file__)

sqlite_path = os.path.join(BASE_DIR, 'csrf.db')

# DB 파일 생성 위치 및 파일명
SQLALCHEMY_DATABASE_URI = f'sqlite:///{sqlite_path}'

# 변경사항 추적 기능 -> 꺼둡니다. False 세팅
SQLALCHEMY_TRACK_MODIFICATIONS = False
