class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None
        
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or 
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "users_db"
        return None
    

class NewAppRouter:
    route_app_labels = {'newapp'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'newapp_db'
        return None
        
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'newapp_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or 
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "newapp_db"
        return None
    

class TestAppRouter:
    route_app_labels = {'testapp'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'testapp_db'
        return None
        
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'testapp_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or 
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "testapp_db"
        return None