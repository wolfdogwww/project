# 登入畫面專案

### 資料來源

本專案透過以下來學習並且完成
[Flask實作_ext_01_Flask-SQLAlchemy_初探](https://hackmd.io/@shaoeChen/SJ9x3N9zz?type=view)

### 安裝

首先你需要在py的環境安裝flask 以及我所使用的Flask-SQLAlchemy

```
pip install flask 
pip install flask-sqlalchemy
```

### 檔案說明

main.py 主要是在做路由轉換以及調動資料的

在method資料夾底下的model.py是在做資料庫創建的 使用的是"Flask-SQLAlchemy"


### 安裝database

執行在 method資料夾底下的creat_db.py 就會引用model_user.py的資料庫格式自動創建資料庫

```python
from model_user import db, app  # 确保将 your_module_name 替换为包含上述代码的文件名（不包括 .py 后缀）

with app.app_context():
    db.create_all()
    print("All tables created")
```
