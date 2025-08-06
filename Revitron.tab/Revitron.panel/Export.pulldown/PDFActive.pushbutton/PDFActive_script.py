import revitron
from revitron import _
from revitronui import PDF
from pyrevit import script
import os
import sys

#prevent error mesaage if we not in a sheet
if hasattr(revitron, "ACTIVE_VIEW"):
	sheet = revitron.ACTIVE_VIEW
else:
	print("Warning: 'ACTIVE_VIEW' it's not a sheet. This command works only in a activeated sheet. Or the Export settings are not correct. Please check tha active view and the Revitron Export Settings.")
	sys.exit(1)
	
sheet = revitron.ACTIVE_VIEW

if _(sheet).getClassName() == 'ViewSheet':
	pdf = PDF()
	path = pdf.export(sheet)
	if path:
		script.get_output().print_html(
		    ':smiling_face: Exported <em>{}</em>'.format(os.path.basename(path))
		)
		script.show_folder_in_explorer(os.path.dirname(path))
	else:
		script.get_output().print_html(':pouting_face: Error exporting')
