from app import app
from flask import render_template

@app.route('/')
def landing():
    home = [{'img': 'https://www.bls.gov/spotlight/2017/sports-and-exercise/images/cover_image.jpg'}]
    return render_template('index.html', img=home)

@app.route('/things')
def things():
    people = [
        {'person': 'Cristiano Ronaldo' ,'img':'https://the18.com/sites/default/files/styles/feature_image_with_focal/public/feature-images/20180402-The18-Image-CR7-afraid.jpg?itok=9nQSwR-j', 'sport': 'soccer'},
        {'person': 'Tiger Woods','img':'https://i.dailymail.co.uk/i/pix/2017/05/30/01/40EA963A00000578-4552628-Tiger_Woods_was_arrested_on_Monday_in_Jupiter_Florida_on_a_charg-a-47_1496103464003.jpg', 'sport': 'golf'},
        {'person': 'Michael Phelps','img':'https://ca-times.brightspotcdn.com/dims4/default/ba59cdc/2147483647/strip/true/crop/311x512+0+0/resize/840x1383!/format/webp/quality/90/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F86%2F26%2F83d4695be4535aec94d1dd326aa4%2Fsdut-in-this-file-photo-provided-ke-20160828', 'sport': 'swimming'},
        {'person': 'Tom Brady','img':'https://cdn.bleacherreport.net/images_root/slides/photos/000/983/739/tom-brady-seriously-wore-this-to-the-kentucky-derby_original_display_image.jpg?1306982366', 'sport': 'football'}, 
        {'person': 'Lewis Hamilton','img':'https://upload.wikimedia.org/wikipedia/commons/1/18/Lewis_Hamilton_2016_Malaysia_2.jpg', 'sport': 'racing'}]
    return render_template('index.html', names=people)
