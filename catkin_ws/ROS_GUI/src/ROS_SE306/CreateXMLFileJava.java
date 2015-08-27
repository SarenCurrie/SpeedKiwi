package ROS_SE306;

import java.io.File;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class CreateXMLFileJava {

	public static String xmlFilePath = "";
	public static String _treeHeight = "1.8";
	public static String _rowWidth = "3.5";
	public static String _rowNumber = "7";
	public static String _columnLength = "70";
	public static String _postSpacing = "5";
	
	public static void GenerateXML() {

		try {
			
			setDirectory();
			
			DocumentBuilderFactory documentFactory = DocumentBuilderFactory.newInstance();

			DocumentBuilder documentBuilder = documentFactory.newDocumentBuilder();

			Document document = documentBuilder.newDocument();

			// root element
			Element root = document.createElement("Configurations");
			document.appendChild(root);

			// treeHeight element
			Element treeHeight = document.createElement("Configure");
			treeHeight.appendChild(document.createTextNode(_treeHeight));
			treeHeight.setAttribute("name", "TreeHeight");
			root.appendChild(treeHeight);

			// rowWidth element
			Element rowWidth = document.createElement("Configure");
			rowWidth.appendChild(document.createTextNode(_rowWidth));
			rowWidth.setAttribute("name", "RowWidth");
			root.appendChild(rowWidth);	

			// rowNumber element
			Element rowNumber = document.createElement("Configure");
			rowNumber.appendChild(document.createTextNode( _rowNumber));
			rowNumber.setAttribute("name", "RowNumber");
			root.appendChild(rowNumber);	

			// columnLength element
			Element columnLength = document.createElement("Configure");
			columnLength.appendChild(document.createTextNode( _columnLength));
			columnLength.setAttribute("name", "ColumnLength");
			root.appendChild(columnLength);

			// postSpacing element
			Element postSpacing = document.createElement("Configure");
			postSpacing.appendChild(document.createTextNode(_postSpacing));
			postSpacing.setAttribute("name", "PostSpacing");
			root.appendChild(postSpacing);	

			// create the xml file
			//transform the DOM Object to an XML File
			Transformer tf = TransformerFactory.newInstance().newTransformer();
			tf.setOutputProperty(OutputKeys.INDENT, "yes");
			tf.setOutputProperty(OutputKeys.METHOD, "xml");
			tf.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");

			DOMSource domSource = new DOMSource(document);
			StreamResult streamResult = new StreamResult(new File(xmlFilePath));

			tf.transform(domSource, streamResult);

		} catch (ParserConfigurationException pce) {
			pce.printStackTrace();
		} catch (TransformerException tfe) {
			tfe.printStackTrace();
		}
	}
	
	public static void setDirectory() {
		String cwd = System.getProperty("user.dir");
		String upperFolder = cwd.substring(0, cwd.lastIndexOf("/"));
		xmlFilePath = upperFolder + "/src/speedkiwi_core/world/Generated_World/WorldVariables.xml";
	}
	
}
