from spacy.lang.en import English
from utils.utilsfns import split_list
import re

def chunking_and_tokenization(pages_and_texts, logger):
    logger.info("inside chunking_and_tokenization.py")
    nlp = English()
    nlp.add_pipe("sentencizer")
    logger.info("SpaCy pipeline added.")

    for item in pages_and_texts:
        item["sentences"] = list(nlp(item["text"]).sents)
        item["sentences"] = [str(sentence) for sentence in item["sentences"]]
        item["page_sentence_count_spacy"] = len(item["sentences"])

    num_sentence_chunk_size = 10
    pages_and_chunks = []
    for item in pages_and_texts:
        item["sentence_chunks"] = split_list(input_list=item["sentences"], slice_size=num_sentence_chunk_size)
        for sentence_chunk in item["sentence_chunks"]:
            chunk_dict = {
                "page_number": item["page_number"],
                "sentence_chunk": re.sub(r'\.([A-Z])', r'. \1', "".join(sentence_chunk).replace("  ", " ").strip()),
            }
            chunk_dict["chunk_char_count"] = len(chunk_dict["sentence_chunk"])
            chunk_dict["chunk_word_count"] = len(chunk_dict["sentence_chunk"].split(" "))
            chunk_dict["chunk_token_count"] = len(chunk_dict["sentence_chunk"]) / 4
            pages_and_chunks.append(chunk_dict)
    
    logger.info(f"Generated {len(pages_and_chunks)} chunks.")
    logger.info("exited chunking_and_tokenization.py")
    return pages_and_chunks