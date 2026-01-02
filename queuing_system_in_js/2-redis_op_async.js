import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

/**
 * Set a new school in Redis
 * @param {string} schoolName
 * @param {string} value
 */
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Promisify get
const getAsync = promisify(client.get).bind(client);

/**
 * Display school value from Redis (async/await)
 * @param {string} schoolName
 */
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
};

// Calls at the end of the file
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
