import requests
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger.info('Started')

url = r"https://breadboard-community.wl.r.appspot.com/boards/@AdorableFox/calico2.bgl.api/run"


#toSend = {
#            "$key": "bb-1d34543t634r5lln245o6g1n1h1w5j635t5ega1n1o64115x49",
#            "context" : [
#                            {
#                                "role": "user",
#                                "text": json.dumps([{"id": 0, "title": "SCREENSHOT: Asia Film Festival: The Day of Reckoning"}, {"id": 1, "title": "SCREENSHOT: Asia Film Festival: Great Absence"}, {"id": 2, "title": "SCREENSHOT: Asia Film Festival: Girls will be Girls"}, {"id": 3, "title": "Pitt-Johnstown Catholic Campus Ministry Mass"}, {"id": 4, "title": "Pitt-Johnstown Sunday Night Experience"}, {"id": 5, "title": "ChangeMaker Series (Fall 2024) Registration Day"}, {"id": 6, "title": "Broken Ground"}, {"id": 7, "title": "For All the People: A Century of Citizen Action in Health Care Reform"}, {"id": 8, "title": "Joe Magarac Returns"}, {"id": 9, "title": "Pitt-Johnstown Esports Competition"}, {"id": 10, "title": "Pitt-Johnstown Men's Golf vs Pitt-Johnstown Sunnehanna Collegiate"}, {"id": 11, "title": "Rewilding"}, {"id": 12, "title": "Applied Micro Brown Bag, Gabby Toborg and Mardo Ayitchehou, University of Pittsburgh, \"Using Textract and ChatGPT to digitize FHA Mortgages\""}, {"id": 13, "title": "Meditation Mondays at Heinz Chapel"}, {"id": 14, "title": "NSF I-Corps Regional Short Course"}, {"id": 15, "title": "Pollinators & Native Seeds Walk"}, {"id": 16, "title": "Preparing for Your Academic Advising Appointment"}, {"id": 17, "title": "The Animal Research Protection Division and its Many Roles"}, {"id": 18, "title": "Promotion in Academic Medicine for Women Series"}, {"id": 19, "title": "Making Connections (C4CxUCC)"}, {"id": 20, "title": "Labor & Development Seminar, Jing Cai, University of Maryland, \"Firm-to-Firm Referrals\""}, {"id": 21, "title": "Econometrics Seminar, Marcelo Moreira, Professor of Economics, Funda\u00e7\u00e3o Get\u00falio Vargas (FGV/EPGE), \"Inference Based on the Continuously Updating Estimator and the CLR Test\" (w/ Whitney Newey and Mahrad Sharifvaghefi)"}, {"id": 22, "title": "Bioastronautics Journal Club"}, {"id": 23, "title": "On the Acceptability of Preselection for Autistic Children"}, {"id": 24, "title": "Pitt Social Work Alumni Speaker Series: MSW to JD: Making the Case"}, {"id": 25, "title": "Pittsburgh Contemporary Writer Series (PCWS) Presents: Ingrid Rojas Contreras and Isabella Hammad"}, {"id": 26, "title": "Pop-Up Course"}, {"id": 27, "title": "What's Driving the Affordable Housing Crisis? Film Screening"}, {"id": 28, "title": "Johnny Cupcakes Visits Pittsburgh at The University Store on Fifth"}, {"id": 29, "title": "Broken Ground"}, {"id": 30, "title": "For All the People: A Century of Citizen Action in Health Care Reform"}, {"id": 31, "title": "Joe Magarac Returns"}, {"id": 32, "title": "LifeSolutions Webinar: Investing 101"}, {"id": 33, "title": "Pitt-Johnstown Esports Competiton"}, {"id": 34, "title": "Pitt-Johnstown Men's Golf vs Pitt-Johnstown Sunnehanna Collegiate"}, {"id": 35, "title": "Rewilding"}, {"id": 36, "title": "Orientation to Research Fundamentals (ORF)"}, {"id": 37, "title": "Allegheny County Financial Empowerment Center Financial Resources Office Hours"}, {"id": 38, "title": "Provost's Office Hours"}, {"id": 39, "title": "Health Informatics (MS) Virtual Information Session"}, {"id": 40, "title": "What is Research?"}, {"id": 41, "title": "Ask A Therapist - Virtual Tuesdays"}, {"id": 42, "title": "Department of Cell Biology Seminar:   Interplay between mitochondrial dysfunction and cell division"}, {"id": 43, "title": "Onco-Nephrology Conference Series"}, {"id": 44, "title": "Thunderbird Trilogy Author and Translator Talk"}, {"id": 45, "title": "Fall 2024 Global Distinction Drop-In Hours"}, {"id": 46, "title": "HPM Seminar: Katherine Callaway Kim"}, {"id": 47, "title": "Introduction to ChatGPT Prompt Engineering for Teaching"}, {"id": 48, "title": "Microeconomic Theory Brown Bag, Xinyang Wang, ITAM, \"Choosing the Right Pond: Status vs. Prestige in School Choice & Party Formation\""}, {"id": 49, "title": "Resources for SHRS Online and Hybrid Graduate Students"}, {"id": 50, "title": "Writing a Data Management and Sharing Plan with DMPTool"}, {"id": 51, "title": "LTT:  Eric Snyder - Is Knowledge of Successor Due to Knowledge of Morphosyntax?"}, {"id": 52, "title": "Agile Project Management in Software Development"}, {"id": 53, "title": "CTSI Research Facilitator Office Hours"}, {"id": 54, "title": "Introduction to LabArchives Scheduler"}, {"id": 55, "title": "Protecting your savings: How to recognize and prevent account takeover schemes (By TIAA)"}, {"id": 56, "title": "Interpersonal Effectiveness Skills Workshop"}, {"id": 57, "title": "PQI Distinguished Seminars in Quantum Science & Engineering - Nathalie de Leon"}, {"id": 58, "title": "From Inbox to Impact: Essential Skills for Successful Emails"}, {"id": 59, "title": "Pitt Votes Tabling"}, {"id": 60, "title": "CommUniversity: Creative Nonfiction"}, {"id": 61, "title": "Movie Screening & Panel Discussion - Seeing the Unseen: Aquatic Invaders & What is at Stake"}, {"id": 62, "title": "Never A Spectator - Smart Advocacy"}, {"id": 63, "title": "Photoshop and Illustrator Community of Practice"}, {"id": 64, "title": "Undergraduate Research and Creative Expression Fair"}, {"id": 65, "title": "Fiber Art: Knit"}, {"id": 66, "title": "Pitt-Johnstown Protestant Campus Ministry Bible Study"}, {"id": 67, "title": "Pitt-Johnstown Faith Share"}, {"id": 68, "title": "PittVotes Vice-Presidential Debate Watch Pajama Party"}, {"id": 69, "title": "Assessment and Teaching Pre-Conference Session"}, {"id": 70, "title": "Broken Ground"}, {"id": 71, "title": "For All the People: A Century of Citizen Action in Health Care Reform"}, {"id": 72, "title": "Joe Magarac Returns"}, {"id": 73, "title": "Pitt-Johnstown Esports Competition"}, {"id": 74, "title": "Rewilding"}, {"id": 75, "title": "Orientation to Research Fundamentals (ORF)"}, {"id": 76, "title": "Bridge to Success: LinkedIn & Portfolio Workshop"}, {"id": 77, "title": "LGBTQIA+ Peer Support Space"}, {"id": 78, "title": "Fall 2024 Flu Shot Clinics"}, {"id": 79, "title": "Africana Studies: Renewing the Fight for Justice Webinar Series"}, {"id": 80, "title": "CCM Grand Rounds- Jacqueline Kruser, MD"}, {"id": 81, "title": "Fostering a Culture of Continuous Quality Improvement - webinar"}, {"id": 82, "title": "Nationality Rooms and Intercultural Exchange Programs Scholarships Info Session"}, {"id": 83, "title": "Sports Science (MS) Application Overview"}, {"id": 84, "title": "VMI/HVI Research Conference"}, {"id": 85, "title": "From Southport to Social Unrest: Insights on Countering Political Violence from the UK\u2019s 2024 Riots"}, {"id": 86, "title": "MyHealth Kitchen Apple Quinoa Salad"}, {"id": 87, "title": "Doctor of Physical Therapy Virtual Information Session"}, {"id": 88, "title": "Experimental/Behavioral Brown Bag, Yucheng Liang, Carnegie Mellon University, \"A Project on Censorship\u201d"}, {"id": 89, "title": "Nourish Peer Support Space"}, {"id": 90, "title": "Labor & Development Brown Bag, Brianna Funderburk, University of Pittsburgh, \u201cThe Impact of Charter School Expansion on Special Education Funding in Traditional Public School Districts.\u201d"}, {"id": 91, "title": "Labor & Development Brown Bag, Marcela Camargo, University of Pittsburgh, \"The Effects of Large Infrastructure Projects in Brazil\""}, {"id": 92, "title": "The Black Instructors Affinity Group Meeting #1"}, {"id": 93, "title": "Soundcraft Studio"}, {"id": 94, "title": "Midterm Mindfulness: Calming your Thoughts"}, {"id": 95, "title": "Money Moves for Moving Off Campus"}, {"id": 96, "title": "African Languages Conversation Hour"}, {"id": 97, "title": "Selling @ Pitt"}, {"id": 98, "title": "Pitt-Johnstown Men's Soccer at Lock Haven Univeristy"}, {"id": 99, "title": "Top-Roping 101"}, {"id": 100, "title": "Broken Ground"}, {"id": 101, "title": "For All the People: A Century of Citizen Action in Health Care Reform"}, {"id": 102, "title": "Joe Magarac Returns"}, {"id": 103, "title": "Pitt-Johnstown Esports Competition"}, {"id": 104, "title": "Rewilding"}, {"id": 105, "title": "Orientation to Research Fundamentals (ORF)"}, {"id": 106, "title": "Data & Literature Club"}, {"id": 107, "title": "Fall 2024 Flu Shot Clinics"}, {"id": 108, "title": "Departmental Networking"}, {"id": 109, "title": "MEMS Graduate Seminar - Dr. Peter Hosemann"}, {"id": 110, "title": "R/Python Office Hours"}, {"id": 111, "title": "EPI Seminar: Life\u2019s Essential 8: Does improving sleep really promote cardiovascular health?"}, {"id": 112, "title": "Dialogic Pedagogy in the University Classroom"}, {"id": 113, "title": "Gilman Writing Workshop 2"}, {"id": 114, "title": "UPMC MyHealth Less Stress Program"}, {"id": 115, "title": "Using Academic Feedback in College"}, {"id": 116, "title": "Dialogue with Faculty from the Epidemiology Area of Emphasis"}, {"id": 117, "title": "Once You Breathed"}, {"id": 118, "title": "Ask A Therapist - Virtual Thursdays"}, {"id": 119, "title": "Best Practices for Issuing and Managing Referrals"}, {"id": 120, "title": "Introduction to LabArchives for Researchers"}, {"id": 121, "title": "Becoming an Off-Campus Student"}, {"id": 122, "title": "Digitization Drop-in Hour"}, {"id": 123, "title": "Optimizing Clinical Trials at Health Systems: The Opportunity for AI"}, {"id": 124, "title": "IE SEMINAR: Amulya Yadav, \"Explainable AI for Non-Profits: Consistently Crossing the Bridge from Development to Deployment\""}, {"id": 125, "title": "Microeconomic Theory Seminar, Aaron Kolb, Economics, University of Indiana Bloomington, \u201cThe Design and Price of Influence\u201d"}, {"id": 126, "title": "Seminar - Martin Zhang"}, {"id": 127, "title": "Bioengineering Seminar: Dr. Anton Bowden"}, {"id": 128, "title": "Geology & Environmental Science Colloquium: Dr. Vikas Khanna"}, {"id": 129, "title": "Hope for Handwriting"}, {"id": 130, "title": "Pitt Votes Tabling"}, {"id": 131, "title": "Anesthesiology Journal Club: Noninvasive Ventilation for Preoxygenation during Emergency Ventilation"}, {"id": 132, "title": "Opening Reception: Fall Exhibitions"}, {"id": 133, "title": "Documentary Screening -RADICAL HARMONIES with Boden Sandstrom"}, {"id": 134, "title": "Natural Hair Discrimination Community Forum"}, {"id": 135, "title": "Doctor of Chiropractic Virtual Information Session"}, {"id": 136, "title": "Pitt Johnstown TimeOut Christian Fellowship"}, {"id": 137, "title": "Pitt-Johnstown Program Board: PUMPKIN HUNT"}, {"id": 138, "title": "A Night of Unleashed Wonder"}, {"id": 139, "title": "Broken Ground"}, {"id": 140, "title": "For All the People: A Century of Citizen Action in Health Care Reform"}, {"id": 141, "title": "Joe Magarac Returns"}, {"id": 142, "title": "Pitt-Johnstown Esports Competition"}, {"id": 143, "title": "Rewilding"}, {"id": 144, "title": "Pitt AuD Friday Audiology Seminar Series"}, {"id": 145, "title": "Assessment and Teaching Conference"}, {"id": 146, "title": "CHE Focused Writing Sessions"}, {"id": 147, "title": "'All of Us' Office Hours"}, {"id": 148, "title": "Colloquium-Dr. John Ruiz, Professor, Clinical Health Psychology, The University of Arizona"}, {"id": 149, "title": "Mitochondrial Adenine Nucleotide Translocase drives Chronic Obstructive Pulmonary Disease and Idiopathic Pulmonary Fibrosis"}, {"id": 150, "title": "LTT:  Tushar Menon - Scientific realism as a normative notion (twice over)"}, {"id": 151, "title": "Bangladesh's Student Revolt History, Today, and Tomorrow"}, {"id": 152, "title": "Human Genetics Seminar - Jennifer Eichmeyer, MS, CGC"}, {"id": 153, "title": "IRB 101: Exempt and Expedited Studies"}, {"id": 154, "title": "Mentoring Academy - Session Two (virtual)"}, {"id": 155, "title": "Nature in Action: Urban Hike"}, {"id": 156, "title": "Center for Health Equity Journal Club"}, {"id": 157, "title": "The Therapeutic Application of Medium Chain Acyl-Carnitines for Genetic Disorders of Long Chain Fatty Acid Oxidation"}, {"id": 158, "title": "Accelerated Second Degree Information Session [In-Person]"}, {"id": 159, "title": "Big Idea Blitz"}, {"id": 160, "title": "Scholar Spotlight - Search for the elusive haplotype of the APOE polymorphism associated with Alzheimer's disease"}, {"id": 161, "title": "Department of Communication - Agora Speaker Series"}, {"id": 162, "title": "Macroeconomics Seminar, Yan Bai, University of Rochester, \"World Financial Cycles\""}, {"id": 163, "title": "Audiology Information Sessions"}, {"id": 164, "title": "Pitt-Johnstown Women's Volleyball vs Edinboro"}, {"id": 165, "title": "Bouldering Basics"}, {"id": 166, "title": "Global Health Case Competition: Application Deadline"}, {"id": 167, "title": "Pitt-Johnstown Program Board ON THE ROAD: Trip to Washington DC"}, {"id": 168, "title": "WORKSHOP: Understanding the History of Redlining"}, {"id": 169, "title": "Michael R. Bennett Memorial Philosophy Workshop"}, {"id": 170, "title": "School of Nursing: Blue & Gold Day"}, {"id": 171, "title": "Fraternity and Sorority Life 101"}, {"id": 172, "title": "STEAM Saturdays"}, {"id": 173, "title": "Heritage Kitchen: Food Presented by the Yugoslav Room Committee"}, {"id": 174, "title": "Pitt-Johnstown Men's Soccer vs Seton Hill University"}, {"id": 175, "title": "Pitt-Johnstown Women's Volleytball  vs Gannon University"}, {"id": 176, "title": "Pitt-Johnstown Catholic Campus Ministry Mass"}, {"id": 177, "title": "Pitt-Johnstown Sunday Night Experience"}, {"id": 178, "title": "Kuzneski Innovation Cup Application Day"}, {"id": 179, "title": "Broken Ground"}, {"id": 180, "title": "Joe Magarac Returns"}, {"id": 181, "title": "National Voter Education Week"}, {"id": 182, "title": "Pitt Law Week 2024"}, {"id": 183, "title": "Pitt-Johnstown Esports Competition"}, {"id": 184, "title": "Pitt-Johnstown Men's Golf at Gannon University Bud Elwell Invitational"}, {"id": 185, "title": "Rewilding"}, {"id": 186, "title": "Painless PubMed"}, {"id": 187, "title": "Commuter Check-In"}, {"id": 188, "title": "Meditation Mondays at Heinz Chapel"}, {"id": 189, "title": "Preparing for Spring Term Financial Aid for SHRS Graduate Students"}, {"id": 190, "title": "Making Connections (C4CxUCC)"}, {"id": 191, "title": "Ask A Therapist - In-Person Mondays"}, {"id": 192, "title": "Pitt-CMU Colloquium: Clarice Aiello (UCLA)"}, {"id": 193, "title": "School of Nursing: BSN Zoom Info Session"}, {"id": 194, "title": "Pop-Up Course"}, {"id": 195, "title": "DNP Nurse Anesthesia Information Session [Virtual]"}, {"id": 196, "title": "Doctor of Occupational Therapy (OTD) Information Sessions"}, {"id": 197, "title": "Broken Ground"}, {"id": 198, "title": "Joe Magarac Returns"}, {"id": 199, "title": "National Voter Education Week"}, {"id": 200, "title": "Pitt Law Week 2024"}, {"id": 201, "title": "Pitt-Johnstown Esports Competiton"}, {"id": 202, "title": "Rewilding"}, {"id": 203, "title": "OB Anesthesiology & Women's Health Grand Rounds: Special Guest Lecture"}, {"id": 204, "title": "Allegheny County Financial Empowerment Center Financial Resources Office Hours"}, {"id": 205, "title": "Fall 2024 Flu Shot Clinics"}, {"id": 206, "title": "Six Strategies for Effective Database Searching"}, {"id": 207, "title": "Qualtrics Basics: Create Your Own Online Surveys"}, {"id": 208, "title": "Ask A Therapist - Virtual Tuesdays"}, {"id": 209, "title": "Fall 2024 Flu Shot Clinics"}, {"id": 210, "title": "LTT: Carl Hoefer - Generic causation in complex, mind-dependent systems"}, {"id": 211, "title": "Building Career Competencies from Experiences"}, {"id": 212, "title": "Fall 2024 Global Distinction Drop-In Hours"}, {"id": 213, "title": "Graduate Workshop Series: Grad School 1-on-1"}, {"id": 214, "title": "Microeconomic Theory Brown Bag, Siyuan Fan, University of Pittsburgh"}, {"id": 215, "title": "Pitt Space Lunch and Learn Seminar"}, {"id": 216, "title": "Preserving Democracy. NATO at 75 and the Importance of Alliances in U.S. Foreign Policy:  A Lawyer's View"}, {"id": 217, "title": "RCR: Evaluating Generative AI for your Research Workflow"}, {"id": 218, "title": "Water in a Changing World"}, {"id": 219, "title": "Alebrijes workshop for staff, faculty, students and community"}, {"id": 220, "title": "Introduction to LabArchives Inventory"}, {"id": 221, "title": "Online Water Cooler for Remote and Hybrid Workers"}, {"id": 222, "title": "Visiting Scholar Series: Francesca Royster"}, {"id": 223, "title": "CommUniversity: Creative Nonfiction"}, {"id": 224, "title": "PQI Distinguished Seminars in Quantum Science & Engineering - Emily Davis"}, {"id": 225, "title": "Photoshop and Illustrator Community of Practice"}, {"id": 226, "title": "Understanding Credit"}, {"id": 227, "title": "education & The Black Fantastic"}, {"id": 228, "title": "Dr. Steffen H\u00f6hne, \"Bohemia, Prague and Kafka. Intercultural Contexts in Central Europe\""}, {"id": 229, "title": "Found Film: Creating a Collage Movie"}, {"id": 230, "title": "Prosthetics and Orthotics Virtual Information Session - Student Panel"}, {"id": 231, "title": "Health Informatics (MS) Virtual Information Session"}, {"id": 232, "title": "Pitt-Johnstown Protestant Campus Ministry Bible Study"}, {"id": 233, "title": "Pitt-Johnstown Faith Share"}, {"id": 234, "title": "Broken Ground"}, {"id": 235, "title": "Joe Magarac Returns"}, {"id": 236, "title": "National Voter Education Week"}, {"id": 237, "title": "Pitt Law Week 2024"}, {"id": 238, "title": "Pitt-Johnstown Esports Competition"}, {"id": 239, "title": "Rewilding"}, {"id": 240, "title": "Fall 2024 Flu Shot Clinics"}, {"id": 241, "title": "Pitt Votes Tabling"}, {"id": 242, "title": "Basic EndNote"}, {"id": 243, "title": "Microsoft PowerPoint: Punch Up Your Presentation"}, {"id": 244, "title": "Aphasia Support Group"}, {"id": 245, "title": "Greater Pittsburgh Law Fair"}, {"id": 246, "title": "Rehabilitation Science (BS) Virtual Information Session"}, {"id": 247, "title": "AI in Action: Incorporating Technology Into Professional Development"}, {"id": 248, "title": "How to Network and Compose a Resume"}, {"id": 249, "title": "Latinx and Hispanic Heritage Month Celebration: Leveraging Cultural Competency for Student Success"}, {"id": 250, "title": "Nutrition Science (BS) Program Information Session"}, {"id": 251, "title": "Quarterly economic and market update (By TIAA)"}, {"id": 252, "title": "VMI/HVI Research Conference"}, {"id": 253, "title": "MyHealth Get up and Go Stretching"}, {"id": 254, "title": "Care Talk: Financial Wellness - Planning Your Financial Future"}, {"id": 255, "title": "Engagement Intersections: Community Research Partnerships Tackling Regional Water Issues"}, {"id": 256, "title": "Experimental/Behavioral Brown Bag, Aniol Llorente-Saguer, Queen Mary of London, \u201cWeighted Voting: Rule Complexity and Information Aggregation\u201d"}, {"id": 257, "title": "Introduction to LabArchives for Education"}, {"id": 258, "title": "U.S. Government Accountability Office Information Session & Alumni Panel"}, {"id": 259, "title": "Labor & Development Brown Bag, Bruno K\u00f6mel, University of Pittsburgh"}, {"id": 260, "title": "Labor & Development Brown Bag, Priyoma Mustafi, University of Pittsburgh"}, {"id": 261, "title": "Data Transparency and Privacy in Generative AI Tools"}, {"id": 262, "title": "Nature Workshop: Mindfulness and Shrin Yoku (Forest Bathing)"}, {"id": 263, "title": "BIPOC Peer Support Space"}, {"id": 264, "title": "African Languages Conversation Hour"}, {"id": 265, "title": "An Overstuffed History of the Jewish Deli"}, {"id": 266, "title": "Italian Program Open House"}, {"id": 267, "title": "Pitt Social Work PhD Degree Virtual  Information Session"}, {"id": 268, "title": "Pitt-Johnstown Men's Soccer at California (PA)"}, {"id": 269, "title": "Trivia Night with FHC"}, {"id": 270, "title": "Pitt-Johnstown Women's Soccer at Clarion"}, {"id": 271, "title": "'Like Being inside a Rainbow': the Stained Glass of Charles J. Connick"}, {"id": 272, "title": "University of Pittsburgh Symphony Orchestra"}, {"id": 273, "title": "Broken Ground"}, {"id": 274, "title": "Joe Magarac Returns"}, {"id": 275, "title": "National Voter Education Week"}, {"id": 276, "title": "Pitt-Johnstown Esports Competition"}, {"id": 277, "title": "Rewilding"}, {"id": 278, "title": "Read & Discuss: All That She Carried by Tiya Miles"}, {"id": 279, "title": "Advancing Trust in Science: Institutional Obligations to Promote Research Integrity"}, {"id": 280, "title": "Pediatric Grand Rounds Eugene S. Wiener Memorial Lecture"}, {"id": 281, "title": "The Palliative Research Center (PaRC) Annual Retreat - From Hospital to Home: Setting the Agenda for Serious Illness Research in Our Communities"}, {"id": 282, "title": "Dissertation Defense - Zijian Huang"}, {"id": 283, "title": "Accelerated Second Degree Information Session [Virtual]"}, {"id": 284, "title": "Data & Literature Club"}, {"id": 285, "title": "Emprendedoras Latinas en Pittsburgh: Stories of Successful Latinas Entrepreneurs"}, {"id": 286, "title": "Mindfulness Skills Workshop"}, {"id": 287, "title": "Departmental Networking"}, {"id": 288, "title": "R/Python Office Hours"}, {"id": 289, "title": "EPI Seminar: Targeting the Subclinical Vascular Contributions to Brain Aging and Alzheimer\u2019s Disease"}, {"id": 290, "title": "Teaching With PowerPoint"}, {"id": 291, "title": "UPMC MyHealth Less Stress Program"}, {"id": 292, "title": "Dialogue with Faculty from the Epidemiology Area of Emphasis"}, {"id": 293, "title": "Stories that Reflect and Heal: Young Women\u2019s Suicide and Care in South Korea"}, {"id": 294, "title": "Ask A Therapist - Virtual Thursdays"}, {"id": 295, "title": "Introduction to LabArchives for Researchers"}, {"id": 296, "title": "Digitization Drop-in Hour"}, {"id": 297, "title": "LGBTQIA+ History Month Open House"}, {"id": 298, "title": "Nature in Action: Bike Ride"}, {"id": 299, "title": "Nature in Action: Bike Ride"}, {"id": 300, "title": "Build Your Own Charcuterie Board!"}, {"id": 301, "title": "Creating Cartoneras with Pantera Cartonera @ Pitt"}, {"id": 302, "title": "All Angles - Overcoming Polarization Beginning with How We Think"}, {"id": 303, "title": "Aging Institute Seminar Series"}, {"id": 304, "title": "Bioengineering Seminar: Bioengineering Cell-based Therapeutics"}, {"id": 305, "title": "Collegiate Recovery Peer Support Space"}, {"id": 306, "title": "International Student Support Space"}, {"id": 307, "title": "Navigating Work Authorization as an International SHRS Student"}, {"id": 308, "title": "Hope for Handwriting"}, {"id": 309, "title": "Speech-Language Pathology (MA/MS) Information Session"}, {"id": 310, "title": "Ask A Therapist - In-Person Thursdays"}, {"id": 311, "title": "Start Smart Legal Series Session: How to Handle Your (and Others') Intellectual Property"}, {"id": 312, "title": "\u201cHow to Handle Your (and Others\u2019) Intellectual Property\u201d Start Smart Legal Session"}, {"id": 313, "title": "Adaptation - Local Notes"}, {"id": 314, "title": "Tackling Tough Convos Workshop"}])
#                                
#                            }
#                        ]
#                    }
#
##json.dumps("{$key: "bb-1d34543t634r5lln245o6g1n1h1w5j635t5ega1n1o64115x49"}")
#
#response = requests.request(method="POST",url=url,json=toSend)
#print(response.text)
#response = json.loads(response.text[6:])
#next = response[-1]
#print(next)
#
#toSend1= {
#            "$key": "bb-1d34543t634r5lln245o6g1n1h1w5j635t5ega1n1o64115x49",
#            "$next":next,
#            "context" : [
#                            {
#                                "role": "user",
#                                "parts": [{ "text": str(input()) }]
#                            }
#                        ]
#        }
#response = requests.request(method="POST",url=url,json=toSend1)
#print(response.text)
#response = json.loads(response.text[6:])
#print(response[1]['outputs']['context'][1]['parts'][0]['text'])

def getEvents(userRequirements, dataFileLight, dataFileFull, attempts=0):
    file = open(dataFileLight, "r")
    data = file.read()
    logger.debug(data)
    toSend = {
            "$key": "bb-1d34543t634r5lln245o6g1n1h1w5j635t5ega1n1o64115x49",
            "context" : [
                            {
                                "role": "user",
                                "text": data
                            }
                        ]
                    }
    response = requests.request(method="POST",url=url,json=toSend)
    logger.info("sent request")
    logger.debug(response.text)
    response = json.loads(response.text[6:])
    next = response[-1]
    logger.debug(next)
    toSend1= {
                "$key": "bb-1d34543t634r5lln245o6g1n1h1w5j635t5ega1n1o64115x49",
                "$next":next,
                "context" : [
                                {
                                    "role": "user",
                                    "parts": [{ "text": str(userRequirements) }]
                                }
                            ]
            }
    response = requests.request(method="POST",url=url,json=toSend1)
    logger.debug(response.text)
    response = json.loads(response.text[6:])
    eventIds = response[1]['outputs']['context'][1]['parts'][0]['text']
    eventIds = eventIds.split(',')
    try:
        eventIds = [int(i) for i in eventIds]
    except:
        if(attempts<5):
            getEvents(userRequirements,dataFileLight, dataFileFull, ++attempts)
        else:
            logger.error(msg="Number of attempts exceeded 5, prompt is probably poor")
    file.close()
    file = open(dataFileFull, "r")
    events = json.load(file)
    toReturn = []
    for i in events:
        if i["id"] in eventIds:
            toReturn.append(i)
    return toReturn

