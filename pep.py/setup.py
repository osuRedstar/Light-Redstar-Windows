#"""Cython build file"""
#from distutils.core import setup
#from distutils.extension import Extension
#from Cython.Build import cythonize
#import os
#
#cythonExt = []
#for root, dirs, files in os.walk(os.getcwd()):
#	for file in files:
#		if file.endswith(".pyx") and ".pyenv" not in root:	# im sorry
#			filePath = os.path.relpath(os.path.join(root, file))
#			cythonExt.append(Extension(filePath.replace("/", ".")[:-4], [filePath]))
#
#setup(
#    name = "lets pyx modules",
#    ext_modules = cythonize(cythonExt, nthreads = 4),
#)

"""Cython build file"""
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os

if __name__ == '__main__':
    compileAll = input("All compile .pyx file? (y/n):").lower() == "y"
    if compileAll:
        cythonExt = []
        for (path, dir, files) in os.walk("./"):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.pyx':
                    print("%s/%s" % (path, filename))
                    cythonExt.append(path + "/" + filename)
        print("\n\n")
        
        setup(
                name = "lets pyx modules",
                ext_modules = cythonize(cythonExt, nthreads = 4),
            )
    else:
        compileFileName = input("Input path : ")
        if compileFileName.endswith(".pyx"):
            setup(
                    name = "lets pyx modules " + compileFileName,
                    ext_modules = cythonize(compileFileName, nthreads = 4),
                )
        else:
            print("Not .pyx file!")