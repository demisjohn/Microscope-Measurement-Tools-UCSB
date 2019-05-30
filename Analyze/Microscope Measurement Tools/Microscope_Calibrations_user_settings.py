'''
	FIJI Plugin
Configuration for Microscope Calibrations
Demis D. John, Univ. of California Santa Barbara, 2019

This version of the settings file contains a pointer to a custom function, which automatically sets the scale by loading a text file that corresponds to the loaded image file.  The custom function is found in a separate file "JEOL_SEM_AutoCal.py", and you can see the class defined in this file being loaded below.
In addition, an instance of the class is inserted into the lists of names/calibrations, and all information will be obtained from the Class/external file.

Please make sure the lists `names`, `cals` and `units` all have the same number of items!

After you edit this file, be sure to delete the corresponding *.pyclass file and restart Fiji for the settings to take effect.
'''


"""
################################
   Microscope Image settings
################################

Microscope scaling/pixel-size calibration settings.
"""

# The names of the microscope calibrations (shows up as the radio button names):
#   For custom functions, pass the handle to an instantiated class instead of a string.

# Custom Function: Load JEOL SEM autocal class from a file:
from JEOL_SEM_AutoCal   import JEOL_SEM_CalFromTxt
jeol_sem_cal_from_txt = JEOL_SEM_CalFromTxt()    # instantiate the class


# This defines the items in the drop-down list:
names = [
        'FluoroScope (Olympus MX51): 5x', 
        'FluoroScope (Olympus MX51): 20x', 
        'FluoroScope (Olympus MX51): 50x', 
        'FluoroScope (Olympus MX51): 100x', 
        'FluoroScope (Olympus MX51): 150x',
        
        'Microscope #2 (Nikon Optiphot 200): 5x',
        'Microscope #2 (Nikon Optiphot 200): 10x',
        'Microscope #2 (Nikon Optiphot 200): 50x',
        'Microscope #2 (Nikon Optiphot 200): 100x',
        'Microscope #2 (Nikon Optiphot 200): 150x',
        
        'Microscope #3 (Nikon Eclipse L200): 5x',
        'Microscope #3 (Nikon Eclipse L200): 10x',
        'Microscope #3 (Nikon Eclipse L200): 20x',
        'Microscope #3 (Nikon Eclipse L200): 50x',
        'Microscope #3 (Nikon Eclipse L200): 100x',
        'Microscope #3 (Nikon Eclipse L200): 150x',
        
        'Microscope #4 (Nikon Eclipse L200D): 5x',
        'Microscope #4 (Nikon Eclipse L200D): 10x',
        'Microscope #4 (Nikon Eclipse L200D): 20x',
        'Microscope #4 (Nikon Eclipse L200D): 50x',
        'Microscope #4 (Nikon Eclipse L200D): 100x',
        'Microscope #4 (Nikon Eclipse L200D): 150x',
        
        'Olympus DUV (MX61A): 5x',
        'Olympus DUV (MX61A): 10x',
        'Olympus DUV (MX61A): 20x',
        'Olympus DUV (MX61A): 50x',
        'Olympus DUV (MX61A): 100x',
        'Olympus DUV (MX61A): DUV 100x',
        
        jeol_sem_cal_from_txt,   # instance of class with custom function `MyClass.cal()` for setting image scale.
        
        ]


# The 'pixel-per-unit' obtained from the "Set Scale..." Dialog, for each named calibration above:
cals = [
        0.9058,     # FluoroScope (Olympus MX51)
        1.81,  
        4.525,  
        9.0667,  
        13.5333,
        
        0.956064,    # Microscope #2 (Nikon)
        1.9149,
        9.6137,
        19.2786,
        28.862,
        
        1.020553,   # Microscope #3 (Nikon)
        2.032475,
        4.084,
        10.171,
        20.354,
        30.696,
        
        0.7464374,   # Microscope #4 (Nikon)
        1.497718,
        2.999,
        7.350,
        14.984,
        22.536,
        
        0.6900,     # Olympus DUV (MX61A)
        1.3903,
        2.7800,
        6.9200,
        13.9000,
        54.6875,
        
        jeol_sem_cal_from_txt,  # placeholder for custom function
        ]
#   This is just 1/pixel_width, in case you were wondering.


# length-units for each calibration:
units = [
        'um',       # FluoroScope (Olympus MX51)
        'um',
        'um',
        'um',
        'um',
        
        'um',       # Microscope #2 (Nikon): 5x
        'um',
        'um',
        'um',
        'um',
        
        'um',       # Microscope #3 (Nikon)
        'um',
        'um',
        'um',
        'um',
        'um',
        
        'um',       # Microscope #4 (Nikon)
        'um',
        'um',
        'um',
        'um',
        'um',
        
        'um',       # Olympus DUV (MX61A)
        'um',
        'um',
        'um',
        'um',
        'um',
        
        jeol_sem_cal_from_txt,
        ]
# for identical units for all cals, use the following line instead (uncomment):
#units = ['um'    for x in cals]    # list-comprehension with constant `um`


# Aspect Ratio for each calibration (default should be 1.0 )
#   Ratio is defined as so: pixelHeight = pixelWidth * AspectRatio
# Uncomment the following line to use custom aspect ratios:
aspect_ratio = [
        1,      # FluoroScope (Olympus MX51)
        1, 
        1, 
        1, 
        1,
        
        1,      # Microscope #2 (Nikon): 5x
        1, 
        1, 
        1, 
        1,
        
        1,      # Microscope #3 (Nikon)
        1,
        1,
        1,
        1,
        1,
        
        1,      # Microscope #4 (Nikon)
        1,
        1,
        1,
        1,
        1,
        
        1,      # Olympus DUV (MX61A)
        1,
        1,
        1,
        1,
        1,
        
        jeol_sem_cal_from_txt,
        ]
# The following sets the aspect ratio to 1 for all calibrations (uncomment to use):
#aspect_ratio =  [ 1.0    for x in cals ]   # list-comprehension with constant `1`





"""
################################
       Draw Line settings
################################

Settings for the script "Draw Measurement - Line

Colors are specified as:
    [R, G, B, transparency] values, from 0->1.0.  
    Leave last value as 1 for completely opaque.  
    Eg. opaque red would be [1,0,0, 1]
    and half-transparent blue would be [0,0,1, 0.5]
    opaque black is [0,0,0, 1]
    opaque white is [1,1,1, 1]
"""

linethickness = 5.0     # in pixels
linecolor = [ 0, 0.7, 0,   1.0]     
textsize = 30           # text height in pixels, I think
textcolor =     [ 0, 0.8, 0,   1.0]
textbackgroundcolor = [ 0, 0, 0,   0.6]       # background color behind text.
#textbackgroundcolor = None      # set to None for no background - uncomment this line
texttoleft = True      # put text on left or right side of last point?










'''
---------------------------------------------------------
Warn user if they run this file as a stand-alone plugin.
'''

def run():
    ''' If someone tries to run this file by itself, warn them of their error.  Unfortunately, since I was too lazy to make Microscope_Calibrations a full plugin (rather than a script), this accompanying settings file will show up in the Scripts menu.'''
    from ij.gui import GenericDialog
    
    gd = GenericDialog("Microscope_Calibrations_user_settings.py")
    gd.addMessage("This file is only for setting the microscope calibrations and settings for the plugins 'Microscope Measurement Tools'.\nNothing is done when this settings file is run by itself.\nPlease open this file in a text editor instead, to edit the calibrations.\n  \n"  +  \
    "The file should reside in a path like the following\n"  +  \
    "Fiji.app/plugins/Scripts/Analyze/Microscope Measurement Tools/Microscope_Calibrations_user_settings.py\n  "  +  "\n" +  \
    "Changes to the settings file are not automatically picked up by Fiji.  The workaround is to\n  1) Quit Fiji.\n  2) Delete the '$py.class' file 'Microscope_Calibrations_user_settings$py.class'\n  3) Open Fiji.  Make sure the new settings show up in 'Choose Microscope Calibration'."  )
    
    gd.showDialog()
#end run()

if __name__ == '__main__':
    run()   # run the above function if the user called this file!

