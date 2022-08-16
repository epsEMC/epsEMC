# Git Local server setting

22.08.16 initial

## 0. Preperation

On doc1_Git_setting, we tried github as online server, but it is restricted wihtin small member with public option also not secured the contents.
So here we are going to try use  local repository for git.
For operating git server on windows system, we are going to use Bonobo git server program. 

Currently, git server is installed on 172.20.108.147 which is the team conference PC.

The server repository location is E:\ElecDevGitServer\Bonobo.Git.Server\App_Data\Repositories
The folder structure refers from Teamfolder "전설1팀_Temp", but not fixed yet.
\DEV1
\DEV2
\DEV3
\OEMDB
\공용
\회람



## 1. Git install

Download git from below
https://git-scm.com/download/win

refer the install steps.
https://taewow.tistory.com/13

Check git install status
Run "git bash" from windows start program or desktop.

![gitbashwindow.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gitbashwindow.jpg?raw=true)

![ gitbashinitial.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gitbashinitial.jpg?raw=true)

or from the file explorer locate the folder that you want use repository, then mouse right click, git bash here.


![gitbashhere.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gitbashhere.jpg?raw=true)

![gitbashhere_folder.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gitbashhere_folder.jpg?raw=true)


or just type "git" from CMD window.


## 2. Git setting for server only

### IIS setting

IIS is the "Internet Information Services" which can support operating webservice like online server or webpage. 
Firast of all, enable IIS fuctions.

Win + R > appwiz.cpl > Windows Function On/off
then check like below.  **"ASP .NET 4.x" shold be enable.**

![IISsetting.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISsetting.jpg?raw=true)

During change the IIS setting, if there is error message "0x800736B3", check .NET framework 
Reinstall .NET.
Open cmd then type below(check the folder name)
```
C:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_regiis -i C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_regiis -i
```

### Bonobo Git server install

> refer from  https://offbyone.tistory.com/417

Bonobo Git Server is the git server manger program for window. 
Download the SW from "https://bonobogitserver.com/"

Unzip from E:\ElecDevGitServer
Then, Bonobo.Git.Server folder is generated.

![bonobogitserverfolder.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobogitserverfolder.jpg?raw=true)

Run IIS(Internet Information Service) from Window key, type IIS.

![IISwebsiteadd.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISwebsiteadd.jpg?raw=true)
Fill the blank like below.

![IISwebsiteadd2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISwebsiteadd2.jpg?raw=true)

Port number is 3000. It can be changed on your network condition.

Add IIS_IUSRS account and grant the modify and write permission on the folder E:\ElecDevGitServer\Bonobo.Git.Server\App_Data\.

Click mouse right button on the folder in file explorer.

![IISiusrsfolder.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISiusrsfolder.jpg?raw=true)

Property > Security tap

![IISiusrsaddacount.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISiusrsaddacount.jpg?raw=true)

but change the position like this as PC location. We can not use HALLA.GRP location. The PC name could be different according to your PC.

![IISiusrsaddposition.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISiusrsaddposition.jpg?raw=true)

Change the user permission.

![IISiusrsaddacountedit.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISiusrsaddacountedit.jpg?raw=true)

The permission change is done. 

Change Bonobo.Git.Server as application on IIS.

![IISbonoboapp.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISbonoboapp.jpg?raw=true)

![IISbonoboapp2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISbonoboapp2.jpg?raw=true)

Sever setting done from IIS.
### Bonobo Git sever setting

Access http://localhost:3000/Bonobo.Git.Server/ from server PC web browser.
The initial admin account is admin/admin.
 
![bonoboaccess.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonoboaccess.jpg?raw=true)

But, the GUI is not supported perpectly, it may be due to Company security policy. So we have to use git command against Bonobo UI for git service.

![bonobogui.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobogui.jpg?raw=true)

Clcik "Create new repository" for a test.

![bonobocreatetest.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobocreatetest.jpg?raw=true)

Now, new folder is generated.
![bonobocreatetestresult2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobocreatetestresult2.jpg?raw=true)
Check whether it is generated on the PC server.

![bonobocreatetestresult.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobocreatetestresult.jpg?raw=true)

Test done. Server works well.

If the application pool is not changed from default seeting it should be changed as ".NET 4.x". Let's change application pool.

![bonobochangeapplicationpool.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobochangeapplicationpool.jpg?raw=true)

![bonobochangeapplicationpool2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobochangeapplicationpool2.jpg?raw=true)

This is the address for accessing server.
**http://localhost:3000/Bonobo.Git.Server**
**http://172.20.108.147:3000/Bonobo.Git.Server**


## 3. Git server and git

Actually, all the git service could run by web UI, but we can not use it due to company policy. So let's try use git command.

the detail explanation refer from "doc1_Git setting"
### 1) Server Structure setting

It can be resister from git command.
Access git command mode.
From the file explorer, move on the git server position.
E:\ElecDevGitServer\Bonobo.Git.Server\App_Data\Repositories\
Generate your own server folder tree.
example.

![doc3_gitserverstructure.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gitserverstructure.jpg?raw=true)


Then, mouse right click > git bash here. 

![doc3_gitserverstructurebashhere.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gitserverstructurebashhere.jpg?raw=true)

![doc3_gitserverstructurebashhere2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gitserverstructurebashhere2.jpg?raw=true)

Now, you can use git command.


### 2) Resister user name/email

Resister user name and email from web ui.

ex)
namgyun.kim
namgyun.kim@halla.com
namgyun.kim82

```
git config --global user.name "사용자이름"
git config --global user.email "이메일@abc.com"
```

Check the user list
```
git config --list
```

### 3) Git commit and push from server

Git bash here on 
"E:\ElecDevGitServer\Bonobo.Git.Server\App_Data\Repositories"

Let's make a folder on the server repository.
```
mkdir testFolder
cd testFolder
git init
```

The folder is initilized as new repository and path name changed as (main) which means connection to git.
Also, in the testFolder, ".git" file is generated.

Connect folder as server repository.
```
git remote add origin http://localhost:3000/Bonobo.Git.Server/testFolder.git
git remote -v
```
The server address is like above.
remote -v shows the server connection.

Now, add any file. Without any changes even empty folder not effect changes.
here we make new text.txt.
```
git add . # if want specific file, git add text.txt
git status
```
git status shows the commit changes.

then you must make a commit about changes.
```
git commit -m "new folder and file"
```
Filnally, upload the file to server.
```
git push origin main
```
This is the test screen.

![doc3_gittest.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gittest.jpg?raw=true)

When the login window pops up, type admin/admin.


Frequently, the git remote connection has problem such as large charater, space or change address. Try belows.
* Change current remote repository address
```
git remote -v
```
* Change the url address with connected remote repository
```
git remote set-url origin "url address"
```
* Remove remote 
```
git remote remove "url address"
```




### 4) Git commit and push from remote PC

according to the new account which made before,
you are going to clone server and modify and push.

Select a folder which you are going to make git remote folder on.
then git bash here.

![doc3_gittest_localgitbashhere.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gittest_localgitbashhere.jpg?raw=true)


```
mkdir testRemote
cd testRemote
git clone http://172.20.108.147:3000/Bonobo.Git.Server/testFolder.git
cd testRemote
cd testFolder #which copied from server.
(then you can see (main)) 
```
> doc3_gittest_localclone.jpg

![doc3_gittest_localclone.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_gittest_localclone.jpg?raw=true)

Then, the files from server are copied to remote PC.
Add new file test2.txt
Then git these.
```
git add test2.txt
git commit -m "add text2.txt"
git push origin main
```
But, you need to check DRM status. you should connect DRM to upload drm files.

Finally check from web UI.

refer 3), 4) from the blog
https://jexe.tistory.com/8



> Written with [StackEdit](https://stackedit.io/).
