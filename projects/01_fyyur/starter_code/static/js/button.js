const deleteVenueButton = document.querySelector(".delete-venue-btn");

deleteVenueButton.addEventListener("click", (e) => {
  /* Get the venue id */
  const venue_id = e.target.dataset["id"];
  /* Get the venue name */
  const venueName = e.target.dataset["name"];
  /* Confirm if the user really wants to delete the venue */
  if (confirm(`Are You Sure You want to Delete venue: ${venueName}`)) {
    /* Send the delete request */
    fetch(`/venues/${venue_id}`, {
      method: "DELETE",
    });

    /* Redirect users to homepage when the delete has been completed */
    document.location = "/";
  }
});

