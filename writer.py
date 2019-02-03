#!/usr/bin/env python3


def report_writer(title, content):
    # Prepares text to be written to report, putting each row of content in a
    # separated line

    text = title + '\r\n\r\n'

    for row in content:
        text += str(row[0]) + ': ' + str(row[1]) + '\r\n'

    text += '\r\n\r\n'

    return text
