#!/usr/bin/env python
# coding: utf-8

# # Perform illumination correction and save the images

# ## Import libraries

# In[1]:


import pathlib
import pprint

import sys

sys.path.append("../utils")
import cp_parallel


# ## Set paths and variables

# In[2]:


# set the run type for the parallelization
run_name = "illum_correction"

# set path for CellProfiler pipeline
path_to_pipeline = pathlib.Path("./illum.cppipe").resolve(strict=True)

# set main output dir for all plates if it doesn't exist
output_dir = pathlib.Path("./Corrected_Images")
output_dir.mkdir(exist_ok=True)

# directory where max-projected images are within the folder
images_dir = pathlib.Path(
    "../1.max_projection/Max_Projected_Images/NF0014"
).resolve(strict=True)

# Get the plate name from the folder name
plate_name = images_dir.stem  # Get the folder name as the plate name
print(plate_name)


# ## Create dictionary to process data

# In[3]:


# create plate info dictionary with all parts of the CellProfiler CLI command to run in parallel
plate_info_dictionary = {
    plate_name: {
        "path_to_images": images_dir,
        "path_to_output": pathlib.Path(f"{output_dir}/{plate_name}"),
        "path_to_pipeline": path_to_pipeline,
    }
}

# view the dictionary to assess that all info is added correctly
pprint.pprint(plate_info_dictionary, indent=4)


# ## Perform illumination correction on data
# 
# The function being called is called "run_cellprofiler_parallel" but can be used if there is only one plate to run. We can also split the data by well and process that way in parallel, but we choose to process at all at once for now.
# 
# Note: This code cell was not ran as we prefer to perform CellProfiler processing tasks via `sh` file (bash script) which is more stable.

# In[ ]:


cp_parallel.run_cellprofiler_parallel(
    plate_info_dictionary=plate_info_dictionary, run_name=run_name
)

