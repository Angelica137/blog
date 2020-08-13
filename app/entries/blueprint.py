from flask import Blueprint, render_template, request

from helpers import object_list
from models import Entry, Tag


def entry_list(template, query, **context):
    search = request.args.get('q')
    if search:
        query = query.filter((Entry.body.contains(search)) | (Entry.title.contains(search)))
    return object_list(template, query, **context)



entries = Blueprint('entries', __name__, template_folder='templates')


@entries.route('/')
def index():
    entries = Entry.query.order_by(Entry.created_timestamp.desc())
    return entry_list('entries/index.html', entries)


@entries.route('/tags/')
def tag_index():
    tags = Tag.query.order_by(Tag.name)
    return entry_list('entries/tag_index.html', tags)


@entries.route('/tags/<slug>')
def tag_detail(slug):
    pass


@entries.route('/<slug>')
def detail(slug):
    entry = Entry.query.filter(Entry.slug == slug).first_or_404()
    return render_template('entries/detail.html', entry=entry)