# Multi-Tenant Blog with Django

## Overview  
This project is a **multi-tenant blog** application built using **Django** and **django-tenants**. Each tenant (organization or user group) can have its own isolated blog with separate data while sharing the same codebase. This architecture is ideal for SaaS platforms, allowing multiple clients to use a single application with their own subdomains or schemas.

## Multi-Tenant Concept  
**Multi-tenancy** is an architecture in which a single instance of the application serves multiple tenants (clients). Each tenant's data is stored separately, either in different schemas or databases. There are two main types of multi-tenancy:  
- **Database-per-tenant**: Each tenant has its own database.  
- **Schema-per-tenant (used here)**: All tenants share a single database, but data is isolated using separate schemas for each tenant.

**Key Advantages of Multi-Tenancy:**
- Centralized maintenance and updates.  
- Data isolation for security.  
- Scalability for SaaS platforms.  

In this project, **django-tenants** is used to implement schema-based multi-tenancy.

---

## Features  
- Schema-based multi-tenancy using **django-tenants**.  
- Basic blog functionality:  
  - Create, read, update, and delete (CRUD) blog posts.  
  - Each tenant has its own set of blog posts.  
- Class-based views for efficient and scalable code.  
- Simple and responsive templates for the user interface.  

---

## Tech Stack  
- **Backend**: Django 4.x  
- **Multi-tenancy**: django-tenants  
- **Database**: PostgreSQL (required for schema-based multi-tenancy)  
- **Frontend**: HTML, CSS (Bootstrap for styling)  
- **Templates**: Django templating engine  

---

## Installation and Setup  
### Prerequisites  
- Python 3.x  
- PostgreSQL  
- Virtualenv (optional but recommended)

### Steps  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/homemix/multitenantBlog
   cd multitenantBlog
   ```

2. **Create and activate a virtual environment:**  
   ```sh
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate  # For Windows
   ```

3. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure the database:**  
   Update the `settings.py` with your PostgreSQL credentials.

5. **Run migrations:**  
   ```sh
   python manage.py makemigrations
   python manage.py migrate_schemas --shared
   ```

6. **Create a superuser:**  
   ```sh
   python manage.py createsuperuser
   ```

7. **Start the server:**  
   ```sh
   python manage.py runserver
   ```

8. **Access the application:**  
   Open your browser and go to `http://localhost:8000`.

---

## Project Structure  
```
multitenant_blog/
    ├── blog/               # Blog application with CRUD functionality
    ├── customers/            # Tenant management
    ├── multitenant_blog/   # Main project settings
    ├── templates/          # HTML templates for the blog
    ├── manage.py           # Django management script
    └── README.md           # Project documentation
```

---

## Example Usage  
1. Register multiple tenants (e.g., `tenant1`, `tenant2`).  
2. Each tenant has its own blog space, accessible at a unique subdomain like:  
   - `tenant1.localhost:8000`  
   - `tenant2.localhost:8000`  
3. Admins and users can manage blog posts within their own tenant space.

---

## Future Improvements  
- Add authentication for tenant-specific user management.  
- Implement a rich text editor for blog content.  
- Enhance the UI with more responsive and modern components.  
- Add an API for external integrations.  

---

## License  
This project is licensed under the MIT License. See `LICENSE` for more information.

---

## Acknowledgements  
- [Django](https://www.djangoproject.com/)  
- [django-tenants](https://django-tenants.readthedocs.io/)  

---
