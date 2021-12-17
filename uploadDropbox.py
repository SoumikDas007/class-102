import cv2
import dropbox
import time
import random



start_time=time.time()

def snapShot():
    num=random.randint(0,100)
    #to open the webcam and 0 is our camera
    videoCaptureObject= cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img="pic"+str(num)+".png"
        cv2.imwrite(img,frame)
        start_time=time.time
        result=False
    print("SNAPSHOT TAKEN")
        #to close the webcam
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    





def upload_files(img_name):
    access_token="sl.A-UdXgZBVuDPWL4Jfl5UnbfLkyngY2ikIlRnurBC5mLJ8caPgG2k9hDUNIgpVnx4UITfYMFuX5viep1qcvopQ-_3VWVuB-AxA2IVmO8MikCns-m8m0GPww11G9m7GqrJcPsa-czAIiIQ"
    file =img_name 
    file_from = file 
    file_to="/python/"+(img_name) 
    dbx = dropbox.Dropbox(access_token) 

    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=10):
            capture=snapShot()
            upload_files(capture)

main()



