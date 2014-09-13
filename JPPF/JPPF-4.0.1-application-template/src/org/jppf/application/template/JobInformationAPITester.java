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
		
		//testSubmitTestJob();
		//testSubmitBlenderJob();
		//testGetJobStatus();
		//testCancelJob();	
		//testGetTotalTasks();
		//testGetNumCompleteTasks();
		//testSubmitRandomizedTestJob();
		testGetTaskStatuses();
	}	
	
	public static void testSubmitTestJob()
	{
		System.out.println("Testing submitTestJob\n");
		
		String jobID = "FAIL";
		try
		{
			jobID = api.submitTestJob("Test Output", 5, 3);
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
			jobID = api.submitTestJob("Test Output", 5, 3);
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
		System.out.println("Testing cancelJob()");
		
		String jobID = "";
		try
		{
			jobID = api.submitTestJob("Test Output", 10, 1);
		}
		catch(Exception e)
		{
			System.out.println("FAIL, threw an exception");
		}		
		
		if(api.cancelJob(jobID) == false)
		{
			System.out.println("FAIL, could not cancel a job");		
		}
	}

	public static void testGetTotalTasks()
	{
		System.out.println("Testing getTotalTasks()");
		int NUMTASKS = 3;
		int WAITTIME = 5;
		
		String jobID = "";
		try
		{
			jobID = api.submitTestJob("Testing getTotalTasks()", WAITTIME, NUMTASKS);
		}
		catch(Exception e)
		{
			System.out.println("FAIL, threw an exception");
		}
	
		int numTasks = api.getTotalTasks(jobID);
		
		if(numTasks != NUMTASKS)
		{
			System.out.println("FAIL, returned the wrong number of tasks: " + numTasks);		
		}
	}

	public static void testGetNumCompleteTasks()
	{
		System.out.println("Testing getNumCompleteTasks()");
		
		String jobID = "";
		try
		{
			jobID = api.submitTestJob("Testing getNumCompleteTasks()", 5, 20);
		}
		catch(Exception e)
		{
			System.out.println("FAIL, threw an exception");
		}
	
		assert(api.getNumCompleteTasks(jobID) == 0);
		
		// Uncomment this code if you want to see it change in real time
		/*
		while(true)
		{
			try 
			{
    			Thread.sleep(1000);
			}
			catch (InterruptedException e) 
			{
    			e.printStackTrace();
			}
			System.out.println(api.getNumCompleteTasks(jobID));
		}
		*/
	}

	public static void testSubmitRandomizedTestJob()
	{
		System.out.println("Testing SubmitRandomizedTestJob()");
		
		String jobID = "";
		try
		{
			jobID = api.submitRandomizedTestJob("Testing SubmitRandomizedTestJob()", 5, 20);
		}
		catch(Exception e)
		{
			System.out.println("FAIL, threw an exception");
		}
	
		// Uncomment this code if you want to see it change in real time
		/*
		while(true)
		{
			try 
			{
    			Thread.sleep(1000);
			}
			catch (InterruptedException e) 
			{
    			e.printStackTrace();
			}
			System.out.println(api.getNumCompleteTasks(jobID));
		}
		*/
		
	}

	public static void testGetTaskStatuses()
	{
		System.out.println("Testing getTaskStatuses()");
		
		String jobID = "";
		try
		{
			jobID = api.submitRandomizedTestJob("Testing SubmitRandomizedTestJob()", 5, 20);
		}
		catch(Exception e)
		{
			System.out.println("FAIL, threw an exception");
		}
	
		// Uncomment this code if you want to see it change in real time
		
		while(true)
		{
			try 
			{
    			Thread.sleep(1000);
			}
			catch (InterruptedException e) 
			{
    			e.printStackTrace();
			}

			for(String s : api.getTaskStatuses(jobID))
			{
				System.out.println(s + ",");
			}
		}
		
	}
}