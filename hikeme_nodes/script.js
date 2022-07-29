function Trail_Warning(id, warning_info, warning_rating) {
    this.id = id;
    this.warning_info = warning_info;
    this.warning_rating = warning_rating;
};

function Trail_Info(id, name, warning) {
    this.id = id;
    this.name = name;
    this.warnings = warning;
};

function Trail_Checkpoint(id, name, trail_info) {
    this.id = id;
    this.name = name;
    this.trail_info = trail_info;
}

var test = new Trail_Warning(1, "test", 85);
console.log(test);
console.log(test);
