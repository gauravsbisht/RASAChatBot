from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
# import pandas as pd


email_content=""

class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        try:
            affirm = tracker.get_slot('email_affirm')
            email_id = tracker.get_slot('email_id')
             ## sendemail
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            msg = MIMEMultipart()
            msg['From'] = "venkygaurav.upgrad@gmail.com"
            msg['TO'] = email_id
            subject = 'Hello from chatbox'
            msg['Subject'] = subject
            body = email_content
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            s.login("venkygaurav.upgrad@gmail.com", "upgrad123")
          #  response = affirm+' id : '+email_id
         #   dispatcher.utter_message("-----" + response)
            if(affirm == 'yes'):
                s.sendmail("venkygaurav.upgrad@gmail.com", email_id, text)
            s.quit()
        ## move to a function later
            response = "Sent. Bon Appetit!"
            dispatcher.utter_message(response)
        except Exception as e:
            dispatcher.utter_message('Issue in sending message \n' + str(e))

        return [SlotSet('email_affirm', affirm)]

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        count = 0
        config = {"user_key": "128343527e861a0747f3baf1c0d09ba6"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('budget')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {
            'american': 1,
            'mexican': 73,
            'italian': 55,
            'thai': 95,
            'chinese': 25,
            'north indian': 50,
            'cafe': 30,
            'bakery': 5,
            'biryani': 7,
            'south indian': 85
        }
#        response = price + loc + cuisine
#        dispatcher.utter_message(response)
        ## venky/gaurav - need to get right codes for the cusines
        response = "Showing you top rated restaurants: \n"
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50000)
        d = json.loads(results)
        if d['results_found'] == 0:
            response = "No restaurant found for your criteria"
        else:
            for restaurant in sorted(d['restaurants'], key=lambda x: x['restaurant']['user_rating']['aggregate_rating'],
                                     reverse=True):

                # Getting Top 10 restaurants for chatbot response
                if ((price == 'low') and (restaurant['restaurant']['average_cost_for_two'] < 300) and (count < 5)):
                    response = response + str(count+1)+ "." + "Restaurant :: " + restaurant['restaurant']['name'] + " in " + \
                               restaurant['restaurant']['location']['address'] + " has been rated " + \
                               restaurant['restaurant']['user_rating']['aggregate_rating'] + "."
                    response = response + " And the average price for two people is: " + str(
                        restaurant['restaurant']['average_cost_for_two']) + "\n"
                    count = count + 1
                elif ((price == 'medium') and (restaurant['restaurant']['average_cost_for_two'] >= 300) and (
                        restaurant['restaurant']['average_cost_for_two'] <= 700) and (count < 5)):
                    response = response + str(count+1) + "." + "Restaurant :: " + restaurant['restaurant']['name'] + " in " + \
                               restaurant['restaurant']['location']['address'] + " has been rated " + \
                               restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"
                    response = response + " And the average price for two people is: " + str(
                        restaurant['restaurant']['average_cost_for_two']) + "\n"
                    count = count + 1
                elif ((price == 'high') and (restaurant['restaurant']['average_cost_for_two'] > 700) and (count < 5)):
                    response = response + str(count+1) + "." + "Restaurant :: " + restaurant['restaurant']['name'] + " in " + \
                               restaurant['restaurant']['location']['address'] + " has been rated " + \
                               restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"
                    response = response + " And the average price for two people is: " + str(
                        restaurant['restaurant']['average_cost_for_two']) + "\n"
                    count = count + 1
        if (count <= 5 and count > 0):
            dispatcher.utter_message(response)
        if (count == 0):
            response = "Sorry, No results found for your criteria. Would you like to search for some other restaurants?"
            dispatcher.utter_message(response)
            return(action_restart)
        global email_content
        email_content = response
        return [SlotSet('location', loc)]



class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["location", "cuisine", "budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        #print("Inside Slot Mapping")
        return {
            "location": [
                self.from_entity(
                    entity="location", intent=["request_restaurant","location_intent"]
                ),
            ],
            "cuisine": [self.from_entity(entity="cuisine", intent=["request_restaurant","cuisine_intent"])],
            "budget": [
                self.from_entity(entity="budget" , intent="budget_intent")
            ],
        }

    # USED FOR DOCS: do not rename without updating in docs
    @staticmethod
    def cuisine_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "chinese",
            "mexican",
            "italian",
            "american",
            "thai",
            "north indian",
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def location_db() -> List[Text]:
        """Database of supported cuisines"""
        places = []

        # open file and read the content in a list
        with open('location.txt', 'r') as filehandle:
            filecontents = filehandle.readlines()

            for line in filecontents:
                # remove linebreak which is the last character of the string
                current_place = line[:-1]

                # add item to the list
                places.append(current_place)
        return places

    def validate_location(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""
		#print("inside validate_location..Loc retrieved",value)
        if value.lower() in self.location_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"location": value}
        else:
            dispatcher.utter_message(template="utter_wrong_location")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"location": None}

    # USED FOR DOCS: do not rename without updating in docs
    def validate_cuisine(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"cuisine": value}
        else:
            dispatcher.utter_message(template="utter_wrong_cuisine")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"cuisine": None}
    @staticmethod
    def budget_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "300-700",
            "more than 700",
            "lesser than 300",
        ]
    def validate_budget(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate budget value."""

        if value.lower() in self.budget_db():
            # validation succeeded, set the value of the "budget" slot to value
            budget_return=""
            #dispatcher.utter_message(value)
            if(value == '300-700'):
                budget_return= 'medium'
            elif(value == "lesser than 300"):
                budget_return = 'low'
            elif(value == "more than 700"):
                budget_return = 'high'
            else:
                budget_return=None
            return {"budget": budget_return}
        else:
            dispatcher.utter_message(template="utter_wrong_budget")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"budget": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
      #  dispatcher.utter_message(template="utter_submit")
        return []


