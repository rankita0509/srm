import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

def extract_predicates(sentence): 
    doc = nlp(sentence)
    predicates = []
    
    for token in doc:
        # Extract attributes and adjectival complements
        if token.dep_ in ['attr', 'acomp']:
            predicates.append(token.text)
        
        # Extract verbs excluding auxiliaries
        if token.pos_ == 'VERB' and token.dep_ != 'aux':
            predicates.append(token.lemma_)
    
    return sorted(set(predicates))

# Sample sentences
sentences = [
    "Sanchin is a cricketer.",
    "Sanchin is a cricketer and plays cricket.",
    "Some boys are intelligent."
]

# Extract and print predicates for each sentence
for sentence in sentences:
    predicates = extract_predicates(sentence)
    print(f"Predicates in the sentence '{sentence}': {predicates}")
