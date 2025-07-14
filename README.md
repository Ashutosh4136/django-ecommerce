# 🛍️ Django E-commerce Website

A professional and fully functional E-commerce web application built using Django and Bootstrap. It features user authentication, product management, shopping cart, coupon application, review and rating system, and a responsive UI for seamless online shopping.

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

### 3️⃣ (Optional) Create `requirements.txt` (if not present)

```bash
pip freeze > requirements.txt
```

### 4️⃣ Install the Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Development Server

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

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, make enhancements, and submit a pull request.

## 👨‍💻 Author

**Ashutosh Rath**  
📧 rathashutosh11@gmail.com   
🐙 [GitHub](https://github.com/Ashutosh4136)

## 📄 License

This project is licensed under the [MIT License](LICENSE).
