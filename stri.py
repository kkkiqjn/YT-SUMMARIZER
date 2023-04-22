
from youtube_transcript_api import YouTubeTranscriptApi
inp="https://www.youtube.com/watch?v=YYQXk1t_JHM"
l=inp.split('/')
print(l)
linkn=l[0]+'//'+l[2]+'/embed/'+l[3][8:]
apifetch=YouTubeTranscriptApi.list_transcripts(l[-1][8:])
# print(apifetch[0]['text'])

transcript = apifetch.find_transcript([ 'en'])
text=""
for ele in transcript.fetch():
    text=text+ele['text']+" "
print(text)    