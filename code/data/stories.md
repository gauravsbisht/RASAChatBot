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
