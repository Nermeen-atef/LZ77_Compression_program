from search import match


def compress(text):
    tags = []
    current_position = 0

    while current_position < len(text):

        # Find the best match at current position
        tag_pos, tag_len = match(text, current_position)

        # No match
        if tag_len == 0:
            next_symbol = text[current_position]
            tags.append((0, 0, next_symbol))

            current_position += 1

        # Match found
        else:
            next_position = current_position + tag_len

            # Make sure there is a next symbol
            if next_position < len(text):
                next_symbol = text[next_position]
                tags.append((tag_pos, tag_len, next_symbol))

                current_position = next_position + 1

            else:
                # Match reaches the end of the text
                tags.append((tag_pos, tag_len, ''))
                current_position = next_position

    return tags