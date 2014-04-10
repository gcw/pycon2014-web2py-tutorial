db.define_table('messages',
                Field('body',
                      requires=IS_NOT_EMPTY(error_message="please have something to say")))
