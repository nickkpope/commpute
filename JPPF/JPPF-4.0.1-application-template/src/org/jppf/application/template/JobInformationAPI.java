import org.jppf.application.template.TemplateApplicationRunner;

/**
 * This class provides a simplified window to the JPPF API focused on job submission and status.
 *
 */
public class JobInformationAPI
{
	private TemplateApplicationRunner jobRunner;

	public JobInformationAPI()
	{
		jobRunner = new TemplateApplicationRunner();
	}

	/**
	* @Returns the ID of the Job that is created
	*/
	public String submitTestJob(String desiredOutput, int secondsLong)
	{
		return "FAIL";
	}
	
	/*
	* @Returns the ID of the Job that is created
	*/
	public void submitBlenderJob(String[] dependencies, String[] nodeIPs)
	{
		TemplateApplicationRunner runner;
	}

	/*
	* @Returns "SUBMITTED", "PENDING", "EXECUTING", "COMPLETE", or "FAILED"
	*/
	public String getJobStatus(String jobID)
	{
		return "FAILED";
	}
}
