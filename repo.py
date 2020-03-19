#!/usr/bin/env python
# coding: utf-8

# In[54]:


import base64
import json


# In[55]:





# In[56]:


repo_filename = 'repo.db'


# In[57]:


def read_file(repo_file):
    with open(repo_file, 'r') as input_file:
        return input_file.readlines()[0]


# In[58]:


def write_file(repo_file, line):
    with open(repo_file, 'w') as output_file:
        output_file.write(line)


# In[59]:


def encode(key, string):
    base64_string = base64.urlsafe_b64encode(string)
    encoded_chars = []
    for index in xrange(len(base64_string)):
        key_char = key[index % len(key)]
        encoded_char = chr(ord(base64_string[index]) + ord(key_char) % 256)
        encoded_chars.append(encoded_char)
    return ''.join(encoded_chars)


# In[60]:


def decode(key, string):
    decoded_chars = []
    for index in xrange(len(string)):
        key_char = key[index % len(key)]
        decoded_char = chr(ord(string[index]) - ord(key_char) % 256)
        decoded_chars.append(decoded_char)
    decoded_string = ''.join(decoded_chars)
    return base64.urlsafe_b64decode(decoded_string)


# In[61]:


def read_repo(key):
    encoded_json_string = read_file(repo_filename)
    json_string = decode(key, encoded_json_string)
    return json.loads(json_string)


# In[62]:


def write_repo(key, tests):
    json_string = json.dumps(tests)
    encoded_json_string = encode(key, json_string)
    write_file(repo_filename, encoded_json_string)

