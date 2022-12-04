from flask import session, redirect, url_for, flash
from main import app


"""View de logout"""
@app.route('/logout')
def logout():
    if 'user_logged' in session or session['userlogged'] is not None:
        session['user_logged'] = None
        flash('nenhum usuário logado','warning')
        return redirect(url_for('index'))
    else:
        flash('NÃO EXISTE USUÁRIO LOGADO','error')
        return redirect(url_for('index'))
