# 🐍 Django Blog Project

A full-featured blog web application built with **Python Django**, following [Corey Schafer’s Django Tutorial Series](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p).  
This project implements key web-development concepts such as authentication, CRUD operations, media handling, and pagination.

---

## 🚀 Features

- 🧑‍💻 User registration and authentication (login, logout, profile)
- ✍️ Create, update, and delete blog posts
- 🖼️ Profile pictures and media uploads
- 📄 Pagination for post lists
- 🔐 Password reset via email
- 🌐 Fully templated frontend with Bootstrap

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Django 5.x |
| **Frontend** | HTML, CSS (Bootstrap) |
| **Database** | SQLite (default, easily switchable to PostgreSQL/MySQL) |
| **Environment** | Python 3.x, Virtualenv |
| **Version Control** | Git & GitHub |

---

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/luciantkd/django_project.git
   cd django_project
   ````

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the server:**

   ```bash
   python manage.py runserver
   ```

7. **Visit the site:**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧠 Learning Goals

This project demonstrates:

* Django MVC (Model-View-Template) architecture
* URL routing and views
* Django ORM and migrations
* User authentication and sessions
* Static & media file handling
* Secure password reset via email
* Template inheritance and Bootstrap integration

---

## 📂 Project Structure

```
django_project/
│
├── blog/              # Blog app (posts, pagination, CRUD)
├── users/             # User app (register, login, profile)
├── media/             # Uploaded images
├── django_project/    # Main project configuration
├── manage.py          # Django management script
└── posts.json         # Example data file
```

---

## 🧑‍💻 Author

**Lucian Procopciuc**
[GitHub Profile](https://github.com/luciantkd)

---

## 🏁 Acknowledgements

Special thanks to **Corey Schafer** for his in-depth Django tutorials that guided this project’s creation.

