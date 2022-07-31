function Trail_Warning(id, warning_info, warning_rating) {
    this.id = id;
    this.warning_info = warning_info;
    this.warning_rating = warning_rating;
};

function Trail_Info(id, name, warning) {
    this.id = id;
    this.name = name;
    this.warnings = {warning};
};

function Trail_Checkpoint(id, name, trail_info) {
    this.id = id;
    this.name = name;
    this.trail_info = {trail_info};
}

var coastalCliffsWarning = new Trail_Warning(0, "Coast Cliffs", 3);
var kentWarning = new Trail_Warning(1, "Avoid Kent!", 5);

var trailCHKpt0Info = new Trail_Info(0, "Cleveland Way", coastalCliffsWarning);
var trailCHKpt0 = new Trail_Checkpoint(0, "Filey", trailCHKpt0Info);
var trailCHKpt1 = new Trail_Checkpoint(1, "Saltburn-by-the-Sea", trailCHKpt1Info);
var trailCHKpt2 = new Trail_Checkpoint(2, "Helmsley", trailCHKpt1Info);

var trailCHKpt1Info = new Trail_Info(1, "England Coastal Path", coastalCliffsWarning);
var trailCHKpt3 = new Trail_Checkpoint(3, "Minehead", trailCHKpt1Info);
var trailCHKpt4 = new Trail_Checkpoint(4, "St Ives", trailCHKpt1Info);
var trailCHKpt5 = new Trail_Checkpoint(5, "Brixham", trailCHKpt1Info);
var trailCHKpt6 = new Trail_Checkpoint(6, "Poole", trailCHKpt1Info);

var trailCHKpt2Info = new Trail_Info(2, "North Downs Way", {kentWarning, coastalCliffsWarning});
var trailCHKpt7 = new Trail_Checkpoint(3, "Dover", trailCHKpt2Info);
var trailCHKpt8 = new Trail_Checkpoint(4, "Kent", trailCHKpt2Info);
var trailCHKpt9 = new Trail_Checkpoint(5, "Otford", trailCHKpt2Info);
var trailCHKpt10 = new Trail_Checkpoint(6, "Farnham", trailCHKpt2Info);



