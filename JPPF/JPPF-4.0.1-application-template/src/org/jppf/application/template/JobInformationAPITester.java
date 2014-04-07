package org.jppf.application.template;

import org.jppf.application.template.TemplateApplicationRunner;
import org.jppf.application.template.JobInformationAPI;
import org.jppf.client.*;
import org.jppf.node.protocol.Task;
import org.jppf.client.submission.*;

public class JobInformationAPITester
{
	private static JobInformationAPI api;
	
	public static void testJobInformationAPI()
	{
		api = new JobInformationAPI();			
		
		testSubmitTestJob();
		testSubmitBlenderJob();
		testGetJobStatus();
		testCancelJob();	
	}	
	
	public static void testSubmitTestJob()
	{
		System.out.println("Testing submitTestJob\n");
		
		String jobID = "FAIL";
		try
		{
			jobID = api.submitTestJob("Test Output", 5);
		}
		catch(Exception e)
		{
			System.out.println("FAIL, threw an exception");
		}	
		
	}

	public static void testSubmitBlenderJob()
	{

	}

	public static void testGetJobStatus()
	{
		System.out.println("Testing getJobStatus\n");
		
		String jobID = "FAIL";
		try
		{
			jobID = api.submitTestJob("Test Output", 5);
		}
		catch(Exception e)
		{
			System.out.println("FAIL, threw an exception");
			return;
		}	
		
		String status = api.getJobStatus(jobID);
		System.out.println("Status was: " + status);
	}

	public static void testCancelJob()
	{

	}


}