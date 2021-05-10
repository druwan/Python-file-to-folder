import os
import shutil
from pathlib import Path

path = Path("D://Downloads")

# Read filename and create folder
for source_name in os.listdir("D://Downloads"):
    if source_name.endswith(".pdf"):
        # If pdf file - create a folder
        source_name_no_ext = os.path.splitext(source_name)[0]
        newFolder = os.path.join(path, source_name_no_ext)
        # Create a path to each file to be moved
        fileDirMove = os.path.join(path, source_name)
        os.mkdir(newFolder)
        shutil.move(fileDirMove, newFolder)

