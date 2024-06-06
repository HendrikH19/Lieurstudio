<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time Face Recognition</title>
</head>
<body>
    <h1>Real-Time Face Recognition</h1>
    <div style="text-align:center;">
        <video id="video" width="640" height="480" autoplay></video>
        <canvas id="canvas" width="640" height="480"></canvas>
        <br>
        <button id="startbutton">Take Picture</button>
    </div>
    <div id="result" style="margin-top:20px;"></div>

    <script>
        var video = document.getElementById('video');
        var canvas = document.getElementById('canvas');
        var context = canvas.getContext('2d');
        var resultDiv = document.getElementById('result');

        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                video.srcObject = stream;
                video.play();
            })
            .catch(function(err) {
                console.log("An error occurred: " + err);
            });

        document.getElementById('startbutton').addEventListener('click', function() {
            context.drawImage(video, 0, 0, 640, 480);
            var dataURL = canvas.toDataURL('image/jpeg');

            fetch('process_image.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: 'image=' + dataURL,
            })
            .then(response => response.text())
            .then(data => {
                resultDiv.innerHTML = data;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
