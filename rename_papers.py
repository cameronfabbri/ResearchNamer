import pdfrw
from pyPdf import PdfFileWriter, PdfFileReader
import sys
import os


def renameFileToPDFTitle(path, fileName):
   fullName = os.path.join(path, fileName)
   newName = pdfrw.PdfReader(fullName).Info.Title
   print 'fileName:',fileName
   print 'newName:',newName
   print
   # Remove surrounding brackets that some pdf titles have
   if newName is not None: newName = newName.strip('()') + '.pdf'
   if newName == '.pdf' or newName is None: pass
   else:
      #newFullName = os.path.join(path, newName)
      #os.rename(fullName, newFullName)
      print 'Name found '+newName

if __name__ == '__main__':

   if len(sys.argv) < 2:
      print '\nUsage:python rename_papers.py [folder path]\n'
      exit()

   path = sys.argv[1]
   if path[-1] != '/': path+='/'

   for fileName in os.listdir(path):
      fullName = os.path.join(path, fileName)
      if (not os.path.isfile(fullName) or fileName[-4:] != '.pdf'):
         continue
      renameFileToPDFTitle(path, fileName)

