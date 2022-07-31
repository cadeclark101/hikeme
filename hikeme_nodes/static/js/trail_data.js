function Trail_Warning(id, warning_info, warning_rating, datetime) {
    this.id = id;
    this.warning_info = warning_info;
    this.warning_rating = warning_rating;
    this.datetime = datetime;
};

function Trail_Info(id, name) {
    this.id = id;
    this.name = name;
};

function Trail_Checkpoint(id, name, trail_info, warning) {
    this.id = id;
    this.name = name;
    this.trail_info = {trail_info};
    this.warnings = {warning};
}

var coastalCliffsWarning = new Trail_Warning(0, "Coast Cliffs", 3, null);
var kentWarning = new Trail_Warning(1, "Avoid Kent!", null);

var trailCHKpt0Info = new Trail_Info(0, "Cleveland Way");
var trailCHKpt0 = new Trail_Checkpoint(0, "Filey", trailCHKpt0Info, {coastalCliffsWarning});
var trailCHKpt1 = new Trail_Checkpoint(1, "Saltburn-by-the-Sea", trailCHKpt1Info, {coastalCliffsWarning});
var trailCHKpt2 = new Trail_Checkpoint(2, "Helmsley", trailCHKpt1Info, {null: null});

var trailCHKpt1Info = new Trail_Info(1, "England Coastal Path", );
var trailCHKpt3 = new Trail_Checkpoint(3, "Minehead", trailCHKpt1Info, {null: null});
var trailCHKpt4 = new Trail_Checkpoint(4, "St Ives", trailCHKpt1Info, {null: null});
var trailCHKpt5 = new Trail_Checkpoint(5, "Brixham", trailCHKpt1Info, {null: null});
var trailCHKpt6 = new Trail_Checkpoint(6, "Poole", trailCHKpt1Info, {null: null});

var trailCHKpt2Info = new Trail_Info(2, "North Downs Way");
var trailCHKpt7 = new Trail_Checkpoint(3, "Dover", trailCHKpt2Info, {null: null});
var trailCHKpt8 = new Trail_Checkpoint(4, "Kent", trailCHKpt2Info, {kentWarning});
var trailCHKpt9 = new Trail_Checkpoint(5, "Otford", trailCHKpt2Info, {null: null});
var trailCHKpt10 = new Trail_Checkpoint(6, "Farnham", trailCHKpt2Info, {null: null});

console.log(trailCHKpt1.warnings);

