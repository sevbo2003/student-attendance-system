![The Well App](https://malikoff.uz/media/post-images/Blue_Ocean_Photo_Summer_Instagram_Post.gif)

<div align='center'>
    <a href='https://github.com/sevbo2003/student-attendance-system/releases'>
    <img style='border-radius:5px;' src='https://shields.io/github/v/tag/sevbo2003/student-attendance-system?color=%23FDD835&label=version&style=for-the-badge'>
    </a><a href='https://github.com/sevbo2003/student-attendance-system/blob/master/LICENSE'>
    <img style='border-radius:5px;' src='https://img.shields.io/github/license/chroline/well_app?style=for-the-badge'>
    </a>
    
</div>
<br />

---

### What does this application do!  🚀

- It is backend part of student attendance system for.
- You can use this application for any kind of educational fields
- ios/android: coming soon 👀
---

<br />

<div align="center">

**[ABOUT PROJECT]() • 
[TECH STACK]() • 
[GETTING STARTED]() • 
[INSTALLATION]() • 
[USAGE]() • 
[CONTRIBUTING]() • 
[LICENSE]()**

</div>

---
<br />

# Built With
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- [![Django][Django]](https://www.djangoproject.com/)
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
- [![Postgres][Postgres.db]](https://www.postgresql.org/)
- [![Redis][Redis]](https://redis.io/)
- ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
- ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
- ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)

<!-- Frontend
* [![Next][Next.js]](Next-url)
* [![React][React.js]][React-url]
* ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* ![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white) -->


---
<br />
<!-- GETTING STARTED -->

# Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

# Prerequisites

You need `linux` machine and Python package manager(`pip`) to run the project.
* pip
  ```bash
  sudo apt install python3-pip
  ```
* git
  ```bash
  sudo apt install git
  ```

# Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sevbo2003/student-attendance-system.git
   ```
2. Go to project directory
   ```sh
   cd student-attendance-system
   ```
3. Create virtual environment
   ```sh
   python3 -m venv venv
   ```
4. Activate virtual environment
   ```sh
    source venv/bin/activate
    ```
5. Install requirements
    ```sh
    pip install -r requirements.txt
    ```
6. Create `.env` file and fill it with your credentials like `.env.example`
    ```sh
    touch .env
    ```
    ```python
    # .env
    DEBUG=True # or False
    SECRET_KEY=your_secret_key
    ALLOWED_HOSTS=*
    
    # db
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
    
    # redis
    REDIS_URL=redis://user:password@host:port

    # cors
    CORS_ORIGIN_WHITELIST=
    ```
7. Run migrations and migrate
    ```sh
    python manage.py makemigrations
    ```
    ```sh
    python manage.py migrate
    ```
8. Create superuser
    ```sh
    python manage.py createsuperuser
    ```
9. Run server
    ```sh
    python manage.py runserver
    ```
10. Install Redis in your machine and run it
    ```sh
    sudo apt install redis-server
    ```
    ```sh
    redis-server
    ```
11. Run celery worker
    ```sh
    celery -A config worker -l info
    ```
12. Run celery beat
    ```sh
    celery -A config beat -l info
    ```
13. All done! Now you can use the application


---
<br />

# Usage
Here you can find important APIs to use the application

- Get token for user
    ```sh
    POST /api/token/
    ```
    ```json
    {
        "email": "your_email",
        "password": "your_password"
    }
    ```
- Get students info
    ```sh
    GET /accounts/users/
    ```
- Get teachers info
    ```sh
    GET /accounts/teachers/
    ```
- Get groups info
    ```sh
    GET /attendance/groups/
    ```
-  Get group subjects info
    ```sh
    GET /attendance/group/{group_id}/subjects/
    ```
- Get group students info
    ```sh
    GET /attendance/group/{group_id}/students/
    ```
- Get attendance info
    ```sh
    GET /attendance/attendance-report/
    ```
- Get daily attendance status
    ```sh
    GET /dailystat/
    ```

---
<br />

# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
<br />

<!-- LICENSE -->
# License

Distributed under the MIT License. See `LICENSE` for more information.


---

<br />

# 💛
Made with ❤️ by [Abdusamad](https://github.com/sevbo2003)
- Reminder that *you are great, you are enough, and your presence is valued.*




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Postgres.db]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Redis]: https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white
[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white