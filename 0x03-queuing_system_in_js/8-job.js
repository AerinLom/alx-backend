import { Queue, Job } from 'kue';

export const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((jobInfo) => {
    const job = queue.create('push_notification_code_3', jobInfo);

    job
      .on('enqueue', () => console.log('Notification job created:', job.id))
      .on('complete', () => console.log('Notification job', job.id, 'completed'))
      .on('failed', (err) => console.log('Notification job', job.id, 'failed:', err.message))
      .on('progress', (progress) => console.log('Notification job', job.id, `${progress}% complete`));

    job.save();
  });
};

export default createPushNotificationsJobs;
