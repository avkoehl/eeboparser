package morph;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;

import com.google.gson.Gson; 
import com.mongodb.client.MongoDatabase; 
import com.mongodb.client.MongoCollection; 
import com.mongodb.client.MongoCursor;
import com.mongodb.MongoClient; 
import com.mongodb.MongoCredential;  
import com.mongodb.BasicDBObject;
import com.mongodb.DBCursor;
import com.mongodb.ServerAddress; 
import org.bson.Document;

public class MongoConnection { 

    static class CredentialsJSON {
	String database = "";
	String host = "";
	int port = -1;
	String user = "";
	String pwd = "";
    }

    public CredentialsJSON read_credentials(String filename) {
	Gson gson = new Gson();
	String json = new String();
	try {
	    json = new String(Files.readAllBytes(Paths.get(filename)), 
		    StandardCharsets.UTF_8);
	}
	catch (IOException e) {
	    e.printStackTrace();
	}
	CredentialsJSON credentials = gson.fromJson(json,
		CredentialsJSON.class);
	return(credentials);
    }

    public MongoDatabase connect_to_db(String filename) {
	CredentialsJSON info = read_credentials(filename);
	MongoClient mongo = new MongoClient(info.host, info.port);
	MongoCredential credential = MongoCredential.createCredential(info.user, 
		info.database, info.pwd.toCharArray());

	MongoDatabase database = mongo.getDatabase(info.database);
	return(database);
    }

    public ArrayList<Document> read_from_db(MongoDatabase db, String collection_name) {
	MongoCollection<Document> collection = db.getCollection(collection_name);
	MongoCursor<Document> cursor = collection.find().iterator();
	ArrayList<Document> docs = new ArrayList<Document>();
	try {
	    while (cursor.hasNext()) {
		docs.add(cursor.next());
	    }
	} finally {
	    cursor.close();
	}
	return(docs);
    }

    public void write_to_db(ArrayList<Document> docs, MongoDatabase db, String collection_name) {
	//probably not used
	MongoCollection<Document> collection = db.getCollection(collection_name);
	collection.drop();
	collection.insertMany(docs);
    }
}
