import kue from 'kue';

// Create queue
const queue = kue.createQueue();

/**
 * Send notification
 * @param {string} phoneNumber
 * @param {string} message
 */
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

// Process jobs from the queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
