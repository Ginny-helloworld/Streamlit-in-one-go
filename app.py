import streamlit as st
st.title('Title-> Welcom to the tutorial of Data Science and Machine learning' )         # Title 
st.header('Header->Data Science and Machine learning' )                                  # Header
st.subheader('Subheader-> Data Analysts')                                                # Subheader
st.text('Text->Hello my name is Ginny Shai')                                             

st.markdown('Aspiring Data Scientist')                                                   # Markdown
st.markdown('# Aspiring Data Scientist')
st.markdown('## Aspiring Data Scientist')
st.markdown('### Aspiring Data Scientist')
st.markdown('#### Aspiring Data Scientist')
st.markdown('##### Aspiring Data Scientist')

st.success('Success!')                                                                   # success
st.info('Information!')                                                                  # info
st.warning('Warning')                                                                    # warning
st.error('Error')                                                                        # error


st.exception(ZeroDivisionError('Div not possible with 0'))                               # Exception

st.help(ZeroDivisionError)                                                               # can pass any function inside help


st.write('range(1,10)')                                                                  # write with ('')-> string
st.write(range(1,10))                                                                    # write with ()-> int
st.write('1+2+3+4+5')
st.write(1+2+3+4+5)

st.code('x=10 \n'                                                                        # Code 
        'for i in range(x): \n'
        '\tprint(i)')

st.checkbox('Male')                                                                      # checkbox 
st.checkbox('Female')                                                                    # *note there cannot be two checkbox with same name 

if(st.checkbox('Adult')):                                                                # checkbox with validation
    st.write('You are an adult')


radioButton=st.radio('Select : ',('Male','Female','Others'))                             # Radio-> it basically selects only one option

if(radioButton== 'Male'):
    st.write("You selected Male")
elif(radioButton=='Female'):
    st.write('You selected Female')
elif(radioButton=='Others'):
    st.write('You selected Others')
    


st.subheader('Select Box')                                                               # Selectbox
st.write('Select your area of interest')
selectBox=st.selectbox("Data Science : ",['Data Analyst','Machine Learning','Web Scrapping','Deep Learning','Natural Language Processing','Computer Vision'])   
st.write("You have selected : ",selectBox)

st.subheader('Multi-Select box')                                                         # Multiselect box

multiSelect=st.multiselect('Data Science : ',['Data Analyst','Data Scientist','Machine Learning', 'Computer Vision', 'Web Scrapping', 'Natural Language Processing','Deep Learning'])

st.write("You have selected: ",len(multiSelect),multiSelect)
st.write("You have selected: ",len(multiSelect),'courses')
    
    
st.subheader('Button box')                                                                  # Button 
if(st.button('Click me')):
    st.write('Welcome, to this page')  
    
    

st.subheader('Slider')
volume=st.slider('Select the volume',0,100,step=1)                                          # Slider
if(volume>=70):
    st.write('High volume may affect your ear')
st.write('Volume is: ',volume)


st.subheader('User Input')                                                                  # User input
Username=st.text_input('Username: ')                                                        
password= st.text_input('Password: ',type='password')                                       # type='password'


st.subheader('Text Area')
st.text_area('Write a paragraph on Ghec')

st.subheader("Input-Number")
st.number_input('Select your age',18,110)

st.subheader("input date")
st.date_input('DOB')

st.subheader("input time")
st.time_input('Time')

