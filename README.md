<p align="center">
	<img src="./asset/logo.png" alt="Logo" width="150" height="50">
</p>

<h1 align="center">Choose Your Own</h1>

<p align="center">
	<strong>Make your own choose-your-own adventures to play!</strong>
</p>

## 🚀 Overview

Welcome to **Choose Your Own**! This program allows you to create your own choose-your-own adventures to play. You can then play your own adventures in a local browser.

> [!NOTE]
> The program does not yet currently look new adventures that are created. They have to be manually added to the game. See [this](#-creating-your-own-adventures) for more information.

## 🎨 Features

- **Customization**: Create your own choose-your-own adventures to play.
- **Aesthetics**: You can create images and change the colors of the text.

## 🛠️ Installation

To get started with the program, follow the steps below:

1. **Clone the Repository**
```sh
git clone https://github.com/321BadgerCode/choose_your_own.git
cd ./choose_your_own/
```

## 📈 Usage

To use the program, follow the instructions below:

1. **Run the program**
```sh
php -S localhost:8000
```

<details>

<summary>📦 Dependencies</summary>

- **PHP:** `sudo apt-get install php`

</details>

## 🎮 Creating Your own Adventures

To create your own adventures, follow the instructions below:

1. **Create the adventure**
```sh
cat ./explorer.txt # if you want to see the format
touch ./adventure.txt && vi ./adventure.txt
```
2. **Convert the .txt file to a .json file**
```sh
python ./txt2json.py ./adventure.txt
```
3. **Add images to the .json file**
You can go into the .json file and add image filenames into the `images` json list.
```sh
vi ./adventure.json
```
4. **Convert the .json file to a .db file**
```sh
python ./json2db.py ./adventure.json
```
5. **Add the .db file to the game**
Within the [index.html](./index.html) file, add the following code using `vi ./index.html`:
```html
<form>
	<label for="db">Select a story:</label>
	<select name="db" id="db">
		<option value="explorer.db">Explorer</option>
		<option value="adventure.db">Adventure</option>
		<!-- Add this previous line of code up here ^^^  -->
	</select>
	<input type="submit" value="Submit">
</form>
```

<details>

<summary>💻 Text Options</summary>

|	Option		|	Description		|
|	:---:		|	:---:			|
|	`<image>`	|	Place an image		|
|	`<br>`		|	Paragraph break		|
|	`<b>${text}</b>`|	Bold text		|
|	`<i>${text}</i>`|	Italicize text		|
|	`"${text}"`	|	Quote text		|

</details>

## 📜 License

[LICENSE](./LICENSE)