document.getElementById('show-all').addEventListener('click', () => {
    fetch('/episodes/display')
    .then(response => response.json())
    .then(data => {
        const episodes = Object.values(data); // Convert object to array
        const episodeList = document.getElementById('episode-list');
        episodeList.innerHTML = '';  // Clear the list
        episodes.forEach(episode => {
            const episodeElement = document.createElement('div');
            episodeElement.innerHTML = `<strong>${episode.name}</strong><br>Season ${episode.season}, Episode ${episode.episode}<br>Description: ${episode.description}<br><br>`;
            episodeList.appendChild(episodeElement);
        });
    })
    .catch(error => console.error('Error fetching episodes:', error));

});


document.getElementById('random-episode').addEventListener('click', () => {
    fetch('/episodes/random')
        .then(response => response.json())
        .then(episode => {
            const episodeList = document.getElementById('episode-list');
            episodeList.innerHTML = '';  // Clear existing list
            const episodeElement = document.createElement('div');
            episodeElement.innerHTML = `<strong>${episode.name}</strong><br>Season ${episode.season}, Episode ${episode.episode}<br>Description: ${episode.description}<br><br>`;
            episodeList.appendChild(episodeElement);
        });
});

document.getElementById('add-episode-form').addEventListener('submit', event => {
    event.preventDefault();

    const season = document.getElementById('season').value;
    const episodeNumber = document.getElementById('episode').value;
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;

    const episodeData = {
        season: parseInt(document.getElementById('season').value, 10),
        episode: parseInt(document.getElementById('episode').value, 10),
        name: document.getElementById('name').value,
        description: document.getElementById('description').value
    };

    fetch('/episodes/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(episodeData)
    })
    .then(response => response.json())
    .then(data => {
        alert('Episode added!');
        season.value = '';
        episodeNumber.value = '';
        name.value = '';
        description.value = '';
    })
    .catch(error => {
        console.error('Error adding episode:', error);
    });
});
