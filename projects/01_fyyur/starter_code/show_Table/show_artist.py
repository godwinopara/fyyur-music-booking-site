from datetime import datetime

def show_artist_details(Artist, Venue, Show, artist_id, format_datetime):
    artist = Artist.query.get(artist_id)

    shows = Show.query.all()

    current_date = datetime.now()

    p_show = []
    u_show = []

    for show in shows:
        venue = Venue.query.get(show.venue_id)
    if artist.id == show.artist_id:
        if show.start_time > current_date:
            u_show.append({
            "venue_id": show.venue_id,
            "venue_name": venue.name,
            "venue_image_link": venue.image_link,
            "start_time": format_datetime(str(show.start_time))
            })
    else:
        p_show.append({
        "venue_id": show.venue_id,
        "venue_name": venue.name,
        "venue_image_link": venue.image_link,
        "start_time": format_datetime(str(show.start_time))
        })

    return {
    "id": artist.id,
    "name": artist.name,
    "genres": artist.genres,
    "city": artist.city,
    "state": artist.state,
    "phone": artist.phone,
    "website": artist.website,
    "facebook_link": artist.facebook_link,
    "seeking_venue": artist.seeking_venue,
    "seeking_description": artist.seeking_description,
    "image_link": artist.image_link,
    "past_shows": p_show,
    "upcoming_shows": u_show,
    "past_shows_count": len(p_show),
    "upcoming_shows_count": len(u_show),
    }
