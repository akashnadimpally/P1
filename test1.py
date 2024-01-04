# import pandas as pd
# import re
# import os
# import xml.etree.ElementTree as ET

# # Load XML file
# xml_file_path = '/Users/akash/Desktop/Alpha/P1/demo2.xml'
# tree = ET.parse(xml_file_path)
# root = tree.getroot()

# # Initialize data for tabulation
# data = {'Resource Type': []}

# # Iterate through mxCell elements and extract information
# for mx_cell in root.findall('.//mxCell'):
#     if mx_cell.get('style') and 'image' in mx_cell.get('style'):
#         resource_type = mx_cell.get('style').split('/')[-1].split('.')[0]

#         # Check if resource_type contains the specified string
#         if 'svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcm' in resource_type:
#             resource_type = 'subnet'

#         data['Resource Type'].append(resource_type)

# # Create a DataFrame from the extracted data
# df = pd.DataFrame(data)

# # Print the tabulated data
# print(df)

import pandas as pd
import re
import os
import xml.etree.ElementTree as ET

# Load XML file
xml_file_path = '/Users/akash/Desktop/Alpha/P1/demo2.xml'
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Initialize data for tabulation
data = {'Resource Type': []}

# Define the pattern to identify the substring
pattern = re.compile(r'svg\+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcm')

# Iterate through mxCell elements and extract information
for mx_cell in root.findall('.//mxCell'):
    if mx_cell.get('style') and 'image' in mx_cell.get('style'):
        resource_type = mx_cell.get('style').split('/')[-1].split('.')[0]

        # Check if pattern is present in resource_type
        if pattern.search(resource_type):
            resource_type = 'subnet'

        data['Resource Type'].append(resource_type)

# Create a DataFrame from the extracted data
df = pd.DataFrame(data)

# Drop rows with invalid "Resource Type" values
df = df[df['Resource Type'] != '']

# Print the tabulated data
print(df)
