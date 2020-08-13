package morph;

import java.util.*;

import edu.northwestern.at.utils.*;
import edu.northwestern.at.morphadorner.MorphAdornerSettings;
import edu.northwestern.at.morphadorner.MorphAdornerLogger;
import edu.northwestern.at.morphadorner.MorphAdornerUtils;
import edu.northwestern.at.morphadorner.corpuslinguistics.adornedword.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.lexicon.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.partsofspeech.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.tokenizer.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.sentencesplitter.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.namestandardizer.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.lexicon.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.postagger.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.postagger.transitionmatrix.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.postagger.guesser.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.postagger.smoothing.contextual.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.postagger.smoothing.lexical.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.lemmatizer.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.spellingmapper.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.spellingstandardizer.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.namestandardizer.*;
import edu.northwestern.at.morphadorner.corpuslinguistics.namerecognizer.*;


public class AdornString
{
    String latinWordsFileName = "./morphadorner-data/resources/latinwords.txt";
    String lemmaSeparator="-";
    Names names = new Names();
    PartOfSpeechTagger tagger = null;
    SpellingStandardizer speller = null;
    Lemmatizer lemmatizer = null;
    SentenceSplitter splitter = null;
    WordTokenizer tokenizer = null;

    PartOfSpeechTags tags = null;
    PartOfSpeechRetagger retagger = null;
    PartOfSpeechGuesser guesser = null;
    ContextualSmoother csmoother1 = null;
    ContextualSmoother csmoother2 = null;
    LexicalSmoother lsmoother1 = null;
    LexicalSmoother lsmoother2 = null;

    PostTokenizer posttokenizer = null;
    WordTokenizer pretokenizer = null;
    Lexicon lexicon = null;
    Lexicon suffix_lexicon = null;
    TransitionMatrix mat = null;
    SpellingMapper map = null;
    NameStandardizer name_std = null;
    MorphAdornerSettings settings = null;
    MorphAdornerLogger logger = null;

    public AdornString() {
	MorphAdornerSettings settings = new MorphAdornerSettings();
	MorphAdornerLogger logger = null;
	try {
	    logger = new MorphAdornerLogger(
		    "./morphadorner-data/morphadornerlog.config",
		    "./morphadorner-data/log/",
		    settings);
	}
	catch (Exception e) {
	    e.printStackTrace();
	}
	settings = this.load_settings(settings, logger);
	this.initializer(settings, logger);
	this.settings = settings;
	this.logger = logger;
    }

    public MorphAdornerSettings load_settings(MorphAdornerSettings settings, 
	    MorphAdornerLogger logger) {
	String setting_args[] =  new String[14];
	setting_args[0] = "-p";
	setting_args[1] = "morphadorner-data/emeplaintext.properties";
	setting_args[2] = "-l";
	setting_args[3] = "morphadorner-data/data/emelexicon.lex";
	setting_args[4] = "-t";
	setting_args[5] = "morphadorner-data/data/emetransmat.mat";
	setting_args[6] = "-u";
	setting_args[7] = "morphadorner-data/data/emesuffixlexicon.lex";
	setting_args[8] = "-a";
	setting_args[9] = "morphadorner-data/data/ememergedspellingpairs.tab";
	setting_args[10] = "-s";
	setting_args[11] = "morphadorner-data/data/standardspellings.txt";
	setting_args[12] = "-w";
	setting_args[13] = "morphadorner-data/data/spellingsbywordclass.txt";

	settings.initializeSettings(logger);
	try {
	    settings.getSettings(setting_args);
	}
	catch (Exception e) {
	    e.printStackTrace();
	}
	return(settings);
    }

    public void initializer (MorphAdornerSettings settings, 
	    MorphAdornerLogger logger) {

	// adapted from MorphAdorner.initializeAdornment()

	// INIT
	tags = PartOfSpeechTagsFactory.newPartOfSpeechTags(settings.properties);
	tagger = PartOfSpeechTaggerFactory.newPartOfSpeechTagger(settings.properties);
	retagger = PartOfSpeechRetaggerFactory.newPartOfSpeechRetagger(settings.properties);
	guesser = PartOfSpeechGuesserFactory.newPartOfSpeechGuesser(settings.properties);
	csmoother1 = ContextualSmootherFactory.newContextualSmoother(settings.properties);
	csmoother2 = ContextualSmootherFactory.newContextualSmoother(settings.properties);
	lsmoother1 = LexicalSmootherFactory.newLexicalSmoother(settings.properties);
	lsmoother2 = LexicalSmootherFactory.newLexicalSmoother(settings.properties);

	tokenizer = WordTokenizerFactory.newWordTokenizer(settings.properties);
	pretokenizer = WordTokenizerFactory.newWordTokenizer(settings.properties);
	posttokenizer = PostTokenizerFactory.newPostTokenizer(settings.properties);

	try {
	    lexicon = MorphAdornerUtils.loadWordLexicon(settings, logger);
	    suffix_lexicon = MorphAdornerUtils.loadSuffixLexicon(settings, logger);
	    map = MorphAdornerUtils.createSpellingMapper(settings.properties);
	}
	catch (Exception e) {
	    e.printStackTrace();
	}


	lemmatizer = LemmatizerFactory.newLemmatizer(settings.properties);
	splitter = SentenceSplitterFactory.newSentenceSplitter(settings.properties);


	// SPAGHETTI
	tagger.setPostTokenizer(posttokenizer);
	retagger.setPostTokenizer(posttokenizer);
	csmoother1.setPartOfSpeechTagger(tagger);
	csmoother2.setPartOfSpeechTagger(retagger);
	lsmoother1.setPartOfSpeechTagger(tagger);
	lsmoother2.setPartOfSpeechTagger(retagger);
	tagger.setContextualSmoother(csmoother1);
	tagger.setLexicalSmoother(lsmoother1);
	retagger.setContextualSmoother(csmoother2);
	retagger.setLexicalSmoother(lsmoother2);
	tagger.setRetagger(retagger);

	lexicon.setPartOfSpeechTags(tags);
	guesser.setCheckPossessives(true);
	guesser.setWordLexicon(lexicon);
	guesser.setSuffixLexicon(suffix_lexicon);
	guesser.addAuxiliaryWordList
	    (
	     new TaggedStringsSet
	     (
	      names.getPlaceNames().keySet(),
	      tags.getSingularProperNounTag()
	     )
	    );
	guesser.addAuxiliaryWordList(
		new TaggedStringsSet(
		    names.getFirstNames(),
		    tags.getSingularProperNounTag())
		);
	guesser.addAuxiliaryWordList(
		new TaggedStringsSet(
		    names.getSurnames(),
		    tags.getSingularProperNounTag())
		);
	guesser.addAuxiliaryWordList(
		MorphAdornerUtils.getWordList(
		    latinWordsFileName,
		    tags.getForeignWordTag("latin"),
		    "loaded_latin_words",
		    settings,
		    logger)
		);

	tagger.setPartOfSpeechGuesser(guesser);
	tagger.setLexicon(lexicon);

	try {
	    MorphAdornerUtils.loadTaggerRules(tagger, settings, logger);
	    mat = MorphAdornerUtils.loadTransitionMatrix(tagger, settings, logger);
	    name_std = MorphAdornerUtils.createNameStandardizer(lexicon, settings, logger);
	    speller = MorphAdornerUtils.createSpellingStandardizer(lexicon, names, settings, logger);
	}
	catch (Exception e) {
	    e.printStackTrace();
	}

	lemmatizer.setLexicon(lexicon);
	lemmatizer.setDictionary(speller.getStandardSpellings());
    }

    public String standardize_spelling(String word, String pos) {
	String std = "";
	if (! ( this.tags.isProperNounTag(pos) || this.tags.isNounTag(pos) ||
		    CharUtils.hasInternalCaps(word) || this.tags.isForeignWordTag(pos) ||
		    this.tags.isNumberTag(pos) )) {
	    std = this.speller.standardizeSpelling(word,tags.getMajorWordClass(pos));
		    }
	return(std);
    }

    public String lemmatize(String word, String pos) {
	String lemma = word;
	String lemmaClass = this.tags.getLemmaWordClass(pos);
	if (!(this.lemmatizer.cantLemmatize(word) || lemmaClass.equals("none"))) {
	    lemma = this.lemmatizer.lemmatize(word, "compound");
	    if (lemma.equals(word)) {
		List wordList = this.tokenizer.extractWords(word);
		if (!this.tags.isCompoundTag(pos) || wordList.size() == 1) {
		    if (lemmaClass.length() == 0) {
			lemma = this.lemmatizer.lemmatize(word);
		    }
		    else {
			lemma = this.lemmatizer.lemmatize(word, lemmaClass);
		    }
		}
		else {
		    lemma = "";
		    String lemmaPiece = "";
		    String[] posTags = this.tags.splitTag(pos);
		    if (posTags.length == wordList.size()){
			for (int i = 0; i < wordList.size(); i++) {
			    String wordPiece = (String)wordList.get(i);
			    if (i > 0) {
				lemma = lemma + lemmaSeparator;
			    }
			    lemmaClass = this.tags.getLemmaWordClass(posTags[i]);
			    lemmaPiece = this.lemmatizer.lemmatize(wordPiece, lemmaClass);
			    lemma = lemma + lemmaPiece;
			}
		    }
		}
	    }
	}
	return (lemma);
    }

    public void adorn_string(String raw) {
	// class needs to be initialized!
	List<List<String>> sentences = this.splitter.extractSentences(raw, this.tokenizer);
	int[] sentence_and_word_count = MorphAdornerUtils.getWordAndSentenceCounts( sentences );
	int wc = sentence_and_word_count[1];

	List<List<AdornedWord>> result = this.tagger.tagSentences(sentences);

	String lemma = "";
	String std = "";
	String original = "";
	String pos = "";
	AdornedWord adorned_word;

	String[] lemmas = new String[wc];
	String[] stds = new String[wc];
	String[] originals = new String[wc];
	String[] poss = new String[wc];

	Iterator<List<AdornedWord>> iterator = result.iterator();

	// iterate through tagged sentences to get lemma,std,pos, original
	int count = 0;
	while (iterator.hasNext()) {
	    List<AdornedWord> sentence = iterator.next();
	    for (int i = 0; i < sentence.size(); i++)
	    {
		adorned_word = sentence.get(i);
		original = adorned_word.getToken();
		pos = adorned_word.getPartsOfSpeech();
		std = this.speller.standardizeSpelling(
			adorned_word.getSpelling() ,
			this.tags.getMajorWordClass(pos));

		std = this.standardize_spelling(std, pos);
		std = this.map.mapSpelling(std);
		lemma = this.lemmatize(adorned_word.getSpelling(), pos);
		lemmas[i] = lemma;
		stds[i] = std;
		originals[i] = original;
		poss[i] = pos;
		System.out.println(original + " " + pos + " " + lemma + " " + std);
	    }//for each word
	}//while sentences
    }

    public static void main( String[] args)
    {
	String raw = "This is a couple of sentences. Please adorn them";
	AdornString adorner = new AdornString();
	adorner.adorn_string(raw);

    }
}
