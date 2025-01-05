// Constant variable to store the fetched data
let itemsData = [];

// Function to fetch data from the Django backend
const fetchItemsByCategory = async (category) => {
  try {
    const response = await fetch(`http://localhost:8000/api/getitems/${category}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json(); // Parse the JSON response
    itemsData = data; // Store the fetched data in the constant variable
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error; // Re-throw the error to handle it in the component
  }
};

// Export the constant variable and the fetch function
export { itemsData, fetchItemsByCategory };