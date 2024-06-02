print('Страп Андріана група 2 лаб 7')
import sqlite3, re
conn = sqlite3.connect('pol_lab07.s3db')
c = conn.cursor()
c.execute('SELECT sgN FROM tnoun ORDER BY RANDOM() LIMIT 1;')
print("".join(c.fetchone()) )
c.execute('SELECT sgI FROM tnoun WHERE sgI LIKE "u%";')
result = c.fetchall()
print(", ".join([row[0] for row in result]))
c.execute("INSERT INTO tnoun(sgN, gender) VALUES('punkt', 1)")

def parse_file(file_path):
    result = {}
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(.+)\t(punkt+)\t(.+)', line.strip())
            if match:
                word, base_form, tags = match.groups()
                forms = re.findall(r'([a-z]{2,3}):([a-z]+):([a-z0-9:.]+)', tags)
                for form in forms:
                    number, case, gender = form
                    key = f'{case}{gender[0]}'
                    result[key] = word
    return result

s = parse_file('parse_lab07.txt')
print(s)
c.execute('''UPDATE [tnoun] 
SET [sgN] = ?, 
    [sgG] = ?, 
    [sgD] = ?, 
    [sgA] = ?, 
    [sgI] = ?, 
    [sgL] = ?, 
    [sgV] = ?, 
    [plN] = ?, 
    [plG] = ?, 
    [plD] = ?, 
    [plA] = ?, 
    [plI] = ?, 
    [plL] = ?, 
    [plV] = ?
WHERE [sgN] = ?;''',
(s['sgn'], s['sgg'], s['sgd'], s['sga'], s['sgi'], s['sgl'], s['sgv'], s['pln'], s['plg'], s['pld'], s['pla'], s['pli'], s['pll'], s['plv'], 'punkt'))
conn.commit()
conn.close()
