from website import create_app
''' import website package and grab the create_function, 'website' folder has become a python package 
due to having named "__init__.py'''
app = create_app()

if __name__ == '__main__': 
 app.run(debug=True)  
'''the reason for this is that this function will be executed 
only if we run the function and not merely open the file.'''