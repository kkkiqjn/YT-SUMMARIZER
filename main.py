

import openai
from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask,render_template,request
app = Flask(__name__)

openai.api_key = "--------------------------------"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
# # summarizer=pipeline("summarization")







@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def success():
    if request.method == 'POST':
        link=request.form.get("search")
        l=link.split('/')
        print(l)
        linkn=l[0]+'//'+l[2]+'/embed/'+l[3][8:]






        apifetch=YouTubeTranscriptApi.list_transcripts(l[-1][8:])
        transcript = apifetch.find_transcript()
        text=""
        for ele in transcript.fetch():
            text=text+ele['text']+" "
        print(text)
       


        prompt="Summarize the text,text:"+text
        summary=generate_response(prompt)
        res=summarizer(text, max_length=250, min_length=30, do_sample=False)
        summary=res[0]['summary_text']



        
        






        return  render_template("result.html",link=linkn,res=summarys[0]['summary_text'])
    
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)
