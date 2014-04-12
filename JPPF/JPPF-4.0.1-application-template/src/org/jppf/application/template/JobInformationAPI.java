package org.jppf.application.template;

import org.jppf.application.template.TemplateApplicationRunner;
import org.jppf.client.*;
import org.jppf.node.protocol.Task;
import org.jppf.client.submission.*;

/**
 * This class provides a simplified window to the JPPF API focused on job submission and status.
 *
 */
public class JobInformationAPI
{
	private TemplateApplicationRunner jobRunner;

	/*
	* Constructor, initializes the application runner
	*/
	public JobInformationAPI()
	{
		// this call reads from the config file and connects to the JPPF server
		jobRunner = TemplateApplicationRunner.getInstance();
	}

	/**
	* @Throws Exception if an error occurs while creating the job.
	* @Returns the ID of the Job that was created
	*/
	public String submitTestJob(String desiredOutput, int secondsLong, int numTasks) throws Exception
	{
		// Create a job
		JPPFJob job = jobRunner.createTestJob(desiredOutput, secondsLong, numTasks);

		// execute a non-blocking job
		jobRunner.executeNonBlockingJob(job);

		return job.getUuid();
	}

	/**
	* Randomized Tasks will sometimes fail.
	* @Throws Exception if an error occurs while creating the job.
	* @Returns the ID of the Job that was created
	*/
	public String submitRandomizedTestJob(String desiredOutput, int maxWaitTime, int numTasks) throws Exception
	{
		// Create a job
		JPPFJob job = jobRunner.createRandomizedTestJob(desiredOutput, maxWaitTime, numTasks);

		// execute a non-blocking job
		jobRunner.executeNonBlockingJob(job);

		return job.getUuid();
	}
	
	/*
	* @Returns the ID of the Job that is created
	*/
	public String submitBlenderJob(String[] dependencies, String[] nodeIPs)
	{
		return "FAIL";
	}

	/*
	* @Returns "SUBMITTED", "PENDING", "EXECUTING", "COMPLETE", "FAILED", or "NONEXISTENT" if the job doesn't exist
	*/
	public String getJobStatus(String jobID)
	{
		JPPFResultCollector results;
		String[] possibleStatuses = new String[]{"SUBMITTED", "PENDING", "EXECUTING", "COMPLETE", "FAILED", "NONEXISTENT"};
		
		// If the job doesn't exist in the jobRunner, it will throw an exception
		try
		{
			results = jobRunner.getResultsForJob(jobID);
		}
		catch(Exception e)
		{
			return "NONEXISTENT";		
		}
	
		for(String status : possibleStatuses)
		{
			if(results.getStatus() == SubmissionStatus.valueOf(status))
			{
				return status;			
			}
		}
	
		// This should never happen.
		return "FAILED";
	}

	/*
	* @Returns true if the job was successfully cancelled, false otherwise
	*/
	public boolean cancelJob(String jobID)
	{
		return jobRunner.cancelJob(jobID);
	}

	/*
	* @Returns the number of tasks in the specified job
	*/
	public int getTotalTasks(String jobID)
	{
		return jobRunner.getTotalTasks(jobID);
	}

	/*
	* @Returns the number of tasks still pending for the specified job
	*/
	public int getNumCompleteTasks(String jobID)
	{
		return jobRunner.getNumCompleteTasks(jobID);
	}
}






