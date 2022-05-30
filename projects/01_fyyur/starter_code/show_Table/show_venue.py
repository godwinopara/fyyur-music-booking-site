from datetime import datetime

def show_venue_details(venue_table,Show, venue_id, format_datetime): 
  # Get the Venue id that its information will be displayed 
    venues = venue_table.query.get(venue_id)

    # Get the current time
    current_time = datetime.today()


    # Get all the venues where a show has been performed
    shows = Show.query.join('venue').join('artist').filter(Show.venue_id == venue_id)


    past_shw = [] # An array that hold all the past shows
    upcoming_shw = [] # An array that hold all upcoming shows

    # Loop Through every row in the Show Model table
    for show in shows:
        
            if show.start_time > current_time:
            # put the shows that are upcoming to the upcoming_show array
                upcoming_shw.append({
                    "artist_id": show.artist.id,
                    "artist_name": show.artist.name,
                    "artist_image_link": show.artist.image_link,
                    "start_time": format_datetime(str(show.start_time))
                })
            else:
                # put the show that already took place in the past_shows array
                past_shw.append({
                    "artist_id": show.artist.id,
                    "artist_name": show.artist.name,
                    "artist_image_link": show.artist.image_link,
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