import org.jppf.application.template.TemplateApplicationRunner;
import org.jppf.client.*;

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
		jobRunner = new TemplateApplicationRunner();
	}

	/**
	* @Throws Exception if an error occurs while creating the job.
	* @Returns the ID of the Job that was created
	*/
	public String submitTestJob(String desiredOutput, int secondsLong) throws Exception
	{
		// Create a job
		JPPFJob job = jobRunner.createJob();

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
	* @Returns "SUBMITTED", "PENDING", "EXECUTING", "COMPLETE", or "FAILED"
	*/
	public String getJobStatus(String jobID)
	{
		return "FAILED";
	}

	/*
	* @Returns true if the job was successfully cancelled, false otherwise
	*/
	public boolean cancelJob(String jobID)
	{
		return false;
	}


}
