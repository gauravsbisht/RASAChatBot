## happy path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
    - utter_ask_email
* email_intent{"email_affirm":"yes", "email_id":"xyz@gmail.com"}
    - slot{"email_affirm":"yes"}
    - slot{"email_id":"xyz@gmail.com"}
    - action_send_email
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart
## happy path2
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
    - utter_ask_email
* email_intent{"email_affirm":"yes"}
    - slot{"email_affirm":"yes"}
    - utter_ask_emailid
* email_intent{"email_id":"jddk.2jmd@kdl.co.in"}
    - slot{"email_id":"jddk.2jmd@kdl.co.in "}
    - action_send_email
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart
## happy path3
* greet
    - utter_greet
* request_restaurant{"cuisine":"chinese", "location":"chandigarh"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
    - utter_ask_email
* email_intent{"email_affirm":"yes", "email_id":"xyz@gmail.com"}
    - slot{"email_affirm":"yes"}
    - slot{"email_id":"xyz@gmail.com"}
    - action_send_email
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart
## happy path4
* greet
    - utter_greet
* request_restaurant{"cuisine":"chinese", "location":"chandigarh"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
    - utter_ask_email
* email_intent{"email_affirm":"no"}
    - utter_goodbye
	- action_restart
	- utter_restart
## happy path5
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
    - utter_ask_email
* email_intent{"email_affirm":"yes", "email_id":"xyz@gmail.com"}
    - slot{"email_affirm":"yes"}
    - slot{"email_id":"xyz@gmail.com"}
    - action_send_email
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart
## happy path6
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - action_search_restaurants
    - utter_ask_email
* email_intent{"email_affirm":"yes"}
    - slot{"email_affirm":"yes"}
    - utter_ask_emailid
* email_intent{"email_id":"xyz@gmail.com"}
    - slot{"email_id":"xyz@gmail.com"}
    - action_send_email
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart
## unhappy path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart

## very unhappy path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
* chitchat
    - utter_chitchat
    - restaurant_form
* chitchat
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart

## stop but continue path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* stop
    - utter_ask_continue
* affirm
    - restaurant_form
    - form{"name": null}
* thankyou
    - utter_goodbye
## stop but continue and chitchat path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* stop
    - utter_ask_continue
* affirm
    - restaurant_form
    - form{"name": null}
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
* stop
    - utter_ask_continue
* affirm
    - restaurant_form
* chitchat
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart

## chitchat, stop and really stop path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
* thankyou
    - utter_goodbye
	- action_restart
	- utter_restart

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
* form: budget_intent{"budget": "more than 700"}
    - form: restaurant_form
    - slot{"budget": "high"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email
* email_intent{"email_affirm": "yes"}
    - slot{"email_affirm": "yes"}
    - utter_ask_emailid
* email_intent{"email_id": "jddk.2jmd@kdl.co.in"}
    - slot{"email_id": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"email_affirm": "yes"}
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
* email_intent{"email_affirm": "yes"}
    - slot{"email_affirm": "yes"}
    - utter_ask_emailid
* email_intent{"email_id": "jddk.2jm@kdl.co.in"}
    - slot{"email_id": "jddk.2jm@kdl.co.in"}
    - action_send_email
    - slot{"email_affirm": "yes"}
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
* email_intent{"email_affirm": "yes"}
    - slot{"email_affirm": "yes"}
    - utter_ask_emailid
* email_intent{"email_id": "jddk.2jmd@kdl.co.in"}
    - slot{"email_id": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"email_affirm": "yes"}
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: location_intent{"location": "mubaim"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: location_intent{"location": "Mumbai"}
    - form: restaurant_form
    - slot{"location": "Mumbai"}
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
    - slot{"location": "Mumbai"}
    - utter_ask_email
* email_intent{"email_affirm": "yes"}
    - slot{"email_affirm": "yes"}
    - utter_ask_emailid
* email_intent{"email_id": "jddk.2jmd@kdl.co.in"}
    - slot{"email_id": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"email_affirm": "yes"}
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* request_restaurant{"cuisine": "chinese", "location": "chennai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* form: budget_intent{"budget": "more than 700"}
    - form: restaurant_form
    - slot{"budget": "high"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email
* email_intent{"email_affirm": "no"}
    - slot{"email_affirm": "no"}
    - utter_goodbye
    - action_restart

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
* form: budget_intent{"budget": "lesser than 300"}
    - form: restaurant_form
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_continue
* affirm
    - action_restart

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
* form: budget_intent{"budget": "lesser than 300"}
    - form: restaurant_form
    - slot{"budget": "low"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_continue
* deny
    - action_restart
