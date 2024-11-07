#FUSE Image Display

#Description: 
#Some images were taken during the FUSE mission and the following code allows one to view the images and save them as a .png
#The images have little scientific use and the objective of this Python Script is to view, not analyze, the images


#Import libraries
import matplotlib.pyplot as plt
from astropy.io import fits
import os

#Begin by changing the variable "Extract_Folder" to your desired folder 
#If you need help with extracting files from a .tar file, refer to main tutorial
Extract_Folder = 'FUSE-m1051211'
Extract_Path = os.path.join(os.path.dirname(__file__), Extract_Folder)

for root, dirs, files in os.walk(Extract_Path):
    for filename in files: 
        if filename.endswith("fesbfcal.fit"):
            ImageFile = os.path.join(root, filename)
            print ("Image File:", ImageFile)
            hdu = fits.open(ImageFile)

            StarName = hdu[0].header["TARGNAME"] #Extract name of the star only present in the first header
            ProgramID = hdu[0].header["ROOTNAME"] #Extract program ID

            #Create subplot
            fig, ax = plt.subplots(len(hdu)-1, 1, layout = "constrained")
            print (f"File contains {len(hdu) - 1} images")
            for i in range(0, len(hdu)-1):

                Filter = hdu[i+1].header["AFESFILT"]

                ImageData = (hdu[i+1].data)
                
                #ax.figure(figsize=(14,8))
                ax[i].imshow(ImageData)
                ax[i].axis("off")
                ax[0].set_title(f"Image of {StarName} (Filter = {Filter})")
            hdu.close()

            #Save the images
            ImageFolder = Extract_Path + r"/Images"
            if not os.path.exists(ImageFolder):
                os.makedirs(ImageFolder)
            plt.savefig(f"{ImageFolder}/Images-{StarName}-{ProgramID}.png", format = "png")
            print (f"Saved images as Images-{StarName}-{ProgramID}.png to {ImageFolder}")
        plt.show()
print("Processing Done")