## happy path Revised
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
    - utter_ask_email
* email_affirm_intent
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}
    - action_send_email
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart	
	
## interactive_story_1
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: location_intent{"location": "bangalore"}
    - form: restaurant_form
    - slot{"location": "bangalore"}
    - slot{"requested_slot": "cuisine"}
* form: cuisine_intent{"cuisine": "thai"}
    - form: restaurant_form
    - slot{"cuisine": "thai"}
    - slot{"requested_slot": "budget"}
* form: budget_intent{"budget": "more than 700"}
    - form: restaurant_form
    - slot{"budget": "high"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* email_affirm_intent{"email_affirm": "yes", "email_id": "xyz@gmail.com"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "xyz@gmail.com"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "xyz@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_send_email
    - slot{"email_affirm": "yes"}
* thankyou
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: location_intent{"location": "chennai"}
    - form: restaurant_form
    - slot{"location": "chennai"}
    - slot{"requested_slot": "cuisine"}
* form: cuisine_intent{"cuisine": "North Indian"}
    - form: restaurant_form
    - slot{"cuisine": "North Indian"}
    - slot{"requested_slot": "budget"}
* form: budget_intent{"budget": "300-700"}
    - form: restaurant_form
    - slot{"budget": "medium"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email
* email_affirm_intent{"email_affirm": "yes", "email_id": "venkateshan@gmail.com"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "venkateshan@gmail.com"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "venkateshan@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_send_email
    - slot{"email_affirm": "yes"}
* thankyou
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* request_restaurant{"location": "Rishikesh"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: location_intent{"location": "Surat"}
    - form: restaurant_form
    - slot{"location": "Surat"}
    - slot{"requested_slot": "cuisine"}
* form: cuisine_intent{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* form: budget_intent{"budget": "more than 700"}
    - form: restaurant_form
    - slot{"budget": "high"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "Surat"}
    - utter_ask_email
* email_affirm_intent{"email_affirm": "yes", "email_id": "xyz@sth.edu"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "xyz@sth.edu"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "xyz@sth.edu"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_send_email
    - slot{"email_affirm": "yes"}
* thankyou
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* request_restaurant{"location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"requested_slot": "cuisine"}
* form: cuisine_intent{"cuisine": "american"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "budget"}
* form: budget_intent{"budget": "lesser than 300"}
    - form: restaurant_form
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email
* email_affirm_intent{"email_affirm": "yes"}
    - slot{"email_affirm": "yes"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email_affirm": "yes"}
    - slot{"requested_slot": "email_id"}
    - utter_ask_email_id
* email_id_intent{"email_id": "jddk.2jmd@kdl.co.in"}
    - slot{"email_id": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"email_affirm": "yes"}
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* request_restaurant{"cuisine": "chinese", "location": "chandigarh"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* form: budget_intent{"budget": "300-700"}
    - form: restaurant_form
    - slot{"budget": "medium"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_email
* email_affirm_intent{"email_affirm": "no"}
    - slot{"email_affirm": "no"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email_affirm": "no"}
    - slot{"email_affirm": "no"}
    - slot{"requested_slot": "email_id"}
    - utter_goodbye
    - utter_restart
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* request_restaurant{"cuisine": "chinese", "location": "Chandigarh"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* form: budget_intent{"budget": "300-700"}
    - form: restaurant_form
    - slot{"budget": "medium"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_ask_email
* email_affirm_intent{"email_affirm": "no"}
    - slot{"email_affirm": "no"}
    - utter_goodbye
    - utter_restart
    - action_restart

## interactive_story_1
* request_restaurant
    - utter_ask_location
* location_intent{"location": "chennai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "chennai"}
    - slot{"requested_slot": "cuisine"}
* form: cuisine_intent{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* form: budget_intent{"budget": "300-700"}
    - form: restaurant_form
    - slot{"budget": "medium"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email
* email_affirm_intent{"email_affirm": "yes", "email_id": "venkateshan@gmail.com"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "venkateshan@gmail.com"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "venkateshan@gmail.com"}
    - slot{"email_affirm": "yes"}
    - slot{"email_id": "venkateshan@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_send_email
    - slot{"email_affirm": "yes"}
* thankyou
    - action_restart
