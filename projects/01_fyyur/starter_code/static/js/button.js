const deleteVenueButton = document.querySelector(".delete-venue-btn");

deleteVenueButton.addEventListener("click", (e) => {
  const id = e.target.dataset["id"];
  const venueName = e.target.dataset["name"];
  if (confirm(`Are You Sure You want to Delete venue: ${venueName}`)) {
    fetch(`/venues/${id}`, {
      method: "DELETE",
    });

    document.location = "/";
  }
});

