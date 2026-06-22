# RailBook - Railway Passenger Booking System

RailBook is a comprehensive, scalable, and secure railway passenger booking system designed as a high-quality placement portfolio project. It provides a complete end-to-end solution for passengers to book train tickets and for administrators to manage operations.

## Features

### For Passengers
- **Account Management**: Secure registration, login, and profile management.
- **Search**: Advanced train search between stations for specific dates.
- **Booking Flow**: Transaction-safe booking process with dynamic passenger additions and real-time fare calculation.
- **My Bookings**: View booking history, check status, and cancel eligible tickets.
- **E-Tickets**: View and print detailed electronic tickets.

### For Administrators
- **Dashboard**: High-level overview with Chart.js analytics for revenue and occupancy.
- **Manage Trains**: Add, edit, and monitor train schedules, routes, and capacities.
- **Manage Stations**: Maintain the network of railway stations.
- **Manage Bookings**: View all system bookings and filter by status.
- **Manage Users**: Monitor passenger and administrative accounts.
- **Reports**: Detailed analytical reports on revenue and booking trends.

## Technology Stack

- **Backend Framework**: Python / Flask (App Factory pattern, Blueprints)
- **Database**: PostgreSQL
- **ORM**: Flask-SQLAlchemy with Flask-Migrate
- **Forms & Validation**: Flask-WTF
- **Authentication**: Flask-Login, Werkzeug Security (pbkdf2:sha256)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla + jQuery)
- **CSS Framework**: Bootstrap 5 (Glassmorphism design system)
- **Icons & Visuals**: FontAwesome 6, Chart.js, DataTables
- **Deployment**: Docker, Docker Compose, Gunicorn

## Project Structure

```
project/
├── app/                    # Application package
│   ├── models/             # Database models (User, Train, Booking, etc.)
│   ├── routes/             # Blueprints for routing
│   ├── services/           # Business logic layer
│   ├── forms/              # WTForms validation classes
│   ├── templates/          # Jinja2 HTML templates
│   ├── static/             # CSS, JS, and image assets
│   ├── utils/              # Helper functions, decorators, seed script
│   ├── __init__.py         # App factory
│   └── extensions.py       # Flask extensions initialization
├── tests/                  # Pytest test suite
├── migrations/             # Alembic database migrations
├── docker-compose.yml      # Docker compose configuration
├── Dockerfile              # Docker image definition
├── start.sh                # Docker entrypoint script
├── requirements.txt        # Python dependencies
├── config.py               # Application configuration
├── run.py                  # Main entry point
└── .env                    # Environment variables (example)
```

## Setup Instructions

### Prerequisites
- Python 3.11+
- PostgreSQL
- Docker (Optional, for containerized deployment)

### Local Development

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Create a PostgreSQL database (e.g., `railbook_db`).
   - Create a `.env` file based on `.env` settings:
     ```
     FLASK_APP=run.py
     FLASK_ENV=development
     DATABASE_URL=postgresql://username:password@localhost/railbook_db
     SECRET_KEY=your-secret-key-here
     ```

5. **Initialize Database and Seed Data**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   flask seed
   ```

6. **Run the Application**:
   ```bash
   flask run
   ```

### Docker Deployment

1. Make sure Docker and Docker Compose are installed.
2. Run the following command in the project root:
   ```bash
   docker-compose up --build
   ```
3. The application will be available at `http://localhost:5000`.

## Testing

The project includes a comprehensive test suite using `pytest`.

To run the tests:
```bash
python -m pytest tests/ -v
```

## Seed Data Accounts
After running `flask seed`, you can use the following default accounts:
- **Admin**: admin@railbook.com / Admin@123
- **User**: john.doe@example.com / Password@123

## Author
Developed as a high-quality portfolio project demonstrating advanced backend architecture, secure transaction handling, and modern responsive frontend design.
