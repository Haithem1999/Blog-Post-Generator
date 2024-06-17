import uuid 
import streamlit as st 
# from decouple import config
from p_blog_generator import write_section, generate_outline

def create_blog_post(topic, blog_subject): 
    
    try:
        # Outline generation 
        with st.spinner("Generating outline..."):
            json_outline = generate_outline(topic, blog_subject)
        blog_title = json_outline['title']
        print(blog_title)
        st.markdown(f"# {blog_title}")
        # Write sections
        blog_sections = json_outline['sections']
        history_text = ''
        for section in blog_sections: 
            st.divider()
            with st.spinner("Writing section {section[header]}..."):
                content = write_section(topic, section['header'], section['sub-sections'], history_text)
            history_text += content
            st.markdown(content)
        return history_text        
        
    except Exception as e:
        print(e)
        return "", ""
    
# page configuration
st.set_page_config(
    page_title='Blog Post Generator',
    page_icon=':pencil2:',
    layout = 'centered')

st.title('Blog Post Generator')
# Page description

st.markdown = f"""
Welcome to Blog Post Generator!\n\n
This site is both simple and powerful, leveraging the latest AI advancements and unique models 
to craft a blog post for you based on just a category and subject.\n\n
NOTE: You can download the generated blog post as a markdown file!

"""

st.markdown = "---"
st.subheader('Generate Your Blog Post', anchor=False)
category = st.selectbox('Category', options = ("", "Travel", "Technology", "Business", "Health", "Science", "Sports", "Entertainment", "Politics", "Education")
                         
                         )

subject = st.text_input('Subject')
generate = st.button('Generate Blog Post')
if generate: 
    # Validate inputs
    error = ""
    if category == "": 
        error+= 'Please select a category.\n\n'
    if subject == "": 
        error+= 'Please select a subject.\n\n'
    if error != "": 
        st.error(error)
        st.stop()
    # Create blog post
    st.divider()
    history = create_blog_post(category, subject)
    st.divider()
    st.success("Blog Post Generated Successfully!")
    random = uuid.uuid4().hex
    downloaded = st.download_button("Download Blog Post", 
                                    str(history), f"{category}_{subject}_{random}.md", "text/markdown", 
                                    help="Note: Generated blog post will disappear, but you can keep the file")
    if downloaded: 
        # save file
        with open(f"{category}_{subject}_{random}.md", "w") as f: 
            f.write(history)
            
            
            
    
    

 







 
    
