# set all the components
class NextionApp:

    # initialization of the components used in device

    def __init__(self):
        self.pages = [
            {'id': 0, 'name': 'initial',
             'components': [
                 {'id': 1, 'type': 'text', 'name': 'txt_temp'},
                 {'id': 2, 'type': 'button', 'name': 'bt_stop'}
             ]}
        ]
##  function get page ID and component ID, based on the names of page and component in the class
def get_Ids(pageName, compName):
   for element in NextionApp().pages:
       if element['name'] == pageName:
           pag_id = element['id']
           for component in element['components']:
               if component['name'] == compName:
                   comp_id = component['id']
                   return pag_id, comp_id

# ###INITIAL INPUTS from NEXTION by name
#initial page
ID_temp = get_Ids('initial', 'txt_temp')
