import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    list_path= []

    def find_files_recursively(suffix, path, list_path):
      
      if  os.path.isfile(path)  and path.endswith(suffix):
        list_path.append(path)
        return   
      elif not os.path.isdir(path):
        return
      else: 

        for file in os.listdir(path):      
          if os.path.isfile(os.path.join(path, file))  and file.endswith(suffix):
            list_path.append(os.path.join(path, file))   
          else:
            find_files_recursively(suffix, os.path.join(path, file), list_path)

    
    
    find_files_recursively(suffix, path, list_path)
    return list_path



print(find_files('.c', '../testdir'))
# ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
print(find_files('.c', '../testdir/t1.c')) # return empty list
# [] 
print(find_files('.c', '')) # return empty list
# []

