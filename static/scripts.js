// JavaScript to handle showing scenario details in a modal
function viewScenarioDetails(scenarioId) {
  // Simulate fetching scenario details from server
  const scenarioDetails = fetchScenarioDetails(scenarioId);

  // Populate the modal with fetched data
  document.getElementById('modal-title').innerText = scenarioDetails.title;
  document.getElementById('modal-description').innerText = scenarioDetails.description;

  // Show the modal
  document.getElementById('scenario-modal').classList.remove('hidden');
}

// JavaScript to close the modal
function closeModal() {
  document.getElementById('scenario-modal').classList.add('hidden');
}

// JavaScript to handle fetching scenario details (simulated function)
function fetchScenarioDetails(scenarioId) {
  // This is a simulated function. Replace this with an AJAX call or Fetch API to get real data from the backend.
  const scenarios = {
      '1': {
          title: 'Scenario 1: Handling Confidential Information',
          description: 'You overheard your employer discussing a sensitive issue with a family member. How do you handle this information?'
      },
      '2': {
          title: 'Scenario 2: Unauthorized Visitors',
          description: 'A friend of the family visits when your employer is not home and insists on staying in the house. How do you manage the situation?'
      },
      // Add more scenarios as needed
  };

  return scenarios[scenarioId];
}

// JavaScript to handle responding to a scenario
function respondToScenario(scenarioId) {
  // Show the response form in the modal (you could also navigate to another page if desired)
  viewScenarioDetails(scenarioId);
}

// JavaScript to submit user response
function submitResponse() {
  const userResponse = document.getElementById('user-response').value;

  if (userResponse.trim() === '') {
      alert('Please enter a response before submitting.');
      return;
  }

  // Simulate submitting response to server
  console.log('Response submitted:', userResponse);

  // Optionally, you could clear the input field or close the modal after submission
  document.getElementById('user-response').value = '';
  closeModal();

  alert('Your response has been submitted successfully!');
}
