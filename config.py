# *************************** Script Options ****************************
# Fusion 360 Project Name
PROJECT_NAME = 'Project Import Test'

# Name of local folder for Fusion 360 Files
LOCAL_FUSION_FOLDER = 'FusionFiles'

# When set to True, it will export the active Fusion 360 project
# This will also disable the import function
DO_EXPORT = True

# When set True, it will skip import when file already exists in project
SKIP_IMPORT_ON_DUPLICATES = True

# When set True, it will skip exporting files with parent references
SKIP_EXPORT_ON_PARENTS = True

# When set True, it will skip exporting files with child references
SKIP_EXPORT_ON_CHILDREN = True

# When set True, will skip export when file already exists in folder
SKIP_EXPORT_ON_DUPLICATES = True

# When set True, will show text command palettes automatically
# Particularly useful when running export command
# For mass distribution should probably be set False
AUTO_SHOW_TEXT_COMMAND_PALETTE = False
# ***********************************************************************
