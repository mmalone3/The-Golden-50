function addQuickActivity(activityName) {
    fetch('/add_activity', {
        method: 'POST',
        body: JSON.stringify({
            name: activityName,
            start_time: new Date().toISOString(),
            end_time: '',
            duration: ''
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log('Activity added:', data))
    .catch(error => console.error('Error adding activity:', error));
}