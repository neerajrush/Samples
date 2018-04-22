extern void FoundWord(const char *start, int len);

/* Words consist of letters only. Everything else is a word delimiter */
extern int isalpha(int c);

/* No words will ever be longer than this: */
#define MAX_WORD_LENGTH 32


typedef struct
{

int  word_found;    // 0 or non-zero as flag:
unsigned int pos;   // pos initiazed with 0 .. first pos of word.
char l_chars[MAX_WORD_LENGTH];  // all the chars read so far.

} MyData;
/* MyData contents will be all 0 before first call to StateMachine() */

#if 0
Hi there, world!
#endif

/* Don’t worry about error handling */
void StateMachine(MyData *state, char c)
{
    if (state->pos <= MAX_WORD_LENGTH+1) {
        if (isappha(c) == 0 && word_found == 0) {  
		if (state->pos <= MAX_WORD_LENGTH) {
			state->l_chars[state->pos++] = c;
		}
        } else {
            // Found a word delimiter
	    state->word_found = 1;
	    FoundWord(state->l_char, state->pos);
	    state->word_found = 0;
            state->pos = 0;    
        }
    }
}

