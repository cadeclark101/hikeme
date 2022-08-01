const fs = require('fs')
const sqlite3 = require('sqlite3').verbose();                                                                                                                                           
const db = new sqlite3.Database('/hikeme/hikeme_database.sqlite3');  

function Person(id, first_name, last_name, contact_number, emergency_contact_number, address, Trail, Status) {
    this.id = id;
    this.first_name = first_name;
    this.last_name = last_name;
    this.contact_number = contact_number;
    this.emergency_contact_number = emergency_contact_number;
    this.address = address;
    this.current_trail = Trail;
    this.current_status = Status;
};

function Status(id, status) {
    this.id = id;
    this.status = status;
};

function Trail_Warning(id, warning_info, warning_rating) {
    this.id = id;
    this.warning_info = warning_info;
    this.warning_rating = warning_rating;
};

function Trail(id, name) {
    this.id = id;
    this.name = name;
};

function Trail_Checkpoint(id, name, Trail, warning) {
    this.id = id;
    this.name = name;
    this.Trail = {Trail};
    this.warnings = {warning};
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
    db.run('INSERT INTO hikeme_app_person(id, first_name, last_name, contact_number, emergency_contact_number, address, current_trail_id, current_status_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', [Person.id, Person.first_name, Person.last_name, Person.contact_number, Person.emergency_contact_number, Person.address, Person.current_trail.id, Person.current_status.id], function(err) {
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
    db.run('INSERT INTO hikeme_app_status(id, status) VALUES(?, ?)', [Stats.id, Status.status], function(err) {
        if (err) {
            return console.log(err.message);
          }
          console.log(`A Status has been inserted with Status.id ${this.lastID}`);
    });
};

var status1 = new Status(1,"okay");
var trail1 = new Trail(1,"trail1");
var person1 = new Person(1,"person1","person1",123,321,"cm21 9bb", trail1, status1);

addTrail(trail1);
addPerson(person1);
db.close();

