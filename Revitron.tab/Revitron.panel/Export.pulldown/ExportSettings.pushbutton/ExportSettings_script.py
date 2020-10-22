import revitron
from revitron import _
from rpw.ui.forms import FlexForm, TextBox, Button, Label, Separator, ComboBox
from collections import defaultdict
from pyrevit import script
import System.Windows

def addFields(components, fields):
	for field in fields:
		if field == '---':
			components.append(Separator())
		else:
			key = revitron.String.sanitize(field)
			components.append(Label(field))
			components.append(TextBox(key, Text=config.get(key)))
	return components

def openHelp(sender, e):
	script.open_url('https://revitron-ui.readthedocs.io/en/latest/tools/export.html')

if not revitron.Document().isFamily():
	
	config = revitron.DocumentConfigStorage().get('revitron.export', defaultdict())
	
	components = addFields([], 
	[
		'Sheet Export Directory',
		'Sheet Naming Template',
		'Sheet Size Parameter Name',
		'Default Sheet Size',
		'Sheet Orientation Parameter Name'
	])

	orientationField = 'Default Sheet Orientation'
	orientationKey = revitron.String.sanitize(orientationField)
	orientations = ['Landscape', 'Portrait']
	default = orientations[0]
	if config.get(orientationKey) in orientations:
		default = config.get(orientationKey)
	components.append(Label(orientationField))
	components.append(ComboBox(orientationKey, orientations, default=default))
	
	components = addFields(components, 
	[
		'---',
		'PDF Printer Address',
		'PDF Temporary Output Path',
		'---',
		'DWG Export Setup'
	])
	
	components.append(Label(''))
	components.append(Button('Open Documentation', on_click=openHelp))
	components.append(Button('Save'))
	
	form = FlexForm('PDF and DWG Export Settings', components)
	form.show()
		  
	if form.values: 
		revitron.DocumentConfigStorage().set('revitron.export', form.values)
