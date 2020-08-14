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

    public Document adorn_doc(StringAdorn adorner, Document doc) {
	String raw = doc.get("raw").toString();
	ArrayList<String[]> results = adorner.adorn_string(raw);

	doc.append("lemma", Arrays.asList(results.get(0)));
	doc.append("std", Arrays.asList(results.get(1)));
	doc.append("raw", Arrays.asList(results.get(2)));
	doc.append("pos", Arrays.asList(results.get(3)));
	return (doc);
    }

    public void adorn_documents(StringAdorn adorner, 
	    ArrayList<Document> docs, 
	    MongoDatabase db,
	    String collection_name,
	    String truncated_collection_name) {
	docs.parallelStream().forEach((temp) -> {
	    Document d = this.adorn_doc(adorner, temp);

	    //MongoCollection<Document> collection = db.getCollection(collection_name);
	    //collection.replaceOne(Filters.eq("_id", d.get("_id")), d);
	});
    }

    public static void main( String[] args)
    {
	MongoConnection con = new MongoConnection();
	MongoDatabase db = con.connect_to_db("../mongo-credentials.json");
	AdornDocsParallel runner = new AdornDocsParallel();
	StringAdorn adorner = new StringAdorn();

	ArrayList<Document> docs = con.read_from_db(db, "docs");
	runner.adorn_documents(adorner, docs, db, "docs", "docs.truncated");
    }// main
}
