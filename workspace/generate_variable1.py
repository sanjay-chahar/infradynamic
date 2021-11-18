#!/usr/bin/python3
import pandas as pd
import openpyxl
from jinja2 import Template
import os
directory = "templates"

# Parent Directory path
parent_dir = "/home/devops/my_project/workspace/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
#os.mkdir(path)
if not os.path.exists(path):
    os.mkdir(path)
    print("path '{}' created ".format(path))
else:
    print("path {} already exists".format(path))
my_file = 'my_first_template'
new_templates_path = os.path.join(path, my_file)
print(new_templates_path)
#list of tab in excel sheet
list_tab_sheet = pd.ExcelFile('test-sheet - Copy.xlsx')
list_tab_sheet.sheet_names
num_tab_sheet = len(list_tab_sheet.sheet_names)
print("list of tab in excel sheet are \n{}.".format(list_tab_sheet.sheet_names))
print("number of tab in sheet = {}" .format(num_tab_sheet))

#df=list_tab_sheet.parse(list_tab_sheet.sheet_names[5])
df=list_tab_sheet.parse(list_tab_sheet.sheet_names[1])
print(df)

interface_template_file = 'ERBFWU01 DNSP TEMPLATE.txt.j2'

#template = 'ERBFWU01 DNSP TEMPLATE.txt.j2'
data = {"first_var" : df.iloc[1, 2]}, "second_var" : df.iloc[2, 2], "third_var" : df.iloc[3, 2], "fourth_var" : df.iloc[4, 2], "fourth_var" : df.iloc[4, 2], "fifth_var" : df.iloc[4, 2]}
with open(interface_template_file) as f:
  interface_template = Template(f.read())

interface_config = interface_template.render(data)
#print(interface_config)

#fin_interface_config = interface_config

#f = open(new_templates_path, "w")
#f.write(interface_config)

#master_template_file = "master-template"
#with open(master_template_file) as x:
#    master_template = Template(x.read())
#z = type(master_template)
#print(z)

#final_master_template = master_template(fin_interface_config)
#print(final_master_template)
