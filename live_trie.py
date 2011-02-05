
class LiveTrie:
    
    def __init__(self):
        self.start_state = 0L
        self.invalid_state = 200000L#how to obtain max unsigned long
        self.states = [{}]

    def add_letter(self, state, letter):
        
        states_count = len(self.states)
        
        if states_count <= state:
            return self.invalid_state
        
        target_state = self.states[state].get(letter, self.invalid_state)
        
        if target_state != self.invalid_state:
            return target_state
        
        ++states_count
        
        self.states[state][letter] = states_count
        self.states.append({})
        
        return states_count
    
    def transfer(self, state, letter):
        
        if len(self.states) <= state:
            return self.invalid_state
        
        return self.states[state].get(letter, self.invalid_state)
    
    def add_word(self, word):
        current_state = self.start_state
        
        for letter in word:            
            
            if current_state == self.invalid_state:
                return current_state
            
            current_state = self.add_letter(current_state, letter)
        
        return current_state
    
    def find_word(self, word):
        
        current_state = self.start_state
        
        for letter in word:            
            
            if current_state == self.invalid_state:
                return current_state
            
            current_state = self.transfer(current_state, letter)
        
        return current_state
    
