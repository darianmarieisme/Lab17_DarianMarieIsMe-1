'''Lab 17 Programming Assignment 1
Darian Marie Bruce
This program modifies a base script to
refactor and handle crashing
05/14/2026'''

from operator import itemgetter

import requests

def get_top_story_ids() -> list[int]:
    '''get the the ids for the current top stories on hacker news
    '''
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url)
    print(f"Status code: {r.status_code}")

    return r.json()

def get_submission_dict(submission_id: int) -> dict[str, str | int]:
    '''Build and return a dictionary containing data for one Hacker 
    News article'''


    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    response_dict = r.json()

    try:
        comments = response_dict['descendants']
    except KeyError:
        comments = 0

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': comments,
    }

    return submission_dict

def get_submission_dicts(submission_ids: list[int]) -> list[dict[str, str | int]]:
    '''Build and return a list of dictionaries for the first 30 Hacker
    News articles.'''

    submission_dicts = []

    for submission_id in submission_ids[:30]:
        submission_dict = get_submission_dict(submission_id)
        submission_dicts.append(submission_dict)

    return submission_dicts

def print_submissions(submission_dicts: list[dict[str, str | int]]) -> None:
    '''Print each article's title, discussion link, and number of comments'''
    
    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")

def main() -> None:
    '''Get, sort, and print the top Hacker News submissions.'''

    submission_ids = get_top_story_ids()
    submission_dicts = get_submission_dicts(submission_ids)

    submission_dicts = sorted(
        submission_dicts,
        key = itemgetter("comments"),
        reverse = True
    )

    print_submissions(submission_dicts)

main()