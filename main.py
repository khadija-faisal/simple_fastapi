from fastapi import FastAPI # type: ignore 
import random

app = FastAPI()


# we will build 2 rwo simple (API) get endpoints
# 1- side_hustles
# 2- money_quotes

side_hustles = [
    "YouTube Channel - Create videos and earn from ads & sponsors!",
    "Online Courses - Teach skills and sell courses on platforms like Udemy!",
    "Handmade Crafts - Sell unique handmade items on Etsy!",
    "Stock Photography - Sell your photos to stock image sites!",
    "Social Media Management - Help businesses grow their online presence!",
    "Virtual Assistant - Provide administrative support remotely!",
    "Tutoring - Teach subjects online or in person!",
    "Pet Sitting - Take care of pets while owners are away!",
    "Car Detailing - Offer mobile car cleaning services!",
    "Home Baking - Sell homemade cakes, cookies, and more!",
]

money_quotes = [
    "Quit talking and begin doing. – Walt Disney",
    "Save first, spend later. – Warren Buffett",
    "Knowledge pays the best interest. – Benjamin Franklin",
    "Getting ahead starts with getting started. – Mark Twain",
    "Money is a great servant, but a bad master. – P.T. Barnum",
    "Self-education builds fortunes. – Jim Rohn",
    "Success is who you are, not what you have. – Bo Bennett",
    "Create opportunities, don’t wait for them. – Chris Grosser",
    "Tell your money where to go. – Dave Ramsey",
    "Control money or it will control you. – Dave Ramsey",
    "Wealth is about management, not income. – Anonymous",
    "Make money work for you. – Robert Kiyosaki",
    "Saving is earning. – Benjamin Franklin",
    "Never rely on one income. – Warren Buffett",
    "Live on your terms, not for money. – Chris Brogan"
]

@app.get("/side_hustles")
def get_side_hustles(api_key: str):
    """return a random side hustle idea"""
    if api_key!= "1234567890":
        return {"error": "Invalid API Key"}, 401
    return {"side_hustles": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(api_key:str):
    """return a random money quote"""
    if api_key!= "1234567890":
        return {"error": "Invalid API Key"}, 401
    return {"money_quotes": random.choice(money_quotes)}

