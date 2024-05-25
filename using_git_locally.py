
cd scripts
atom all_checks.py

#File with code
#!/usr/bin/env python3

import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

main()
git commit -a -m "Call check_reboot from main, exit with 1 on error"
# a short to stage any cahnges to tracked file and commit them in one step.
git log

git log -p
Code output:

commit 033f27a8196987d61c4fd42930f2148b23434a03 (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jul 15 14:39:18 2019 +0200

    Call check_reboot from main, exit with 1 on error

diff --git a/all_checks.py b/all_checks.py

index 340f1f7..710266a 100644

--- a/all_checks.py

+++ b/all_checks.py

@@ -1,12 +1,15 @@

 #!/usr/bin/env python3

 

 import os

+import sys

 

 def check_reboot():

     """Returns True if the computer has a pending reboot."""

     return os.path.exists("/run/reboot-required")

(...)

git log

Code output:

commit 033f27a8196987d61c4fd42930f2148b23434a03 (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jul 15 14:39:18 2019 +0200

    Call check_reboot from main, exit with 1 on error

commit cc1acbf10fdea6cc07ebf827697666b6a35b0f36

Author: My name <me@example.com>

Date:   Thu Jul 11 17:19:32 2019 +0200

    Add a check_reboot function

(...)

user@ubuntu:~/scripts$ git show cc1acbf10fdea6cc07ebf827697666b6a35b0f36

commit cc1acbf10fdea6cc07ebf827697666b6a35b0f36

Author: My name <me@example.com>

Date:   Thu Jul 11 17:19:32 2019 +0200

    Add a check_reboot function

diff --git a/all_checks.py b/all_checks.py

index c0d03b3..340f1f7 100644

--- a/all_checks.py

+++ b/all_checks.py

@@ -1,5 +1,11 @@

 #!/usr/bin/env python3

 

+import os

+

+def check_reboot():

+    """Returns True if the computer has a pending reboot."""

+    return os.path.exists("/run/reboot-required")

+

 def main():

     Pass

1
git log --stat

Code output:

commit 033f27a8196987d61c4fd42930f2148b23434a03 (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jul 15 14:39:18 2019 +0200

    Call check_reboot from main, exit with 1 on error

 all_checks.py | 5 ++++-

 1 file changed, 4 insertions(+), 1 deletion(-)

(...)

1
atom  all_checks.py

File in video

12345678910111213141516171819
#!/usr/bin/env python3  import osimport sys def check_reboot():    """Returns True if the computer has a pending reboot."""    return os.path.exists("/run/reboot-required") def main():    if check_reboot():        print("Pending Reboot.")        sys.exit(1)     print("Everything ok.")    sys.exit(0) main() 

1
git diff

Code output:

diff --git a/all_checks.py b/all_checks.py

index 710266a..fdc4476 100644

--- a/all_checks.py

+++ b/all_checks.py

@@ -12,4 +12,7 @@ def main():

         print("Pending Reboot.")

         sys.exit(1)

 

+    print("Everything ok.")

+    sys.exit(0)

+

 main()

1
git  add -p

Code output:

diff --git a/all_checks.py b/all_checks.py

index 710266a..fdc4476 100644

--- a/all_checks.py

+++ b/all_checks.py

@@ -12,4 +12,7 @@ def main():

         print("Pending Reboot.")

         sys.exit(1)

 

+    print("Everything ok.")

+    sys.exit(0)

+

 main()

Stage this hunk [y,n,q,a,d,e,?]? y

user@ubuntu:~/scripts$ 

123
git diffgit diff --staged 

Code output:

diff --git a/all_checks.py b/all_checks.py

index 710266a..fdc4476 100644

--- a/all_checks.py

+++ b/all_checks.py

@@ -12,4 +12,7 @@ def main():

         print("Pending Reboot.")

         sys.exit(1)

 

+    print("Everything ok.")

+    sys.exit(0)

+

 main()

1
git commit -m 'Add a message when everything is ok'

Code output:

[master 49d610b] Add a message when everything is ok

 1 file changed, 3 insertions(+)
 
 Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course. 

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

12
cd checks/ls -l

Code output:

total 8

-rw-rw-r-- 1 user user 659 Jul  9 19:28 disk_usage.py

-rw-rw-r-- 1 user user 659 Jul 15 21:43 processes.py

1
git rm process.py

Code output:

rm '
processes.py
'

1
ls -l 

Code output:

total 4

-rw-rw-r-- 1 user user 659 Jul  9 19:28 disk_usage.py

1
git status

Code output:

On branch master

Changes to be committed:

  (use "git reset HEAD <file>..." to unstage)

        deleted:    
processes.py


1
git commit -m 'Delete unneeded processes file'

Code output:

[master 9939311] Delete unneeded processes file

 1 file changed, 24 deletions(-)

 delete mode 100644 processes.py

123
git mv disk_usage.py check_free_space.pygit status 

Code output:

On branch master

Changes to be committed:

  (use "git reset HEAD <file>..." to unstage)

        renamed:    disk_usage.py -> check_free_space.py

1
git commit -m 'New name for disk_usage.py'

Code output:

[master 7d7167b] New name for disk_usage.py

 1 file changed, 0 insertions(+), 0 deletions(-)

12
echo .DS_STORE > gitignorels -la

Code output:

total 20

drwxrwxr-x  3 user user 4096 Jul 15 22:15 .

drwxr-xr-x 19 user user 4096 Jul 15 16:37 ..

-rw-rw-r--  1 user user  659 Jul  9 19:28 check_free_space.py

drwxrwxr-x  8 user user 4096 Jul 15 21:52 .git

-rw-rw-r--  1 user user   10 Jul 15 22:15 .gitignore

12
git add .gitignore git commit -m 'Add a gitignore file, ignoring .DS_STORE files'

Code output:

[master abb0632] Add a gitignore file, ignoring .DS_STORE files

 1 file changed, 1 insertion(+)

 create mode 100644 .gitignore

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


12
cd checks
git log -1
Code output:

commit abb063210c1f011b0d6470a4c5f1d8f672edd3ef (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jul 15 22:20:45 2019 +0200

    Add a gitignore file, ignoring .DS_STORE files

1
git log -2
Code output:

commit abb063210c1f011b0d6470a4c5f1d8f672edd3ef (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jul 15 22:20:45 2019 +0200

    Add a gitignore file, ignoring .DS_STORE files

commit 7d7167b2db44abf8cf014230f9b9708786e41c2a

Author: My name <me@example.com>

Date:   Mon Jul 15 21:52:59 2019 +0200

    New name for disk_usage.py

1
git show 30e70712882267ca2dd749acfa02ea3aacfd0b24
Code output:

Author: My name <me@example.com>

Date:   Mon Jul 15 21:52:59 2019 +0200

    New name for disk_usage.py

diff --git a/disk_usage.py b/check_free_space.py

similarity index 100%

rename from disk_usage.py

rename to check_free_space.py

1
git show 30
Code output:

fatal: ambiguous argument '7d': unknown revision or path not in the working tree.

Use '--' to separate paths from revisions, like this:

'git <command> [<revision>...] -- [<file>...]'

1
git show 30e7
Code output:

commit 7d7167b2db44abf8cf014230f9b9708786e41c2a

Author: My name <me@example.com>

Date:   Mon Jul 15 21:52:59 2019 +0200

    New name for disk_usage.py

diff --git a/disk_usage.py b/check_free_space.py

similarity index 100%

rename from disk_usage.py

rename to check_free_space.py

1
git revert 30e7
Code output:

Revert "New name for disk_usage.py"

Rollback reason: the previous name was actually better.

This reverts commit 7d7167b2db44abf8cf014230f9b9708786e41c2a.

# Please enter the commit message for your changes. Lines starting

# with '#' will be ignored, and an empty message aborts the commit.

#

# On branch master

# Changes to be committed:

#       renamed:    check_free_space.py -> disk_usage.py

#

1
git revert 7d71
Code output:

[master 80b2dac] Revert "New name for disk_usage.py"

 1 file changed, 0 insertions(+), 0 deletions(-)

 rename check_free_space.py => disk_usage.py (100%)

1
git show 7d1de19
Code output:

commit 80b2dacef4b567196e61651064f03089c5e70b5e (HEAD -> master)

Author: My name <me@example.com>

Date:   Wed Jul 17 00:02:39 2019 +0200

    Revert "New name for disk_usage.py"

    

    Rollback reason: the previous name was actually better.

    

    This reverts commit 7d7167b2db44abf8cf014230f9b9708786e41c2a.

diff --git a/check_free_space.py b/disk_usage.py

similarity index 100%

rename from check_free_space.py

rename to disk_usage.py

