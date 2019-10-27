from .models import db


def add_instance(model, need_commit, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    if need_commit:
        commit()
    return instance


def delete_instance(model, _id, need_commit):
    model.query.filter_by(id=_id).delete()
    if need_commit:
        commit()


def edit_instance(model, _id, need_commit, **kwargs):
    instance = model.query.filter_by(id=_id).all()[0]
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    if need_commit:
        commit()
    return instance


def commit():
    db.session.commit()
