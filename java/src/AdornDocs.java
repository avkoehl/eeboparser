package morph;

import java.nio.file.*;
import java.io.*;
import java.util.*;
import java.nio.charset.StandardCharsets;
import java.util.stream.Stream;

import edu.northwestern.at.morphadorner.MorphAdorner;
import com.mongodb.client.FindIterable; 
import com.mongodb.client.MongoDatabase; 
import com.mongodb.client.MongoCollection; 
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.UpdateOptions; 
import static com.mongodb.client.model.Filters.eq;
import org.bson.Document;

import morph.MongoConnection;
import morph.StringAdorn;

public class AdornDocs 
{
    public boolean check_database(int id, MongoDatabase db) {
	// if already adorned return true; else return false 
	// if lemma, assume it exists in the others..
	Document l = db.getCollection("docs.lemma")
	    .find(Filters.eq("_id", id)).first();

	if (l != null) {
	    if (!l.getString("lemma").isEmpty()) {
	        return true;
	    }
	}
	return false;
    }

    public void write_documents(int id, ArrayList<String> lemma, 
	    ArrayList<String> pos, ArrayList<String> std,
	    ArrayList<String> original, MongoDatabase db) {

	Document ld = new Document();
	ld.append("lemma", String.join("\t", lemma)).append("_id", id);
	db.getCollection("docs.lemma").deleteOne(Filters.eq("_id", id));
	db.getCollection("docs.lemma").insertOne(ld);

	// write to docs.pos
	Document pd = new Document();
	pd.append("pos", String.join("\t", pos)).append("_id", id);
	db.getCollection("docs.pos").deleteOne(Filters.eq("_id", id));
	db.getCollection("docs.pos").insertOne(pd);

	// write to docs.std
	Document sd = new Document();
	sd.append("std", String.join("\t", std)).append("_id", id);
	db.getCollection("docs.std").deleteOne(Filters.eq("_id", id));
	db.getCollection("docs.std").insertOne(sd);

	// add fields to docs.truncated (std, lemma, pos)
	int index = Math.min(500, original.size());
	Document td = new Document();
	td.append("_id", id)
	    .append("lemma", String.join("\t", lemma.subList(0, index)))
	    .append("pos", String.join("\t", pos.subList(0, index)))
	    .append("std", String.join("\t", std.subList(0, index)))
	    .append("original", String.join("\t", original.subList(0, index)));
	db.getCollection("docs.truncated").deleteOne(Filters.eq("_id", id));
	db.getCollection("docs.truncated").insertOne(td);
    }

    public void write_empty_documents(int id, MongoDatabase db) {
	Document ld = new Document();
	ld.append("lemma", "").append("_id", id);
	db.getCollection("docs.lemma").deleteOne(Filters.eq("_id", id));
	db.getCollection("docs.lemma").insertOne(ld);

	Document pd = new Document();
	pd.append("pos", "").append("_id", id);
	db.getCollection("docs.pos").deleteOne(Filters.eq("_id", id));
	db.getCollection("docs.pos").insertOne(pd);

	Document sd = new Document();
	sd.append("std", "").append("_id", id);
	db.getCollection("docs.std").deleteOne(Filters.eq("_id", id));
	db.getCollection("docs.std").insertOne(sd);

	Document td = new Document();
	td.append("_id", id).append("std", "").append("lemma", "")
	    .append("pos", "").append("original", "");
	db.getCollection("docs.truncated").deleteOne(Filters.eq("_id",id));
	db.getCollection("docs.truncated").insertOne(td);
    }

    public void adorn_documents(StringAdorn adorner, 
	    ArrayList<Document> docs, 
	    MongoDatabase db) {

	// redo this
	docs.forEach((temp) -> {
	    int id = (int)temp.get("_id");
	    String text = temp.get("text").toString();
	    System.out.println("Processing doc " + String.valueOf(id));

	    if (text.isEmpty()) {
		this.write_empty_documents(id, db);
		System.out.println("... writing empty document");
		return;
	    }

	    if (this.check_database(id, db)) {
		System.out.println("... already in database, skipping");
		return;
	    }

	    try {
		ArrayList<String[]> result = adorner.adorn_string(text); 
		ArrayList<String> original = new ArrayList<String>();
		ArrayList<String> std = new ArrayList<String>();
		ArrayList<String> lemma = new ArrayList<String>();
		ArrayList<String> pos = new ArrayList<String>();

		for (int i = 0; i < result.size(); i++) {
		    original.add(result.get(i)[0]);
		    std.add(result.get(i)[1]);
		    lemma.add(result.get(i)[2]);
		    pos.add(result.get(i)[3]);

		}
		this.write_documents(id, lemma, pos, std, original, db);
	    }
	    catch (Exception e) {
		System.out.println(e.getMessage());
	    }
	});
    }

    public static void main( String[] args)
    {
	boolean overwrite = false;

	if (args.length != 0) {
	    if (args[0] == "--overwrite") {
		overwrite = true;
	    }
	}

	long heapMaxSize = Runtime.getRuntime().maxMemory() / 1000000;
	System.out.println(heapMaxSize);

	System.out.println("connecting to database");
	MongoConnection con = new MongoConnection();
	MongoDatabase db = con.connect_to_db("../mongo-credentials.json");
	System.out.println("reading data from database");
	ArrayList<Document> docs = con.read_from_db(db, "docs.text");

	System.out.println("initializing adorner");
	AdornDocs runner = new AdornDocs();
	StringAdorn adorner = new StringAdorn();

	System.out.println("Adorning documents");

	if (overwrite) {
	    MongoCollection<Document> lemmacol = db.getCollection("docs.lemma");
	    MongoCollection<Document> poscol = db.getCollection("docs.pos");
	    MongoCollection<Document> stdcol = db.getCollection("docs.std");
	    MongoCollection<Document> truncatedcol = db.getCollection("docs.truncated");
	    lemmacol.drop();
	    poscol.drop();
	    stdcol.drop();
	    truncatedcol.drop();
	}

	runner.adorn_documents(adorner, docs, db);
    }// main
}
