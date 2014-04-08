package org.jppf.application.template;

import org.jppf.application.template.JobInformationAPI;

import java.net.InetAddress; 

import org.apache.xmlrpc.common.TypeConverterFactoryImpl;
import org.apache.xmlrpc.server.XmlRpcServer; 
import org.apache.xmlrpc.server.XmlRpcServerConfigImpl; 
import org.apache.xmlrpc.webserver.WebServer; 
import org.apache.xmlrpc.server.*;

public class Main
{	
	public static void main(String[] args) throws Exception
	{

		WebServer webServer = new WebServer(8080, InetAddress.getByName("127.0.0.1")); 
        
        XmlRpcServer xmlRpcServer = webServer.getXmlRpcServer(); 
        
        /*DynamicHandlerMapping dhm = new DynamicHandlerMapping(new TypeConverterFactoryImpl(), true); 
    
        // add "Calculator" handler - used by regular agent 
        dhm.addHandler("jobs", JobInformationAPI.class);
        xmlRpcServer.setHandlerMapping(dhm); 
        
        XmlRpcServerConfigImpl serverConfig = (XmlRpcServerConfigImpl) xmlRpcServer.getConfig(); 
        serverConfig.setEnabledForExtensions(true); 
        serverConfig.setContentLengthOptional(false);
*/
        webServer.start(); 

		//JobInformationAPITester.testJobInformationAPI();
		
		//System.exit(0);
	}
}