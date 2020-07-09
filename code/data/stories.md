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
    - export

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
* chitchat
    - utter_chitchat
    - restaurant_form
    - form{"name": null}
* thankyou
    - utter_goodbye

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