from datetime import datetime

#____________________________________________________________________
#____________________________________________________________________

##### SEARCH DATABASE BASED ON USER INPUT ON SEARCH BAR #############

def search_db(search_name, search_term, Show):
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