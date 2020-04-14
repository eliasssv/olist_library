from django.db.models import ObjectDoesNotExist

### GENERICS METHODS TO TESTS ### 

def generic_setUp(objects_to_create):
    """
    Generic setUp
    \n@param objects_to_create : List of objects to save in database
    \n@since 2020-04-13
    \n@author eliasssv
    """
    for obj in objects_to_create:
        obj.save()

def generic_get(self, model, objects_to_get):
    """
    Generic Get
    \n@param model : Class of the model
    \n@param objects_to_create : List dict with:
        {
            search_field: name of the field search,
            search_value: value of the search field,
            compare_field: name of the field to compare,
            compare_value: value of the comparation,
        }
    \n@since 2020-04-13
    \n@author eliasssv
    """
    for obj in objects_to_get:
        kwargs = {}
        kwargs[obj['search_field']] = obj['search_value']
        db_obj = model.objects.get(**kwargs)
        self.assertEqual(eval(f"db_obj.{obj['compare_field']}"), obj['compare_value'])

def generic_delete(self, model, objects_to_delete):
    """
    Generic Delete
    \n@param objects_to_delete : List of objects to delete in database
    \n@since 2020-04-13
    \n@author eliasssv
    """
    for obj in objects_to_delete:
        obj.delete()
        with self.assertRaisesMessage(ObjectDoesNotExist,f'{type(obj).__name__} matching query does not exist.'):
            model.objects.get(id=obj.id)

