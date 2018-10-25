## gree story
* greet
    - utter_greet

## gree and default story
* greet
    - utter_greet
* default
    - utter_default
    - utter_goodbye
    - action_goodbye
    - export

## default story
* default
    - utter_default
    - utter_goodbye
    - action_goodbye
    - export

## Goodbye story
* goodbye
    - utter_goodbye
    - action_goodbye
## Generated Story -3065047515619587552 Mail  with no reset
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* goodbye{"budget": "600"}
    - slot{"budget": "600"}
    - slot{"lat": 18.520469}
    - slot{"lon": 73.85662}
    - slot{"city_id": 5}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"7\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"],\"10\":[\"GeoBistro\",\"Row House 2, Nand Gaon, Clover Park, Datta Mandir Chowk, Behind Phoenix Market City, Viman Nagar, Pune\",\"1300\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "pune"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"7\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"],\"10\":[\"GeoBistro\",\"Row House 2, Nand Gaon, Clover Park, Datta Mandir Chowk, Behind Phoenix Market City, Viman Nagar, Pune\",\"1300\",\"4.6\"]}"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - action_send_email
    - slot{"email": "test@gmail.com"}
    - utter_goodbye
    - action_goodbye
    - export
## Generated Story -3065047515619587552 Mail  with slot reset
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* goodbye{"budget": "600"}
    - slot{"budget": "600"}
    - slot{"lat": 18.520469}
    - slot{"lon": 73.85662}
    - slot{"city_id": 5}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"7\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"],\"10\":[\"GeoBistro\",\"Row House 2, Nand Gaon, Clover Park, Datta Mandir Chowk, Behind Phoenix Market City, Viman Nagar, Pune\",\"1300\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "pune"}
    - slot{"api_response": "{\"1\":[\"Laa Unico\",\"Arihant Aura Building, Above Comet Stationery, Next to Sujay Garden, Commercial Complex, Near Laxmi Narayan Theatre, Mukundnagar, Swargate, Pune\",\"1100\",\"4.8\"],\"2\":[\"Chili's American Grill & Bar\",\"UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune\",\"1400\",\"4.8\"],\"3\":[\"Agent Jack's\",\"Ground Floor, Kapila Matrix, Koregaon Park Annexe, Mundhwa, Pune\",\"1300\",\"4.7\"],\"4\":[\"Cafe 1730\",\"21/1, Serene Bay, Lane 6, Off North Main Road, Koregaon Park, Pune\",\"1500\",\"4.6\"],\"5\":[\"Darshan\",\"759/60, Prabhat Road, Opposite Indian Bank, Deccan Gymkhana, Pune\",\"700\",\"4.6\"],\"6\":[\"Baraza Bars & Bites\",\"Unit 10, Pubtown, Creaticity Mall, Shastri Nagar, Yerawada, Pune\",\"1400\",\"4.6\"],\"7\":[\"Effingut Brewerkz\",\"End of Lane Number 6, Koregaon Park, Pune\",\"1700\",\"4.6\"],\"8\":[\"Hard Rock Cafe\",\"81/82, East Main Road, Koregaon Park Extension, Mundhwa, Pune\",\"2500\",\"4.6\"],\"9\":[\"Agent Jack's\",\"West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune\",\"1300\",\"4.6\"],\"10\":[\"GeoBistro\",\"Row House 2, Nand Gaon, Clover Park, Datta Mandir Chowk, Behind Phoenix Market City, Viman Nagar, Pune\",\"1300\",\"4.6\"]}"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - action_send_email
    - slot{"email": "test@gmail.com"}
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story 9088986941805542097 No-mail with no reset
* greet
    - utter_greet
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "1200"}
    - slot{"budget": "1200"}
    - slot{"lat": 23.25}
    - slot{"lon": 77.4167}
    - slot{"city_id": 26}
    - slot{"cuisine_key": "55"}
    - slot{"api_response": "{\"1\":[\"The Public House Caf\u00e9 n Restaurant\",\"Mahadev Complex, Lower Ground Floor, Shivaji Nagar Opposite Board Office, Maharana Pratap Nagar, Bhopal\",\"800\",\"4.8\"],\"2\":[\"La Kuchina - Jehan Numa Palace\",\"157, Hotel Jehan Numa Palace, Shymala Hills, TT Nagar, Bhopal\",\"2200\",\"4.5\"],\"3\":[\"Olive & Honey Restaurant\",\"Shaan-e-Fiza Apartment, New Saifia College Road, Housing Board Colony, Kohefiza, Bhopal\",\"600\",\"4.2\"],\"4\":[\"The Urban Socialite\",\"5th Floor, Hotel Lake View Ashoka, Shyamla Hills, TT Nagar, Bhopal\",\"900\",\"4.1\"],\"5\":[\"Momo Cafe - Courtyard Marriot\",\"Courtyard By Marriot, 4th Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\",\"1000\",\"4.1\"],\"6\":[\"Da pizzeria\",\"177, Zone 2, Maharana Pratap Nagar, Bhopal\",\"500\",\"4.0\"],\"7\":[\"Greek Food & Beyond\",\"Third Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\",\"1000\",\"4.0\"],\"8\":[\"Domino's Pizza\",\"Aashima Mall, Food Court, Gulmohar Colony, Bhopal Hoshangabad Road\",\"700\",\"3.9\"],\"9\":[\"Pizza Inn\",\"Opposite Petrol Pump, Yamana Square, Polytechnic Square, Kamla Park Road, TT Nagar, Bhopal\",\"450\",\"3.9\"],\"10\":[\"Domino's Pizza\",\"27, Navri Road, Lal Ghati, Airport Area, Bhopal\",\"700\",\"3.8\"]}"}
    - action_restaurant
    - slot{"location": "bhopal"}
    - slot{"api_response": "{\"1\":[\"The Public House Caf\u00e9 n Restaurant\",\"Mahadev Complex, Lower Ground Floor, Shivaji Nagar Opposite Board Office, Maharana Pratap Nagar, Bhopal\",\"800\",\"4.8\"],\"2\":[\"La Kuchina - Jehan Numa Palace\",\"157, Hotel Jehan Numa Palace, Shymala Hills, TT Nagar, Bhopal\",\"2200\",\"4.5\"],\"3\":[\"Olive & Honey Restaurant\",\"Shaan-e-Fiza Apartment, New Saifia College Road, Housing Board Colony, Kohefiza, Bhopal\",\"600\",\"4.2\"],\"4\":[\"The Urban Socialite\",\"5th Floor, Hotel Lake View Ashoka, Shyamla Hills, TT Nagar, Bhopal\",\"900\",\"4.1\"],\"5\":[\"Momo Cafe - Courtyard Marriot\",\"Courtyard By Marriot, 4th Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\",\"1000\",\"4.1\"],\"6\":[\"Da pizzeria\",\"177, Zone 2, Maharana Pratap Nagar, Bhopal\",\"500\",\"4.0\"],\"7\":[\"Greek Food & Beyond\",\"Third Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\",\"1000\",\"4.0\"],\"8\":[\"Domino's Pizza\",\"Aashima Mall, Food Court, Gulmohar Colony, Bhopal Hoshangabad Road\",\"700\",\"3.9\"],\"9\":[\"Pizza Inn\",\"Opposite Petrol Pump, Yamana Square, Polytechnic Square, Kamla Park Road, TT Nagar, Bhopal\",\"450\",\"3.9\"],\"10\":[\"Domino's Pizza\",\"27, Navri Road, Lal Ghati, Airport Area, Bhopal\",\"700\",\"3.8\"]}"}
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - action_goodbye
    - export
## Generated Story with slot reset
* greet
    - utter_greet
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "1200"}
    - slot{"budget": "1200"}
    - slot{"lat": 23.25}
    - slot{"lon": 77.4167}
    - slot{"city_id": 26}
    - slot{"cuisine_key": "55"}
    - slot{"api_response": "{\"1\":[\"The Public House Caf\u00e9 n Restaurant\",\"Mahadev Complex, Lower Ground Floor, Shivaji Nagar Opposite Board Office, Maharana Pratap Nagar, Bhopal\",\"800\",\"4.8\"],\"2\":[\"La Kuchina - Jehan Numa Palace\",\"157, Hotel Jehan Numa Palace, Shymala Hills, TT Nagar, Bhopal\",\"2200\",\"4.5\"],\"3\":[\"Olive & Honey Restaurant\",\"Shaan-e-Fiza Apartment, New Saifia College Road, Housing Board Colony, Kohefiza, Bhopal\",\"600\",\"4.2\"],\"4\":[\"The Urban Socialite\",\"5th Floor, Hotel Lake View Ashoka, Shyamla Hills, TT Nagar, Bhopal\",\"900\",\"4.1\"],\"5\":[\"Momo Cafe - Courtyard Marriot\",\"Courtyard By Marriot, 4th Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\",\"1000\",\"4.1\"],\"6\":[\"Da pizzeria\",\"177, Zone 2, Maharana Pratap Nagar, Bhopal\",\"500\",\"4.0\"],\"7\":[\"Greek Food & Beyond\",\"Third Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\",\"1000\",\"4.0\"],\"8\":[\"Domino's Pizza\",\"Aashima Mall, Food Court, Gulmohar Colony, Bhopal Hoshangabad Road\",\"700\",\"3.9\"],\"9\":[\"Pizza Inn\",\"Opposite Petrol Pump, Yamana Square, Polytechnic Square, Kamla Park Road, TT Nagar, Bhopal\",\"450\",\"3.9\"],\"10\":[\"Domino's Pizza\",\"27, Navri Road, Lal Ghati, Airport Area, Bhopal\",\"700\",\"3.8\"]}"}
    - action_restaurant
    - slot{"location": "bhopal"}
    - slot{"api_response": "{\"1\":[\"The Public House Caf\u00e9 n Restaurant\",\"Mahadev Complex, Lower Ground Floor, Shivaji Nagar Opposite Board Office, Maharana Pratap Nagar, Bhopal\",\"800\",\"4.8\"],\"2\":[\"La Kuchina - Jehan Numa Palace\",\"157, Hotel Jehan Numa Palace, Shymala Hills, TT Nagar, Bhopal\",\"2200\",\"4.5\"],\"3\":[\"Olive & Honey Restaurant\",\"Shaan-e-Fiza Apartment, New Saifia College Road, Housing Board Colony, Kohefiza, Bhopal\",\"600\",\"4.2\"],\"4\":[\"The Urban Socialite\",\"5th Floor, Hotel Lake View Ashoka, Shyamla Hills, TT Nagar, Bhopal\",\"900\",\"4.1\"],\"5\":[\"Momo Cafe - Courtyard Marriot\",\"Courtyard By Marriot, 4th Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\",\"1000\",\"4.1\"],\"6\":[\"Da pizzeria\",\"177, Zone 2, Maharana Pratap Nagar, Bhopal\",\"500\",\"4.0\"],\"7\":[\"Greek Food & Beyond\",\"Third Floor, DB City Mall, Maharana Pratap Nagar, Bhopal\",\"1000\",\"4.0\"],\"8\":[\"Domino's Pizza\",\"Aashima Mall, Food Court, Gulmohar Colony, Bhopal Hoshangabad Road\",\"700\",\"3.9\"],\"9\":[\"Pizza Inn\",\"Opposite Petrol Pump, Yamana Square, Polytechnic Square, Kamla Park Road, TT Nagar, Bhopal\",\"450\",\"3.9\"],\"10\":[\"Domino's Pizza\",\"27, Navri Road, Lal Ghati, Airport Area, Bhopal\",\"700\",\"3.8\"]}"}
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - action_goodbye
    - export
## Handcrafted
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": null}
    - slot{"location": null}
    - action_restaurant

## Generated Story Not operating city corrected
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "400"}
    - slot{"budget": "400"}
    - action_restaurant
    - slot{"location": null}
    - utter_ask_location
* location
    - action_restaurant
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - slot{"lat": 15.4989}
    - slot{"lon": 73.8278}
    - slot{"city_id": 13}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Habanero\",\"The Milky Way Road, Khobra Vaddo, Baga, Goa\",\"1800\",\"4.3\"],\"2\":[\"Antojitos\",\"Taleigao Bypass Road, Panaji, Goa\",\"600\",\"4.2\"],\"3\":[\"Cantare\",\"7/73 B, Cruz Waddo, Saligao, Near Calangute, Goa\",\"800\",\"4.0\"],\"4\":[\"Divo Cafe & Bar\",\"Khobra Vaddo Baga Road, Calangute Bardez, Goa\",\"1000\",\"3.7\"],\"5\":[\"Harbour Cafe\",\"The Crown Hotel, Lobby Level, Bairo Alto Dos Pilotos, Jose Falcao Road, Panaji, Goa\",\"1000\",\"3.6\"],\"6\":[\"Zoori's Grill Restaurant\",\"Poonam Resort Road, Dmello Vaddo, Anjuna, Goa,\",\"1000\",\"3.6\"],\"7\":[\"The Station\",\"80 Belloy Nuvem , NH 17 Goa, Nuvem, Majorda, Goa\",\"800\",\"3.5\"],\"8\":[\"Honey Bar and Restaurant\",\"Arpora, Baga, Goa\",\"550\",\"3.3\"],\"9\":[\"The Bunk House\",\"6/8A, Khobra Vaddo, Calangute Baga Road, Calangute, Goa\",\"1200\",\"0\"],\"10\":[\"Moving Flavours\",\"Saligao, Goa.\",\"200\",\"0\"]}"}
    - action_restaurant
    - slot{"location": "goa"}
    - slot{"api_response": "{\"1\":[\"Habanero\",\"The Milky Way Road, Khobra Vaddo, Baga, Goa\",\"1800\",\"4.3\"],\"2\":[\"Antojitos\",\"Taleigao Bypass Road, Panaji, Goa\",\"600\",\"4.2\"],\"3\":[\"Cantare\",\"7/73 B, Cruz Waddo, Saligao, Near Calangute, Goa\",\"800\",\"4.0\"],\"4\":[\"Divo Cafe & Bar\",\"Khobra Vaddo Baga Road, Calangute Bardez, Goa\",\"1000\",\"3.7\"],\"5\":[\"Harbour Cafe\",\"The Crown Hotel, Lobby Level, Bairo Alto Dos Pilotos, Jose Falcao Road, Panaji, Goa\",\"1000\",\"3.6\"],\"6\":[\"Zoori's Grill Restaurant\",\"Poonam Resort Road, Dmello Vaddo, Anjuna, Goa,\",\"1000\",\"3.6\"],\"7\":[\"The Station\",\"80 Belloy Nuvem , NH 17 Goa, Nuvem, Majorda, Goa\",\"800\",\"3.5\"],\"8\":[\"Honey Bar and Restaurant\",\"Arpora, Baga, Goa\",\"550\",\"3.3\"],\"9\":[\"The Bunk House\",\"6/8A, Khobra Vaddo, Calangute Baga Road, Calangute, Goa\",\"1200\",\"0\"],\"10\":[\"Moving Flavours\",\"Saligao, Goa.\",\"200\",\"0\"]}"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "jpr.saurabh@gmail.com"}
    - slot{"email": "jpr.saurabh@gmail.com"}
    - action_send_email
    - slot{"email": "jpr.saurabh@gmail.com"}
    - utter_goodbye
    - action_goodbye
    - export


## Generated Story 600278197254133861
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": "raebareli"}
    - export

## Generated Story -6714059600070157139
* restaurant_search{"cuisine": "north indian", "location": "hyderabad"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "hyderabad"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "50"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@testmail.com"}
    - slot{"email": "test@testmail.com"}
    - action_send_email
    - slot{"email": "test@testmail.com"}
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story -4407532458322318847
* restaurant_search{"cuisine": "north indian", "location": "hyderabad"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "hyderabad"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"AB's - Absolute Barbecues\",\"8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\",\"1500\",\"4.9\"],\"6\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"7\":[\"Nimrah Cafe And Bakery\",\"Beside Mecca Masjid, Charminar Road, Charminar, Hyderabad\",\"100\",\"4.8\"],\"8\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"9\":[\"Farzi Cafe\",\"1200, Road 59, Jubilee Hills, Hyderabad\",\"1800\",\"4.7\"],\"10\":[\"Sahib\u2019s Barbeque by Ohri\u2019s\",\"Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur\",\"1400\",\"4.7\"]}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@testmail.com"}
    - slot{"email": "test@testmail.com"}
    - action_send_email
    - slot{"email": "test@testmail.com"}
    - utter_goodbye
    - action_goodbye
    - export

