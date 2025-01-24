from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    last_chunk = docs[-1]
    print("page count={}, last_chunk={}".format(len(docs), last_chunk))
    return last_chunk

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()
    pdf_text = "\n".join([doc.page_content for doc in documents])
    separators=[ "\s+第 [一二三四五六七八九十]+ 章\s+", "\s+第 \d+-\d+ 條\s+", "\s+第 \d+ 條\s+"]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1,
                                                   chunk_overlap=0,
                                                   keep_separator = True,
                                                   is_separator_regex=True,
                                                   separators=separators)
    chunks = text_splitter.split_text(pdf_text)
    chunk_count = len(chunks)
    print("chunk_count={}".format(chunk_count))
    for i, v in enumerate(chunks):
        pass
        #print("chunk {}={}".format(i, v[:20]))
    return chunk_count
