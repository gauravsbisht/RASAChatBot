from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

email_content=""

class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        affirm = tracker.get_slot('email_affirm')
        email_id = tracker.get_slot('email_id')
         ## sendemail
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("venkygaurav.upgrad@gmail.com", "upgrad123")
        s.sendmail("venkygaurav.upgrad@gmail.com", "venkateshan@gmail.com", email_content)
        s.quit()
        ## move to a function later
        response = "Email has been sent"
        dispatcher.utter_message("-----" + response)
        return [SlotSet('email_affirm', affirm)]

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                         'south indian': 85}
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
        d = json.loads(results)
        response = "Showing you top rated restaurants: \n"
        if d['results_found'] == 0:
            response = "no results"
        else:
            for restaurant in d['restaurants']:
                response = response + "Found " + restaurant['restaurant']['name'] + " in " + \
                           restaurant['restaurant']['location']['address'] + " has been rated  " + \
                           restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"

        dispatcher.utter_message("-----" + response)
        email_content=response
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

        return {
            "location": [
                self.from_entity(
                    entity="location", intent="location_intent"
                ),
            ],
            "cuisine": [self.from_entity(entity="cuisine", intent="cuisine_intent")],
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

    def validate_num_people(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        if self.is_int(value) and int(value) > 0:
            return {"num_people": value}
        else:
            dispatcher.utter_message(template="utter_wrong_num_people")
            # validation failed, set slot to None
            return {"num_people": None}

    def validate_outdoor_seating(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate outdoor_seating value."""

        if isinstance(value, str):
            if "out" in value:
                # convert "out..." to True
                return {"outdoor_seating": True}
            elif "in" in value:
                # convert "in..." to False
                return {"outdoor_seating": False}
            else:
                dispatcher.utter_message(template="utter_wrong_outdoor_seating")
                # validation failed, set slot to None
                return {"outdoor_seating": None}

        else:
            # affirm/deny was picked up as T/F
            return {"outdoor_seating": value}

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


