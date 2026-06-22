"""
Entry point for the RailBook application.
"""
import os
from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.station import Station
from app.models.train import Train
from app.models.route import Route
from app.models.booking import Booking
from app.models.passenger import Passenger
from app.models.payment import Payment

app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Provides shell context for flask shell command."""
    return {
        'db': db,
        'User': User,
        'Station': Station,
        'Train': Train,
        'Route': Route,
        'Booking': Booking,
        'Passenger': Passenger,
        'Payment': Payment
    }

if __name__ == '__main__':
    app.run(debug=True)
