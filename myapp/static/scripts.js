// Selects the first element with the class "content-box" in the document
document.addEventListener("DOMContentLoaded", function() {
    const contentBox = document.querySelector(".content-box");

// Add an event listener to the "link-profile" element that triggers when clicked
    document.getElementById("link-profile").addEventListener("click", function(event) {
// Prevent the click on the link (link-profile) from navigating to a new page
        event.preventDefault();
