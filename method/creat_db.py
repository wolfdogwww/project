from model_user import db, app  # 确保将 your_module_name 替换为包含上述代码的文件名（不包括 .py 后缀）

with app.app_context():
    db.create_all()
    print("All tables created")