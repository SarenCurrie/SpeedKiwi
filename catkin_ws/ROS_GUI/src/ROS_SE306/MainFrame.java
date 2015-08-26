package ROS_SE306;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SpringLayout;

import layout.SpringUtilities;


/**
 * GUI for the ROS generation
 * 
 * @author Chester and Karen from Speedkiwi
 */

public class MainFrame extends JFrame{

	// Holds the singleton instance.
	private static MainFrame _mainFrameInstance = null;

	// Makes sure only one singleton exists.
	public static MainFrame getInstance() {
		if(_mainFrameInstance == null) {
			_mainFrameInstance = new MainFrame();
		}
		return _mainFrameInstance;
	}

	// Main Panel/Pane(s)
	private JPanel _topFeatures;
	private JPanel _features;

	// Holds the user-friendly buttons.
	private JPanel _bigButtons; 

	// Series of big user-friendly buttons.
	private JButton _defaultButton; 
	private JButton _customButton; 
	private JButton _testButton;

	// Singleton constructor.
	protected MainFrame(){

		_features = new JPanel(new FlowLayout(FlowLayout.LEFT, 0, 0));
		_features.setPreferredSize(new Dimension(640, 360));
		_features.setBackground(Color.DARK_GRAY);
		add(_features, BorderLayout.NORTH);

		String[] labels = {"Tree height: ", "Row width: ", "Number of rows: ", "Column Length: ", "Post Spacing: "};
		int numPairs = labels.length;
		
		_topFeatures = new JPanel(new SpringLayout());
		_topFeatures.setPreferredSize(new Dimension(640,260));
		_topFeatures.setBackground(Color.LIGHT_GRAY);
		
		for (int i = 0; i < numPairs; i++) {
		    JLabel l = new JLabel(labels[i], JLabel.TRAILING);
		    _topFeatures.add(l);
		    JTextField textField = new JTextField(10);
		    l.setLabelFor(textField);
		    _topFeatures.add(textField);
		}

		//Lay out the panel.
		SpringUtilities.makeCompactGrid(_topFeatures,
		                                numPairs, 2, //rows, cols
		                                6, 6,        //initX, initY
		                                6, 6);       //xPad, yPad
		
		_features.add(_topFeatures, BorderLayout.NORTH);

		// A panel containing the three buttons: Default, Configure and Test
		_bigButtons = new JPanel(new GridLayout(1,3,0,0));
		_bigButtons.setPreferredSize(new Dimension(640,100));
		_bigButtons.setBackground(Color.LIGHT_GRAY);
		_features.add(_bigButtons, BorderLayout.SOUTH);


		// The buttons on the right.
		_defaultButton = new JButton("<html><center>Default<br>World</center></html");
		_customButton = new JButton("<html><center>Custom<br>World</center></html");
		_testButton = new JButton("<html><center>Test<br>World</center></html");

		// Adding the circle buttons.
		_bigButtons.add(_defaultButton, BorderLayout.CENTER);
		_bigButtons.add(_customButton, BorderLayout.CENTER);
		_bigButtons.add(_testButton, BorderLayout.CENTER);


		// Run the default world
		_defaultButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent arg0) {
				try {
					
					//TODO
					// KAREN, these COMMANDS WONT RUN!
					String cwd = System.getProperty("user.dir");
					String upperFolder = cwd.substring(0, cwd.lastIndexOf("/"));
					System.out.println(upperFolder);
					//System.setProperty("user.dir", upperFolder);
					
					//runBashCommand("source devel/setup.bash");
					//runPython("src/speedkiwi_core/world/Default_World/WorldConfiguration.py");
					//runBashCommand("roslaunch speedkiwi_core DefaultLaunch.launch");	
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

			}
		});

		// Run the configured world
		_customButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent arg0) {
				try {
					runBashCommand("python src/speedkiwi_core/world/Generated_World/WorldConfiguration.py");
					runBashCommand("roslaunch speedkiwi_core GeneratedLaunch.launch");	
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

			}
		});

		// Run the tests
		_testButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent arg0) {
				try {
					runBashCommand("python src/speedkiwi_core/world/Default_World/WorldConfiguration.py");
					runBashCommand("roslaunch speedkiwi_core DefaultLaunch.launch");	
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

			}
		});

		// Completing the Mainframe setup.
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setResizable(false);
		this.setVisible(true);
		this.setTitle("World Configuration Settings");
		pack();
	}


	static Process runBashCommand(String cmd) throws Exception{
		ProcessBuilder s = new ProcessBuilder("/bin/bash", "-c",cmd);
		Process sProcess=s.start();
		return sProcess;
	}
	
	static Process runPython(String fileName) throws Exception {
		ProcessBuilder pb = new ProcessBuilder("python", fileName);
		Process process = pb.start();
		return process;
	}

}

