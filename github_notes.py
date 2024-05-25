You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

12
git clone https://github.com/redquinoa/health-checks.git 

Code output: 

Cloning into 'health-checks'...

Username for 'https://github.com': redquinoa

Password for 'https://redquinoa@github.com': 

remote: Enumerating objects: 3, done.

remote: Counting objects: 100% (3/3), done.

remote: Compressing objects: 100% (2/2), done.

remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0

Unpacking objects: 100% (3/3), done.

12
cd health-checks/ls -l

Code output: 

total 4

-rw-rw-r-- 1 user user 62 Jan  6 14:06 README.md

5
This repo will be populated with lots of fancy checks. 
1
git commit -a -m "Add one more line to README.md"

Code output:

[master 807cb50] Add one more line to README.md

 1 file changed, 2 insertions(+)

1
git push

Code output: 

Username for 'https://github.com': redquinoa

Password for 'https://redquinoa@github.com': 

Enumerating objects: 5, done.

Counting objects: 100% (5/5), done.

Delta compression using up to 4 threads

Compressing objects: 100% (2/2), done.

Writing objects: 100% (3/3), 347 bytes | 347.00 KiB/s, done.

Total 3 (delta 0), reused 0 (delta 0)

To https://github.com/redquinoa/health-checks.git

   3d9f86c..807cb50  master -> master

1
git config --global credential.helper cache

1
git pull

Code output: 

Username for 'https://github.com': redquinoa

Password for 'https://redquinoa@github.com': 

Already up to date.

1
git pull

Code output: 
    
#notes 1
You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

12
cd health-checks/git remote -v

Code output: 

origin  https://github.com/redquinoa/health-checks.git (fetch)

origin  https://github.com/redquinoa/health-checks.git (push)

1
git remote show origin

Code output: 

Username for 'https://github.com': redquinoa

Password for 'https://redquinoa@github.com': 

* remote origin

  Fetch URL: https://github.com/redquinoa/health-checks.git

  Push  URL: https://github.com/redquinoa/health-checks.git

  HEAD branch: master

  Remote branch:

    master tracked

  Local branch configured for 'git pull':

    master merges with remote master

  Local ref configured for 'git push':

    master pushes to master (up to date)

1
git branch -r

Code output:

  origin/HEAD -> origin/master

  origin/master


1
git status

Code output: 

On branch master

Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

#notes 2

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

12
cd health-checks/git remote show origin

Code output: 

* remote origin

  Fetch URL: https://github.com/redquinoa/health-checks.git

  Push  URL: https://github.com/redquinoa/health-checks.git

  HEAD branch: master

  Remote branch:

    master tracked

  Local branch configured for 'git pull':

    master merges with remote master

  Local ref configured for 'git push':

    master pushes to master (local out of date)

1
git fetch

Code output:

remote: Enumerating objects: 5, done.

remote: Counting objects: 100% (5/5), done.

remote: Compressing objects: 100% (4/4), done.

remote: Total 4 (delta 0), reused 4 (delta 0), pack-reused 0

Unpacking objects: 100% (4/4), done.

From https://github.com/redquinoa/health-checks

   807cb50..b62dc2e  master     -> origin/master

1
git log origin/master

Code output:

commit b62dc2eacfa820cd9a762adab9213305d1c8d344 (origin/master, origin/HEAD)

Author: Blue Kale <bluekale@example.com>

Date:   Mon Jan 6 14:32:45 2020 -0800

    Add initial files for the checks

commit 807cb5037ccac5512ba583e782c35f4e114f8599 (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jan 6 14:09:41 2020 -800

    Add one more line to README.md

commit 3d9f86c50b8651d41adabdaebd04530f4694efb5

Author: Red Quinoa <55592533+redquinoa@users.noreply.github.com>

Date:   Sat Sep 21 14:04:15 2019 -0700

    Initial commit

1
git status

Code output: 

On branch master

Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.

  (use "git pull" to update your local branch)

nothing to commit, working tree clean

1
git merge origin/master

Code output: 

Updating 807cb50..b62dc2e

Fast-forward

 all_checks.py | 18 ++++++++++++++++++

 disk_usage.py | 24 ++++++++++++++++++++++++

 2 files changed, 42 insertions(+)

 create mode 100755 all_checks.py

 create mode 100644 disk_usage.py

1
git log

Code output:

commit 1e0a1dfccf01183bfca7e30fb25f115889f95022 (HEAD -> master, origin/master, origin/HEAD)

commit b62dc2eacfa820cd9a762adab9213305d1c8d344 (HEAD -> master, origin/master, origin/HEAD)

Author: Blue Kale <bluekale@example.com>

Date:   Mon Jan 6 14:32:45 2020 -0800

    Add initial files for the checks

commit 807cb5037ccac5512ba583e782c35f4e114f8599 (HEAD -> master)

Author: My name <me@example.com>

Date:   Mon Jan 6 14:09:41 2020 -800

    Add one more line to README.md

commit 3d9f86c50b8651d41adabdaebd04530f4694efb5

Author: Red Quinoa <55592533+redquinoa@users.noreply.github.com>

Date:   Sat Sep 21 14:04:15 2019 -0700

#notes 3
You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

1
git pull

Code output: 

remote: Enumerating objects: 8, done.

remote: Counting objects: 100% (8/8), done.

remote: Compressing objects: 100% (5/5), done.

Unpacking objects: 100% (6/6), done.

remote: Total 6 (delta 1), reused 6 (delta 1), pack-reused 0

From https://github.com/redquinoa/health-checks

   807cb50..b62dc2e  master       -> origin/master

 * [new branch]      experimental -> origin/experimental

Updating 807cb50..b62dc2e

Fast-forward

 all_checks.py | 15 +++++++++++++++

 1 file changed, 15 insertions(+)

1
git -log -p -1

Code output: 

commit 922d65950b5325109525a24b71d8df8a46412d04 (HEAD -> master, origin/master, origin/HEAD)

Author: Blue Kale <bluekale@example.com>

Date:   Mon Jan 6 14:42:44 2020 -0800

    Add disk full check to all_checks.py

diff --git a/all_checks.py b/all_checks.py

index fdc4476..e46cdae 100755

--- a/all_checks.py

+++ b/all_checks.py

@@ -1,16 +1,31 @@

 #!/usr/bin/env python3

 

 import os

+import shutil

 import sys

(...)

def(check_reboot): 

	""" Returns True if the computer has a pending reboot."""

	Return os.path.exists(“/run/reboot-required”)

+def check_disk_full(disk, mmin_absolute, min_percent):

+	"""Returns True if there isn’t enough disk space, False otherwise."""

+	du = shutil.disk_usage(disk)

+	# Calculate the percentage of free space

+	percent_free = 100 * du.free / du.total

+	# Calculate how many free gigabytes

1
git remote show origin

Code output: 

* remote origin

  Fetch URL: https://github.com/redquinoa/health-checks.git

  Push  URL: https://github.com/redquinoa/health-checks.git

  HEAD branch: master

  Remote branches:

    experimental tracked

    master       tracked

  Local branch configured for 'git pull':

    master merges with remote master

  Local ref configured for 'git push':

    master pushes to master (up to date)

1
git checkout experimental 

Code output: 

Branch 'experimental' set up to track remote branch 'experimental' from 'origin'.

Switched to a new branch 'experimental'


#note 4
git add -p

git commit -m 'Rename min_absolute to min_gb, use parameter names'

Code output: 

[master 03923d0] Rename min_absolute to min_gb, use parameter names

 1 file changed, 3 insertions(+), 3 deletions(-)

1
git push

Code output: 

Username for 'https://github.com': redquinoa

Password for 'https://redquinoa@github.com': 

To https://github.com/redquinoa/health-checks.git

 ! [rejected]        master -> master (fetch first)

error: failed to push some refs to 'https://github.com/redquinoa/health-checks.git'

hint: Updates were rejected because the remote contains work that you do

hint: not have locally. This is usually caused by another repository pushing

hint: to the same ref. You may want to first integrate the remote changes

hint: (e.g., 'git pull ...') before pushing again.

hint: See the 'Note about fast-forwards' in 'git push --help' for details.

1
git pull

Code output: 

remote: Enumerating objects: 5, done.

remote: Counting objects: 100% (5/5), done.

remote: Compressing objects: 100% (2/2), done.

remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0

Unpacking objects: 100% (3/3), done.

From https://github.com/red-quinoa/health-checks

   92d659..a2dc118  master     -> origin/master

Auto-merging all_checks.py

CONFLICT (content): Merge conflict in all_checks.py

Automatic merge failed; fix conflicts and then commit the result.

1
git log --graph --oneline --all

Code output: 

* 03d23d0 Rename min_absolute to min_gb, use parameter names

| * 42dc118 (origin/master, origin/HEAD) reorder conditional to match parameter order

|/  

| * 4d99c56 (origin/experimental, experimental) Empty check_load function

|/  

* 922d659 Add disk full check to all_checks.py

* b62dc2e Add initial files for the checks

* 807cb50 Add one more line to README.md

* 3d9f86c Initial commit

1
git log -p origin/master

Code output: 

commit a2dc1181e5cccf36fec30d6eeefbe569a13883de (origin/master, origin/HEAD)

Author: Blue Kale <bluekale@example.com>

Date:   Mon Jan 6 14:52:23 2020 -0800

    Reorder conditional to match parameter order

diff --git a/all_checks.py b/all_checks.py

index e46cdae..6dda356 100755

--- a/all_checks.py

+++ b/all_checks.py

@@ -15,7 +15,7 @@ def check_disk_full(disk, min_absolute, min_percent):

     percent_free = 100 * du.free / du.total

     # Calculate how many free gigabytes

     gigabytes_free = du.free / 2**30

-    if percent_free < min_percent or gigabytes_free < min_absolute:

+    if gigabytes_free < min_absolute or percent_free < min_percent:

         return True

     return False

commit 922d65950b5325109525a24b71d8df8a46412d04 (HEAD -> master, origin/master, origin/HEAD)

Author: Blue Kale <bluekale@example.com>

Date:   Mon Jan 6 14:42:44 2020 -0800

    Add disk full check to all_checks.py

diff –git a/all_checks.py b/all_checks.py


12
git add all_checks.py git commit

Code output: 

Merge branch 'master' of https://github.com/redquinoa/health-checks

Fixed check_disk_usage conditional to use the new order and new variable name.

# Conflicts:

#       all_checks.py

#

(...)

1
git push

Code output: 

Enumerating objects: 10, done.

Counting objects: 100% (10/10), done.

Delta compression using up to 2 threads

Compressing objects: 100% (6/6), done.

Writing objects: 100% (6/6), 877 bytes | 877.00 KiB/s, done.

Total 6 (delta 2), reused 0 (delta 0)

remote: Resolving deltas: 100% (2/2), completed with 1 local object.

To https://github.com/redquinoa/health-checks.git

   a2dc118..58351ff  master -> master

1
git log --graph --oneline

Code output: 

* 58351ff (Head -> master, origin/master, origin/HEAD) Merge branch ‘master’ of https://github.com/redquinoa/health-checks.git

|\

| * 42dc118 (origin/master, origin/HEAD) reorder conditional to match parameter order

* | 03d23d0 Rename min_absolute to min_gb, use parameter names

|/  

| * 4d99c56 (origin/experimental, experimental) Empty check_load function

|/  

* 922d659 Add disk full check to all_checks.py

* b62dc2e Add initial files for the checks

* 807cb50 Add one more line to README.md

* 3d9f86c Initial commit

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

1
git checkout -b refactor

Code output: 

Switched to a new branch 'refactor'

1234567891011
atom all_checks.py (...)def main():    if check_reboot():        print("Pending Reboot.")        sys.exit(1)    if check_disk_full(disk="/", min_gb=2, min_percent=10):        print("Disk full.")        sys.exit(1)(...)

12345678910111213
(...)def check_root_full():    """Returns True if the root partition is full, False otherwise."""    return check_disk_full(disk="/", min_gb=2, min_percent=10) def main():    if check_reboot():        print("Pending Reboot.")        sys.exit(1)    if check_root_full():        print("Root partition full.")        sys.exit(1)(...)

1
./all_checks.py 

Code output: 

Everything ok.

1
git commit -a -m 'Create wrapper function for check_disk_full'

Code output: 

[refactor e914aee] Create wrapper function for check_disk_full

 1 file changed, 8 insertions(+), 2 deletions(-)

12345678910111213141516171819
(...)def check_root_full():    """Returns True if the root partition is full, False otherwise."""    return check_disk_full(disk="/", min_gb=2, min_percent=10) def main():    checks = [            (check_reboot, "Pending Reboot."),            (check_root_full, "Root partition full"),            ]     for check, msg in checks:        if check():            print(msg)            sys.exit(1)     print("Everything ok.")    sys.exit(0)(...)

1
./all_checks.py 

Code output: 

Everything ok.

1
git commit -a -m 'Iterate over a list of checks and messages to avoid code duplication'

Code output: 

[refactor 75bdd43] Iterate over a list of checks and messages to avoid code duplication

 1 file changed, 8 insertions(+), 6 deletions(-)

12345678910111213141516171819
(...)    def main():    checks = [            (check_reboot, "Pending Reboot."),            (check_root_full, "Root partition full"),            ]everything_ok = True    for check, msg in checks:        if check():            print(msg)            everything_ok = False     if not everything_ok:        sys.exit(1)     print("Everything ok.")   sys.exit(0)(...) 

12
./all_checks.py  

Code output: 

Everything ok.

1
git commit -a -m 'Allow printing more than one error message'

Code output: 

[refactor cbee3f7] Allow printing more than one error message

 1 file changed, 7 insertions(+), 1 deletion(-)

12
git push -u origin refactor 

Code output: 

Username for 'https://github.com': redquinoa

Password for 'https://redquinoa@github.com': 

Enumerating objects: 11, done.

Counting objects: 100% (11/11), done.

Delta compression using up to 4 threads

Compressing objects: 100% (9/9), done.

Writing objects: 100% (9/9), 1.34 KiB | 1.34MiB/s, done.

Total 9 (delta 3), reused 0 (delta 0)

remote: Resolving deltas: 100% (3/3), completed with 1 local object.

remote: 

remote: Create a pull request for 'refactor' on GitHub by visiting:

remote:      https://github.com/redquinoa/health-checks/pull/new/refactor

remote: 

To https://github.com/redquinoa/health-checks.git

 * [new branch]      refactor -> refactor

Branch 'refactor' set up to track remote branch 'refactor' from 'origin'.
note 5 
You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

1
git checkout master

Code output: 

Switched to branch 'master'

Your branch is up to date with 'origin/master'.

1
git pull

Code output: 

Remote: Enumerating objects: 5, done. 

Remote: Counting objects: 100% (5/5), done. 

Remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0

Unpacking objects: 10% (3/3), done. 

From https://github.com/redquinoa/healthchecks

    58351ff..0789f64  master    -> origin/master

Updating 58351ff..0789f64

Fast-forward

 README.md | 2 ++

 1 file changed, 2 insertions(+)

1
git log --graph --oneline --all

Code output: 

* 0789f64 (HEAD -> master, origin/master, origin/HEAD) Add reference to all_checks.py to README

| * cbee3f7 (origin/refactor, refactor) Allow printing more than one error message

| * 75bdd43 Iterate over a list of checks and messages to avoid code duplication

| * e914aee Create wrapper function for check_disk_full

|/  

*   58351ff Merge branch 'master' of https://github.com/redquinoa/health-checks

|\  

| * a2dc118 Reorder conditional to match parameter order

* | 03d23d0 Rename min_absolute to min_gb, use parameter names

|/  

| * 4d99c56 (origin/experimental, experimental) Empty check_load function

|/  

* 922d659 Add disk full check to all_checks.py

* b62dc2e Add initial files for the checks

* 807cb50 Add one more line to README.md

* 3d9f86c Initial commit

1
git checkout refactor

Code output: 

Switched to branch 'refactor'

Your branch is up to date with 'origin/refactor'.

1
git rebase master

Code output: 

First, rewinding head to replay your work on top of it...

Applying: Create wrapper function for check_disk_full

Applying: Iterate over a list of checks and messages to avoid code duplication

Applying: Allow printing more than one error message

1
git log --graph --oneline

Code output: 

* f5813b1 (HEAD -> refactor) Allow printing more than one error message

* 18257a0 Iterate over a list of checks and messages to avoid code duplication

* e914aee Create wrapper function for check_disk_full

* 0789f64 (origin/master, origin/HEAD, master) Add reference to all_checks.py to README

*   58351ff Merge branch 'master' of https://github.com/redquinoa/health-checks

|\  

| * a2dc118 Reorder conditional to match parameter order

* | 03d23d0 Rename min_absolute to min_gb, use parameter names

|/  

* 922d659 Add disk full check to all_checks.py

* b62dc2e Add initial files for the checks

* 807cb50 Add one more line to README.md

* 3d9f86c Initial commit

1
git checkout master

Code output: 

Switched to branch 'master'

Your branch is up to date with 'origin/master'.

1
git merge refactor

Code output: 

Updating 0789f64..f5813b1

Fast-forward

 all_checks.py | 24 +++++++++++++++++-----

 1 file changed, 19 insertions(+), 5 deletions(-)

1
git push --delete origin refactor

Code output: 

Username for 'https://github.com': redquinoa

Password for 'https://redquinoa@github.com': 

To https://github.com/redquinoa/health-checks.git

 - [deleted]         refactor

1
git branch -d refactor

Code output: 

Deleted branch refactor (was f5813b1).

1
git push

Code output: 

Enumerating objects: 11, done.

Counting objects: 100% (11/11), done.

Delta compression using up to 4 threads

Compressing objects: 100% (9/9), done.

Writing objects: 100% (9/9), 1.37 KiB | 1.37 MiB/s, done.

Total 9 (delta 3), reused 0 (delta 0)

remote: Resolving deltas: 100% (3/3), completed with 1 local object.

To https://github.com/red-quinoa/health-checks.git

   0789f64..f5813b1  master -> master
   
#note 6
Introduction

This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course. 

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

123456789101112131415161718192021222324
atom all_checks.py (...)import socket(...)def check_root_full():    """Returns True if the root partition is full, False otherwise."""    return check_disk_full(disk="/", min_gb=2, min_percent=10) def check_no_network():    """Returns True if it fails to resolve Google's URL, False otherwise."""        try:        socket.gethostbyname("www.google.com")        return False    except:        return True def main():    checks = [            (check_reboot, "Pending Reboot."),            (check_root_full, "Root partition full"),            (check_no_network, "No working network."),            ](...)

1
git commit -a -m 'Add a simple network connectivity check'

Code output:

[master aa8da6f] Add a simple network connectivity check

 1 file changed, 10 insertions(+), 1 deletion(-)

1
git fetch

Code output:

remote: Enumerating objects: 6, done.

remote: Counting objects: 100% (6/6), done.

remote: Compressing objects: 100% (4/4), done.

remote: Total 5 (delta 1), reused 5 (delta 1), pack-reused 0

Unpacking objects: 100% (5/5), done.

From https://github.com/redquinoa/health-checks

  f5813b1...d8c8fcd master     -> origin/master  

1
git rebase origin/master

Code output:

First, rewinding head to replay your work on top of it...

Applying: Add a simple network connectivity check

Using index info to reconstruct a base tree...

A       all_checks.py

Falling back to patching base and 3-way merge...

Auto-merging health_checks.py

CONFLICT (content): Merge conflict in health_checks.py

error: Failed to merge in the changes.

Patch failed at 0001 Add a simple network connectivity check

hint: Use 'git am --show-current-patch' to see the failed patch

Resolve all conflicts manually, mark them as resolved with

"git add/rm <conflicted_files>", then run "git rebase --continue".

You can instead skip this commit: run "git rebase --skip".

To abort and get back to the state before "git rebase", run "git rebase --abort".

12345678910111213141516171819202122232425262728293031323334353637
atom health_checks.py (...)<<<<<<< HEAD:health_checks.pydef check_cpu_constrained():    """Returns True if the cpu is having too much usage, False otherwise."""    return psutil.cpu_percent(1) > 75 def main():    checks = [            (check_reboot, "Pending Reboot."),            (check_root_full, "Root partition full"),            (check_cpu_constrained, "CPU load too high."),            ]    everything_ok = True=======def check_no_network():    """Returns True if it fails to resolve Google's URL, False otherwise."""    try:        socket.gethostbyname("google.com")        return False    except:        return True>>>>>>> Add a simple network connectivity check:all_checks.py def main():    checks = [            (check_reboot, "Pending Reboot."),            (check_root_full, "Root partition full"),<<<<<<< HEAD:health_checks.py            (check_cpu_constrained, "CPU load too high."),=======            (check_no_network, "No working network."),>>>>>>> Add a simple network connectivity check:all_checks.py            ](...) 

12345678910111213141516171819202122232425262728293031
(...)def check_cpu_constrained():    """Returns True if the cpu is having too much usage, False otherwise."""    return psutil.cpu_percent(1) > 75 def main():    checks = [            (check_reboot, "Pending Reboot."),            (check_root_full, "Root partition full"),            (check_cpu_constrained, "CPU load too high."),            ]    everything_ok = True def check_no_network():    """Returns True if it fails to resolve Google's URL, False otherwise."""    try:        socket.gethostbyname("google.com")        return False    except:        return True def main():    checks = [            (check_reboot, "Pending Reboot."),            (check_root_full, "Root partition full"),            (check_cpu_constrained, "CPU load too high."),             (check_no_network, "No working network."),            ](...) 

1
./health_checks.py 

Code output:

Traceback (most recent call last: 

  File ".health_checks.py", line 61, in <module>

    main()

  File ".health_checks.py", line 49, in main

    If check():

  File ".health_checks.py", line 30, in check_cpu_constrained

    Return psutil.cpu_percent(1) >75

NameError: name ‘psutil’ is not defined

123456789
atom health_checks.py import osimport shutilimport sysimport socketimport psutil (...)

1
./health_checks.py 

Code output:

Everything ok.

12
git add health_checks.py git rebase --continue

Code output:

Applying: Add a simple network connectivity check

1
git log --graph --oneline

Code output:

* 160b5f3 (HEAD -> master) Add a simple network connectivity check

* b52b7a2 (origin/master, origin/HEAD) Add cpu_constrained check

* 9fc7275 Rename all_checks.py to health_checks.py

* f5813b1 Allow printing more than one error message

* 18257a0 Iterate over a list of checks and messages to avoid code duplication

* 5d2e3eb Create wrapper function for check_disk_full

* 0789f64 Add reference to all_checks.py to README 

*   58351ff Merge branch 'master' of https://github.com/redquinoa/health-checks

|\  

| * a2dc118 Reorder conditional to match parameter order

* | 03d23d0 Rename min_absolute to min_gb, use parameter names

|/  

* 922d659 Add disk full check to all_checks.py

* b62dc2e Add initial files for the checks

* 807cb50 Add one more line to README.md

* 3d9f86c Initial commit

1
git push

Code output:

Username for 'https://github.com': redquinoa

Password for 'https://redquinoa@github.com': 

Enumerating objects: 5, done.

Counting objects: 100% (5/5), done.

Delta compression using up to 4 threads

Compressing objects: 100% (3/3), done.

Writing objects: 100% (3/3), 501 bytes | 501.00 KiB/s, done.

Total 3 (delta 2), reused 0 (delta 0)

remote: Resolving deltas: 100% (2/2), completed with 2 local objects.

To https://github.com/redquinoa/health-checks.git

   b52b7a2..160b5f3  master -> master



