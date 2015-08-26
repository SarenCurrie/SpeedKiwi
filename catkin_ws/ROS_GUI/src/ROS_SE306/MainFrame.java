package ROS_SE306;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;


/**
 * GUI for the ROS generation
 * 
 * @author Chester and Karen from Speedkiwi
 */

public class MainFrame extends JFrame {

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

		_topFeatures = new JPanel(new FlowLayout(FlowLayout.LEFT, 0, 0));
		_topFeatures.setPreferredSize(new Dimension(640,260));
		_topFeatures.setBackground(Color.LIGHT_GRAY);
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


		// Completing the Mainframe setup.
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setResizable(false);
		this.setVisible(true);
		pack();
	}

}
