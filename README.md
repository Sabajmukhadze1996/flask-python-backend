# Django Blog Project with REST APIs and Vue.js Frontend

## Project Overview

This is a robust, full-stack project that integrates a Django backend with a Vue.js frontend. The Django application serves as an API provider and includes an administrative panel for managing content. The project utilizes `django-ninja` for REST API development, `Redis` for session management, and MongoDB for data synchronization through Django signals. The frontend is implemented in Vue 3 and supports user authentication, blog management, and commenting functionalities.

## Key Features

### Backend (Django)

- **Custom User Model**: Includes a profile image field.
- **Session Management**: Uses Redis for session storage.
- **RESTful API**: Built using `django-ninja`, providing endpoints for:
  - User registration and authentication (JWT-based).
  - Blog management (create, update, delete, filter).
  - Commenting system (create, update, delete).
  - Category, tag, and menu retrieval.
- **Admin Panel**: Customizable with TinyMCE integration for rich text editing and media management.
- **MongoDB Synchronization**: Syncs key models to MongoDB through Django signals for efficient API fetching and filtering.
- **Swagger Documentation**: API documentation available at `/api/docs`, accessible only to admin users.

### Frontend (Vue.js)

- **User Authentication**: Includes login, registration, password reset, and profile management.
- **Blog Management**: Users can create, edit, and delete blogs with media attachments.
- **Comment System**: Users can post, reply to, and manage comments on blog posts.
- **Form Validations**: All forms include client-side validation for a seamless user experience.

## Installation and Setup

### Prerequisites

Ensure the following are installed:

- Python 3.8+
- Node.js and npm
- Redis
- MongoDB

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sabajmukhadze1996/django-blog-project.git
   cd django-blog-project
   ```
