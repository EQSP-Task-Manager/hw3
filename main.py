import os
import requests


def telegram_bot_sendtext(bot_token, bot_chat_id, bot_message):
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={bot_message}'
    response = requests.get(send_text)

    return response.json()


def main():
    bot_token = os.environ["INPUT_BOT_TOKEN"]
    bot_chat_id = os.environ["INPUT_BOT_CHAT_ID"]
    is_success = os.environ["INPUT_IS_SUCCESS"] == "true"
    project_name = os.environ["PROJECT_NAME"]

    if (is_success):
        if (project_name != None):
            bot_message = f"Your project \" {project_name} \" is successfully built"
        else:
            bot_message = f"Your project is successfully built"
    else:
        if (project_name != None):
            bot_message = f"Your project \" {project_name} \" built failed"
        else:
            bot_message = f"Your project build failed"

    telegram_bot_sendtext(bot_token=bot_token,
                          bot_chat_id=bot_chat_id, bot_message=bot_message)


if __name__ == "__main__":
    main()
