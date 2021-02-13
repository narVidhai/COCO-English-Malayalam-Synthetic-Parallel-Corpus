from glob import glob
from natsort import natsorted
import string

english_allowed_chars = string.ascii_letters + string.digits + string.punctuation + ' '

txt_files = natsorted(glob('raw/*.txt'))

out_en = open('coco.en', 'w', encoding='utf-8')
out_ml = open('coco.ml', 'w', encoding='utf-8')

for txt_file in txt_files:
    print('Processing:', txt_file)
    for line in open(txt_file, encoding='utf-8'):
        line = line.strip()
        try:
            eng, mal = line.split('.')
        except:
            for i, c in enumerate(line):
                if c not in english_allowed_chars:
                    break
            if i == len(line)-1:
                print('Failed to split:', line)
                continue
            else:
                if line[i-1] == '"' and line[i-2] == '"':
                    i -= 1
                eng, mal = line[:i], line[i:]
        
        eng = eng.strip()
        mal = mal.strip()
        
        if eng and mal:
            out_en.write(eng); out_en.write('\n')
            out_ml.write(mal); out_ml.write('\n')

out_en.close()
out_ml.close()
