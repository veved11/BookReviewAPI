# BookReviewAPI

Book Review API built using Django REST Framework (DRF).

---

## Project Features

- User Registration
- JWT Authentication
- Change Password
- Book Management
- Review Management
- Swagger Documentation
- Admin Dashboard

---

## Technologies Used

- Python 3
- Django
- Django REST Framework
- Simple JWT Authentication
- SQLite3
- drf-yasg (Swagger)

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/register/` | Register new user |
| POST | `/api/token/` | Login and get JWT token |
| POST | `/api/token/refresh/` | Refresh token |
| POST | `/api/change-password/` | Change password |

---

### Books

| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/books/` | List all books |
| POST | `/api/books/` | Add new book (Admin only) |
| GET | `/api/books/<id>/` | Retrieve book details |
| PUT | `/api/books/<id>/` | Update book |
| DELETE | `/api/books/<id>/` | Delete book |

---

### Reviews

| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/books/<book_id>/reviews/` | Get all reviews |
| POST | `/api/books/<book_id>/reviews/` | Add review |
| PUT | `/api/reviews/<id>/` | Edit review |
| DELETE | `/api/reviews/<id>/` | Delete review |

---

## Authentication

This project uses JWT Authentication.

Login endpoint:

POST `/api/token/`

Use token in headers:

Authorization: Bearer your_token

---

## Swagger Documentation

Swagger UI:

http://127.0.0.1:8000/swagger/

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/veved11/BookReviewAPI.git
2. Install Requirements
pip install -r requirements.txt
3. Run Server
python manage.py runserver


⸻


Testing
You can test the API using:
Swagger UI
Postman
Browser


⸻


Project Screenshots
Add screenshots inside the screenshots folder.


⸻


Author
Developed by Software Engineering Student.
