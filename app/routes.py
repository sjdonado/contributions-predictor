from flask import render_template, session, Blueprint

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@main_bp.route('/')
def index():
  return render_template(
    'index.html',
    current_user = session.get('current_user'),
    username = '' if session.get('username') is None else session.get('username'),
    weeks = session.get('current_user')['weeks'] if session.get('current_user') else None
  )