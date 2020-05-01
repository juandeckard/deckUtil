"""A module designed to make coordinate visualization easier."""

__all__     = ["geoMap", "mapMarkers"] # We need to restrict the use of some modules in here, so we define the ones to use as public.
__version__ = '0.1'                    # Version

# Imports
from folium import Map, Marker, Popup, Icon
from pandas import DataFrame, concat

# Constants
__valid_colors = ["red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige", "darkblue", "darkgreen", "cadetblue", "darkpurple", "white", "pink", "lightblue", "lightgreen", "gray", "black", "lightgray"]

def geoMap(location, zoom=10, view="OpenStreetMap", key=None):
    """Return a Map of a given location.
       Parameters:
           location : Coordinates to center the map. This need to be a tuple with element (x,y).
           zoom     : An integer of how much zoom you want. Some maps have restrictions on this zoom. Optional.
                      Default: 10.
           view     : The map style you want to use. Optional.
                      Free options: openstreetmap, cartodb, stamen terrain.
                      Free options with zoom restrictions: mapbox control room , mapbox bright.
                      Options with valid key: cloudmade, mapbox.
                      Default: openstreetmaps.
           key      : An API key, only needed if you are going to use cloudmade or mapbox.
           
       Example      : The following example will return you the area near downtown Portland.
                          
                          map = geoMap((45.523, -122.675))
           
       Output:      : folium.Map
    """
    
    if type(zoom) == int:                                                                       # Check type for zoom
        if view.lower() == "cloudmade" or view.lower == "mapbox":                               # Check if we need a key in this case.
            if key:                                                                             # Check if we have a key to work with.
                try:
                    return Map(location=location, zoom_start=zoom, tiles=view, API_key=key)     # Return map.
                except:
                    raise                                                                       # Raise error if something goes wrong.
            else:
                raise ValueError("Key required for " +  view + " view.")                        # Raise error if no key provided.
        elif view.lower() in ["openstreetmap", "cartodb", "stamen terrain",                             # Check if given view is actually a valid view.
                              "mapbox control room", "mapbox bright"]:
            try:
                return Map(location=location, zoom_start=zoom, tiles=view)                      # return map.
            except:
                raise                                                                           # Raise error if something goes wrong
        else:
            raise ValueError(view + " is not a valid view, check documentation for more info.") # Raise error if view is not valid. Check docstring.
    else:
        raise TypeError("Zoom type most be int, not " + str(type(zoom)) + ".")                  # Raise error if zoom is not an int
        
def mapMarkersSingleSet(fmap, data, text = None, color = None, icon = "", prefix = "glyphicon"):
    """Adds markers to a map, with a single set of data. Does most of the validations.
       Parameters
           fmap        : A map instance from folium. Check out function geoMap for more info about maps by doing geoMap.__doc__.
           data        : A list of lists or a list of DataFrames with coordinates to pin. Coordinates given as tuples (x,y).
           text        : A list of lists or a list of DataFrames with text to lable each pin. 
           color       : A list of colors to color each subset.
                         Supported colors: "red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige", "darkblue",
                                           "darkgreen", "cadetblue", "darkpurple", "white", "pink", "lightblue", "lightgreen",
                                           "gray", "black", "lightgray"
           icon        : An icon to use in each subset. You can get a list of supported icons from 
                         https://fontawesome.com/icons?d=gallery     or     https://getbootstrap.com/docs/3.3/components/
           prefix      : If you are going to use FontAwesome icons, set to fa, else glyphicon (bootstrap) comes as default.
       Example         : This will show a single subset inside the downtown Portland area.
       
                             map   = geoMap((45.523, -122.675))
                             data  = [(45.525, -122.674),(45.522, -122.675),(45.521, -122.677)]
                             text  = ["Casita","Room","Igloo"]
                             color = "orange"
                             icon  = "glyphicon-home"
                             
                             mapMarkersSingleSet(map, data, text, color, icon)
                             
                             map
                         
       Output          : None
    """
    
    # Change type of data to dataframe
    if type(data) == list:
        data = DataFrame(data)
    # Change type of text to dataframe.
    if type(text) == list:
        text = DataFrame(text)
    elif not type(text) == DataFrame:
        raise TypeError("Type of text most be list or DataFrame, not " + str(type(text)) + ".")

    if type(color) == str:
        # Check if color is actually on the palette
        if color not in __valid_colors:
            raise ValueError("Color " + str(color) + " not a posibility. Check the documentation for a list of colors.")
    if data.shape[0] == text.shape[0]: # Check shape consistancy. 
        for geo_location in concat([data,text, DataFrame([color] * text.size), DataFrame([icon] * text.size)], axis=1).iterrows():
            x, y, text_popup, icon_color, icon_type = tuple([elem for elem in geo_location[1]]) # Unpack data from DataFrame.
            Marker(location = (x,y), popup = Popup(text_popup), prefix=prefix, icon=Icon(color=icon_color, icon=icon_type)).add_to(fmap) # Add marker to map.
    else:
        raise ValueError("Data shape " + str(data.shape) + " needs to be the same as text shape " + str(text.shape) + ".") # Raise an error if shape of data and text is not the same.
        
def mapMarkers(fmap, data, text = None, colors = None, icons = None, fontAwesome = False):
    """Plugs multiple sets of markers into a map. Can change color and text of the pins.
       Parameters
           fmap        : A map instance from folium. Check out function geoMap for more info about maps by doing geoMap.__doc__.
           data        : A list of lists or a list of DataFrames with coordinates to pin. Coordinates given as tuples (x,y).
           text        : A list of lists or a list of DataFrames with text to lable each pin. 
           colors      : A list of colors to color each subset.
                         Supported colors: "red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige", "darkblue",
                                           "darkgreen", "cadetblue", "darkpurple", "white", "pink", "lightblue", "lightgreen",
                                           "gray", "black", "lightgray"
           icons       : An icon to use in each subset. You can get a list of supported icons from 
                         https://fontawesome.com/icons?d=gallery     or     https://getbootstrap.com/docs/3.3/components/
           fontAwesome : If you are going to use FontAwesome icons, set to True. Note: can't use both at the same time.
    
       Example         : The following example will add a few red pins and green pins around downtown Portland.
                             
                             map    = geoMap((45.523, -122.675))
                             data   = [[(45.525, -122.674),(45.522, -122.675),(45.541, -122.637)],[(45.545, -122.644),(45.532, -122.672),(45.517, -122.652)]]
                             text   = [["Casita","Room","Igloo"],["Tent with amazing view","RV","Cabin"]]
                             colors = ["green","red"]
                             
                             mapMarkers(map, data, text, colors, "glyphicon-home")
                             
                             map
                             
       Output          : None
    """
    
    prefix = "glyphicon"                                                                    # Set bootstrap as standard.
    if fontAwesome:
        prefix = "fa"                                                                       # Use fontAwesome if flaged.
    
    if len(data) == len(text) and len(data) == len(colors):
        for data_info, text_info, color_info, icon_info in zip(data, text, colors, icons):  # Loop over the data and info sets.

            mapMarkersSingleSet(fmap, data_info, text_info, color_info, icon_info, prefix)  # Draw a single set first.
    else:
        # Error if size of data, text or colors don't match.
        raise ValueError("Size of data, text and colors should be the same, but data is " + len(data) + " while text is " + len(text) + " while colors is " + len(colors) + ".")