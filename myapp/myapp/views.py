from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>🚀 CI/CD Django Project</h1>
    <h2>Deployment Successful!</h2>
    <p>This project is deployed using:</p>
    <ul>
        <li>Docker</li>
        <li>GitHub</li>
        <li>AWS EC2</li>
        <li>CI/CD Pipeline</li>
    </ul>
    """)
