"""Module for importing code mapping files: only LOINC required for now"""
from testdata import LOINC_FILE
import argparse
import csv

class Loinc:
    """Creates loinc code instances and holds global loinc dictionary"""
    info = {} # Dictionary of loinc code information

    @classmethod
    def load(cls,loinc_list):
      """Loads code_info dictionary for LOINC codes in loinc_list"""
      
      # Open data file and read in the first (header) record
      loincs = csv.reader(file(LOINC_FILE,'U'),dialect='excel-tab')
      header = loincs.next() 
      # Now, read in loinc codes:
      for loinc in loincs: 
        l = dict(zip(header,loinc)) # build row dictionary of values
        if l['LOINC_NUM'] in loinc_list: # See if we're interested in this code  
          cls(l) # If so, creat a loinc instance and store it in Loinc.info

    def __init__(self,l):
        """Creates a loinc instance and save it in Loinc.info"""
        self.code = l['LOINC_NUM']
        self.name= l['SHORTNAME'] 
        self.system = l['SYSTEM']
        self.scale = l['SCALE_TYP']
        self.ucum = l['EXAMPLE_UCUM_UNITS']
        self.source= l['SOURCE']
        self.units_required = l['UNITSREQUIRED']
        self.__class__.info[self.code]=self

if __name__== '__main__':

  parser = argparse.ArgumentParser(description='Test Data Codes Module')
  group = parser.add_mutually_exclusive_group()
  group.add_argument('--loinc', nargs='?',const='25324-5',
                      help='Display info for a LOINC code (default = 25324-5)')
  args = parser.parse_args()

  Loinc.load([args.loinc])
  if not args.loinc in Loinc.info: 
     parser.error("LOINC code %s not found"%args.loinc)
  else: 
    l = Loinc.info[args.loinc]
    print l.code, l.name,l.scale,l.ucum, l.system 
