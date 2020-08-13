package morph;

import java.nio.file.*;
import java.io.*;
import java.util.*;
import java.nio.charset.StandardCharsets;
import java.util.stream.Stream;

import edu.northwestern.at.morphadorner.MorphAdorner;
import com.mongodb.client.MongoDatabase; 

import morph.MongoConnection;
import morph.AdornString;

public class AdornDocsParallel 
{
    public static void main( String[] args)
    {
	MongoConnection con = new MongoConnection();
	MongoDatabase db = con.connect_to_db("../mongo-credentials.json");

	// create docs list
	

	// load data from mongodbcollection into docs list

	// convert docs list to Stream

	// parallel call AdornDocs

	// delete collections

	// write to collections

	String raw = "This is a couple of sentences. Please adorn them";
	AdornString adorner = new AdornString();
	adorner.adorn_string(raw);
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
