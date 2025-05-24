from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatOpenAI(
    callbacks=[StreamingStdOutCallbackHandler()], temperature=0
)

print(chat([HumanMessage(content="write me a song about sparkling water.")]))