package morph;

import java.util.Arrays;
import java.lang.Math.*;

class Doc {
    int id = -1;
    String[] original = null;
    String[] std = null;
    String[] lemma = null;
    String[] pos = null;

    public Doc(int id, String[] original, String[] std, String[] lemma, String[] pos) {
	this.id = id;
	this.original = original;
	this.std = std;
	this.lemma = lemma;
	this.pos = pos;
    }

    public void truncate_self() {
	int count = original.length;
	int index = Math.min(count, 500);

        //Arrays.copyOfRange(t, 0, index); 
    }
}
