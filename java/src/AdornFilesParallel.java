package morph;

import java.nio.file.*;
import java.io.*;
import java.util.*;
import java.nio.charset.StandardCharsets;
import java.util.stream.Stream;
import edu.northwestern.at.morphadorner.MorphAdorner;

import morph.MongoConnection;
import com.mongodb.client.MongoDatabase; 

public class AdornFilesParallel 
{
    public static void adornFile (Path path, String odir, String dataroot)
    {
	String args[] =  new String[17];
	args[0] = "-p";
	args[1] = dataroot + "emeplaintext.properties";
	args[2] = "-l";
	args[3] = dataroot + "data/emelexicon.lex";
	args[4] = "-t";
	args[5] = dataroot + "data/emetransmat.mat";
	args[6] = "-u";
	args[7] = dataroot + "data/emesuffixlexicon.lex";
	args[8] = "-a";
	args[9] = dataroot + "data/ememergedspellingpairs.tab";
	args[10] = "-s";
	args[11] = dataroot + "data/standardspellings.txt";
	args[12] = "-w";
	args[13] = dataroot + "data/spellingsbywordclass.txt";
	args[14] = "-o";
	args[15] = odir;
	args[16] = path.toString();
	MorphAdorner.main(args);
    }

    public static void main( String[] args)
    {
	String idir = args[0];
	String odir = args[1];
	String dataroot = args[2];

	MongoConnection con = new MongoConnection();
	MongoDatabase db = con.connect_to_db("../../mongo-credentials.json");

	/*
	try { 
	    Stream<Path> files = Files.list(Paths.get(idir));
	    files.forEach(f -> 
		    { adornFile(
			f, odir, dataroot); }
		    );
	    files.close();
	} catch (IOException e) 
	{
	    e.printStackTrace();
	}
	*/
    }// main
}
