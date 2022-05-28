from app import Show, Venue
from datetime import datetime

def venue_upcoming_show_and_past_show(venue_id):
    shows = Show.query.all()

    current_time = datetime.today()

    upcoming_shw = [] # An array that hold all upcoming shows

     # Loop Through every row in the Show Model table
    for show in shows:

        # For every row in the Show Model Table 
        # Find the venue id that matches the venue_id on the search_parameter from the show model Table
        if show.venue_id == venue_id:
            venue = Venue.query.get(venue_id) 
            # put the shows that are upcoming to the upcoming_show array
            if show.start_time > current_time:
                upcoming_shw.append({
                "id": show.venue_id,
                "name": venue.name,
                "num_upcoming_shows": len(upcoming_shw)
                })
