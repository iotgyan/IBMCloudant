
# coding: utf-8

# In[30]:


from cloudant.client import Cloudant
# Create client using auto_renew to automatically renew expired cookie auth
client = Cloudant("UserName", "Passowrd", url='url',
                 connect=True,
                 auto_renew=True)


# In[31]:


my_database = client.create_database('DBName')

# You can check that the database exists
if my_database.exists():
    print('SUCCESS!!')


# In[32]:


my_database = client['my_database']


# In[34]:


my_document = my_database['12345']

# Display the document
print(my_document)


# In[35]:


for document in my_database:
    print(document)


# In[36]:


data = {
    '_id': '12345', # Setting _id is optional
    'name': 'Abhishek',
    'age': 22,
    'pets': ['cat', 'dog', 'frog']
    }

# Create a document using the Database API
my_document = my_database.create_document(data)

# Check that the document exists in the database
if my_document.exists():
    print('SUCCESS!!')


# In[38]:


my_document = my_database['12345']

# Update the document content
# This can be done as you would any other dictionary
my_document['name'] = "G D Abhishek"
my_document['age'] = 23

# You must save the document in order to update it on the database
my_document.save()


# In[39]:


my_document = my_database['12345']

# Display the document
print(my_document)


# In[40]:


# Delete a database using an initialized client
client.delete_database('my_database')


# In[41]:


1+2

