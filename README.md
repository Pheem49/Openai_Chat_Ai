#How to use Openai_Chat_Ai

Install Python

Set up a virtual environment (optional)
python -m venv openai-env

Once you’ve created the virtual environment, you need to activate it. On Windows, run:
openai-env\Scripts\activate

On Unix or MacOS, run:
source openai-env/bin/activate

Install the OpenAI Python library
pip install --upgrade openai

Set up your API key
MacOS
Open Terminal: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
Edit Bash Profile: Use the command nano ~/.bash_profile or nano ~/.zshrc (for newer MacOS versions) to open the profile file in a text editor.
Add Environment Variable: In the editor, add the line below, replacing your-api-key-here with your actual API key:
export OPENAI_API_KEY='your-api-key-here'
Save and Exit: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.
Load Your Profile: Use the command source ~/.bash_profile or source ~/.zshrc to load the updated profile.
Verification: Verify the setup by typing echo $OPENAI_API_KEY in the terminal. It should display your API key.

Windows
Open Command Prompt: You can find it by searching "cmd" in the start menu.

Set environment variable in the current session: To set the environment variable in the current session, use the command below, replacing your-api-key-here with your actual API key:

setx OPENAI_API_KEY "your-api-key-here"
This command will set the OPENAI_API_KEY environment variable for the current session.
Permanent setup: To make the setup permanent, add the variable through the system properties as follows:

Right-click on 'This PC' or 'My Computer' and select 'Properties'.
Click on 'Advanced system settings'.
Click the 'Environment Variables' button.
In the 'System variables' section, click 'New...' and enter OPENAI_API_KEY as the variable name and your API key as the variable value.
Verification: To verify the setup, reopen the command prompt and type the command below. It should display your API key: echo %OPENAI_API_KEY%

Set up your API key for a single project
If you only want your API key to be accessible to a single project, you can create a local .env file which contains the API key and then explicitly use that API key with the Python code shown in the steps to come.

Start by going to the project folder you want to create the .env file in.
Once you create the .gitignore and .env files using the terminal or an integrated development environment (IDE), copy your secret API key and set it as the OPENAI_API_KEY in your .env file. If you haven't created a secret key yet, you can do so on the API key page.

The .env file should look like the following:

Once you add your API key below, make sure to not share it with anyone! The API key should remain private.

OPENAI_API_KEY="your-api-key-here"

To run the code, enter python openai-test.py into the terminal / command line.
