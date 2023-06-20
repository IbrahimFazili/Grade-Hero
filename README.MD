# Grade Hero

To run it, you'll need to be in the virtual env in one console in the root directory

```
source venv/bin/activate
```


## Running backend

to run the backend in the virtual console, navigate to the backend folder and run the command

```
flask --app main.py --debug run
```

this will run it in hot reload (no need to close the program and run it again unless new files are added)

## Running the front end

in another console, navigate to the frontend/grade-hero-front-end folder and run 

```
npm install
```

to make sure you have all the modules. Then run 

```
npm run dev
```

You can register an account right now but not much done yet

## TODO

### Front End
- need to create the hover effect for selection
- need to work on the upload to send to Mongo + create a random colour not white for now at least
- need to figure out how to render the grade
- and more
...

### Back End
- need to create routes for uploading courses to reflect in db
- and more ...
