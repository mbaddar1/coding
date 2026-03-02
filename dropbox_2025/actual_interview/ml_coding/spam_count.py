"""
Given a set of spam keywords
k = ["offer","now","aaa","baa"]
email_text = ["buy this offer now aaaat our website"
return dict of each keyword and existence count in email
"""
from data_processing.regex.valid_email1 import print_match_object


def find_counts(keywords,email)->dict:
    keywords_count = {}
    for k in keywords:
        counter = 0
        for i in range(len(email)):
            for j in range(len(k)):

                # if i+j < len(email) and email[i+j] != k[j]: - this is wrong
                if i+j < len(email) and email[i+j] != k[j]:
                    break
            if j == len(k)-1 and i+j < len(email) and email[i+j] == k[j]:
                counter += 1
        keywords_count[k] = counter
    return keywords_count
if __name__ == "__main__":
    # keywords = ["offer","now","aaa","baa"]
    keywords = ["aaa"]
    email = "aaaat offer"
    counts = find_counts(keywords,email)
    print(counts)
