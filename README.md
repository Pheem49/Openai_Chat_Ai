# How to use Openai_Chat_Ai

สวัสดี! คุณดื่มไฟล์ Markdown ต้องใช้ๆ** StackEdit **สำหรับ StackEdit ที่ต้องอ่านคำขอ Markdown ไม่จำเป็นต้องทำกับระบบปฏิบัติการในไฟล์เปิด** file explorer **ที่มุมของรังสีนี้


## Install Python

To download Python, head to the [official Python website](https://www.python.org/downloads/) and download the latest version. To use the OpenAI Python library, you need at least Python 3.7.1 or newer. If you are installing Python for the first time

## Set up a virtual environment (optional)

Once you have Python installed, it is a good practice to create a virtual python environment to install the OpenAI Python library. Virtual environments provide a clean working space for your Python packages to be installed so that you do not have conflicts with other libraries you install for other projects. You are not required to use a virtual environment, so skip to step 3 if you do not want to set one up.

To create a virtual environment, Python supplies a built in [venv module](https://docs.python.org/3/tutorial/venv.html) which provides the basic functionality needed for the virtual environment. Running the command below will create a virtual environment named "openai-env" inside the current folder you have selected in your terminal / command line:
 ```
 python -m venv openai-env
 ```
**If it goes error, delete the openai-env folder and reinstall.

 Once you’ve created the virtual environment, you need to activate it. On Windows, run:
  ```
 openai-env\Scripts\activate
 ```
 On Unix or MacOS, run:
 ```
source openai-env/bin/activate
 ```
                                                                                                                                                          
## Install the OpenAI Python library

Once you have Python 3.7.1 or newer installed and (optionally) set up a virtual environment, the OpenAI Python library can be installed. From the terminal / command line, run:

```text
pip install --upgrade openai
```

Once this completes, running  `pip list`  will show you the Python libraries you have installed in your current environment, which should confirm that the OpenAI Python library was successfully installed.

## Set up your API key for all projects (recommended)

The main advantage to making your API key accessible for all projects is that the Python library will automatically detect it and use it without having to write any code.

### MacOS

1.  **Open Terminal**: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
    
2.  **Edit Bash Profile**: Use the command  `nano ~/.bash_profile`  or  `nano ~/.zshrc`  (for newer MacOS versions) to open the profile file in a text editor.
    
3.  **Add Environment Variable**: In the editor, add the line below, replacing  `your-api-key-here`  with your actual API key:
    

```text
export OPENAI_API_KEY='your-api-key-here'
```

4.  **Save and Exit**: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.
    
5.  **Load Your Profile**: Use the command  `source ~/.bash_profile`  or  `source ~/.zshrc`  to load the updated profile.
    
6.  **Verification**: Verify the setup by typing  `echo $OPENAI_API_KEY`  in the terminal. It should display your API key.

### Windows

1.  **Open Command Prompt**: You can find it by searching "cmd" in the start menu.
    
2.  **Set environment variable in the current session**: To set the environment variable in the current session, use the command below, replacing  `your-api-key-here`  with your actual API key:
    

```text
setx OPENAI_API_KEY "your-api-key-here"
```

```text
This command will set the OPENAI_API_KEY environment variable for the current session.
```

3.  **Permanent setup**: To make the setup permanent, add the variable through the system properties as follows:
    
    -   Right-click on 'This PC' or 'My Computer' and select 'Properties'.
    -   Click on 'Advanced system settings'.
    -   Click the 'Environment Variables' button.
    -   In the 'System variables' section, click 'New...' and enter OPENAI_API_KEY as the variable name and your API key as the variable value.
4.  **Verification**: To verify the setup, reopen the command prompt and type the command below. It should display your API key:  `echo %OPENAI_API_KEY%`


## Set up your API key for a single project
If you only want your API key to be accessible to a single project, you can create a local  `.env`  file which contains the API key and then explicitly use that API key with the Python code shown in the steps to come.

Start by going to the project folder you want to create the  `.env`  file in.

In order for your  **.env**  file to be ignored by version control, create a  **.gitignore**  file in the root of your project directory. Add a line with  **.env**  on it which will make sure your API key or other secrets are not accidentally shared via version control.

Once you create the  `.gitignore`  and  `.env`  files using the terminal or an integrated development environment (IDE), copy your secret API key and set it as the  `OPENAI_API_KEY`  in your  `.env`  file. If you haven't created a secret key yet, you can do so on the  [API key page](https://platform.openai.com/account/api-keys).

The  `.env`  file should look like the following:
```text
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.

OPENAI_API_KEY="your-api-key-here"
```

## [](https://platform.openai.com/docs/quickstart/step-3-sending-your-first-api-request)

## Sending your api request

After you have Python configured and set up an API key, the final step is to send a request to the OpenAI API using the Python library. To do this, create a file named `ai_chat.py` using th terminal or an IDE.

To run the code, enter `python ai_chat.py` into the terminal / command line.
