def match(text,current_position):
    start=0
    search_buffer=text[start:current_position]
    lookahead=text[current_position:]

    tag_pos=0
    tag_len=0

    for i in range(len(search_buffer)):
        pos=len(search_buffer)-i
        length=0

        while length<len(lookahead):
            src_index=current_position-pos+length

            if src_index>=current_position:
                src_index=current_position-pos+(length%pos)

            if text[src_index]!=lookahead[length]:
                break
            
            length+=1


            if length>tag_len:
                tag_len=length
                tag_pos=pos

         
    return tag_pos,tag_len





