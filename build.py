import os
import shutil

# define variables
header = ''
navigation = ''
index = ''
attivita = ''
approfondimenti = ''
news = ''
footer = ''

print('deleting dist... ', end='', flush=True)
try:
  shutil.rmtree('dist')
except:
  pass
os.makedirs('dist')
print('done')

# get data
print('reading data... ', end='', flush=True)
with open('src/00_header.html','r') as f:
  header = f.read()
with open('src/10_navigation.html','r') as f:
  navigation = f.read()
with open('src/20_index.html','r') as f:
  index = f.read()
with open('src/30_attivita.html','r') as f:
  attivita = f.read()
with open('src/40_approfondimenti.html','r') as f:
  approfondimenti = f.read()
with open('src/50_news.html','r') as f:
  news = f.read()
with open('src/99_footer.html','r') as f:
  footer = f.read()
print('done')

# write files
print('building website... ', end='', flush=True)
with open('dist/index.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(index)
  f.write(footer)
with open('dist/attivita.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(attivita)
  f.write(footer)
with open('dist/approfondimenti.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(approfondimenti)
  f.write(footer)
with open('dist/news.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(news)
  f.write(footer)
print('done')

print('copyng assets... ', end='', flush=True)
shutil.copytree('src/assets','dist/assets')
shutil.copytree('src/js','dist/js')
shutil.copytree('src/style','dist/style')
print('done')
