import os
import sys
import json

def txt2json(txt):
	scenes = {}
	scene = None
	text = None
	choices = None
	for line in txt.split("\n"):
		if line.startswith("scene:"):
			if scene:
				scenes[scene] = {
					"text": text,
					"images": [""],
					"choices": choices
				}
			scene = line.split(":")[1]
			text = ""
			choices = []
		elif line.startswith("text:"):
			text = line.split(":")[1]
		elif line.startswith("choices:"):
			choices = []
		elif line:
			next_scene, choice_description = line.split(":")
			choices.append({
				"description": choice_description,
				"next_scene": next_scene
			})
	if scene:
		scenes[scene] = {
			"text": text,
			"images": [""],
			"choices": choices
		}
	return {
		"scenes": scenes
	}

def main():
	if len(sys.argv) != 2:
		print(f"Usage: {sys.argv[0]} <text filename>")
		sys.exit(1)
	input_path = sys.argv[1]
	output_path = os.path.splitext(input_path)[0] + ".json"
	with open(input_path, "r") as f:
		txt = f.read()
	txt = "\n".join([line for line in txt.split("\n") if line])
	txt = txt.replace("\"\"", "\"")
	json_data = txt2json(txt)
	with open(output_path, "w") as f:
		json.dump(json_data, f, indent=8)
	with open(output_path, "r") as f:
		data = f.read()
	data = data.replace("        ", "\t")
	with open(output_path, "w") as f:
		f.write(data)
	print(f"Converted {input_path} to {output_path}")

if __name__ == "__main__":
	main()