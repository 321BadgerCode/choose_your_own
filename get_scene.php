<?php
function getDatabaseConnection($database) {
	$db = new SQLite3($database);
	return $db;
}

function getScene($tag, $database) {
	$db = getDatabaseConnection($database);

	$stmt = $db->prepare('SELECT * FROM scenes WHERE tag = :tag');
	$stmt->bindValue(':tag', $tag, SQLITE3_TEXT);
	$result = $stmt->execute();
	$scene = $result->fetchArray(SQLITE3_ASSOC);

	$stmt = $db->prepare('SELECT * FROM choices WHERE scene_id = :scene_id');
	$stmt->bindValue(':scene_id', $scene['id'], SQLITE3_INTEGER);
	$choicesResult = $stmt->execute();

	$choices = [];
	while ($row = $choicesResult->fetchArray(SQLITE3_ASSOC)) {
		$choices[] = $row;
	}

	$stmt = $db->prepare('SELECT filename FROM images WHERE scene_id = :scene_id');
	$stmt->bindValue(':scene_id', $scene['id'], SQLITE3_INTEGER);
	$imagesResult = $stmt->execute();

	$images = [];
	while ($row = $imagesResult->fetchArray(SQLITE3_ASSOC)) {
		$images[] = $row['filename'];
	}

	$db->close();

	$scene['choices'] = $choices;
	$scene['images'] = $images;

	return json_encode($scene);
}

if ((!empty($_GET['tag']) && isset($_GET['tag']) && (!empty($_GET['db']) && isset($_GET['db'])))) {
	$tag = $_GET['tag'];
	$database = $_GET['db'];
	echo getScene($tag, $database);
} else {
	echo json_encode(['error' => 'No scene tag provided']);
}
?>