import os
import sys
import json
import sqlite3
import base64

def image_to_base64(filename):
	if filename == '':
		return
	if not os.path.exists(filename):
		return
	with open(filename, "rb") as image_file:
		return base64.b64encode(image_file.read()).decode('utf-8')

if len(sys.argv) != 2:
	print(f"Usage: {sys.argv[0]} <json file>")
	sys.exit(1)

filename = sys.argv[1]
with open(filename) as f:
	adventure_data = json.load(f)
db_filename = os.path.splitext(filename)[0] + ".db"

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS scenes')
cursor.execute('DROP TABLE IF EXISTS images')
cursor.execute('DROP TABLE IF EXISTS choices')

cursor.execute('''
CREATE TABLE IF NOT EXISTS scenes (
	id INTEGER PRIMARY KEY,
	tag TEXT UNIQUE,
	text TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS images (
	id INTEGER PRIMARY KEY,
	scene_id INTEGER,
	filename TEXT,
	FOREIGN KEY(scene_id) REFERENCES scenes(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS choices (
	id INTEGER PRIMARY KEY,
	scene_id INTEGER,
	description TEXT,
	next_scene_tag TEXT,
	FOREIGN KEY(scene_id) REFERENCES scenes(id)
)
''')

scene_id = 0
for tag, scene in adventure_data['scenes'].items():
	cursor.execute('''
	INSERT OR IGNORE INTO scenes (tag, text)
	VALUES (?, ?)
	''', (tag, scene['text']))
	scene_id += 1

	for filename in scene['images']:
		cursor.execute('''
		INSERT INTO images (scene_id, filename)
		VALUES (?, ?)
		''', (scene_id, image_to_base64(filename)))

	for choice in scene['choices']:
		cursor.execute('''
		INSERT INTO choices (scene_id, description, next_scene_tag)
		VALUES (?, ?, ?)
		''', (scene_id, choice['description'], choice['next_scene']))

conn.commit()
conn.close()

print("Database created successfully.")