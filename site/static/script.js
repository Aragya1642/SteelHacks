//Global variable
const allEvents = new Set([]);

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

function printToConsole() {
  const textBoxValue = document.getElementById("textBox").value;
  console.log(textBoxValue);
}

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
  // open and read sample.csv
  // var csvData = $.csv.toObjects(csv);
  $.ajax(
    "http://127.0.0.1:5000/getObjects",
    {
      type: 'POST',
      data: {description: "I am interested in engineering."},
      success: function(data, status, xhr) {
        console.log("here")
        console.log(status)
        console.log(data.data)
        {
          const eventsContainer = document.querySelector(".events-container");
          eventsContainer.innerHTML = ""; // Clear the container before adding events
          const addedEventsContainer = document.querySelector(".sidebar");
    
          data.data.forEach((item) => {
            // Destructure event object
            const { title, location, date, url } = item.event;
    
            // if item id not in csv, skip
            // if (!csvData.find((element) => element.id === item.id)) {
            //   return;
            // }
    
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
                      <a href="${url}.ics" class="add-event" data-url="${url}.ics">Add to Calendar</a>
            `;
    
            // Append the event card to the container
            eventsContainer.appendChild(eventCard);
    
            // Add an event listener to the "Add to Calendar" button
            const addEventButton = eventCard.querySelector(".add-event");
            addEventButton.addEventListener("click", (e) => {
              e.preventDefault(); // Prevent the link from being followed
              const icsUrl = e.target.dataset.url; // Get the .ics URL from data attribute
              
              if (!allEvents.has(icsUrl)) {
                allEvents.add(icsUrl); // Add the URL to the global set if it's not already present
                alert(`Added ${title} to the list for download.`);
                
                // Need to add blocks on the sidebar
                const addedEventCard = document.createElement("div");
                addedEventCard.classList.add("eventAdded");
    
                // Create the HTML for the card
                addedEventCard.innerHTML = `
                          <a href="${url}" target="_blank" class="event-link">
                            <h3>${title}</h3>
                            <p>Location: ${location}</p>
                            <p>Date: ${date}</p>
                          </a>
                `;
    
                // Append to the container
                addedEventsContainer.appendChild(addedEventCard);
    
    
              } else {
                alert(`Already added ${title}.`);
              }
    
            });
          });
        }
      },
      error: function(xhr, status, error) {
        console.log("herebad")
        console.log(error)
      }
    }
  );


  // fetch("full_output.json")
  //   .then((response) => response.json())
  //   .then((data) => 
  //     )

    // .catch((error) => console.error("Error loading events:", error));
}

function initDownload(){
  // Add a button to download all selected .ics files
  const sidebar = document.querySelector(".sidebar");

  const downloadButton = document.createElement("button");
  downloadButton.textContent = "Download All Events as .ics";
  downloadButton.classList.add("download-button");
  downloadButton.addEventListener("click", downloadAllIcsFiles);
  sidebar.appendChild(downloadButton);
}

// Function to download all .ics files
function downloadAllIcsFiles() {  
  // Need to parse the ics files and combine
  


  // const combinedIcsContent = icsUrls.map(url => `BEGIN:VEVENT\nUID:${url}\nEND:VEVENT`).join('\n');
  // const blob = new Blob([combinedIcsContent], { type: 'text/calendar' });
  // const url = URL.createObjectURL(blob);
  
  // const a = document.createElement('a');
  // a.href = url;
  // a.download = 'events.ics';
  // document.body.appendChild(a);
  // a.click();
  // document.body.removeChild(a);
  // URL.revokeObjectURL(url); // Clean up the URL object
}

// Call the function to load events when the page loads
window.addEventListener("DOMContentLoaded", loadEvents);
window.addEventListener("DOMContentLoaded", initDownload);