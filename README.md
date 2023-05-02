# HumanActionRecognition

We can run the project locally or over the cloud. 

Setup to run the project over the cloud:
1. Access the below URL to view the web application.
	https://har-ccn.herokuapp.com/

2. Download any video from the below site by searching for the below labels:
	https://www.pexels.com/

Labels:
- Archery (https://www.pexels.com/video/woman-doing-archery-in-the-snow-6603191/)
- Playing flute (https://www.pexels.com/video/a-woman-playing-flute-8927326/)
- Walking
- Brushing hair
- Boxing
- Catching fish
- Cleaning toilet
- Clapping
- Stretching arms
- Fixing hair
- Tying bow tie
- Sign Language Interpretation
- Push ups
- Squats
- Finger Snapping

3. Upload the video in to the web application by browsing to the downloaded file.
4. CLick on submit button

The video will be transmitted to the machine learning model stored in AWS Cloud and will be processed.
The predicted action label will be transmitted to the front-end and will be displayed to the user.



Setup to run the project in local machine:


Prerequisites:

Before we start with the installation process, we need to have the following installed on your system:
	A computer running either Windows, macOS, or Linux.
	An internet connection to download the installation files.
	Sufficient administrative privileges to install the software.

Installing Python:

Python is a popular programming language that is widely used in web development, data analysis, and scientific computing. Follow the steps below to install Python on your system:
1. Go to the official Python website at https://www.python.org/downloads/ and download the latest version of Python for your operating system.
2. Once the download is complete, run the installer and follow the instructions on the screen.
3. During the installation process, make sure to check the option "Add Python to PATH" so that you can access Python from the command line.
4. After the installation is complete, open a command prompt and type python --version to confirm that Python is installed correctly.

Installing NodeJS:

NodeJS is an open-source JavaScript runtime environment that allows developers to run JavaScript code outside of a web browser. Follow the steps below to install NodeJS on your system:
1. Go to the official NodeJS website at https://nodejs.org/en/download/ and download the latest version of NodeJS for your operating system.
2. Once the download is complete, run the installer and follow the instructions on the screen.
3. During the installation process, make sure to check the option "Add to PATH" so that you can access NodeJS from the command line.
4. After the installation is complete, open a command prompt and type node --version to confirm that NodeJS is installed correctly.

Installing Visual Studio:

Visual Studio is an integrated development environment (IDE) developed by Microsoft that is used to build software, mobile applications, web applications, and more. Follow the steps below to install Visual Studio on your system:

1. Go to the official Visual Studio website at https://visualstudio.microsoft.com/downloads/ and download the latest version of Visual Studio for your operating system.
2. Once the download is complete, run the installer and follow the instructions on the screen.
3. During the installation process, choose the workloads that you want to install. You can select from a variety of workloads depending on your development needs, such as .NET desktop development, web development, mobile development, gaming development, and more.
4. After selecting the workloads, choose the optional components that you want to install. These components include additional features, tools, and libraries that you may need for your development work.
5. Once you have made your selections, click the install button to begin the installation process. This may take some time depending on the components you have chosen.
6. After the installation is complete, launch Visual Studio. 

To setup and run the project in local:

1.	Open command prompt
2.	Navigate to the project folder “front-end”
3.	Run the following commands. 
		“npm install”
		“npm install -g nodemon”
		“nodemon app”
4.	Now, open another terminal 
5.	Navigate to the project folder “back-end”
6.	Run following commands.
		“pip install flask”
		“pip install numpy”
		“python app.py”
7.	Now, download some sample videos from the below links.
	https://www.pexels.com/video/a-woman-playing-flute-8927326/
	https://www.pexels.com/video/woman-doing-archery-in-the-snow-6603191/
8.	Open the url : http://localhost:3000/
9.	Now upload the downloaded video and click on submit button. 
10.	The model will recognize the action and print the action. 
