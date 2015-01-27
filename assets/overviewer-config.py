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

def signFilter(poi):
	if poi['id'] == 'Sign':
		text = '\n'.join(poi['Text'+str(i)].strip('"') for i in range(1,5)).strip('\n')
		if text.startswith('#'):
			return text

def screenshotFilter(poi):
	'''This looks for signs that have their first line in the '#img:<id>' format, where <id> is an
	id from an Imgur.com image.'''
	if poi['id'] == 'Sign':
		if poi['Text1'].startswith('#img:'):
			poi['icon'] = "painting_icon.png"
			image_html = "<style>.infoWindow img[src='{icon}'] {{display: none}}</style><a href='http://imgur.com/{id}'><img src='http://imgur.com/{id}s.jpg' /></a>".format(icon=poi['icon'], id=poi['Text1'][5:])
			return '\n'.join([image_html] + [poi[ti].strip('"') for ti in ['Text2', 'Text3', 'Text4']]) 

signs = {'name': 'Signs',
		 'filterFunction': signFilter
}

screenshots = {'name': 'Screenshots',
			   'filterFunction': screenshotFilter
}

renders['Day'] = {
        'world': 'm.fe80.eu',
        'title': 'Overworld',
		'markers': [signs, screenshots]
}

renders['Night'] = {
        'world': 'm.fe80.eu',
        'title': 'Nighttime',
        'rendermode': 'night',
		'markers': [signs, screenshots]
}

