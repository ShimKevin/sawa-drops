# 🧊 Sawa Drops - Purified Drinking Water Delivery Web App

[![Made with Flask](https://img.shields.io/badge/Built%20with-Flask-blue)](https://flask.palletsprojects.com/)
[![Hosted on Heroku](https://img.shields.io/badge/Hosted%20on-Heroku-430098)](https://sawa-drops-23e95508dc5f.herokuapp.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Sawa Drops** is a sleek, mobile-friendly web application developed using the **Flask** framework. It supports the digital operations of **Sawa Drops**, a purified drinking water delivery service based in **Kitale Town, Kenya**. Designed with both usability and functionality in mind, the platform allows users to browse water products, place inquiries, and admins to manage content seamlessly.

Live Demo: 🌐 [https://sawa-drops-23e95508dc5f.herokuapp.com/](https://sawa-drops-23e95508dc5f.herokuapp.com/)

---

## 🚀 Key Features

✅ **Product Catalog with Pricing**  
Display a clean and organized list of available bottled water products with their prices.

✅ **Dynamic Image Gallery**  
Highlight your brand, delivery service, and hygiene through an interactive gallery.

✅ **Contact and Inquiry Support**  
A contact section for users to reach out with inquiries, orders, or support questions.

✅ **Admin Panel**  
A secure and easy-to-use backend interface to add, edit, or delete products and gallery items.

✅ **Image Upload System**  
Admins can upload multiple product or promotional images via the dashboard.

✅ **Mobile Responsive UI**  
Responsive design ensures smooth experience across smartphones, tablets, and desktops.

✅ **Secure Routing**  
Sensitive routes like the admin panel are protected with basic access restrictions.

---

## 🛠️ Installation & Setup

Follow the instructions below to set up Sawa Drops locally on your development machine using VS Code:

### 1. Clone the Repository
```bash
git clone https://github.com/ShimKevin/sawa-drops.git
cd sawa-drops
2. Create Virtual Environment (Recommended)
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Flask Server
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000 in your browser.

🗂️ Project Structure
php
Copy
Edit
sawa-drops/
│
├── static/
│   ├── css/                 # Custom stylesheets
│   ├── images/              # Static assets (logos, banners, etc.)
│   └── uploads/             # Dynamically uploaded images by admin
│
├── templates/
│   ├── index.html           # Homepage with product display and gallery
│   ├── login.html           # Admin login form
│   └── admin.html           # Admin dashboard for content management
│
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
🔐 Admin Access
To access the backend dashboard and upload images:

📍 Navigate to /upload or /admin (if implemented).
🔑 Credentials must be entered (future versions may include login logic).

📌 Ensure to implement proper user authentication before deploying in production.

✨ Technologies Used
Python 3

Flask

Werkzeug (for secure file uploads)

HTML5/CSS3

JavaScript (Vanilla)

Heroku (Hosting)

🌍 Deployment
This app is currently live and publicly accessible via Heroku.

🔗 Live URL:
https://sawa-drops-23e95508dc5f.herokuapp.com/

To deploy your own version:

Push your code to a GitHub repo.

Link the repo to Heroku.

Add a Procfile and set buildpacks (heroku/python).

Deploy the app.

📬 Contact & Support
If you have feedback, issues, or feature requests, feel free to reach out:

📧 Email: sawadrops@gmsil.com

📞 Phone: +254 790 229 112

📍 Address: Teriyet Business Centre, Kitale Town, Kenya

We truly value your support and interest in Sawa Drops — your trusted partner for safe, clean, and fast drinking water delivery 💧.

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.

🙌 Contributing
Want to improve this project or fix a bug?

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a pull request

Developed with ❤️ in Kitale by Kevin Shimanjala.

python
Copy
Edit

---

Let me know if you'd like this automatically uploaded to your GitHub repo or if you'd like a `Procfile`, `.gitignore`, or `login.html` template added to support full deployment