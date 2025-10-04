roemi/                ← root project
│
├── manage.py
├── roemi/            ← folder utama project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── myapp/                 ← aplikasi utama
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── myapp/
    │       ├── individu_list.html
    │       ├── individu_detail.html
    │       ├── individu_form.html
    │       └── individu_confirm_delete.html
    └── migrations/
