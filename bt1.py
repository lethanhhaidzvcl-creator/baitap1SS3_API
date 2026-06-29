from fastapi import FastAPI
app = FastAPI(
    title="Library API",
    description="API kiểm tra hệ thống và lấy danh sách sách",
    version="1.0.0"
)

# Dữ liệu mẫu
books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019
    }
]

@app.get("/")
def home():
    return {
        "message": "Welcome to Library API"
    }

# API kiểm tra hệ thống
@app.get("/health")
def health():
    return {
        "message": "Library API is running"
    }

# API lấy danh sách sách
@app.get("/books")
def get_books():
    return books