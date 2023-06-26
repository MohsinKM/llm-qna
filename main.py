
"""
Please install these following libraries
# tiktoken, openai, langchain, llama_index, pypdf, gradio
# Have your OpenAI key ready and set in the Environment variable
"""

from llama_index import SimpleDirectoryReader  # Reading docs
from llama_index import VectorStoreIndex  # for vector index management
from llama_index import StorageContext  # for index storing locally
from llama_index import load_index_from_storage  # to retrieve locally stored index
import gradio as gr

# os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY  # need to placed under env variables form run config
DOC_PATH = './llama_docs'
INDEX_PATH = './llama_index'


def construct_index(doc_path=DOC_PATH, index_store=INDEX_PATH, use_cache=False):
    """

    :param doc_path: Relative path where document will be stored to be indexed
    :param index_store: Relative path where index files will be stored
    :param use_cache: if True then won't use previously generated index store
    :return: None, index is locally stored in index_store location
    """
    if use_cache:
        # rebuild storage context
        storage_context = StorageContext.from_defaults(persist_dir=index_store)
        index = load_index_from_storage(storage_context)  # load index
    else:
        documents = SimpleDirectoryReader(doc_path).load_data()
        print(f"total_doc/pages found in the directory: {len(documents)}")
        print("Generating index...")
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=index_store)
    return None


def qabot(input_text):
    """

    :param input_text: input prompt
    :return: response to the prompt
    """
    storage_context = StorageContext.from_defaults(persist_dir="./llama_index")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    return response.response


if __name__ == "__main__":
    construct_index(DOC_PATH, use_cache=True)
    iface = gr.Interface(fn=qabot, inputs=gr.inputs.Textbox(lines=7, label='Enter your query'),
                         outputs="text",
                         title="Question and Answering App")
    iface.launch(share=False)
