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



  // fetch("full_output.json")
  //   .then((response) => response.json())
  //   .then((data) => 
  //     )

    // .catch((error) => console.error("Error loading events:", error));

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