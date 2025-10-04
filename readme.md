# Proyek Django: Roemi

Proyek ini adalah contoh implementasi CRUD (Create, Read, Update, Delete) menggunakan **Django** untuk entitas `Individu`.  
Struktur ini bisa dengan mudah diduplikasi untuk entitas lain seperti **Lembaga**, **Event**, atau **Panitia**.

---

## 📂 Struktur Folder

```plaintext
roemi/                # Root project
├── manage.py              # Entry point untuk perintah Django
│
├── roemi/            # Folder utama project Django
│   ├── __init__.py
│   ├── asgi.py            # Entry untuk ASGI server
│   ├── settings.py        # Konfigurasi utama project (apps, DB, static, template, dsb.)
│   ├── urls.py            # Routing URL utama
│   └── wsgi.py            # Entry untuk WSGI server (deployment)
│
└── myapp/                 # Aplikasi utama (CRUD untuk entitas)
    ├── __init__.py
    ├── admin.py           # Registrasi model ke Django Admin
    ├── apps.py            # Konfigurasi aplikasi
    ├── models.py          # Definisi model database
    ├── views.py           # View class/function untuk CRUD
    ├── urls.py            # Routing URL khusus aplikasi
    ├── migrations/        # File migrasi database
    │   └── __init__.py
    │
    └── templates/
        └── myapp/
            ├── individu_list.html           # Halaman daftar individu
            ├── individu_detail.html         # Halaman detail individu
            ├── individu_form.html           # Halaman create/update individu
            └── individu_confirm_delete.html # Halaman konfirmasi hapus individu
