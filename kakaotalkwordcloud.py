import os

from wordcloud import WordCloud

# Read the text file
with open('input3.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Check if the text is empty
if not text:
    print('Error: The text file is empty.')
else:
    # Remove the word "example" from the text
    # text = text.replace('(알 수 없음)', '')
    text = text.replace('정하빈', '')
    text = text.replace('나에게', '')
    text = text.replace('특별한', '')
    text = text.replace('재학', '')
    text = text.replace('2022년', '')
    text = text.replace('2023년', '')
    text = text.replace('월', '')
    text = text.replace('일', '')
    text = text.replace('오전', '')
    text = text.replace('오후', '')

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=800, background_color='white', colormap='viridis', max_words=200, font_path='NanumGothic.ttf').generate(text)

    # Save the word cloud image
    wordcloud.to_file(os.path.join('output6.png'))

    print('Word cloud generated successfully!')