from this import d
import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth
from .models import CarDealer, DealerReview

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))


def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))

    if kwargs.api_key:
   # Basic authentication GET
        requests.get(url, params=kwargs.params, auth=, ...)
    else:
   # no authentication GET
        requests.get(url, params=kwargs.params)

    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, params=kwargs.params, headers={'Content-Type': 'application/json'},
         auth=HTTPBasicAuth('apikey', kwargs.api_key))
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# to get all reviews by dealer's id. Then it converts the JSON result into a list of DealerReview objects.


def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealerId)
    if json_result:
        # Get the row list in JSON as dealers
        reviews = json_result["rows"]
        # For each dealer object
        for review in reviews:
            # Get its content in `doc` object
            review_doc = review["doc"]
            # Create a CarDealer object with values in `doc` object
            review_obj = DealerReview(dealership=review_doc["dealership"], name=review_doc["name"], purchase=review_doc["purchase"],
             review=review_doc["review"], purchase_date=review_doc[
                 "purchase_date"], car_make=review_doc["car_make"], car_model=review_doc["car_model"],
              car_year=review_doc["car_year"], sentiment="SENTIMIENTO Y PASION", id=review_doc["id"])
            results.append(review_obj)

    return results


# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(text, **kwargs):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
  params = dict()
  params["text"] = kwargs["text"]
  params["version"] = kwargs["version"]
  params["features"] = kwargs["features"]
  params["return_analyzed_text"] = kwargs["return_analyzed_text"]
  response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)

