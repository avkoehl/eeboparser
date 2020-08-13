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


public class Test
{
    String latinWordsFileName = "./morphadorner-data/resources/latinwords.txt";
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

    public String standardize_spelling(String word, String pos, SpellingStandardizer speller) {
	String std = "";
	if ( this.tags.isProperNounTag(pos) || this.tags.isNounTag(pos) ||
		CharUtils.hasInternalCaps(word) || this.tags.isForeignWordTag(pos) ||
		this.tags.isNumberTag(pos) ) {
		}
	else
	{
	    std    =
		speller.standardizeSpelling
		(
		 word,
		 tags.getMajorWordClass(pos)
		);
	}
	return(std);
    }

    public static void main( String[] args)
    {
	String raw = "This is a couple of sentences. Please adorn them";
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

	Test test = new Test();
	settings = test.load_settings(settings, logger);
	test.initializer(settings, logger);

	List<List<String>> sentences = test.splitter.extractSentences(raw, test.tokenizer);

	List<List<AdornedWord>> result = test.tagger.tagSentences(sentences);

	String lemma = "";
	String std = "";
	String original = "";
	String pos = "";
	AdornedWord adorned_word;

	Iterator<List<AdornedWord>> iterator = result.iterator();

	// iterate through tagged sentences to get lemma,std,pos, original
	while (iterator.hasNext()) {
	    List<AdornedWord> sentence = iterator.next();
	    for (int i = 0; i < sentence.size(); i++)
	    {
		adorned_word = sentence.get(i);
		original = adorned_word.getToken();
		pos = adorned_word.getPartsOfSpeech();
		std = test.speller.standardizeSpelling(
			adorned_word.getSpelling() ,
			test.tags.getMajorWordClass(pos));


		std = test.standardize_spelling(std, pos, test.speller);
		std = test.map.mapSpelling(std);
		System.out.println(original + " " + pos + " " + " " + std);

	    }//for each word
	}//while sentences
    }
}

