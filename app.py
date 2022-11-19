from flask import Flask
from flask import request
import json
import whisper
from pytube import YouTube 
import os.path
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    videoid= str(request.args.get('input'))
    link='https://www.youtube.com/watch?v='+videoid
   
    try: 

    # object creation using YouTube
    # which was imported in the beginning 
        
         yt = YouTube(link) 
        
        #     result = model.transcribe("GoogleImagen.mp4")
        #     print(result['text'])
        #  except: 
        #    print("nothing")
    except: 
       print("Connection Error")
   
    
    # print(result)
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(139)
    stream.download('',"GoogleImagen.mp4")
    
    model = whisper.load_model("base")
    print(os.path.isfile("GoogleImagen.mp4"))
    result = model.transcribe("GoogleImagen.mp4")
    data_set= {'videoid':videoid}
    json_dump=json.dumps(data_set)
    print(result['text'])
        #  try:
  
    
    return json_dump


# if __name__ =="__main__":
#     app.run(debug=True)
