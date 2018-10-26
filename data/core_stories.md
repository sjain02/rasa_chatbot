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
## location intent
* location
    - action_restaurant

## cuisine intent
* cuisine
    - action_restaurant

## budget intent
* budget
    - action_restaurant

## Goodbye story
* goodbye
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story Mail
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyd"}
    - slot{"location": "hyd"}
    - utter_ask_cuisine
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* cuisine{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 33.8495}
    - slot{"lon": -87.2714}
    - slot{"city_id": 4067}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"Sakura Japanese Restaurant\",\"300 Highway 78 W, Jasper\",\"25\",\"3.6\"],\"2\":[\"China Gourmet\",\"902 Highway 78 E, Jasper 35501\",\"10\",\"3.6\"],\"3\":[\"Lin Garden II\",\"300 Hwy 78, Jasper 35501\",\"10\",\"3.5\"],\"4\":[\"Golden Dragon\",\"1814 21st St, Haleyville 35565\",\"0\",\"3.7\"],\"5\":[\"China Gourmet\",\"42461 Hwy 195, Haleyville 35565\",\"0\",\"3.2\"],}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"Sakura Japanese Restaurant\",\"300 Highway 78 W, Jasper\",\"25\",\"3.6\"],\"2\":[\"China Gourmet\",\"902 Highway 78 E, Jasper 35501\",\"10\",\"3.6\"],\"3\":[\"Lin Garden II\",\"300 Hwy 78, Jasper 35501\",\"10\",\"3.5\"],\"4\":[\"Golden Dragon\",\"1814 21st St, Haleyville 35565\",\"0\",\"3.7\"],\"5\":[\"China Gourmet\",\"42461 Hwy 195, Haleyville 35565\",\"0\",\"3.2\"],}"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
* goodbye
    - utter_goodbye
    - action_goodbye
    - export

## Generated Story No-Mail
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyd"}
    - slot{"location": "hyd"}
    - utter_ask_cuisine
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"cuisine": "chinese"}
* cuisine{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"lat": 33.8495}
    - slot{"lon": -87.2714}
    - slot{"city_id": 4067}
    - slot{"cuisine_key": "25"}
    - slot{"api_response": "{\"1\":[\"Sakura Japanese Restaurant\",\"300 Highway 78 W, Jasper\",\"25\",\"3.6\"],\"2\":[\"China Gourmet\",\"902 Highway 78 E, Jasper 35501\",\"10\",\"3.6\"],\"3\":[\"Lin Garden II\",\"300 Hwy 78, Jasper 35501\",\"10\",\"3.5\"],\"4\":[\"Golden Dragon\",\"1814 21st St, Haleyville 35565\",\"0\",\"3.7\"],\"5\":[\"China Gourmet\",\"42461 Hwy 195, Haleyville 35565\",\"0\",\"3.2\"],}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - slot{"api_response": "{\"1\":[\"Sakura Japanese Restaurant\",\"300 Highway 78 W, Jasper\",\"25\",\"3.6\"],\"2\":[\"China Gourmet\",\"902 Highway 78 E, Jasper 35501\",\"10\",\"3.6\"],\"3\":[\"Lin Garden II\",\"300 Hwy 78, Jasper 35501\",\"10\",\"3.5\"],\"4\":[\"Golden Dragon\",\"1814 21st St, Haleyville 35565\",\"0\",\"3.7\"],\"5\":[\"China Gourmet\",\"42461 Hwy 195, Haleyville 35565\",\"0\",\"3.2\"],}"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
* goodbye
    - utter_goodbye
    - export

## Story with No service to city
* restaurant_search{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": null}
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_restaurant
    - slot{"location": "faridabad"}
* cuisine{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "1500"}
    - slot{"budget": "1500"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": 28.3956}
    - slot{"lon": 77.319399}
    - slot{"city_id": 1}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"Ministry Of Beer\",\"M 43, Outer Circle, Connaught Place, New Delhi\",\"1500\",\"4.9\"],\"2\":[\"Feel ALIVE\",\"SCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\",\"1200\",\"4.9\"],\"3\":[\"38 Barracks\",\"M-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\",\"1600\",\"4.8\"],\"4\":[\"Punjabi Angithi\",\"Shop 32-22, A-4, DDA Market, Paschim Vihar, New Delhi\",\"500\",\"4.8\"],\"5\":[\"The Hook\",\"SCO 30, Sector 29, Gurgaon\",\"1600\",\"4.8\"],\"6\":[\"Sanadige\",\"22/48, Commercial Centre, Chanakyapuri, New Delhi\",\"2200\",\"4.8\"],\"7\":[\"Phonebooth Reloaded\",\"G14b, Ground Floor, Vijay Nagar, Hudson lane, Delhi University-GTB Nagar, New Delhi\",\"1000\",\"4.8\"],\"8\":[\"Cafe Cones & Curries\",\"A44&44 Galaxybusiness park galactic court shop no 8\",\"400\",\"4.8\"],\"9\":[\"Mellow Garden\",\"J2/7, 2nd & 3rd Floor, BK Dutta Market, Rajouri Garden, New Delhi\",\"1200\",\"4.8\"],\"10\":[\"The Mughal Trail\",\"BK Dutt Market, Rajouri Garden, New Delhi\",\"500\",\"4.8\"]}"}
    - action_restaurant
    - slot{"location": "faridabad"}
    - slot{"api_response": "{\"1\":[\"Ministry Of Beer\",\"M 43, Outer Circle, Connaught Place, New Delhi\",\"1500\",\"4.9\"],\"2\":[\"Feel ALIVE\",\"SCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon\",\"1200\",\"4.9\"],\"3\":[\"38 Barracks\",\"M-38, Outer Circle, Opposite Shankar Market, Connaught Place, New Delhi\",\"1600\",\"4.8\"],\"4\":[\"Punjabi Angithi\",\"Shop 32-22, A-4, DDA Market, Paschim Vihar, New Delhi\",\"500\",\"4.8\"],\"5\":[\"The Hook\",\"SCO 30, Sector 29, Gurgaon\",\"1600\",\"4.8\"],\"6\":[\"Sanadige\",\"22/48, Commercial Centre, Chanakyapuri, New Delhi\",\"2200\",\"4.8\"],\"7\":[\"Phonebooth Reloaded\",\"G14b, Ground Floor, Vijay Nagar, Hudson lane, Delhi University-GTB Nagar, New Delhi\",\"1000\",\"4.8\"],\"8\":[\"Cafe Cones & Curries\",\"A44&44 Galaxybusiness park galactic court shop no 8\",\"400\",\"4.8\"],\"9\":[\"Mellow Garden\",\"J2/7, 2nd & 3rd Floor, BK Dutta Market, Rajouri Garden, New Delhi\",\"1200\",\"4.8\"],\"10\":[\"The Mughal Trail\",\"BK Dutt Market, Rajouri Garden, New Delhi\",\"500\",\"4.8\"]}"}
    - slot{"budget": "1500"}
    - slot{"cuisine": "north indian"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
* goodbye
    - utter_goodbye
    - export

## Generated Story No Cuisine Find send mail
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"cuisine": null}
* cuisine{"cuisine": "mexican"}
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
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "jpr.saurabh@gmail.com"}
    - slot{"email": "jpr.saurabh@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"location": null}
    - slot{"cuisine": null}
* goodbye
    - utter_goodbye
    - export

## Generated Story No Cuisine Find send mail
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"cuisine": null}
* cuisine{"cuisine": "mexican"}
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
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
* goodbye
    - utter_goodbye
    - export

## Generated Story no cuisine found email not sent
* restaurant_search{"cuisine": "north indian", "location": "erode"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "erode"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"cuisine": "north indian"}
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"lat": -27.3918316209}
    - slot{"lon": 153.0120202527}
    - slot{"city_id": 298}
    - action_restaurant
    - slot{"location": "erode"}
    - slot{"cuisine": null}
* cuisine{"cuisine": "mexican"}
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
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - utter_get_email_confirmation
* deny
    - action_goodbye
* goodbye
    - utter_goodbye
    - export

## Generated Story -3065047515619587552 Mail  with no reset
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_restaurant
    - slot{"cuisine": "pune"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "600"}
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
* goodbye
    - utter_goodbye
    - action_goodbye
    - export
