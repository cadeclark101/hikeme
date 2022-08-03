const fs = require('fs')
const sqlite3 = require('sqlite3').verbose();                                                                                                                                           
const db = new sqlite3.Database('/hikeme/hikeme_database.sqlite3');  

function Person(id, first_name, last_name, contact_number, emergency_contact_number, address, Trail_Checkpoint, Status) {
    this.id = id;
    this.first_name = first_name;
    this.last_name = last_name;
    this.contact_number = contact_number;
    this.emergency_contact_number = emergency_contact_number;
    this.address = address;
    this.current_trail_checkpoint = Trail_Checkpoint;
    this.current_status = Status;
};

function Status(id, status) {
    this.id = id;
    this.status = status;
};

function Trail_Warning(id, warning, warning_rating, Trail_Checkpoint) {
    this.id = id;
    this.warning = warning;
    this.warning_rating = warning_rating;
    this.Trail_Checkpoint = {Trail_Checkpoint};
};

function Trail(id, name) {
    this.id = id;
    this.name = name;
};

function Trail_Checkpoint(id, name, Trail) {
    this.id = id;
    this.name = name;
    this.Trail = {Trail};
}

function checkDatabaseExists() {
    const path = '/hikeme/hikeme_database.sqlite3'
    try {
    if (fs.existsSync(path)) {
        console.log("Found Hikeme database.")
    }
    } catch(err) {
    console.error(err)
    }
};

function addPerson(Person) {
    db.run('INSERT INTO hikeme_app_person(id, first_name, last_name, contact_number, emergency_contact_number, address, current_trail_checkpoint_id, current_status_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', [Person.id, Person.first_name, Person.last_name, Person.contact_number, Person.emergency_contact_number, Person.address, Person.current_trail_checkpoint.id, Person.current_status.id], function(err) {
        if (err) {
            return console.log(err.message);
          }
          console.log(`A Person has been inserted with Person.id ${this.lastID}`);
    });
};

function addTrail(Trail) {
    db.run('INSERT INTO hikeme_app_trail(id, name) VALUES(?, ?)', [Trail.id, Trail.name], function(err) {
        if (err) {
            return console.log(err.message);
          }
          console.log(`A Trail has been inserted with Trail.id ${this.lastID}`);
    });
};

function addStatus(Status) {
    db.run('INSERT INTO hikeme_app_status(id, status) VALUES(?, ?)', [Status.id, Status.status], function(err) {
        if (err) {
            return console.log(err.message);
          }
          console.log(`A Status has been inserted with Status.id ${this.lastID}`);
    });
};

function addTrailCheckPoint(Trail_Checkpoint) {
    db.run('INSERT INTO hikeme_app_trail_checkpoint(id, name, trail_id) VALUES(?, ?, ?)', [Trail_Checkpoint.id, Trail_Checkpoint.name, Trail_Checkpoint.Trail.id], function(err) {
        if (err) {
            return console.log(err.message);
          }
          console.log(`A Status has been inserted with Status.id ${this.lastID}`);
    });
};

function addWarning(Warning) {
    db.run('INSERT INTO hikeme_app_warning(id, warning, warning_rating, trail_checkpoint_id) VALUES(?, ?, ?)', [Warning.id, Warning.name, Warning.warning_rating, Warning.Trail_Checkpoint.id], function(err) {
        if (err) {
            return console.log(err.message);
          }
          console.log(`A Warning has been inserted with Warning.id ${this.lastID} onto Trail_Checkpoint with Trail_Checkpoint.id ${this.Trail_Checkpoint.id}`);
    });
};

function populateDB() {
    // This is only here because I keep deleting the SQLite file.
    var trail0 = new Trail(0, "Cleveland Way");
    var trail1 = new Trail(1, "England Coastal Path");
    var trail2 = new Trail(2, "North Downs Way");

    var trailCheckpoint0 = new Trail_Checkpoint(0, "Filey", 0);
    var trailCheckpoint1 = new Trail_Checkpoint(1, "Saltburn-by-the-Sea", 0);
    var trailCheckpoint2 = new Trail_Checkpoint(2, "Helmsley", 0);
    var trailCheckpoint3 = new Trail_Checkpoint(3, "Minehead", 1);
    var trailCheckpoint4 = new Trail_Checkpoint(4, "St Ives", 1);
    var trailCheckpoint5 = new Trail_Checkpoint(5, "Brixham", 1);
    var trailCheckpoint6 = new Trail_Checkpoint(6, "Poole", 1);
    var trailCheckpoint7 = new Trail_Checkpoint(7, "Dover", 2);
    var trailCheckpoint8 = new Trail_Checkpoint(8, "Kent", 2);
    var trailCheckpoint9 = new Trail_Checkpoint(9, "Otford", 2);
    var trailCheckpoint10 = new Trail_Checkpoint(10, "Farnham", 2);

    var status0 = new Status(0, "Good");
    var status1 = new Status(1, "Eh");
    var status2 = new Status(2, "Bad");

    var person0 = new Person(0, "Cade","Clark",123,321,"CM21 9BB", trail0, status0);
    var person1 = new Person(1, "Cerys","Murray",123,321,"SG18 8EJ", trail1, status1);
    var person2 = new Person(2, "Liam","Halpin",123,321,"AB12 3CD", trail2, status2);
}


//var status1 = new Status(1,"okay");
//var trail1 = new Trail(1,"trail1");
//var person1 = new Person(1,"person1","person1",123,321,"cm21 9bb", trail1, status1);
//addStatus(status1);
//addTrail(trail1);
//addPerson(person1);
db.close();

