package morph;

import java.nio.file.*;
import java.io.*;
import java.util.*;
import java.nio.charset.StandardCharsets;
import java.util.stream.Stream;

import edu.northwestern.at.morphadorner.MorphAdorner;
import com.mongodb.client.MongoDatabase; 
import com.mongodb.client.MongoCollection; 
import com.mongodb.client.model.Filters;
import org.bson.Document;

import morph.MongoConnection;
import morph.StringAdorn;

public class AdornDocsParallel 
{
    public void adorn_documents(StringAdorn adorner, 
	    ArrayList<Document> docs, 
	    MongoDatabase db) {

	    MongoCollection<Document> lemma = db.getCollection("docs.lemma");
	    MongoCollection<Document> pos = db.getCollection("docs.pos");
	    MongoCollection<Document> std = db.getCollection("docs.std");
	    MongoCollection<Document> truncated = db.getCollection("docs.truncated");
	    lemma.drop();
	    pos.drop();
	    std.drop();
	    truncated.drop();

	docs.forEach((temp) -> {
	    String id = temp.get("_id").toString();
	    String text = temp.get("text").toString();

	    ArrayList<String[]> result = adorner.adorn_string(text); 
	    String lemmastring = String.join(" ", result.get(0)); 
	    String posstring = String.join(" ", result.get(3));
	    String stdstring = String.join(" ", result.get(1));

	    System.out.println("-----------------");
	    System.out.println("text: " +text.substring(0, 100));
	    System.out.println("lemma: " + lemmastring.substring(0, 80));
	    System.out.println(posstring.substring(0, 80));
	    System.out.println("std: " + stdstring.substring(0, 80));

	    // write to docs.lemma
	    Document ld = new Document();
	    ld.append("lemma", String.join(" ", result.get(0)));
	    ld.append("_id", id);
	    lemma.insertOne(ld);


	    // write to docs.pos
	    Document pd = new Document();
	    ld.append("pos", String.join(" ", result.get(3)));
	    pd.append("_id", id);
	    pos.insertOne(pd);

	    // write to docs.std
	    Document sd = new Document();
	    ld.append("std", String.join(" ", result.get(1)));
	    sd.append("_id", id);
	    std.insertOne(sd);

	    // add fields to docs.truncated (std, lemma, pos)
	    int index = Math.min(500, result.get(0).length);
	    Document td = new Document();
	    td.append("_id", id);
	    td.append("lemma", Arrays.asList(Arrays.copyOfRange(result.get(0), 0, index)));
	    td.append("pos", Arrays.asList(Arrays.copyOfRange(result.get(3), 0, index)));
	    td.append("std", Arrays.asList(Arrays.copyOfRange(result.get(1), 0, index)));
	    truncated.insertOne(td);
	});
    }

    public static void main( String[] args)
    {
	MongoConnection con = new MongoConnection();
	MongoDatabase db = con.connect_to_db("../mongo-credentials.json");
	AdornDocsParallel runner = new AdornDocsParallel();
	StringAdorn adorner = new StringAdorn();

	ArrayList<Document> docs = con.read_from_db(db, "docs.text");
	runner.adorn_documents(adorner, docs, db);
    }// main
}
