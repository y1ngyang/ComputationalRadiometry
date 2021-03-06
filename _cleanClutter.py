#clean a precisely defined set of files from a precisely defined directory set.
#the specified files are deleted, after the user has been prompted

import os
import os.path, fnmatch
import sys

#lists the files in a directory and subdirectories (from Python Cookbook)
def listFiles(root, patterns='*', recurse=1, return_folders=0):
    # Expand patterns from semicolon-separated string to list
    pattern_list = patterns.split(';')
    filenames = []
    filertn = []

    if sys.version_info[0] < 3:

        # Collect input and output arguments into one bunch
        class Bunch(object):
            def __init__(self, **kwds): self.__dict__.update(kwds)
        arg = Bunch(recurse=recurse, pattern_list=pattern_list,
            return_folders=return_folders, results=[])

        def visit(arg, dirname, files):
            # Append to arg.results all relevant files (and perhaps folders)
            for name in files:
                fullname = os.path.normpath(os.path.join(dirname, name))
                if arg.return_folders or os.path.isfile(fullname):
                    for pattern in arg.pattern_list:
                        if fnmatch.fnmatch(name, pattern):
                            arg.results.append(fullname)
                            break
            # Block recursion if recursion was disallowed
            if not arg.recurse: files[:]=[]
        os.path.walk(root, visit, arg)
        return arg.results

    else:
        for dirpath,dirnames,files in os.walk(root):
            if dirpath==root or recurse:
                for filen in files:
                    filenames.append(os.path.abspath(os.path.join(os.getcwd(),dirpath,filen)))
                if return_folders:
                    for dirn in dirnames:
                        filenames.append(os.path.abspath(os.path.join(os.getcwd(),dirpath,dirn)))
        for name in filenames:
            if return_folders or os.path.isfile(name):
                for pattern in pattern_list:
                    if fnmatch.fnmatch(name, pattern):
                        filertn.append(name)
                        break

    return filertn


#function to delete files in specified directory
#  first parameter defines if the search must be recursively 0=not, 1=recursive
#  second parameter specifies the path
#  third parameter specifies the file patterns to erase
#  the user is promted before the files are deleted
def QueryDelete(recurse,dir,patn):
    thefiles = listFiles(dir, patn,recurse)
    if thefiles is not None:
        if len(thefiles)>0:
            for filename in thefiles:
                print(filename)
            if sys.version_info[0] < 3:
                instr = raw_input("Delete these files? (y/n)")
            else:
                instr = input("Delete these files? (y/n)")
            if instr=='y':
                for filename in thefiles:
                    os.remove(filename)

#we take the conservative approach and do not do blanket erase,
#rather do it by type, asking the user first
QueryDelete(0,'.', '*.tex')
QueryDelete(0,'.', '*.pdf')
QueryDelete(0,'.', '*.png')
QueryDelete(0,'.', '*.eps;*.jpg;*.tiff;*.dat;*.lut;*.fl7;flamesensordata.*;sample.*;siemensstar.*')
QueryDelete(0,'.', 'tape7-*.txt;tape7-*;arr*.txt;Traje*.txt;trian*.txt;vertex*.txt;Intensity-max.*;test.txt;')
QueryDelete(0,'.', 'arrfile*.*;colourcoordinates.*;tar;tropical-23krural-45deg-space.*;testwith.svg;*.bib;' )
QueryDelete(0,'.', 'modtrandata.tar;modtrandata.tgz;tape7VISNIR5kmTrop23Vis;arrayplot*.*;savegraph.svg' )
QueryDelete(0,'.', 'arrayplotdemo.*;img2*.*;sensornoise.*;Colored_Bullseye-wikipedia.*;binfile.bin;' )
QueryDelete(0,'.', 'lwir100mm0150us*.*;LWIR-BBre*.*;img2*.*;pyradiSample*.*;lw*.txt;lw*.xml;Unity.txt' )
QueryDelete(0,'.', '*.ps')
QueryDelete(0,'.', 'missLUT-2000-e.*;path1kmflamesensor.txt;pathspaceflamesensor.txt')
QueryDelete(0,'.', 'sampleReflectance.txt;samplesVis.txt;LowPressureSodiumLamp.txt;detectorflamesensor.txt;fluorescent.txt;ciexyz31_1.txt')
QueryDelete(0,'.', '*.log')
QueryDelete(0,'.', '*.bbl;comment.cut')
QueryDelete(0,'.', '*.bbl;*.sav;*.bak;*.synctex;*.log;*.svn')
QueryDelete(0,'.', '*.blg;*.dfn;*.smb;*.bak;*.aux;*.out;*.lot;*.lof;*.toc;*.tex.bak;*.dvi;*.efc;Backup_of_*.*;*.abr')
QueryDelete(0,'.', 'PAOutput.txt')






