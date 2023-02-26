from nea_site.settings import ENCRYPT_KEY

# source https://stackoverflow.com/questions/5131227/custom-python-encryption-algorithm
def encrypt_data(value):
    encrypted = []
    for i, c in enumerate(value):
        key_c = ord(ENCRYPT_KEY[i % len(value)])
        msg_c = ord(c)
        encrypted.append(chr((msg_c + key_c) % 127))
    return ''.join(encrypted)


def decrypt_data(encrypted_value):
    msg = []
    for i, c in enumerate(encrypted_value):
        key_c = ord(ENCRYPT_KEY[i % len(ENCRYPT_KEY)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

# Define function to generate trigrams for a given string
def generate_trigrams(text):
    trigrams = []
    for i in range(len(text)-2):
        trigrams.append(text[i:i+3])
    return trigrams

def fuzzy_text_search(query, corpus, threshold=0.5):
    # Generate trigrams for query
    query_trigrams = generate_trigrams(query.lower())
    # Generate trigrams for corpus
    corpus_trigrams = generate_trigrams(corpus.lower())
    # Check if any query trigrams are in corpus trigrams
    for trigram in query_trigrams:
        if trigram in corpus_trigrams:
            # Calculate similarity score
            query_words = set(query.lower().split())
            text_words = set(corpus.lower().split())
            shared_words = query_words.intersection(text_words)
            similarity = len(shared_words) / float(len(query_words) + len(text_words) - len(shared_words))
            # Return true if similarity score is above threshold
            if similarity >= threshold:
                return True
    # Return false if no matching trigrams were found
    return False


def find_matching_notes(search_str,notes_list):
    if(search_str==''):
        return notes_list
    matched_list=[]
    for note in notes_list:
        match=fuzzy_text_search(search_str,note['body_text'],0.2)
        if(match):
            matched_list.append(note)
    return matched_list
