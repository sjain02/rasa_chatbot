## greet story
* greet
    - utter_greet

## Default: Verfied Out of context message
* default
    - utter_default
* greet
    - utter_greet
    - export

## Story Default: Verified
* default
    - utter_default
    - export

## goodbye
* goodbye
    - action_goodbye
    - utter_goodbye

## Story location: Verified
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - export

## Story cuisine: Verfied
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - export

## Story budget: Verified
* budget{"budget": "1200"}
    - slot{"budget": "1200"}
    - action_restaurant
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": "1200"}
    - export

## restaurant search
* restaurant_search
    - action_restaurant

## Story -verified Happy path sending email
* greet
    - utter_greet
* restaurant_search{"location": "hyd"}
    - slot{"location": "hyd"}
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"5\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"6\":[\"Mekong - Marigold Hotel\",\"Green Lands, Begumpet, Hyderabad\",\"2500\",\"4.7\"],\"7\":[\"The Fisherman's Wharf\",\"304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\",\"1500\",\"4.6\"],\"8\":[\"Barbeque Nation\",\"6-3-249/5/1, 1st Floor, ANR Centre, Road 1, Banjara Hills, Hyderabad\",\"1600\",\"4.6\"],\"9\":[\"Prost Brew Pub\",\"882/A Road No 45, Jubilee Hills, Hyderabad\",\"2200\",\"4.6\"],\"10\":[\"SodaBottleOpenerWala\",\"Unit 4, Ground Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\",\"1400\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"5\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"6\":[\"Mekong - Marigold Hotel\",\"Green Lands, Begumpet, Hyderabad\",\"2500\",\"4.7\"],\"7\":[\"The Fisherman's Wharf\",\"304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\",\"1500\",\"4.6\"],\"8\":[\"Barbeque Nation\",\"6-3-249/5/1, 1st Floor, ANR Centre, Road 1, Banjara Hills, Hyderabad\",\"1600\",\"4.6\"],\"9\":[\"Prost Brew Pub\",\"882/A Road No 45, Jubilee Hills, Hyderabad\",\"2200\",\"4.6\"],\"10\":[\"SodaBottleOpenerWala\",\"Unit 4, Ground Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\",\"1400\",\"4.6\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "chinese"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "abcd@gmail.com"}
    - slot{"email": "abcd@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
* goodbye
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Story verified invalid cuisine correction mail sent
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "1200"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "abcd@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - export
* goodbye
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

    
## Story VERIFIED Invalid Cuisine no mail
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "1200"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"api_response": "{\"1\":[\"Guzman y Gomez\",\"Emporium, Shop 31, 1000 Ann Street, Fortitude Valley, Brisbane\",\"30\",\"4.5\"],\"2\":[\"Billy Kart Kitchen\",\"1 Eric Crescent, Annerley\",\"50\",\"4.4\"],\"3\":[\"IndiMex Cafe-Bar-Restaurant\",\"Shop 22, 401 Logan Road, Stones Corner, Brisbane\",\"70\",\"4.4\"],\"4\":[\"Pepe's Mexican Restaurant\",\"184 Enoggera Road, Newmarket, Brisbane\",\"70\",\"4.3\"],\"5\":[\"Guzman y Gomez\",\"142 Albert Street, Brisbane CBD, Brisbane\",\"30\",\"4.3\"],\"6\":[\"La Quinta Mexican Cafe & Bar\",\"Shop 1, 189 Oxford Street, Bulimba, Brisbane\",\"80\",\"4.2\"],\"7\":[\"El Torito\",\"146 Boundary Street, West End, Brisbane\",\"80\",\"4.1\"],\"8\":[\"Guzman y Gomez\",\"Westfield Carindale Shopping Centre, Shop 1204, Ground Level, 1151 Creek Road, Carindale, Brisbane\",\"30\",\"4.1\"],\"9\":[\"Guzman y Gomez\",\"179 Grey Street, South Bank, Brisbane\",\"30\",\"4.1\"],\"10\":[\"Mucho Mexicano\",\"Shop 15, Little Stanley Street, South Bank, Brisbane\",\"90\",\"4.0\"]}"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
* goodbye
    - export

## Story -VERIFIED invalid location mail sent
* restaurant_search{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - slot{"cuisine": "mexican"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "73"}
    - slot{"api_response": "{\"1\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"2\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"3\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"4\":[\"Churrolto\",\"Ground Floor, Shop 3, Opposite IndusInd Bank, Madhapur Main Road, Madhapur, Hyderabad\",\"1200\",\"4.8\"],\"5\":[\"Coffee Cup\",\"E 89, 1rst floor, Above Canara Bank, Sainikpuri, Secunderabad\",\"800\",\"4.7\"],\"6\":[\"B-Dubs\",\"Plot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad\",\"1600\",\"4.7\"],\"7\":[\"Hard Rock Cafe\",\"Ground Floor, GVK One, Road 1, Banjara Hills, Hyderabad\",\"2000\",\"4.7\"],\"8\":[\"B-Dubs\",\"Plot 189 to 198, Survey 50, Gachibowli Village, Gachibowli, Hyderabad\",\"1600\",\"4.7\"],\"9\":[\"L\u00e9 Vantage Cafe Bar\",\"Plot 197/A & 197, Road 13, Jubilee Hills, Hyderabad\",\"1000\",\"4.6\"],\"10\":[\"Ciclo Cafe\",\"801, Road 36, Jubilee Hills, Hyderabad\",\"2100\",\"4.6\"]}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"2\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"3\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.8\"],\"4\":[\"Churrolto\",\"Ground Floor, Shop 3, Opposite IndusInd Bank, Madhapur Main Road, Madhapur, Hyderabad\",\"1200\",\"4.8\"],\"5\":[\"Coffee Cup\",\"E 89, 1rst floor, Above Canara Bank, Sainikpuri, Secunderabad\",\"800\",\"4.7\"],\"6\":[\"B-Dubs\",\"Plot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad\",\"1600\",\"4.7\"],\"7\":[\"Hard Rock Cafe\",\"Ground Floor, GVK One, Road 1, Banjara Hills, Hyderabad\",\"2000\",\"4.7\"],\"8\":[\"B-Dubs\",\"Plot 189 to 198, Survey 50, Gachibowli Village, Gachibowli, Hyderabad\",\"1600\",\"4.7\"],\"9\":[\"L\u00e9 Vantage Cafe Bar\",\"Plot 197/A & 197, Road 13, Jubilee Hills, Hyderabad\",\"1000\",\"4.6\"],\"10\":[\"Ciclo Cafe\",\"801, Road 36, Jubilee Hills, Hyderabad\",\"2100\",\"4.6\"]}"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* default
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Story VERIFIED Invalid location mail not sent
* restaurant_search{"cuisine": "north indian", "location": "raebareli"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "1500"}
    - slot{"budget": "1500"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 12.971606}
    - slot{"lon": 77.594376}
    - slot{"city_id": 4}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Punjab Grill\",\"26/1, Dr. Rajkumar Road, In Brigade Gateway Campus, Malleshwaram ,Bangalore\",\"2000\",\"4.9\"],\"4\":[\"AB's - Absolute Barbecues\",\"2nd Floor,I20-A2, EPIP Zone, Near Vydehi Hospital Whitefield, Bangalore\",\"1400\",\"4.9\"],\"5\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"6\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"9\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"10\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Punjab Grill\",\"26/1, Dr. Rajkumar Road, In Brigade Gateway Campus, Malleshwaram ,Bangalore\",\"2000\",\"4.9\"],\"4\":[\"AB's - Absolute Barbecues\",\"2nd Floor,I20-A2, EPIP Zone, Near Vydehi Hospital Whitefield, Bangalore\",\"1400\",\"4.9\"],\"5\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"6\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"9\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"10\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"]}"}
    - slot{"budget": "1500"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
    - slot{"location": null}
    - slot{"api_response": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - utter_goodbye
    - export

## Generated Story 5048231483003727086
* greet
    - utter_greet
* default
    - utter_default
* restaurant_search
    - action_restaurant
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
* location{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* location{"location": "bnglr"}
    - slot{"location": "bnglr"}
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* budget{"budget": "1200"}
    - slot{"budget": "1200"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 12.971606}
    - slot{"lon": 77.594376}
    - slot{"city_id": 4}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"4\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"5\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"6\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"9\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"],\"10\":[\"AB's - Absolute Barbecues\",\"100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\",\"1400\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"4\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"5\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"6\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"7\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"8\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"9\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"],\"10\":[\"AB's - Absolute Barbecues\",\"100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\",\"1400\",\"4.8\"]}"}
    - slot{"budget": "1200"}
    - slot{"cuisine": "chinese"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* default{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - export

## Story -VERIFIED All use cases with EMAIL response filtering
* greet
    - utter_greet
* default
    - utter_default
* restaurant_search
    - action_restaurant
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
* location{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* location{"location": "bnglr"}
    - slot{"location": "bnglr"}
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* budget{"budget": "1000"}
    - slot{"budget": "1000"}
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 12.971606}
    - slot{"lon": 77.594376}
    - slot{"city_id": 4}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"4\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"5\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"6\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"7\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"8\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"9\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"],\"10\":[\"AB's - Absolute Barbecues\",\"100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\",\"1400\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - slot{"api_response": "{\"1\":[\"Byg Brewski Brewing Company\",\"Behind MK Retail, Sarjapur Road, Bangalore\",\"1600\",\"4.9\"],\"2\":[\"The Black Pearl\",\"20/7, Swamy Legato, Outer Ring Road, Kadubeesanahalli, Marathahalli, Bangalore\",\"1500\",\"4.9\"],\"3\":[\"Big Pitcher\",\"LR Arcade,4121, Old Airport Road, Bangalore\",\"2000\",\"4.8\"],\"4\":[\"Brew and Barbeque - A Microbrewery Pub\",\"36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"5\":[\"House Of Commons\",\"122/B, Jyothi Nivas Road, 5th Block, Koramangala 5th Block, Bangalore\",\"1000\",\"4.8\"],\"6\":[\"TBC Sky Lounge\",\"Astra Hotel, 2795, 27th Main, Sector 1, HSR Layout, Bangalore\",\"1000\",\"4.8\"],\"7\":[\"AB's - Absolute Barbecues\",\"90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\",\"1400\",\"4.8\"],\"8\":[\"Biergarten\",\"2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore\",\"1500\",\"4.8\"],\"9\":[\"The Globe Grub\",\"2nd Floor, Soul Space Paradigm,\nLandmark- Next to Innovative Multiplex, Above Bata Showroom, Outer Ring Road Marathahalli, Bangalore\",\"1300\",\"4.8\"],\"10\":[\"AB's - Absolute Barbecues\",\"100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\",\"1400\",\"4.8\"]}"}
    - slot{"budget": "1000"}
    - slot{"cuisine": "chinese"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "abcd@gmail.com"}
    - slot{"email": "abcd@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - export