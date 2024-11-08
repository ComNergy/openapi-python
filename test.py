from suanleme_sdk import SuanlemeAPI

api = SuanlemeAPI(
    token="<your-token>",
)

print(api.get_task_list_page())
