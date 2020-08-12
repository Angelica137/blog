import os
sys.path.append(os.getswd())
from main import db


if __name__ == '__main__':
    db.create_all()