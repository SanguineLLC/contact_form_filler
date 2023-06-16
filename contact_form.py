import requests

# Read the list of websites from the file
with open("list.txt", "r") as file:
    websites = file.read().splitlines()

# Iterate over each website and fill out the contact form
for website in websites:
    # Replace "YOUR_CONTACT_DETAILS" with the appropriate values
    contact_details = {
        "name": "Jason  Gilbert ",  # Replace with the name or first and last name
        "subject": "Real Estate Transaction",
        "email": "sales@thebrickpit.co",
        "message": "Please would you be able to represent us in a real estate transaction? We are about to purchase a new property at the moment and would need your legal advice and if possible you can assist us in the real estate transaction. Please let me know when we can set up a phone call or come over to your office. I can also send the sales agreement and the two parties involved for conflict check. . Thank you for your assistance. Please stay safe."
    }

    # Make a POST request to the website's contact form
    response = requests.post(website, data=contact_details)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Contact form submitted successfully for {website}")
    else:
        print(f"Failed to submit contact form for {website}")
