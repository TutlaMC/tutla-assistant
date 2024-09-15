from ..Module import * 
from ..Utils import *
from assistantdata import db
import requests
import random

# Lists to store facts and quotes
facts = [
    "Honey never spoils.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries aren't.",
    "Octopuses have three hearts.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "There are more stars in the universe than grains of sand on Earth.",
    "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
    "Humans share 60% of their DNA with bananas.",
    "A single strand of spaghetti is called a 'spaghetto'.",
    "The shortest war in history lasted 38 minutes.",
    "A group of flamingos is called a 'flamboyance'.",
    "The longest time between two twins being born is 87 days.",
    "The inventor of the Pringles can is now buried in one.",
    "A jiffy is an actual unit of time: 1/100th of a second.",
    "A blue whale's heart is the size of a small car.",
    "Some cats are allergic to humans.",
    "The unicorn is the national animal of Scotland.",
    "A snail can sleep for three years.",
    "There are more fake flamingos in the world than real ones.",
    "A crocodile cannot stick its tongue out.",
    "The world's smallest reptile was discovered in 2021.",
    "The moon has moonquakes.",
    "Goosebumps are meant to ward off predators.",
    "Humans are the only animals that blush.",
    "The wood frog can hold its pee for up to eight months.",
    "The hottest spot on the planet is in Libya.",
    "Only two mammals like spicy food: humans and the tree shrew.",
    "The longest wedding veil was longer than 63 football fields.",
    "The inventor of the microwave appliance received only \$2 for his discovery.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "There's a fruit that tastes like chocolate pudding.",
    "More people visit France than any other country.",
    "A chef's hat has 100 pleats.",
    "The world's longest place name is 85 letters long.",
    "The unicorn is the national animal of Scotland.",
    "Bees sometimes sting other bees.",
    "The total weight of ants on earth once equaled the total weight of people.",
    "E is the most common letter and appears in 11 percent of all English words.",
    "A dozen bodies were once found in Benjamin Franklin's basement.",
    "The healthiest place in the world is in Panama.",
    "A pharaoh once lathered his slaves in honey to keep bugs away from him.",
    "Some people have an extra bone in their knee (and it's getting more common).",
    "Pringles aren't actually potato chips.",
    "There's a giant fish with a transparent head.",
    "The first computer was invented in the 1940s.",
    "Space smells like seared steak.",
    "The longest hiccuping spree lasted 68 years.",
    "The shortest commercial flight in the world is in Scotland.",
    "The longest musical performance lasted 639 years.",
    "The world's largest grand piano was built by a 15-year-old."
]

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to predict the future is to invent it. - Alan Kay",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "Do not let making a living prevent you from making a life. - John Wooden",
    "Life is a succession of lessons which must be lived to be understood. - Ralph Waldo Emerson",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. - Ralph Waldo Emerson",
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "You define your own life. Don't let other people write your script. - Oprah Winfrey",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "At the end of the day, we can endure much more than we think we can. - Frida Kahlo",
    "Do what you feel in your heart to be right – for you’ll be criticized anyway. - Eleanor Roosevelt",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "If you want to achieve greatness stop asking for permission. - Anonymous",
    "Things work out best for those who make the best of how things work out. - John Wooden",
    "To live a creative life, we must lose our fear of being wrong. - Anonymous",
    "If you are not willing to risk the usual you will have to settle for the ordinary. - Jim Rohn",
    "Trust because you are willing to accept the risk, not because it's safe or certain. - Anonymous",
    "All our dreams can come true if we have the courage to pursue them. - Walt Disney",
    "Good things come to people who wait, but better things come to those who go out and get them. - Anonymous",
    "If you do what you always did, you will get what you always got. - Anonymous",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "Just when the caterpillar thought the world was ending, he turned into a butterfly. - Proverb",
    "Successful entrepreneurs are givers and not takers of positive energy. - Anonymous",
    "Whenever you see a successful person you only see the public glories, never the private sacrifices to reach them. - Vaibhav Shah",
    "Opportunities don't happen, you create them. - Chris Grosser",
    "Try not to become a person of success, but rather try to become a person of value. - Albert Einstein",
    "Great minds discuss ideas; average minds discuss events; small minds discuss people. - Eleanor Roosevelt",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison"
]

async def fact_callback(CommandObject, message, self, params, command_data):
    fact = random.choice(facts)
    await message.channel.send(f"Did you know? {fact}")

async def quote_callback(CommandObject, message, self, params, command_data):
    quote = random.choice(quotes)
    await message.channel.send(f"{quote}")

fact_command = Command("fact", "Get a random fact", fact_callback, TOOLS, aliases=["fax"])
quote_command = Command("quote", "Get a random quote", quote_callback, TOOLS, aliases=["getquote"])
