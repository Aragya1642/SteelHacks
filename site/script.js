// Function to handle light/dark mode toggle
const toggleButton = document.getElementById("theme-toggle");
const bodyElement = document.body;

toggleButton.addEventListener("click", () => {
  // Toggle the 'dark-mode' class on the body
  bodyElement.classList.toggle("dark-mode");

  // Change the button text based on the current mode
  if (bodyElement.classList.contains("dark-mode")) {
    toggleButton.textContent = "☀️ Light Mode";
  } else {
    toggleButton.textContent = "🌙 Dark Mode";
  }
});

// Initialize based on user’s previous preference (if stored in localStorage)
if (localStorage.getItem("theme") === "dark") {
  bodyElement.classList.add("dark-mode");
  toggleButton.textContent = "☀️ Light Mode";
}

// Save the theme preference in localStorage
toggleButton.addEventListener("click", () => {
  if (bodyElement.classList.contains("dark-mode")) {
    localStorage.setItem("theme", "dark");
  } else {
    localStorage.setItem("theme", "light");
  }
});

// Function to fetch JSON data and populate the events
function loadEvents() {
  fetch("full_output.json")
    .then((response) => response.json())
    .then((data) => {
      const eventsContainer = document.querySelector(".events-container");
      eventsContainer.innerHTML = ""; // Clear the container before adding events

      data.forEach((item) => {
        // Destructure event object
        const { title, location, date, url } = item.event;

        // Create the HTML structure for each event
        const eventCard = document.createElement("div");
        eventCard.classList.add("event");

        // Wrap the entire card in an anchor element
        eventCard.innerHTML = `
                  <a href="${url}" target="_blank" class="event-link">
                      <h3>${title}</h3>
                      <p>Location: ${location}</p>
                      <p>Date: ${date}</p>
                  </a>
                  <a href="${url}.ics" class="add-event">Add to Calendar</button>
              `;

        // Append the event card to the container
        eventsContainer.appendChild(eventCard);

        // Add an event listener to the "Add to Calendar" button
        const addButton = eventCard.querySelector(".add-event");
        // addButton.addEventListener("click", (e) => {
        //   e.stopPropagation(); // Prevent the link from being followed
        //   alert(`Added ${title} to calendar`);
        // });
      });
    })
    .catch((error) => console.error("Error loading events:", error));
}
// Call the function to load events when the page loads
window.addEventListener("DOMContentLoaded", loadEvents);
