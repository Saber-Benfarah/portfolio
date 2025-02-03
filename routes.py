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
    {"id": 1, "title": "Project 1", "description": "AI-based chatbot", "images": ["project1-1.jpg", "project1-2.jpg"]},
    {"id": 2, "title": "Project 2", "description": "E-commerce Website", "images": ["project2-1.jpg", "project2-2.jpg"]},
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
