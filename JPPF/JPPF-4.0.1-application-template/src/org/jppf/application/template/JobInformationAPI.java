import org.jppf.application.template.TemplateApplicationRunner;
import org.apache.xmlrpc.server.*;

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
