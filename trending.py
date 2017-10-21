# # CSCI 121 Fall 2017
# #
# # Project 2 option #2: Visualizing Twitter Topics Across America
# #
# # This file contains the start of the source code that you are to modify
# # in order to complete the Project 2 assignment.  Your job is to build a
# # series of tools that filter out tweets according to a text query.  You
# # will also build tools that help us map out locations of tweets and, in
# # particular, to give us a geographic picture of "tweet trends" in the US.
# # Your code will be used to present a US "heat map" of a tweet topic, 
# # coloring each US state by our estimate of how popular that topic is in
# # each state.
# #
# # You are to write these functions:
# #
# # is_in_state    -- determines whether a tweet occurred within a state's borders.
# # hits_border    -- function used by the above; checks for location relative
# #                   to a state's border line.
# # count_by_state -- computes the number of occurrences of a list of tweets,
# #                   broken down by state.  Uses 'is_in_state'.
# # heat_by_state  -- computes our estimate of how important a tweet is, broken
# #                   down by state; uses the function 'count_by_state', then
# #                   normalizes that count to a "heat value" between 0 and 1.
# # make_query     -- builds a tweet query from a search term.
# # 
# # These are used by the procedure 'draw_map_for_query', which draws a map of
# # the US states, colored according to your heat information.  You can see
# # examples of that procedure's use, commented out, at the bottom of this 
# # file.

# from data import load_tweets
# from datetime import datetime
# from geo import (us_states, 
#                  us_state_pop, 
#                  geo_distance, 
#                  make_position, 
#                  longitude, 
#                  latitude)
# from maps import draw_state, wait
# import random


# ###############################
# # Working With Tweets: Part 1 #
# ###############################

# # The tweet abstract data type, implemented as a dictionary.

# def make_tweet(text, time, lat, lon):
#     """Return a tweet, represented as a Python dictionary.

#     text  -- A string; the text of the tweet, all in lowercase
#     time  -- A datetime object; the time that the tweet was posted
#     lat   -- A number; the latitude of the tweet's location
#     lon   -- A number; the longitude of the tweet's location

#     >>> t = make_tweet("just ate lunch", datetime(2012, 9, 24, 13), 38, 74)
#     >>> tweet_text(t)
#     'just ate lunch'
#     >>> tweet_time(t)
#     datetime.datetime(2012, 9, 24, 13, 0)
#     >>> p = tweet_location(t)
#     >>> latitude(p)
#     38
#     >>> tweet_string(t)
#     '"just ate lunch" @ (38, 74)'
#     """
#     return {'text': text, 'time': time, 'latitude': lat, 'longitude': lon}

# def tweet_text(tweet):
#     """Return a string, the words in the text of a tweet."""
#     return 'Nothing'

# def tweet_time(tweet):
#     """Return the datetime object representing when a tweet was posted."""
#     return 'Now'

# def tweet_location(tweet):
#     """Return a position representing a tweet's location."""
#     return make_position(0.0,0.0)

# def tweet_string(tweet):
#     """Return a string representing a functional tweet."""
#     location = tweet_location(tweet)
#     point = (latitude(location), longitude(location))
#     return '"{0}" @ {1}'.format(tweet_text(tweet), point)


# #######################################
# # The Geometry of Maps: Parts 2 and 3 #
# #######################################

# def hits_border(location,border1,border2):
#     """ 
#         Casts a ray due east from a map position 'location' to see if that ray hits
#         a border line segment that spans from position 'border1' to position 'border2'.
#     """
#     return True

# def count_hits_region(location, region):
#     """ 
#     Casts a ray due east from a map position 'location'.  Counts how times
#     a ray passes through the edges of a polygonal region.  Returns that count.

#     location -- A location on the earth as a list of two coordinates, its latitude 
#                     and its longitude.

#     region   -- A list of map positions that specify the borders of a polygonal
#                 region.  Each successive pair of list points specify a line segment
#                 on the region's border.  The first and last points in the list are
#                 at the same position because the region is a closed polygon.

#     So this code should just count how many border edges sit due east of 'location'
#     using 'hits_border'.

#     """
#     return 0

# def is_in_region(location, region):
#     """Finds if a location resides within a polygonal region using
#     algorithm at http://en.wikipedia.org/wiki/Point_in_polygon.

#     This uses 'hits_in_region' to cast a ray due east through the 
#     edges of a polygonal region, counting how many edges are hit.
#     If that count is odd, then the location resides within the
#     region.  If that count is even it resides outside the region.

#     location -- A location on the earth as a list of two coordinates, its latitude 
#                     and its longitude.

#     region   -- A list of map positions that specify the borders of a polygonal
#                 region.  Each successive pair of list points specify a line segment
#                 on the region's border.  The first and last points in the list are
#                 at the same position because the region is a closed polygon.

#     """
#     return True

# def is_in_state(location, state_regions):
#     """
#     Finds if a location is inside a state. Uses the ray casting 
#     algorithm at http://en.wikipedia.org/wiki/Point_in_polygon to
#     check whether that location is within the borders of a state.
#     Cast a ray due east through the borders that form the outline 
#     of a state's region, see how many of them intersect that ray.  
#     You can use 'check_intersect' above to individual border check.    

#     location      -- A location on the earth as a list of two coordinates, its latitude 
#                      and its longitude.

#     state_regions -- A list of a state's regions (some states, like Michigan, are
#                      made up of several regions. Each region is described as a list
#                      of earth locations (a pair of coordinates) that are the corner
#                      points of its border.

#     """
#     return True


# ###########################################
# # The Tweets of the Nation: Parts 4 and 5 #
# ###########################################

# def count_by_state(tweets):
#     """
#     Return a dictionary that aggregates a list of tweets by their state of origin.

#     Each entry's value in the dictionary should be a count of the number of tweets 
#     in the list 'tweets' whose location is within that US state.  Each entry's key
#     should be a string of the state's US postal code (e.g. 'OR', 'WA').  

#     tweets -- a list of tweets, normally filtered according to a topic

#     You should use the dictinary 'us_states' to get the map regions of every state.
#     For example, us_states['HI'] gives a list of polygons for the outlines of the
#     islands of Hawaii.

#     You can use 'is_in_state' to check whether a tweet occurs within a state.  Note
#     that some tweets don't occur within any state.  They won't be included in any
#     count.

#     """
#     count = { state:0 for state in us_states }
#     # None counted yet, just returning that dictionary.
#     return count


# def heat_by_state(tweets):
#     """
#     Return a dictionary that aggregates a list of tweets by their state of origin
#     by giving the per capita normalized "heat" per state.

#     Each entry's value in the dictionary should be a heat value from 0.0 to 1.0.
#     A state has a heat value of 1.0 if it the origin of the most tweets per capita
#     for the tweets in the list 'tweets'.  Another state would have a heat value then, 
#     say, of 0.5 if it has half as many tweets per capita in the list.  The heat value 
#     is near 0.0 if it has a trivial number of tweets per capita.

#     Each entry's key should be a string of the state's US postal code (e.g. 'OR', 'WA').  

#     You can use the global variable 'us_state_pop' to get the 2013 estimate of a state's
#     population (e.g. us_state_pop['OR'] would give the population of the state of Oregon).

#     tweets -- a list of tweets, normally filtered according to a topic

#     Use 'count_by_state' to do this work.  Remember, when normalizing, there may be topics
#     that are very unpopular in the US, and so the counts might all be 0.  You wouldn't 
#     want to divide by zero in that case!

#     """
#     heat = { state:0.0 for state in us_states }
#     # No heat values calculated, just returning a dictionary containing 0.0 for every state.
#     return heat


# ####################
# # Queries (Part 6) #
# ####################

# def dunkin_query(text):
#     """
#     Return True if text contains "dunkin" as a substring.
#     Results should not be case-sensitive.  When text includes "DUnkin", 
#     for example, should return True.
#     """
#     return 'dunkin' in text.lower()

# def canada_query(text):
#     """
#     Return True if text contains "canada" as a substring.
#     Results should not be case-sensitive.  When text includes "CAnada", 
#     for example, should return True.
#     """
#     return 'canada' in text.lower()

# def make_query(term):
#     """
#     Returns a test that searches for term as a substring of a given string.
#     Results should not be case-sensitive.

#     For example, make_query("canada") should behave identically to canada_query,
#     as should make_query("CAnada").
#     """
#     # Only returns the canada query.  Broken!
#     return canada_query


# #########################
# # Map Drawing Functions #
# #########################

# def draw_state_frequencies(state_frequencies):
#     """Draw all U.S. states in colors corresponding to their frequency value."""
#     for name, shapes in us_states.items():
#         frequency = state_frequencies.get(name, None)
#         draw_state(shapes, frequency)

# def draw_map_for_query(test, new_file_name=None):
#     if new_file_name == None:
#         random.seed()
#         new_file_name = str(random.randint(0, 1000000000))
#     """Draw the frequency map corresponding to the tweets that pass the test.
#     """
#     tweets = load_tweets(make_tweet, test, new_file_name)
#     tweets_by_state = heat_by_state(tweets)
#     draw_state_frequencies(tweets_by_state)
#     wait()



# ########################
# # Use what you've done #
# ########################

# """
#    Uncomment any of these to test your work, or devise your own tests.
# """

# # draw_map_for_query(dunkin_query)
# # draw_map_for_query(make_query("dunkin"))
# # draw_map_for_query(make_query(input("Enter a query string: ")))
































# # CSCI 121 Fall 2017
# #
# # Project 2 option #2: Visualizing Twitter Topics Across America
# #
# # This file contains the start of the source code that you are to modify
# # in order to complete the Project 2 assignment.  Your job is to build a
# # series of tools that filter out tweets according to a text query.  You
# # will also build tools that help us map out locations of tweets and, in
# # particular, to give us a geographic picture of "tweet trends" in the US.
# # Your code will be used to present a US "heat map" of a tweet topic, 
# # coloring each US state by our estimate of how popular that topic is in
# # each state.
# #
# # You are to write these functions:
# #
# # is_in_state    -- determines whether a tweet occurred within a state's borders.
# # hits_border    -- function used by the above; checks for location relative
# #                   to a state's border line.
# # count_by_state -- computes the number of occurrences of a list of tweets,
# #                   broken down by state.  Uses 'is_in_state'.
# # heat_by_state  -- computes our estimate of how important a tweet is, broken
# #                   down by state; uses the function 'count_by_state', then
# #                   normalizes that count to a "heat value" between 0 and 1.
# # make_query     -- builds a tweet query from a search term.
# # 
# # These are used by the procedure 'draw_map_for_query', which draws a map of
# # the US states, colored according to your heat information.  You can see
# # examples of that procedure's use, commented out, at the bottom of this 
# # file.

# from data import load_tweets
# from datetime import datetime
# from geo import (us_states, 
#                  us_state_pop, 
#                  geo_distance, 
#                  make_position, 
#                  longitude, 
#                  latitude)
# from maps import draw_state, wait
# import random


# ###############################
# # Working With Tweets: Part 1 #
# ###############################

# # The tweet abstract data type, implemented as a dictionary.

# def make_tweet(text, time, lat, lon):
#     """Return a tweet, represented as a Python dictionary.

#     text  -- A string; the text of the tweet, all in lowercase
#     time  -- A datetime object; the time that the tweet was posted
#     lat   -- A number; the latitude of the tweet's location
#     lon   -- A number; the longitude of the tweet's location

#     >>> t = make_tweet("just ate lunch", datetime(2012, 9, 24, 13), 38, 74)
#     >>> tweet_text(t)
#     'just ate lunch'
#     >>> tweet_time(t)
#     datetime.datetime(2012, 9, 24, 13, 0)
#     >>> p = tweet_location(t)
#     >>> latitude(p)
#     38
#     >>> tweet_string(t)
#     '"just ate lunch" @ (38, 74)'
#     """
#     return {'text': text, 'time': time, 'latitude': lat, 'longitude': lon}

# def tweet_text(tweet):
#     """Return a string, the words in the text of a tweet."""
#     return 'Nothing'

# def tweet_time(tweet):
#     """Return the datetime object representing when a tweet was posted."""
#     return 'Now'

# def tweet_location(tweet):
#     """Return a position representing a tweet's location."""
#     return make_position(0.0,0.0)

# def tweet_string(tweet):
#     """Return a string representing a functional tweet."""
#     location = tweet_location(tweet)
#     point = (latitude(location), longitude(location))
#     return '"{0}" @ {1}'.format(tweet_text(tweet), point)


# #######################################
# # The Geometry of Maps: Parts 2 and 3 #
# #######################################

# def hits_border(location,border1,border2):
#     """ 
#         Casts a ray due east from a map position 'location' to see if that ray hits
#         a border line segment that spans from position 'border1' to position 'border2'.
#     """
#     return True

# def count_hits_region(location, region):
#     """ 
#     Casts a ray due east from a map position 'location'.  Counts how times
#     a ray passes through the edges of a polygonal region.  Returns that count.

#     location -- A location on the earth as a list of two coordinates, its latitude 
#                     and its longitude.

#     region   -- A list of map positions that specify the borders of a polygonal
#                 region.  Each successive pair of list points specify a line segment
#                 on the region's border.  The first and last points in the list are
#                 at the same position because the region is a closed polygon.

#     So this code should just count how many border edges sit due east of 'location'
#     using 'hits_border'.

#     """
#     return 0

# def is_in_region(location, region):
#     """Finds if a location resides within a polygonal region using
#     algorithm at http://en.wikipedia.org/wiki/Point_in_polygon.

#     This uses 'hits_in_region' to cast a ray due east through the 
#     edges of a polygonal region, counting how many edges are hit.
#     If that count is odd, then the location resides within the
#     region.  If that count is even it resides outside the region.

#     location -- A location on the earth as a list of two coordinates, its latitude 
#                     and its longitude.

#     region   -- A list of map positions that specify the borders of a polygonal
#                 region.  Each successive pair of list points specify a line segment
#                 on the region's border.  The first and last points in the list are
#                 at the same position because the region is a closed polygon.

#     """
#     return True

# def is_in_state(location, state_regions):
#     """
#     Finds if a location is inside a state. Uses the ray casting 
#     algorithm at http://en.wikipedia.org/wiki/Point_in_polygon to
#     check whether that location is within the borders of a state.
#     Cast a ray due east through the borders that form the outline 
#     of a state's region, see how many of them intersect that ray.  
#     You can use 'check_intersect' above to individual border check.    

#     location      -- A location on the earth as a list of two coordinates, its latitude 
#                      and its longitude.

#     state_regions -- A list of a state's regions (some states, like Michigan, are
#                      made up of several regions. Each region is described as a list
#                      of earth locations (a pair of coordinates) that are the corner
#                      points of its border.

#     """
#     return True


# ###########################################
# # The Tweets of the Nation: Parts 4 and 5 #
# ###########################################

# def count_by_state(tweets):
#     """
#     Return a dictionary that aggregates a list of tweets by their state of origin.

#     Each entry's value in the dictionary should be a count of the number of tweets 
#     in the list 'tweets' whose location is within that US state.  Each entry's key
#     should be a string of the state's US postal code (e.g. 'OR', 'WA').  

#     tweets -- a list of tweets, normally filtered according to a topic

#     You should use the dictinary 'us_states' to get the map regions of every state.
#     For example, us_states['HI'] gives a list of polygons for the outlines of the
#     islands of Hawaii.

#     You can use 'is_in_state' to check whether a tweet occurs within a state.  Note
#     that some tweets don't occur within any state.  They won't be included in any
#     count.

#     """
#     count = { state:0 for state in us_states }
#     # None counted yet, just returning that dictionary.
#     return count


# def heat_by_state(tweets):
#     """
#     Return a dictionary that aggregates a list of tweets by their state of origin
#     by giving the per capita normalized "heat" per state.

#     Each entry's value in the dictionary should be a heat value from 0.0 to 1.0.
#     A state has a heat value of 1.0 if it the origin of the most tweets per capita
#     for the tweets in the list 'tweets'.  Another state would have a heat value then, 
#     say, of 0.5 if it has half as many tweets per capita in the list.  The heat value 
#     is near 0.0 if it has a trivial number of tweets per capita.

#     Each entry's key should be a string of the state's US postal code (e.g. 'OR', 'WA').  

#     You can use the global variable 'us_state_pop' to get the 2013 estimate of a state's
#     population (e.g. us_state_pop['OR'] would give the population of the state of Oregon).

#     tweets -- a list of tweets, normally filtered according to a topic

#     Use 'count_by_state' to do this work.  Remember, when normalizing, there may be topics
#     that are very unpopular in the US, and so the counts might all be 0.  You wouldn't 
#     want to divide by zero in that case!

#     """
#     heat = { state:0.0 for state in us_states }
#     # No heat values calculated, just returning a dictionary containing 0.0 for every state.
#     return heat


# ####################
# # Queries (Part 6) #
# ####################

# def dunkin_query(text):
#     """
#     Return True if text contains "dunkin" as a substring.
#     Results should not be case-sensitive.  When text includes "DUnkin", 
#     for example, should return True.
#     """
#     return 'dunkin' in text.lower()

# def canada_query(text):
#     """
#     Return True if text contains "canada" as a substring.
#     Results should not be case-sensitive.  When text includes "CAnada", 
#     for example, should return True.
#     """
#     return 'canada' in text.lower()

# def make_query(term):
#     """
#     Returns a test that searches for term as a substring of a given string.
#     Results should not be case-sensitive.

#     For example, make_query("canada") should behave identically to canada_query,
#     as should make_query("CAnada").
#     """
#     # Only returns the canada query.  Broken!
#     return canada_query


# #########################
# # Map Drawing Functions #
# #########################

# def draw_state_frequencies(state_frequencies):
#     """Draw all U.S. states in colors corresponding to their frequency value."""
#     for name, shapes in us_states.items():
#         frequency = state_frequencies.get(name, None)
#         draw_state(shapes, frequency)

# def draw_map_for_query(test, new_file_name=None):
#     if new_file_name == None:
#         random.seed()
#         new_file_name = str(random.randint(0, 1000000000))
#     """Draw the frequency map corresponding to the tweets that pass the test.
#     """
#     tweets = load_tweets(make_tweet, test, new_file_name)
#     tweets_by_state = heat_by_state(tweets)
#     draw_state_frequencies(tweets_by_state)
#     wait()



# ########################
# # Use what you've done #
# ########################

# """
#    Uncomment any of these to test your work, or devise your own tests.
# """

# # draw_map_for_query(dunkin_query)
# # draw_map_for_query(make_query("dunkin"))
# # draw_map_for_query(make_query(input("Enter a query string: ")))



















# MATH 121 Fall 2015 
# Sections F02 and F04
# Instructor: J. Fix
#
# Project 2: Visualizing Twitter Topics Across America
#
# This file contains the start of the source code that you are to modify
# in order to complete the Project 2 assignment.  Your job is to build a
# series of tools that filter out tweets according to a text query.  You
# will also build tools that help us map out locations of tweets and, in
# particular, to give us a geographic picture of "tweet trends" in the US.
# Your code will be used to present a US "heat map" of a tweet topic, 
# coloring each US state by our estimate of how popular that topic is in
# each state.
#
# You are to write these functions:
#
# is_in_state    -- determines whether a tweet occurred within a state's borders.
# hits_border    -- function used by the above; checks for location relative
#                   to a state's border line.
# count_by_state -- computes the number of occurrences of a list of tweets,
#                   broken down by state.  Uses 'is_in_state'.
# heat_by_state  -- computes our estimate of how important a tweet is, broken
#                   down by state; uses the function 'count_by_state', then
#                   normalizes that count to a "heat value" between 0 and 1.
# make_query     -- builds a tweet query from a search term.
# 
# These are used by the procedure 'draw_map_for_query', which draws a map of
# the US states, colored according to your heat information.  You can see
# examples of that procedure's use, commented out, at the bottom of this 
# file.

from data import load_tweets
from datetime import datetime
from geo import (us_states, 
                 us_state_pop, 
                 geo_distance, 
                 make_position, 
                 longitude, 
                 latitude)
from maps import draw_state, wait
import random


###################################
# Working With Tweets: Exercise 1 #
###################################

# The tweet abstract data type, implemented as a dictionary.

def make_tweet(text, time, lat, lon):
    """Return a tweet, represented as a Python dictionary.

    text  -- A string; the text of the tweet, all in lowercase
    time  -- A datetime object; the time that the tweet was posted
    lat   -- A number; the latitude of the tweet's location
    lon   -- A number; the longitude of the tweet's location

    >>> t = make_tweet("just ate lunch", datetime(2012, 9, 24, 13), 38, 74)
    >>> tweet_text(t)
    'just ate lunch'
    >>> tweet_time(t)
    datetime.datetime(2012, 9, 24, 13, 0)
    >>> p = tweet_location(t)
    >>> latitude(p)
    38
    >>> tweet_string(t)
    '"just ate lunch" @ (38, 74)'
    """
    return {'text': text, 'time': time, 'latitude': lat, 'longitude': lon}

def tweet_text(tweet):
    """Return a string, the words in the text of a tweet."""
    return tweet['text']

def tweet_time(tweet):
    """Return the datetime object representing when a tweet was posted."""
    return tweet['time']

def tweet_location(tweet):
    """Return a position representing a tweet's location."""
    return make_position(tweet['latitude'],tweet['longitude'])
    

def tweet_string(tweet):
    """Return a string representing a functional tweet."""
    location = tweet_location(tweet)
    point = (latitude(location), longitude(location))
    return '"{0}" @ {1}'.format(tweet_text(tweet), point)


###########################################
# The Geometry of Maps: Exercises 2 and  3 #
###########################################

def hits_border(location,border1,border2):
    """ 
        Casts a ray due east from a map position 'location' to see if that ray hits
        a border line segment that spans from position 'border1' to position 'border2'.
    """
    y = latitude(location)
    if latitude(border1) > latitude(border2):
        maxy = latitude(border1)
        miny = latitude(border2)
    else:
        maxy = latitude(border2)
        miny = latitude(border1)
    if  miny < y < maxy :
        x = ((longitude(border2)-longitude(border1))*(y - latitude(border1))/(latitude(border2)-latitude(border1)))+longitude(border1)
        if x > longitude(location):
            return True
        else:
            return False
    else:
        return False
        



def count_hits_region(location, region):
    """ 
    Casts a ray due east from a map position 'location'.  Counts how times
    a ray passes through the edges of a polygonal region.  Returns that count.

    location -- A location on the earth as a list of two coordinates, its latitude 
                    and its longitude.

    region   -- A list of map positions that specify the borders of a polygonal
                region.  Each successive pair of list points specify a line segment
                on the region's border.  The first and last points in the list are
                at the same position because the region is a closed polygon.

    So this code should just count how many border edges sit due east of 'location'
    using 'hits_border'.

    """
    l=len(region)
    c=0
    for i in range(0,l-1):
        if hits_border(location,region[i],region[i+1])==True:
            c=c+1
    return c

def is_in_region(location, region):
    """Finds if a location resides within a polygonal region using
    algorithm at http://en.wikipedia.org/wiki/Point_in_polygon.

    This uses 'hits_in_region' to cast a ray due east through the 
    edges of a polygonal region, counting how many edges are hit.
    If that count is odd, then the location resides within the
    region.  If that count is even it resides outside the region.

    location -- A location on the earth as a list of two coordinates, its latitude 
                    and its longitude.

    region   -- A list of map positions that specify the borders of a polygonal
                region.  Each successive pair of list points specify a line segment
                on the region's border.  The first and last points in the list are
                at the same position because the region is a closed polygon.

    """
    c= count_hits_region(location, region)
    if c%2==1:
        return True
    else:
        return False

def is_in_state(location, state_regions):
    """
    Finds if a location is inside a state. Uses the ray casting 
    algorithm at http://en.wikipedia.org/wiki/Point_in_polygon to
    check whether that location is within the borders of a state.
    Cast a ray due east through the borders that form the outline 
    of a state's region, see how many of them intersect that ray.  
    You can use 'check_intersect' above to individual border check.    

    location      -- A location on the earth as a list of two coordinates, its latitude 
                     and its longitude.

    state_regions -- A list of a state's regions (some states, like Michigan, are
                     made up of several regions. Each region is described as a list
                     of earth locations (a pair of coordinates) that are the corner
                     points of its border.

    """
    flag=0
    for each in state_regions:
        if is_in_region(location,each)==True:
            flag=1
    if flag==1:
        return True
    else:
        return False


###############################################
# The Tweets of the Nation: Exercises 4 and 5 #
###############################################

def count_by_state(tweets):
    """
    Return a dictionary that aggregates a list of tweets by their state of origin.

    Each entry's value in the dictionary should be a count of the number of tweets 
    in the list 'tweets' whose location is within that US state.  Each entry's key
    should be a string of the state's US postal code (e.g. 'OR', 'WA').  

    tweets -- a list of tweets, normally filtered according to a topic

    You should use the dictinary 'us_states' to get the map regions of every state.
    For example, us_states['HI'] gives a list of polygons for the outlines of the
    islands of Hawaii.

    You can use 'is_in_state' to check whether a tweet occurs within a state.  Note
    that some tweets don't occur within any state.  They won't be included in any
    count.

    """
   
    
    s_d=dict()
    name_state=us_states
    for state in name_state:
        s_d[state]=0
        for each in tweets:
            if is_in_state(tweet_location(each), us_states[state])==True:
                s_d[state]=s_d[state]+1
    return s_d



def heat_by_state(tweets):
    """
    Return a dictionary that aggregates a list of tweets by their state of origin
    by giving the per capita normalized "heat" per state.

    Each entry's value in the dictionary should be a heat value from 0.0 to 1.0.
    A state has a heat value of 1.0 if it the origin of the most tweets per capita
    for the tweets in the list 'tweets'.  Another state would have a heat value then, 
    say, of 0.5 if it has half as many tweets per capita in the list.  The heat value 
    is near 0.0 if it has a trivial number of tweets per capita.

    Each entry's key should be a string of the state's US postal code (e.g. 'OR', 'WA').  

    You can use the global variable 'us_state_pop' to get the 2013 estimate of a state's
    population (e.g. us_state_pop['OR'] would give the population of the state of Oregon).

    tweets -- a list of tweets, normally filtered according to a topic

    Use 'count_by_state' to do this work.  Remember, when normalizing, there may be topics
    that are very unpopular in the US, and so the counts might all be 0.  You wouldn't 
    want to divide by zero in that case!

    """
    
    max=0
    new_dict=count_by_state(tweets)
    for each in new_dict:
        new_dict[each]=new_dict[each]/us_state_pop[each]
        if new_dict[each]>=max:
            max=new_dict[each]
    for each in new_dict:
        new_dict[each]=new_dict[each]/max
    return new_dict


########################
# Queries (Exercise 6) #
########################

def dunkin_query(text):
    """
    Return True if text contains "dunkin" as a substring.
    Results should not be case-sensitive.  When text includes "DUnkin", 
    for example, should return True.
    """

    return 'dunkin' in text.lower()

def canada_query(text):
    """
    Return True if text contains "canada" as a substring.
    Results should not be case-sensitive.  When text includes "CAnada", 
    for example, should return True.
    """
    return 'canada' in text.lower()

def make_query(term):
    """
    Returns a test that searches for term as a substring of a given string.
    Results should not be case-sensitive.

    For example, make_query("canada") should behave identically to canada_query,
    as should make_query("CAnada").
    """
    def search(text):
        s=term.lower()
        if s in text.lower():
            return True
        return False
    return search




#########################
# Map Drawing Functions #
#########################

def draw_state_frequencies(state_frequencies):
    """Draw all U.S. states in colors corresponding to their frequency value."""
    for name, shapes in us_states.items():
        frequency = state_frequencies.get(name, None)
        draw_state(shapes, frequency)

def draw_map_for_query(test, new_file_name=None):
    if new_file_name == None:
        random.seed()
        new_file_name = str(random.randint(0, 1000000000))
    """Draw the frequency map corresponding to the tweets that pass the test.
    """
    tweets = load_tweets(make_tweet, test, new_file_name)
    tweets_by_state = heat_by_state(tweets)
    draw_state_frequencies(tweets_by_state)
    wait()



########################
# Use what you've done #
########################

"""
   Uncomment any of these to test your work, or devise your own tests.
"""

#draw_map_for_query(dunkin_query)
#draw_map_for_query(make_query("dunkin"))
#draw_map_for_query(make_query(input("Enter a query string: ")))
