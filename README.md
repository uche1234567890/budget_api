# 💰 Budget Tracker API

A **Django + Django REST Framework** backend project that provides a fully functional **Budget Tracking API**.  
This API allows users to register, log in, and manage their **categories and transactions**.  
It is designed as a learning project for **building REST APIs with Django**.

---

## 🚀 Features

### 🔐 User Management
- User **registration, login**
- JWT authentication with **access & refresh tokens**
- Secure password hashing
- Each user can **only manage their own data**

### 📂 Categories
- Create, Read, Update, and Delete categories
- Each category belongs to the authenticated user
- Examples: *Food, Transport, Entertainment, Bills*

### 💳 Transactions
- Create, Read, Update, and Delete transactions
- Fields: **amount, description, category, date**
- Linked to user’s categories
- Automatically calculates summaries

### 📊 Budget Summary
- Get a breakdown of transactions per category
- View total income/expenses
- Helps track spending habits

### 🛡️ Permissions
- Only **owners** can access/edit their categories and transactions
- Unauthorized users cannot access others’ data

### 🌍 Deployment
- Works with **PostgreSQL** (production) or SQLite (development)
- Deployable to **Heroku** or **PythonAnywhere**