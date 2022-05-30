from datetime import datetime

def show_venue_details(venue_table, artist_table, show_table, venue_id, format_datetime): 
  # Get the Venue detail by the venue id 
    venues = venue_table.query.get(venue_id)

    # Get all the show from the database
    shows = show_table.query.all()

    current_time = datetime.today()

    past_shw = [] # An array that hold all the past shows
    upcoming_shw = [] # An array that hold all upcoming shows

    # Loop Through every row in the Show Model table
    for show in shows:

        # For every row in the Show Model Table 
        # Find the venue id that matches the venue_id on the url_parameter from the show model Table
        if show.venue_id == venue_id:
            # on the show table every artist that has a show is on the same row with the 
            # venue where the show will take place
            # Therefore if found a venue id the matches the url_parameter then get the artist_id 
            artist = artist_table.query.get(show.artist_id)
            # put the shows that are upcoming to the upcoming_show array
            if show.start_time > current_time:
                upcoming_shw.append({
                    "artist_id": artist.id,
                    "artist_name": artist.name,
                    "artist_image_link": artist.image_link,
                    "start_time": format_datetime(str(show.start_time))
                })
            else:
                # put the show that already took place in the past_shows array
                past_shw.append({
                    "artist_id": artist.id,
                    "artist_name": artist.name,
                    "artist_image_link": artist.image_link,
                    "start_time": format_datetime(str(show.start_time))
                })


    return {
    "id": venues.id,
    "name": venues.name,
    "genres": venues.genres,
    "city": venues.city,
    "state": venues.state,
    "phone": venues.phone,
    "website": venues.website,
    "facebook_link": venues.facebook_link,
    "seeking_talent": venues.seeking_talent,
    "seeking_description": venues.seeking_description,
    "image_link": venues.image_link,
    "past_shows": past_shw,
    "upcoming_shows": upcoming_shw,
    "past_shows_count": len(past_shw),
    "upcoming_shows_count": len(upcoming_shw),
    }