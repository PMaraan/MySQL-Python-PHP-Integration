<?php
$output = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Define the path to the Python executable and the script
    $python = 'python'; // Adjust the path to your Python executable
    $scriptPath = 'C:\xampp\htdocs\Maraan\00_execute_script.py'; // Update this to the path of your script

    // Execute the Python script and capture the output
    $output = shell_exec("$python $scriptPath");
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Run Python Script</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #28a745;
            color: white;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #218838;
        }
        pre {
            background: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Run Python Integration</h1>
        <form method="post">
            <button type="submit">Run Script</button>
        </form>
        <?php if ($output): ?>
            <h2>Output:</h2>
            <pre><?php echo htmlspecialchars($output); ?></pre>
        <?php endif; ?>
    </div>
</body>
</html>