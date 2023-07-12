#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os,shutil



# In[30]:


path=r"C:/data analyst/"


# In[31]:


file_name = os.listdir(path)
#print(file_name)


# In[35]:


folder_name=['csv files' ,'Excel files' , 'Power Bi files' , 'EXE files' , 'PDF files']
for loop in range(0,5):
    if not os.path.exists(path+folder_name[loop]):
        print(path+folder_name[loop])
        os.makedirs(path+folder_name[loop])

for file in file_name:
    if ".csv" in file and not os.path.exists(path+"csv files/"+file):
        shutil.move(path+file,path+"csv files/"+file)
    elif ".xlsx" in file and not os.path.exists(path+"Excel files/"+file):
        shutil.move(path+file,path+"Excel files/"+file)
    elif ".pdf" in file and not os.path.exists(path+"PDF files/"+file):
        shutil.move(path+file,path+"PDF files/"+file)
    elif ".pbix" in file and not os.path.exists(path+"Power Bi files/"+file):
        shutil.move(path+file,path+"Power Bi files/"+file)
    elif ".exe" in file and not os.path.exists(path+"EXE files/"+file):
        shutil.move(path+file,path+"EXE files/"+file)
   


# In[28]:





# In[21]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




