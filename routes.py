from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

services = {
    "python-development": "Python Development",
    "web-development": "Web Development",
    "mobile-development": "Mobile App Development",
    "ar-vr": "AR/VR Development",
    "ai-model": "AI Model Training",
    "cv-creation": "CV Creation",
    "logo-design": "Logo Design",
    "custom-project": "Custom Work"
}


projects = [
    {
        "id": 1,
        "title": "Text-to-Test-Case Generation",
        "short_description": "AI-powered automation using Transformer models to generate test cases from software requirements.",
        "description": "This project focused on fine-tuning Transformer models like T5 and GPT to generate automated test cases from text-based software requirements. The model improved testing accuracy and efficiency in software development workflows.",
        "technologies": "Python, Hugging Face, Transformers, NLP, AI",
        "features": [
            "Fine-tuned AI models for automated test generation",
            "Improved accuracy and efficiency in software testing",
            "Developed a framework for AI-driven test automation"
        ],
        "image": "text to test.png",
        "images": ["text-to-test-1.png", "text-to-test-2.png"]
    },
    {
        "id": 2,
        "title": "School Management App",
        "short_description": "A full-stack web application for managing students, teachers, and school activities.",
        "description": "Developed a complete school management system that allows teachers to track attendance, record grades, and schedule events. The application provides an intuitive interface for both students and administrators.",
        "technologies": "Flask, SQLAlchemy, HTML, CSS, JavaScript",
        "features": [
            "Attendance tracking and grade reporting",
            "Admin dashboard for managing users",
            "Event scheduling and notifications"
        ],
        "image": "school-management.png",
        "images": ["school-management-1.jpg", "school-management-2.jpg"]
    },
    {
        "id": 3,
        "title": "Portfolio Website",
        "short_description": "A responsive personal portfolio website showcasing my projects and skills.",
        "description": "This is my personal portfolio website, built using Flask, Bootstrap, and CSS. It highlights my work, skills, and professional experience in a clean and structured manner.",
        "technologies": "Flask, Bootstrap, HTML, CSS",
        "features": [
            "Responsive design",
            "Showcases projects and skills",
            "Simple and elegant UI"
        ],
        "image": "Portfolio.png",
        "images": ["portfolio-1.png", "portfolio-2.png"]
    },
]

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/services")
def service():
    return render_template("services.html", services=services)

@main.route("/order/<service>")
def order_service(service):
    service_name = services.get(service, "Custom Work")
    return render_template("order_service.html", service_name=service_name)


@main.route("/projects")
def project():
    return render_template("projects.html", projects=projects)

@main.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    return render_template("project_detail.html", project=project)


@main.route("/contact")
def contact():
    return render_template("contact.html")
