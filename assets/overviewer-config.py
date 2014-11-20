# This is a sample config file, meant to give you an idea of how to format your
# config file and what's possible.

# Define the path to your world here. 'My World' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['m.fe80.eu'] = "/mnt/worlddata"

# Define where to put the output here.
outputdir = "/mnt/mapdata"

# Where to get textures to render from
texturepath = "/usr/share/overviewer/textures.zip"

# This is an item usually specified in a renders dictionary below, but if you
# set it here like this, it becomes the default for all renders that don't
# define it.
# Try "smooth_lighting" for even better looking maps!
rendermode = "smooth_lighting"

renders["Day"] = {
        'world': 'm.fe80.eu',
        'title': 'Overworld',
}

renders["Night"] = {
        'world': 'm.fe80.eu',
        'title': 'Nighttime',
        'rendermode': 'night',
}

