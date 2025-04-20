

```markdown
# 🐉 AniBlog - Anime Blog Platform

AniBlog is a web application where users can post and explore blogs about their favorite anime series. Built using **Python Flask**, **Jinja2 templating**, and a **SQL database**, it provides a minimal yet expressive platform for anime enthusiasts to share thoughts, reviews, and recommendations.

---

## 🚀 Features

- 📝 Create, read, update, and delete anime blog posts
- 🔍 Explore blogs based on latest or most popular
- 👤 User authentication (optional - if implemented)
- 🎨 Jinja2 templating for dynamic page rendering
- 💾 SQL database for persistent storage

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Templating Engine:** Jinja2
- **Database:** SQLite / MySQL / PostgreSQL (depending on your setup)
- **Frontend:** HTML5, CSS3, JavaScript (basic)


---

## 🔧 Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/ShreyasChavan1/aniblog.git
cd aniblog
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure the database**

Make sure your `config.py` contains the correct database URI. Example for SQLite:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///aniblog.db'
```

5. **Initialize the database**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Run the app**

```bash
flask run
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---


## ✨ Future Improvements

- User registration & login system
- Comment system for each blog post
- Markdown support for writing posts
- Categories & tags for blogs
- API support (RESTful routes)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

Have any questions or suggestions?

- Email: shreyas.c@somaiya.edu
```
