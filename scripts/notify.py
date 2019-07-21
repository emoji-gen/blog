#!/usr/bin/env python

import os
import sys
import slackweb

author_name = 'blog'
icon_url = 'https://i.imgur.com/FLjAA35.png'
username = 'CircleCI'


def main():
    message = sys.argv[1]
    if message == 'started':
        _notify('Deploy started', '#66d3e4')
    elif message == 'successful':
        _notify('Deploy successful', '#41aa58')
    elif message == 'failed':
        _notify('Deploy failed', '#d10c20')
    else:
        raise RuntimeError('invalid message')


def _notify(text, color):
    if 'CIRCLE_BUILD_URL' in os.environ:
        text += ' <{}|#{}>'.format(
            os.environ['CIRCLE_BUILD_URL'],
            os.environ['CIRCLE_BUILD_NUM']
        )

    slack = slackweb.Slack(url=os.environ['SLACK_INCOMING_WEBHOOK'])
    attachment = {
        'color': color,
        'text': text,
        'author_name': author_blog,
    }
    slack.notify(
        username=username,
        icon_url=icon_url,
        attachments=[attachment]
    )


if __name__ == '__main__':
    main()
