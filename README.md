# 🛍️ Django E-commerce Website

A professional and fully functional E-commerce web application built using Django and Bootstrap. It features user authentication, product management, shopping cart, coupon application, review and rating system, and a responsive UI for seamless online shopping.

![Homepage Screenshot](https://via.placeholder.com/800x400.png?text=E-commerce+Home+Page)
![Product Page Screenshot](https://via.placeholder.com/800x400.png?text=Product+Detail+Page)
![Cart Page Screenshot](https://via.placeholder.com/800x400.png?text=Shopping+Cart)
![Checkout Page Screenshot](https://via.placeholder.com/800x400.png?text=Checkout+Page)

## 🚀 Features

- 🛍 Product Listing by Category  
- 🔍 Product Detail Page with Image, Description, and Price  
- 🛒 Add to Cart / Remove from Cart / Quantity Update (+/-)  
- 📦 Cart Summary View  
- 💳 Checkout Page with Order Summary  
- 🎟 Coupon Code Application (Expiry + Usage Limit)  
- ⭐ Star Rating and Product Review System  
- 👤 User Registration, Login, Logout  
- 🧾 Admin Panel for Product, Category, Coupon Management  
- 📂 Category Filtering  
- ⚙️ Custom Middleware and Context Processor for Cart and Coupon Access  

## 📁 Project Structure

```
ecommerce/
├── accounts/            # User authentication
├── cart/                # Cart functionality
├── checkout/            # Order processing and checkout
├── coupons/             # Coupon system
├── products/            # Product and review logic
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── ecommerce/           # Main project settings
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## 🛠️ Installation and Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/django-ecommerce.git
cd django-ecommerce
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Now open your browser and visit:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔐 Admin Login

Visit the Django admin at:  
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  
Login with the superuser credentials you just created.

## 🧠 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (can be upgraded to PostgreSQL/MySQL)  
- **Security:** Django Authentication, Sessions  
- **Other:** Django Admin, Forms, Custom Middleware, Context Processor  

## 🌐 Live Demo

_(Optional: Add deployment link here if hosted on Render, Railway, etc.)_

## 📸 Screenshots

_(Replace these URLs with actual hosted screenshots if available)_

- ![Home](https://via.placeholder.com/800x400.png?text=Home)
- ![Products](https://via.placeholder.com/800x400.png?text=Products)
- ![Cart](https://via.placeholder.com/800x400.png?text=Cart)
- ![Checkout](https://via.placeholder.com/800x400.png?text=Checkout)

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, make enhancements, and submit a pull request.

## 👨‍💻 Author

**Ashutosh Rath**  
📧 ashutoshrath.dev@example.com  
🌐 [Portfolio](https://yourportfolio.com)  
🐙 [GitHub](https://github.com/your-username)

## 📄 License

This project is licensed under the [MIT License](LICENSE).
