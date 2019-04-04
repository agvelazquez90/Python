import pandas as pd
import os

#Choose your work directory.Use foward slash or double back slash. 
#Eg: C:/Desktop or C:\\Desktop
os.chdir('your working Directory')

#Create function to validate if the file comes from local directory or remote server and then read the file
def arg_input(server=None, user=None, pw=None, target_path=None):
    if(server is None or user is None or pw is None):
        print("Local path selected...")
        df = pd.read_csv(target_path,sep='|', index_col=False, error_bad_lines=False) #read local file
        return(df)
    else:
        print("Remote Connection selected...")
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None #set hostkey NULL
        s = sftp.Connection(host=server, username=user, password=pw, cnopts=cnopts) #establish connection
        with s.open(target_path) as f: #open the file from server
            df = pd.read_csv(f,sep='|', index_col=False, error_bad_lines=False) #read remote file
        s.close() #close connection
        return(df)
