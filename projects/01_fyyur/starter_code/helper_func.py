from app import Show, Venue, Artist, format_datetime
from datetime import datetime
from flask import request


def displayTableContents(table_name, table_id):
  # Get the Table detail by the table id 
  table = table_name.query.get(table_id)

  # Get all the show from the database
  shows = Show.query.all()

  current_time = datetime.today()

  past_shw = [] # An array that hold all the past shows
  upcoming_shw = [] # An array that hold all upcoming shows
  
  # Loop Through every row in the Show Model table
  for show in shows:

        if table_name == 'Venue':

            # For every row in the Show Model Table 
            # Find the venue id that matches the venue_id on the url_parameter from the show model Table
            if show.venue_id == table_id:
                # on the show table every artist that has a show is on the same row with the 
                # venue where the show will take place
                # Therefore if found a venue id the matches the url_parameter then get the artist_id 
                artist = Artist.query.get(show.artist_id)
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
        else:

            if show.artist_id == table_id:

                venue = Venue.query.get(show.venue_id)


            if show.start_time > current_time:
                upcoming_shw.append({
                "artist_id": venue.id,
                "artist_name": venue.name,
                "artist_image_link": venue.image_link,
                "start_time": format_datetime(str(show.start_time))
                })
            else:
            # put the show that already took place in the past_shows array
                past_shw.append({
                "artist_id": venue.id,
                "artist_name": venue.name,
                "artist_image_link": venue.image_link,
                "start_time": format_datetime(str(show.start_time))
                })


  return  {
    "id":table.id,
    "name":table.name,
    "genres":table.genres,
    "city":table.city,
    "state":table.state,
    "phone":table.phone,
    "website":table.website,
    "facebook_link":table.facebook_link,
    "seeking_talent":table.seeking_talent,
    "seeking_description":table.seeking_description,
    "image_link":table.image_link,
    "past_shows": past_shw,
    "upcoming_shows": upcoming_shw,
    "past_shows_count": len(past_shw),
    "upcoming_shows_count": len(upcoming_shw),
  }


#____________________________________________________________________
#____________________________________________________________________

##### SEARCH DATABASE BASED ON USER INPUT ON SEARCH BAR #############

def search_db(search_name, search_term):
    search_items = search_name.query.filter(search_name.name.ilike('%' + search_term + '%'))
    shows = Show.query.all()
    current_date = datetime.today()
    data = []
    count = 0


    for search_item in search_items:
        count += 1
        upcoming_show_count = 0
    

        for show in shows:
            if search_name == 'Artist':
                if show.artist_id == search_item.id:
                    if show.start_time > current_date:
                        upcoming_show_count += 1
            elif search_name == 'Venue':
                if show.venue_id == search_item.id:
                    if show.start_time > current_date:
                        upcoming_show_count += 1

        data.append({
        "id": search_item.id,
        "name": search_item.name,
        "num_upcoming_shows": upcoming_show_count,
        })

    return {"count": count,"data": data}