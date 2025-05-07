from .create_video_chat import CreateVideoChat
from .discard_group_call import DiscardGroupCall


class Calls(
    CreateVideoChat,
    DiscardGroupCall,
):
    pass
