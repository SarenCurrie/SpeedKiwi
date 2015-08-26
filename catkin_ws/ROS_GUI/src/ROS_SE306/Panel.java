package ROS_SE306;

import javax.swing.JPanel;


public class Panel extends JPanel {

	static Process runBashCommand(String cmd) throws Exception{
		ProcessBuilder s=new ProcessBuilder("/bin/bash", "-c",cmd);
		Process sProcess=s.start();
		return sProcess;
	}
	
	
}
