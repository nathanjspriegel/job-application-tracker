from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from .models import Application
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        company = request.form.get('company')
        position = request.form.get('position')
        status = request.form.get('status')
        date_applied = datetime.strptime(request.form.get('date_applied'), '%Y-%m-%d').date()
        link = request.form.get('link')
        note = request.form.get('note')

        new_application = Application(company=company, position=position, status=status, date_applied=date_applied, link=link, note=note, user_id=current_user.id)

        db.session.add(new_application)
        db.session.commit()
        flash('Application added!', category='success')
        return redirect(url_for('views.home'))
    
    return render_template("home.html", user=current_user)

@views.route('/delete-application/<int:id>', methods=['POST'])
@login_required
def delete_application(id):
    application = Application.query.get_or_404(id)

    if application.user_id != current_user.id:
        flash('You can not delete other\'s applications', category='error')
        return redirect(url_for('views.home'))

    db.session.delete(application)
    db.session.commit()
    flash('Application deleted.', category='success')
    return redirect(url_for('views.home'))