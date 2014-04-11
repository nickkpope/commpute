package org.jppf.application.template;

import org.jppf.application.template.JobInformationAPI;

import java.net.InetAddress; 

import org.apache.xmlrpc.common.TypeConverterFactoryImpl;
import org.apache.xmlrpc.server.XmlRpcServer; 
import org.apache.xmlrpc.server.XmlRpcServerConfigImpl; 
import org.apache.xmlrpc.webserver.WebServer; 
import org.apache.xmlrpc.server.*;
import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;
import java.net.URL;

public class Main
{	
	public static void main(String[] args) throws Exception
	{

            //JPPFXmlRpcServer server = new JPPFXmlRpcServer();

	    JobInformationAPITester.testJobInformationAPI();
		
	    //System.exit(0);
	}
}
