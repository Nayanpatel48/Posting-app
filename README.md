# Django Posts App

A simple Django application that allows users to register, login, and manage their own posts (CRUD). Each user sees only their own posts.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the App](#running-the-app)
6. [Database Schema](#database-schema)

   * [User Table](#user-table)
   * [Post Table](#post-table)
7. [Example Data](#example-data)
8. [Forms](#forms)
9. [Views & URLs](#views--urls)
10. [Contributing](#contributing)
11. [License](#license)

---

## Project Overview

This project is a basic blogging platform built with Django. Users can:

* Register and log in
* Create, read, update, and delete their own posts
* Upload an optional image with each post
* View a personalized dashboard showing only their posts

Authentication uses Django's built-in `User` model. Posts are represented in a custom `Post` model.

## Features

* **User Registration & Authentication**: Secure signup/login/logout flows
* **Post Management**: CRUD operations on posts
* **Image Upload**: Optional image per post, stored in `MEDIA_ROOT/post_images/`
* **Access Control**: Users see and modify only their own posts

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/django-posts-app.git
   cd django-posts-app
   ```
2. **Create & activate virtual environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**:
   Copy `.env.example` to `.env` and configure secret key, database URL, etc.

## Configuration

* **Database**: Default is SQLite. To use PostgreSQL or another DB, update `DATABASES` in `settings.py` or via `DATABASE_URL`.
* **Media**: Ensure `MEDIA_ROOT = BASE_DIR / 'media'` and `MEDIA_URL = '/media/'` in settings.
* **Static**: Configure `STATIC_ROOT` and `STATIC_URL` as needed.

## Running the App

1. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```
2. **Create superuser (optional)**:

   ```bash
   python manage.py createsuperuser
   ```
3. **Run development server**:

   ```bash
   python manage.py runserver
   ```
4. **Access**:

   * Admin: `http://127.0.0.1:8000/admin/`
   * App: `http://127.0.0.1:8000/`

## Database Schema

### User Table

Django's built-in `auth_user` table stores user credentials and metadata.

| Column        | Type         | Description                     |
| ------------- | ------------ | ------------------------------- |
| id            | INTEGER (PK) | Auto-incrementing primary key   |
| password      | VARCHAR(128) | Hashed password                 |
| last\_login   | DATETIME     | Last login timestamp (nullable) |
| is\_superuser | BOOLEAN      | Superuser flag                  |
| username      | VARCHAR(150) | Unique username                 |
| first\_name   | VARCHAR(150) | First name (optional)           |
| last\_name    | VARCHAR(150) | Last name (optional)            |
| email         | VARCHAR(254) | Email address (optional)        |
| is\_staff     | BOOLEAN      | Staff flag                      |
| is\_active    | BOOLEAN      | Active flag                     |
| date\_joined  | DATETIME     | Account creation timestamp      |

### Post Table

Custom table `posts_post` for storing user-created posts.

| Column      | Type         | Description                                   |
| ----------- | ------------ | --------------------------------------------- |
| id          | INTEGER (PK) | Auto-incrementing primary key                 |
| author\_id  | INTEGER (FK) | References `auth_user.id` (on delete CASCADE) |
| title       | VARCHAR(200) | Post title                                    |
| image       | VARCHAR(100) | File path under `post_images/` (nullable)     |
| content     | TEXT         | Post body content                             |
| created\_at | DATETIME     | Timestamp of creation (auto\_now\_add=True)   |

## Example Data

### Sample Users

| id | username | email                                         | date\_joined        |
| -- | -------- | --------------------------------------------- | ------------------- |
| 1  | alice    | [alice@example.com](mailto:alice@example.com) | 2025-06-10 14:22:05 |
| 2  | bob      | [bob@example.com](mailto:bob@example.com)     | 2025-06-12 09:15:42 |

### Sample Posts

| id | author\_id | title           | image      | content                  | created\_at         |
| -- | ---------- | --------------- | ---------- | ------------------------ | ------------------- |
| 1  | 1          | Hello World     | hello.jpg  | First post by Alice.     | 2025-06-10 15:00:00 |
| 2  | 1          | Django Tips     | NULL       | Some useful Django tips. | 2025-06-11 10:30:00 |
| 3  | 2          | My Travel Plans | travel.png | Planning my next trip.   | 2025-06-12 12:00:00 |

> **Note**: Each user sees only their own posts when logged in.

## Forms

* **RegisterForm**: Extends `UserCreationForm` to capture `username`, `email`, and `password`.
* **PostForm**: ModelForm for `Post`, includes `title`, `image`, and `content` fields.

## Views & URLs

| View           | URL Pattern              | Template                    | Purpose                            |
| -------------- | ------------------------ | --------------------------- | ---------------------------------- |
| register\_view | `/register/`             | `posts/register.html`       | User signup                        |
| login\_view    | `/login/`                | `posts/login.html`          | User login                         |
| logout\_view   | `/logout/`               | Redirect to login           | User logout                        |
| home           | `/` (home)               | `posts/home.html`           | Dashboard: list of user's posts    |
| post\_create   | `/post/create/`          | `posts/post_form.html`      | Create a new post                  |
| post\_update   | `/post/<int:pk>/edit/`   | `posts/post_form.html`      | Update an existing post (own only) |
| post\_delete   | `/post/<int:pk>/delete/` | `posts/confirm_delete.html` | Delete a post (confirm, own only)  |