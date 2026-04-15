import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator

from PIL import Image

st.title("Note Summary and Quiz Generator " ,anchor=None)
st.markdown("Upload max 3 Images to generate Note Summary and Quiz Generator")
st.divider()

with st.sidebar:
    
    st.header("Controller")
    #images
    images = st.file_uploader("Upload the Photos of your note", type=["jpg","png","jpeg"], accept_multiple_files=True)
    
    pil_images = []
    
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    
    if images:
                
        if len(images)>3:
            st.error("Upload at max 3 Images")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))
            
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    #difficulty
    selected_option = st.selectbox("Enter Yours Difficulty and Quiz",("Easy","Medium","Hard"), index=None)
    
    # if selected_option:
    #     st.markdown(f"You selected **{selected_option}** as difficulty of your Quiz")
    # else:
    #     st.error("You Must select a difficulty")
    
    pressed = st.button("Click the Button to initiate AI", type="primary",)
    
if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty")
        
    if images and selected_option:
        
        #Note
        with st.container(border=True):
            st.subheader("Your Note")
            # The portion below will be replaced by API Call
            # st.text("Note will be show here")
            
            with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)
        
        #Audio transcript
        with st.container(border=True):
            st.subheader("Your Audio Transcription")
            # The portion below will be replaced by API Call
            
            with st.spinner("AI is generating Audio transcript for you"):
                # clearing markdown
                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("`","")
                generated_notes = generated_notes.replace("|","")
                
                audio_transcript = audio_transcription(generated_notes)
                # st.audio("Audio Transcripts will be show here")
                st.audio(audio_transcript)
        #Quiz
        with st.container(border=True):
            st.subheader(f"Your Quiz ({selected_option}) Difficulty")
            # The portion below will be replaced by API Call
            with st.spinner("AI is generating the Quiz for you"):
                quizzes = quiz_generator(pil_images,selected_option)
                # st.text("Quiz will be show here")
                    
                st.markdown(quizzes)
