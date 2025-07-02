# Abhishek-portfolio
🧑‍💻 Abhishek Jha – Portfolio Website



For your project—a personal portfolio website with Django, MongoDB, a job submission form, admin login, and resume integration—a **clear and informative README** helps showcase your work to recruiters, collaborators, or open-source users.

Here’s a professional and tailored `README.md` descriptions

---

# 🧑‍💻 Abhishek Jha – Portfolio Website

A fully responsive personal portfolio website built with **Django** and **MongoDB**, featuring:

* 💼 Resume and professional background
* 📩 Job offer submission form
* 🔐 Admin authentication for viewing submissions
* 📸 Profile image and clean UI
* 🧰 Deployment-ready structure with DevOps integrations (CI/CD, Docker-ready)

## 🔍 Features

* **Homepage** showcasing profile, key skills, tools, and experience
* **Job Submission Form** to receive offers from recruiters
* **Admin Panel** (secured via Django) to manage form data
* **Static file support** (profile image, CSS, custom styles)
* Clean navigation and footer

## 🚀 Technologies Used

* **Backend:** Django, Python
* **Frontend:** HTML5, CSS3, Bootstrap
* **Database:** SQLite (default), easily switchable to PostgreSQL or MongoDB
* **DevOps Ready:** Structure designed for future Docker, Jenkins, or cloud deployment

## 📁 Folder Structure

```bash
portfolio-site/
├── jobs/                # Django app for job form and views
├── static/              # CSS and image files
│   ├── css/style.css
│   └── images/profile.jpg
├── templates/
│   └── jobs/home.html
├── portfolio_site/      # Main project config
└── manage.py
```

## ⚙️ Setup Instructions

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/portfolio-site.git
   cd portfolio-site
   ```

2. **Create virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations & start server:**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the site:**
   Visit `http://127.0.0.1:8000/`

## 🔐 Admin Login

To view submissions:

```bash
python manage.py createsuperuser
# Then login at: http://127.0.0.1:8000/admin
```

## 📸 Screenshot

![Home Page](static/images/screenshot-home.png)


![image](https://github.com/user-attachments/assets/d63ef402-2ba8-4de6-9a8f-72162d450d55)

![image](https://github.com/user-attachments/assets/f99f9a75-befd-49c6-b3d8-8964a0c68b7d)

![image](https://github.com/user-attachments/assets/df890136-861a-4dc1-bdc4-30b3534e0be8)


---


