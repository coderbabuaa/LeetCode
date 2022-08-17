class Solution {
 public:
  int uniqueMorseRepresentations(vector<string>& words) {
    const vector<string> morse{
        ".-",   "-...", "-.-.", "-..",  ".",   "..-.", "--.",  "....", "..",
        ".---", "-.-",  ".-..", "--",   "-.",  "---",  ".--.", "--.-", ".-.",
        "...",  "-",    "..-",  "...-", ".--", "-..-", "-.--", "--.."};
      //Makes sure that only unnique elements stay
    unordered_set<string> transformations;

    for (const string& word : words) {
      string transformation;
      for (const char c : word)
        transformation += morse[c - 'a'];//gives correct index of char in morse
      transformations.insert(transformation);
    }

    return transformations.size();
  }
};
