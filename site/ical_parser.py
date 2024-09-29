from icalendar import Calendar, Event
import os

files = ["catholic-campus-ministry-mass.ics", "screenshot-asia-film-festival-the-day-of-reckoning.ics"]

def combine_ics(files, output_file):
    combined_calendar = Calendar()

    for file_path in files:
        with open(file_path, 'r') as ics_file:
            # Read and parse the ICS file
            ics_content = ics_file.read()
            calendar = Calendar.from_ical(ics_content)

            # Append each event to the combined calendar
            for component in calendar.walk():
                if component.name == "VEVENT":
                    combined_calendar.add_component(component)

    # Write the combined calendar to the output file
    with open(output_file, 'wb') as output:
        output.write(combined_calendar.to_ical())

combine_ics(files, "out.ics")