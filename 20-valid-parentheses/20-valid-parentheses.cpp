class Solution {
public:
    //Match opening with closing
    char closing(char c) {
        char tc;
        switch (c) {
            case ')':
                tc = '(';
                break;
            case ']':
                tc = '[';
                break;
            case '}':
                tc = '{';
                break;
        }
        return tc;
    }
    
    bool isValid(string s) {
        stack<char> st;
        for (int i = 0; i < s.size(); i++) {
            if (s.at(i) == '(' || s.at(i) == '[' || s.at(i) == '{')
                //if its an opening bracket push it to stack
                st.push(s[i]);
            if (s.at(i) == ')' || s.at(i) == ']' || s.at(i) == '}') {
                //If its a closing bracket match it with its corresponding opening bracket, if matched pop it from stack
                if (st.empty())
                    return false;
                if (st.top() == closing(s[i]))
                    st.pop();
                else
                    return false;
            }
        }
        if (!st.empty()) return false;
        else return true;
        }
};