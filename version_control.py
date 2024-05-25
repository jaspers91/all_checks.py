# 1
# cat rearrange1.py 

#   Code output:

# #!/usr/bin/env python3

# import re

# def rearrange_name(name):

#     result = re.search(r"^([\w .]*), ([\w .]*)$", name)

#     if result == None:

#         return name

#     return "{} {}".format(result[2], result[1])

# user@ubuntu:~$ cat rearrange2.py 

# #!/usr/bin/env python3

# import re

# def rearrange_name(name):

#     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

#     if result == None:

#         return name


#     return "{} {}".format(result[2], result[1])

# 1
# cat rearrange2.py 

# Code output:

# #!/usr/bin/env python3

# import re

# def rearrange_name(name):

#     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

#     if result == None:

#         return name

#     return "{} {}".format(result[2], result[1])

# 1
# diff rearrange1.py rearrange2.py 

# Code output:

# 6c6

# <     result = re.search(r"^([\w .]*), ([\w .]*)$", name)

# ---

# >     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

# 1
# diff validations1.py validations2.py 

# Code output:

# 5c5,6

# <	assert (type(username) == str), "username must be a string"

# --

# >	if type(username != str: 

# > 	    raise TypeError("username must be a string"

# 11a13,15

# >	    return False

# >	# Usernames can't begin with a number

# >	if username[0].isnumeric():

# 1
# diff -u validations1.py validations2.py 

# Code output:

# --- validations1.py	2019-06-06 14:28:49.639209499 +0200

# +++ validations2.py	2019-06-06 14:30:48.019360890 +0200

# @@ -2,7 +2,8 @@

 

 

#  def validate_user(username, minlen):

# -    assert type(username) == str, "username must be a string"

# +    if type(username) != str:

# +        raise TypeError("username must be a string")

#      if minlen < 1:

#          raise ValueError("minlen must be at least 1")

     

# @@ -10,5 +11,8 @@

#          return False

#      if not username.isalnum():

#         return False

# +    # Usernames can't begin with a number

# +    if username[0].isnumeric():

# +        return False

#      return True


# 1
# cat cpu_usage.py 

# cat cpu_usage.py 

# Code output:

# #!/usr/bin/env python3

# import psutil

# def check_cpu_usage(percent):

#     usage = psutil.cpu_percent()

#     return usage < percent

# if not check_cpu_usage(75):

#     print("ERROR! CPU is overloaded")

# else:


#     print("Everything ok")

# 1
# cat cpu_usage.diff 

# Code output:

# --- cpu_usage.py	2019-06-23 08:16:04.666457429 -0700

# +++ cpu_usage_fixed.py	2019-06-23 08:15:37.534370071 -0700

# @@ -2,7 +2,8 @@

#  import psutil

 

#  def check_cpu_usage(percent):

# -    usage = psutil.cpu_percent()

# +    usage = psutil.cpu_percent(1)

# +    print("DEBUG: usage: {}".format(usage))

#      return usage < percent

 

#  if not check_cpu_usage(75):

# 1
# patch cpu_usage.py < cpu_usage.diff 

#   Code output:

# patching file cpu_usage.py

# 1
# cat cpu_usage.py 

# Code output:

# #!/usr/bin/env python3

# import psutil

# def check_cpu_usage(percent):

#     usage = psutil.cpu_percent(1)

#     print("DEBUG: usage: {}".format(usage))

#     return usage < percent

# if not check_cpu_usage(75):

#     print("ERROR! CPU is overloaded")

# else:


#     print("Everything ok")

1234567891011121314151617181920212223
#!/usr/bin/env python3 import shutilimport sys def check_disk_usage(disk, min_absolute, min_percent):    """Returns True if there is enough free disk space, false otherwise."""    du = shutil.disk_usage(disk)    # Calculate the percentage of free space    percent_free = 100 * du.free / du.total    # Calculate how many free gigabytes    gigabytes_free = du.free / 2**30    if percent_free < min_percent or gigabytes_free < min_absolute:        return False    return True # Check for at least 2 GB and 10% freeif not check_disk_usage("/", 2*2**30, 10):    print("ERROR: Not enough disk space")    sys.exit(1) print("Everything ok")sys.exit(0)

1
./disk_usage_fixed.py

Code output:

ERROR: Not enough disk space

File with code

Instructor changed change check_disk_usage("/", 2*2**30, 10) in previous file to check_disk_usage("/", 2, 10).

1234567891011121314151617181920212223
#!/usr/bin/env python3 import shutilimport sys def check_disk_usage(disk, min_absolute, min_percent):    """Returns True if there is enough free disk space, false otherwise."""    du = shutil.disk_usage(disk)    # Calculate the percentage of free space    percent_free = 100 * du.free / du.total    # Calculate how many free gigabytes    gigabytes_free = du.free / 2**30    if percent_free < min_percent or gigabytes_free < min_absolute:        return False    return True # Check for at least 2 GB and 10% freeif not check_disk_usage("/", 2, 10):    print("ERROR: Not enough disk space")    sys.exit(1) print("Everything ok")sys.exit(0)

1
./disk_usage_fixed.py 

Code output:

Everything ok

12
diff -u disk_usage_original.py disk_usage_fixed.py > disk_usage.diffcat disk_usage.diff 

Code output:

--- disk_usage_original.py	2019-06-22 15:13:38.591579963 -0700

+++ disk_usage_fixed.py	2019-06-22 15:41:35.013023839 -0700

@@ -1,6 +1,7 @@

 #!/usr/bin/env python3

 

 import shutil

+import sys

 

 def check_disk_usage(disk, min_absolute, min_percent):

     """Returns True if there is enough free disk space, false otherwise."""

@@ -14,9 +15,9 @@

     return True

 

 # Check for at least 2 GB and 10% free

-if not check_disk_usage("/", 2*2**30, 10):

+if not check_disk_usage("/", 2, 10):

     print("ERROR: Not enough disk space")

-    return 1

+    sys.exit(1)

 

 print("Everything ok")

-return 0

+sys.exit(0)

12
patch disk_usage.py < disk_usage.diff patching file disk_usage.py

Code output:

patching file disk_usage.py

1
./disk_usage.py 

Code output:
    


This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course. 

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

12
cp disk_usage.py disk_usage_original.py cp disk_usage.py disk_usage_fixed.py 

File with code

2322171819202114151612345678910111213
 return 0if not check_disk_usage("/", 2*2**30, 10):    print("ERROR: Not enough disk space")    return 1 print("Everything ok")    return True # Check for at least 2 GB and 10% free#!/usr/bin/env python3 import shutil def check_disk_usage(disk, min_absolute, min_percent):    """Returns True if there is enough free disk space, false otherwise."""    du = shutil.disk_usage(disk)    # Calculate the percentage of free space    percent_free = 100 * du.free / du.total    # Calculate how many free gigabytes    gigabytes_free = du.free / 2**30    if percent_free < min_percent or gigabytes_free < min_absolute:        return False

  

1234
./disk_usage_fixed.py  #this throws an error 

Code output:

File "./disk_usage_fixed.py", line 19

    return 1

    ^

SyntaxError: 'return' outside function

File with code

The instructor adds import sys at the beginning, then change return 1 to sys.exit(1) and return 0 to sys.exit(0).

1234567891011121314151617181920212223
#!/usr/bin/env python3 import shutilimport sys def check_disk_usage(disk, min_absolute, min_percent):    """Returns True if there is enough free disk space, false otherwise."""    du = shutil.disk_usage(disk)    # Calculate the percentage of free space    percent_free = 100 * du.free / du.total    # Calculate how many free gigabytes    gigabytes_free = du.free / 2**30    if percent_free < min_percent or gigabytes_free < min_absolute:        return False    return True # Check for at least 2 GB and 10% freeif not check_disk_usage("/", 2*2**30, 10):    print("ERROR: Not enough disk space")    sys.exit(1) print("Everything ok")sys.exit(0)

1
./disk_usage_fixed.py

Code output:

ERROR: Not enough disk space

File with code

Instructor changed change check_disk_usage("/", 2*2**30, 10) in previous file to check_disk_usage("/", 2, 10).

1234567891011121314151617181920212223
#!/usr/bin/env python3 import shutilimport sys def check_disk_usage(disk, min_absolute, min_percent):    """Returns True if there is enough free disk space, false otherwise."""    du = shutil.disk_usage(disk)    # Calculate the percentage of free space    percent_free = 100 * du.free / du.total    # Calculate how many free gigabytes    gigabytes_free = du.free / 2**30    if percent_free < min_percent or gigabytes_free < min_absolute:        return False    return True # Check for at least 2 GB and 10% freeif not check_disk_usage("/", 2, 10):    print("ERROR: Not enough disk space")    sys.exit(1) print("Everything ok")sys.exit(0)

1
./disk_usage_fixed.py 

Code output:

Everything ok

12
diff -u disk_usage_original.py disk_usage_fixed.py > disk_usage.diffcat disk_usage.diff 

Code output:

--- disk_usage_original.py	2019-06-22 15:13:38.591579963 -0700

+++ disk_usage_fixed.py	2019-06-22 15:41:35.013023839 -0700

@@ -1,6 +1,7 @@

 #!/usr/bin/env python3

 

 import shutil

+import sys

 

 def check_disk_usage(disk, min_absolute, min_percent):

     """Returns True if there is enough free disk space, false otherwise."""

@@ -14,9 +15,9 @@

     return True

 

 # Check for at least 2 GB and 10% free

-if not check_disk_usage("/", 2*2**30, 10):

+if not check_disk_usage("/", 2, 10):

     print("ERROR: Not enough disk space")

-    return 1

+    sys.exit(1)

 

 print("Everything ok")

-return 0

+sys.exit(0)

12
patch disk_usage.py < disk_usage.diff patching file disk_usage.py

Code output:

patching file disk_usage.py

1
./disk_usage.py 

Code output:

Everything ok

Using diff -u

You use the diff -u command to compare two files, line by line, and have the differing lines compared side-by-side in the same output. For an example of what this looks like, see below:

302921222324252627282345678910111213141516171819201
 +Strawberries-Menu1:+Menu:  Apples Bananas-Oranges-Pears+GrapesMenu1: ApplesBananasOrangesPears ~$ cat menu2.txt Menu: ApplesBananasGrapesStrawberries ~$ diff -u menu1.txt menu2.txt --- menu1.txt   2019-12-16 18:46:13.794879924 +0900+++ menu2.txt   2019-12-16 18:46:42.090995670 +0900@@ -1,6 +1,6 @@~$ cat menu1.txt 

The patch command

The patch command is useful for applying file differences. See the example below, which compares two files. The comparison is saved as a .diff file, which is then patched to the original file!

123456789101112131415161718192021
~$ cat hello_world.txt Hello World~$ cat hello_world_long.txt Hello World It's a wonderful day!~$ diff -u hello_world.txt hello_world_long.txt --- hello_world.txt     2019-12-16 19:24:12.556102821 +0900+++ hello_world_long.txt        2019-12-16 19:24:38.944207773 +0900@@ -1 +1,3 @@ Hello World++It's a wonderful day!~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff~$ patch hello_world.txt < hello_world.diff patching file hello_world.txt~$ cat hello_world.txt Hello World It's a wonderful day! 

Resources for more information

There are other interesting patch and diff commands such as patch -p1 and diff -r . For more information on these commands, check out the following resources:

 # First steps with Git

git config --global user.email "me@example.com"
git config --global user.name "My name"

mkdir checks
cd checks
git init

ls -la

# Code output:

total 12

drwxrwxr-x  3 user user 4096 Jul  9 18:16 .

drwxr-xr-x 18 user user 4096 Jul  9 18:16 ..

drwxrwxr-x  7 user user 4096 Jul  9 18:16 .git

user@ubuntu:~/checks$ ls -l .git/

total 32

drwxrwxr-x 2 user user 4096 Jul  9 18:16 branches

-rw-rw-r-- 1 user user   92 Jul  9 18:16 config

-rw-rw-r-- 1 user user   73 Jul  9 18:16 description

-rw-rw-r-- 1 user user   23 Jul  9 18:16 HEAD

drwxrwxr-x 2 user user 4096 Jul  9 18:16 hooks

drwxrwxr-x 2 user user 4096 Jul  9 18:16 info

drwxrwxr-x 4 user user 4096 Jul  9 18:16 objects

drwxrwxr-x 4 user user 4096 Jul  9 18:16 refs

ls -l

Code output:

total 4

-rw-rw-r-- 1 user user 657 Jul  9 18:26 disk_usage.py

1
ls -l .git/

Code output:

total 32

drwxrwxr-x 2 user user 4096 Jul  9 18:16 branches

-rw-rw-r-- 1 user user   92 Jul  9 18:16 config

-rw-rw-r-- 1 user user   73 Jul  9 18:16 description

-rw-rw-r-- 1 user user   23 Jul  9 18:16 HEAD

drwxrwxr-x 2 user user 4096 Jul  9 18:16 hooks

drwxrwxr-x 2 user user 4096 Jul  9 18:16 info

drwxrwxr-x 4 user user 4096 Jul  9 18:16 objects

drwxrwxr-x 4 user user 4096 Jul  9 18:16 refs

12
cp ../disk_usage.py .ls -l

Code output:

total 4

-rw-rw-r-- 1 user user 657 Jul  9 18:26 disk_usage.py

12
git add disk_usage.py git status

Code output:

On branch master

No commits yet

Changes to be committed:

  (use "git rm --cached <file>..." to unstage)

	new file:   disk_usage.py

1
git commit

Code output:

 GNU nano 3.2         /home/user/checks/.git/COMMIT_EDITMSG                    

# Please enter the commit message for your changes. Lines starting

# with '#' will be ignored, and an empty message aborts the commit.

#

# On branch master

#

# Initial commit

#

# Changes to be committed:

#       new file:   disk_usage.py

Code output:

total 4

-rw-r--r-- 1 user user 657 Jul  9 12:52 disk_usage.py

user@ubuntu:~/checks$ git status

On branch master

nothing to commit, working tree clean

1
git status

Code output:

On branch master

nothing to commit, working on clean tree

12
atom disk_usage.py git status

Code output:

On branch master

Changes to be committed:

  (use "git restore --staged <file>..." to unstage)

	modified:   disk_usage.py

1
git commit -m 'Add periods to the end of sentences.'

Code output:

[master ae8d19c] Add periods to the end of sentences.

 1 file changed, 2 insertions(+), 2 deletions(-)

1
git status

Code output:

On branch master

nothing to commit, working tree clean



123
mkdir scriptscd scriptsgit init

Code output:

Initialized empty Git repository in /home/user/scripts/.git/

1
git config -l

Code output:

user.email=me@example.com

user.name=My name

core.repositoryformatversion=0

core.filemode=true

core.bare=false

core.logallrefupdates=true

File with code

1234567
#!/usr/bin/env python3 def main():    pass main() 

12
chmod +x all_checks.pygit status

Code output:

On branch master

No commits yet

Untracked files:

  (use "git add <file>..." to include in what will be committed)

	all_checks.py

nothing added to commit but untracked files present (use "git add" to track)

12
git add all_checks.pygit commit

File with code

123456789101112
Create an empty all_checks.# Please enter the commit message for your changes. Lines starting# with '#' will be ignored, and an empty message aborts the commit.## On branch master## Initial commit## Changes to be committed:#       new file:   all_checks.py# 

File with code

12345678910111213
#!/usr/bin/env python3 import os def check_reboot():    """Returns True if the computer has a pending reboot."""    return os.path.exists("/run/reboot-required")    def main():    pass main() 

1
git status

On branch master

Changes not staged for commit:

  (use "git add <file>..." to update what will be committed)

  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   all_checks.py

no changes added to commit (use "git add" and/or "git commit -a")

12
git add all_checks.py git status

Code output:

On branch master

Changes to be committed:

  (use "git reset HEAD <file>..." to unstage)

	modified:   all_checks.py

1
git commit -m 'Add a check_reboot function'

Code output:

[master d8e139c] Add a check_reboot function

 1 file changed, 6 insertions(+)
 
 Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course. 

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.


1
cat example_commit.txt 

Code output:

Provide a good commit message example

The purpose of this commit is to provide an example of a hand-crafted,

artisanal commit message. The first line is a short, approximately 50-character

summary, followed by an empty line. The subsequent paragraphs are jam-packed

with descriptive information about the change, but each line is kept under 72

characters in length.

If even more information is needed to explain the change, more paragraphs can

be added after blank lines, with links to issues, tickets, or bugs. Remember

that future you will thank current you for your thoughtfulness and foresight!

# Please enter the commit message for your changes. Lines starting

# with '#' will be ignored, and an empty message aborts the commit.

#

# On branch master

#

# Changes to be committed:

# new file:   super_script.py

# new file:   cool_config.txt

#

12
cd scriptsgit log

Code output:

commit d8e139cc4f7dcd13b75cff67cfb68527e24c59c5 (HEAD -> master)

Author: My name <me@example.com>

Date:   Thu Jul 11 17:19:32 2019 +0200

    Add a check_reboot function

commit 6cfc29966acda8213fcd8ac2735b31f3fdbc6c53

Author: My name <me@example.com>

Date:   Thu Jul 11 12:08:46 2019 +0200

    Create and empty all_checks.py

Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course. 

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.


12
cd scriptsatom all_checks.py

File in video

123456789101112131415
#!/usr/bin/env python3  import osimport sys def main():    if check_reboot():        print("Pending Reboot.")        sys.exit(1)     print("Everything ok.")    sys.exit(0) main() 

1
./all_checks.py 

Code output:

Traceback (most recent call last):

  File "all_checks.py", line 14, in <module>

    main()

  File "all_checks.py", line 7, in main

    if check_reboot():

NameError: name 'check_reboot' is not defined

1
git status

Code output:

On branch master

Changes not staged for commit:

  (use "git add <file>..." to update what will be committed)

  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   all_checks.py

123
git checkout all_checks.pygit status 

Code output:

On branch master

nothing to commit, working tree clean

user@ubuntu:~/scripts$ ./all_checks.py 

Everything ok.

1
./all_checks.py 

Code output:

Everything ok.

123
./all_checks.py > output.txtgit add *git status
Code output:

On branch master

Changes to be committed:

  (use "git reset HEAD <file>..." to unstage)

        new file:   output.txt

12
git reset HEAD output.txtgit status

Code output:

On branch master

Untracked files:

  (use "git add <file>..." to include in what will be committed)

        Output.txt

1
git commit -m "it should be os.path.exists"


