"""
Microvellum 
Appliances 
Stores all of the Logic, Product, and Insert Class definitions for appliances
"""

import os
from mv import fd_types, unit
from . import appliance_classes

BATHROOM_SINK_PATH = os.path.join(os.path.dirname(__file__),"Bathroom_Sinks")
BATHROOM_FAUCETS_PATH = os.path.join(os.path.dirname(__file__),"Bathroom Faucets")
KITCHEN_FAUCETS_PATH = os.path.join(os.path.dirname(__file__),"Kitchen Faucets")

#---------PRODUCT: BATHROOM SINKS    

class PRODUCT_Bachata_2609_MU(appliance_classes.Countertop_Appliance):
    
    def __init__(self):
        self.category_name = "Bathroom Sinks"
        self.assembly_name = "Bachata 2609-MU"
        self.appliance_path = os.path.join(BATHROOM_SINK_PATH,"Bachata 2609-MU.blend")  

#---------PRODUCT: BATHROOM FAUCETS            
        
class PRODUCT_Alteo_45100_4(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Bathroom Faucets"
        self.appliance_path = os.path.join(BATHROOM_FAUCETS_PATH,"Alteo 45100-4.blend")        
        
#---------PRODUCT: KITCHEN FAUCETS             

class PRODUCT_Antique_149_3(appliance_classes.Object_Appliance):
    
    def __init__(self):
        self.category_name = "Kitchen Faucets"
        self.appliance_path = os.path.join(KITCHEN_FAUCETS_PATH,"Antique 149-3.blend")    