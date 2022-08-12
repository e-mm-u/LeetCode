/**
 * @param {string[]} sentences
 * @return {number}
 */
 var mostWordsFound = function(sentences) {
    
    let len = sentences.length;
    let word_counts = 0;

    for(let i=0; i<len; i++){

        let sentence = sentences[i];
        let words = sentence.split(" ");

        let temp = words.length;

        word_counts = Math.max(word_counts,temp);
    }

    return word_counts;
};