import revitron
from revitron import _
from collections import defaultdict

config = revitron.DocumentConfigStorage().get('revitron.export', defaultdict())

exporter = revitron.PDFExporter(config.get('PDF_Printer_Address'), config.get('PDF_Temporary_Output_Path'))

sizeParamName = config.get('Sheet_Size_Parameter_Name')
defaultSize = config.get('Default_Sheet_Size')
orientationParamName = config.get('Sheet_Orientation_Parameter_Name')
defaultOrientation = config.get('Default_Sheet_Orientation')

sheets = revitron.Selection().get()

if not sheets:
    sheets = [revitron.ACTIVEVIEW]

for sheet in sheets:

	if sheet.Category.Name == 'Sheets':		

		sheetSize = False
		sheetOrientation = False

		if sizeParamName:
			sheetSize = _(sheet).get(sizeParamName)

		if orientationParamName:
			sheetOrientation = _(sheet).get(orientationParamName)
			
		if not sheetSize:
			sheetSize = defaultSize
			
		if not sheetOrientation:
			sheetOrientation = defaultOrientation

		exporter.printSheet(sheet, 
							sheetSize, 
							sheetOrientation, 
							config.get('Sheet_Export_Directory'), 
							config.get('Sheet_Naming_Template')
							)
