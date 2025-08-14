from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def get_watson_response(user_input):
    authenticator = IAMAuthenticator('your-api-key')
    assistant = AssistantV2(
        version='2021-06-14',
        authenticator=authenticator
    )
    assistant.set_service_url('your-service-url')

    session_id = assistant.create_session(assistant_id='your-assistant-id').get_result()['session_id']
    response = assistant.message(
        assistant_id='your-assistant-id',
        session_id=session_id,
        input={'message_type': 'text', 'text': user_input}
    ).get_result()

    return response['output']['generic'][0]['text']
