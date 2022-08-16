# Git Local server setting

22.08.16 initial

## 0. Preperation
Currently, git is installed to 172.20.108.147 which is the team PC.
The main server is installed on e:\ElecDevGitServer\
The folder structure refers from Teamfolder "전설1팀_Temp", but not same.
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

![IISsetting.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISsetting.jpg?raw=true)


During change the IIS setting, if there is error message "0x800736B3", check .NET framework 
Reinstall it.
Open cmd then type below(check the folder name)
```
C:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_regiis -i C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_regiis -i
```

### Bonobo Git server install and setting

> refer from  https://offbyone.tistory.com/417

Bonobo Git Server is the git server for window. It is similar Subversion of Tortoise SVN.
Download the SW from "https://bonobogitserver.com/"

Unzip from E:\ElecDevGitServer
Then, Bonobo.Git.Server folder is generated.

![bonobogitserverfolder.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobogitserverfolder.jpg?raw=true)

Run IIS(Internet Information Service) from Window key, type IIS.

![IISwebsiteadd.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISwebsiteadd.jpg?raw=true)
Fill the blank like below.
> IISwebsiteadd2.jpg
![IISwebsiteadd2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISwebsiteadd2.jpg?raw=true)

Port number 80 or 8080 is used frequently for test, so define as 3000.


Add IIS_IUSRS account and grant the modify and write permission on the folder E:\ElecDevGitServer\Bonobo.Git.Server\App_Data\.

Click mouse right button on the folder in file explorer.

![IISiusrsfolder.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISiusrsfolder.jpg?raw=true)

Property > Security tap

![IISiusrsaddacount.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISiusrsaddacount.jpg?raw=true)

but change the position like this as PC location.

![IISiusrsaddposition.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISiusrsaddposition.jpg?raw=true)

Change the user permission.

![IISiusrsaddacountedit.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISiusrsaddacountedit.jpg?raw=true)

Change Bonobo.Git.Server as application on IIS.

![IISbonoboapp.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISbonoboapp.jpg?raw=true)

![IISbonoboapp2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_IISbonoboapp2.jpg?raw=true)

Access http://localhost:3000/Bonobo.Git.Server/ from web browser.
admin/admin for basic admin account.
 
![bonoboaccess.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonoboaccess.jpg?raw=true)

But, the GUI is not supported maybe due to Company security policy.

![bonobogui.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobogui.jpg?raw=true)

Clcik "Create new repository" for test.

![bonobocreatetest.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobocreatetest.jpg?raw=true)

![bonobocreatetestresult2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobocreatetestresult2.jpg?raw=true)

![bonobocreatetestresult.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobocreatetestresult.jpg?raw=true)

Change application pool.

![bonobochangeapplicationpool.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobochangeapplicationpool.jpg?raw=true)

![bonobochangeapplicationpool2.jpg](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc3_bonobochangeapplicationpool2.jpg?raw=true)



**http://localhost:3000/Bonobo.Git.Server**
**http://172.20.108.147:3000/Bonobo.Git.Server**



### 1) Resister user name/email

Resister user name and email.

```
git config --global user.name "사용자이름"
git config --global user.email "이메일@abc.com"
```

Check the user list
```
git config --list
```


or it is possible from web ui.
ex
namgyun.kim
namgyun.kim@halla.com
namgyun.kim82

### 2) commit from remote

refer the blog
https://jexe.tistory.com/8



> Written with [StackEdit](https://stackedit.io/).
