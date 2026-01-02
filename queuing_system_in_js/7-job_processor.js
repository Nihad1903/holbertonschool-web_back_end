import kue from 'kue';

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create queue
const queue = kue.createQueue();

/**
 * Send notification
 * @param {string} phoneNumber
 * @param {string} message
 * @param {Object} job
 * @param {Function} done
 */
const sendNotification = (phoneNumber, message, job, done) => {
  // Track initial progress
  job.progress(0, 100);

  // Check blacklist
  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  // Continue processing
  job.progress(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  done();
};

// Process jobs (2 at a time)
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
