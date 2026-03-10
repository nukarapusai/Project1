# Project1

A Django web application with a CI/CD pipeline powered by GitHub Actions.

## Project Structure

```
Project1/
├── myapp/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── myapp/
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Getting Started

### Prerequisites

- Python 3.12+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nukarapusai/Project1.git
   cd Project1
   ```

2. Install dependencies:
   ```bash
   pip install -r myapp/requirements.txt
   ```

3. Run the development server:
   ```bash
   python myapp/manage.py runserver
   ```

### Running with Docker

```bash
cd myapp
docker-compose up --build
```

## CI/CD

This project uses GitHub Actions for continuous integration. The pipeline runs on every push to the `main` or `master` branch and performs:

- Python setup (3.12)
- Dependency installation
- Django system checks (`manage.py check`)

## Granting Repository Access to Collaborators

As the repository owner, you can give other GitHub users access to this repository by adding them as collaborators. Follow these steps:

1. **Go to your repository** on GitHub:
   `https://github.com/nukarapusai/Project1`

2. **Click on "Settings"** (gear icon) in the top navigation bar of the repository.

3. **Select "Collaborators"** from the left sidebar (under "Access").

4. **Click "Add people"** button.

5. **Search for the GitHub username, full name, or email** of the person you want to add.

6. **Select the appropriate permission level**:
   - **Read** – Can view and clone the repository.
   - **Triage** – Can manage issues and pull requests without write access.
   - **Write** – Can push code and manage issues/pull requests.
   - **Maintain** – Can manage the repository without access to sensitive settings.
   - **Admin** – Full access, including settings and adding collaborators.

7. **Click "Add [username] to this repository"**.

8. The invited person will receive an email invitation. They must **accept the invitation** before they gain access.

> **Note:** For organization-owned repositories, access is managed through Teams in the organization settings. Navigate to `https://github.com/orgs/<your-org>/teams` to manage team-based access.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request
