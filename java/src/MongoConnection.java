package morph;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

import com.google.gson.Gson; 
import com.mongodb.client.MongoDatabase; 
import com.mongodb.MongoClient; 
import com.mongodb.MongoCredential;  
import com.mongodb.ServerAddress; 

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
	MongoCredential credential = MongoCredential.createCredential(info.user, 
		info.database, info.pwd.toCharArray());
	MongoClient mongo = new MongoClient(new ServerAddress(info.host, info.port),
		Arrays.asList(credential));

	MongoDatabase database = mongo.getDatabase(info.database);
	return(database);
    }

    public void read_from_db() {
	// creates stream of the values from the 'raw' field for each doc in docs.
    }

    public void write_to_db() {
	    // need to update docs and docs.truncated
	    // add fields standardized, lemma, partofspeech, xml
	    // look up chandni's code
    }

    public static void main( String args[] ) {  
	MongoConnection con = new MongoConnection();
	MongoDatabase database = con.connect_to_db("../../mongo-credentials.json");
    } 
}
