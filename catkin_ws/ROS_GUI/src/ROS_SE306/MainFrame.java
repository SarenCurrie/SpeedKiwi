package ROS_SE306;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import javax.swing.ImageIcon;
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
	private JPanel _logoPanel;

	// Holds the user-friendly buttons.
	private JPanel _bigButtons; 

	// Series of big user-friendly buttons.
	private JButton _defaultButton; 
	private JButton _customButton; 
	private JButton _testButton;
	private URL _logoURL = getClass().getResource("Logo.png");

	// Singleton constructor.
	protected MainFrame(){

		_features = new JPanel(new FlowLayout(FlowLayout.LEFT, 0, 0));
		_features.setPreferredSize(new Dimension(540, 360));
		_features.setBackground(Color.DARK_GRAY);
		add(_features, BorderLayout.NORTH);

		final List<JTextField> fields = new ArrayList<JTextField>();
		
		String[] labels = {"Tree height: ", "Row width: ", "Number of rows: ", "Column Length: ", "Post Spacing: "};
		int numPairs = labels.length;
		
		_topFeatures = new JPanel(new SpringLayout());
		_topFeatures.setPreferredSize(new Dimension(180,260));
		_topFeatures.setBackground(Color.LIGHT_GRAY);
		
		_logoPanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 0, 0));
		_logoPanel.setPreferredSize(new Dimension(360,260));
		
		ImageIcon _speedkiwi = new ImageIcon(_logoURL);
		JLabel _logoLabel = new JLabel("", _speedkiwi, JLabel.CENTER);
		_logoPanel.add(_logoLabel, BorderLayout.CENTER);
		
		for (int i = 0; i < numPairs; i++) {
		    JLabel l = new JLabel(labels[i], JLabel.TRAILING);
		    _topFeatures.add(l);
		    JTextField textField = new JTextField(10);
		    fields.add(textField);
		    l.setLabelFor(textField);
		    _topFeatures.add(textField);
		}

		//Lay out the panel.
		SpringUtilities.makeCompactGrid(_topFeatures,
		                                numPairs, 2, //rows, cols
		                                6, 6,        //initX, initY
		                                6, 6);       //xPad, yPad
		
		_features.add(_topFeatures, BorderLayout.NORTH);
		_features.add(_logoPanel, BorderLayout.NORTH);

		// A panel containing the three buttons: Default, Configure and Test
		_bigButtons = new JPanel(new GridLayout(1,3,0,0));
		_bigButtons.setPreferredSize(new Dimension(540,100));
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
					String cwd = System.getProperty("user.dir");
					String scriptFile = cwd + "/run1.sh";
					String cmd = scriptFile + " d 2>&1  ";
					System.out.println(execShell(cmd));
					execShell(cmd);
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
					CreateXMLFileJava._treeHeight = fields.get(0).getText();
					CreateXMLFileJava._rowWidth = fields.get(1).getText();
					CreateXMLFileJava._rowNumber = fields.get(2).getText();
					CreateXMLFileJava._columnLength = fields.get(3).getText();
					CreateXMLFileJava._postSpacing = fields.get(4).getText();
					CreateXMLFileJava.GenerateXML();
					String cwd = System.getProperty("user.dir");
					String scriptFile = cwd + "/run1.sh";
					String cmd = scriptFile + " c 2>&1  ";
					System.out.println(execShell(cmd));
					execShell(cmd);
					//runBashCommand("python src/speedkiwi_core/world/Generated_World/WorldConfiguration.py");
					//runBashCommand("roslaunch speedkiwi_core GeneratedLaunch.launch");	
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
					String cwd = System.getProperty("user.dir");
					String scriptFile = cwd + "/run1.sh";
					String cmd = scriptFile + " t 2>&1  ";
					System.out.println(execShell(cmd));
					execShell(cmd);
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


	public static String execShell(String command) {
		try {
			Process p = Runtime.getRuntime().exec(new String[]{"bash","-c",command});
			BufferedReader reader = 
				  new BufferedReader(new InputStreamReader(p.getInputStream()));

			StringBuilder sb = new StringBuilder();
            String line;
            while ((line = reader.readLine())!= null) {
                sb.append(line);
                sb.append("\n");
            }
			return sb.toString();
		} catch (Exception e) {
			return null;
		}

	}

}

