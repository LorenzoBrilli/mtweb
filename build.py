import os
import shutil

# define variables
header = ''
navigation = ''
index = ''
attivita = ''
approfondimenti = ''
news = ''
cookie_policy = ''
footer = ''

print('deleting dist... ', end='', flush=True)
try:
  shutil.rmtree('docs')
except:
  pass
os.makedirs('docs')
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
with open('src/90_cookie-policy.html','r') as f:
  cookie_policy = f.read()
with open('src/99_footer.html','r') as f:
  footer = f.read()
print('done')

# write files
print('building website... ', end='', flush=True)
with open('docs/index.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(index)
  f.write(footer)
with open('docs/attivita.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(attivita)
  f.write(footer)
with open('docs/approfondimenti.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(approfondimenti)
  f.write(footer)
with open('docs/news.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(news)
  f.write(footer)
with open('docs/cookie-policy.html','w') as f:
  f.write(header)
  f.write(navigation)
  f.write(cookie_policy)
  f.write(footer)
print('done')

print('copying assets... ', end='', flush=True)
shutil.copytree('src/assets','docs/assets')
shutil.copytree('src/js','docs/js')
shutil.copytree('src/style','docs/style')
shutil.copy('src/CNAME','docs/CNAME')
print('done')
