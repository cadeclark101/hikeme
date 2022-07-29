const trail_warnings =[
    {
        id: 0,
        warning_info: "Muddy.",
        warning_severity_rating: 1
    },
    {
        id: 1,
        warning_info: "Coastal Cliffs.",
        warning_severity_rating: 3
    }
]

const trail_authority =[
    {
        id: 0,
        authority_name: "Cleveland Mountain Rescue Team.",
        authority_contact_number: "999"
    },
    {
        id: 1,
        authority_name: "Mountain Rescue England and Wales.",
        authority_contact_number: "999"
    },
    {
        id: 2,
        authority_name: "Surrey Search and Rescue.",
        authority_contact_number: "999"
    }
]

const trail_infos =[
    {
        id: 0,
        trail_name: "Cleveland Way.",
        length: "177",
        warnings: [trail_warnings[0], trail_warnings[1]],
    },
    {
        id: 1,
        trail_name: "England Coast Path.",
        length: "4500",
        warnings: [trail_warnings[1]],
    },
    {
        id: 2,
        trail_name: "North Downs Way",
        length: "246",
        warnings: [trail_warnings[0]],
    }
]

const trail_checkpoints = [
    { 
        id: 0, 
        name: "Filey",
        info: trail_infos[0],
        authority: trail_authority[0]
    },
    { 
        id: 1, 
        name: "Saltburn-by-the-Sea",
        info: trail_infos[0],
        authority: trail_authority[0]
    },
    { 
        id: 2, 
        name: "Helmsley",
        info: trail_infos[0],
        authority: trail_authority[0]
    },
    { 
        id: 3, 
        name: "Minehead",
        info: trail_infos[1],
        authority: trail_authority[1]
    },
    { 
        id: 4, 
        name: "St Ives",
        info: trail_infos[1],
        authority: trail_authority[1]
    },
    { 
        id: 5, 
        name: "Brixham",
        info: trail_infos[1],
        authority: trail_authority[1]
    },
    { 
        id: 6,
        name: "Poole", 
        info: trail_infos[2],
        authority: trail_authority[2]
    },
    { 
        id: 7,
        name: "Dover", 
        info: trail_infos[2],
        authority: trail_authority[2]
    },
    { 
        id: 8, 
        name: "Kent",
        info: trail_infos[2],
        authority: trail_authority[2]
    },
    { 
        id: 9, 
        name: "Otford",
        info: trail_infos[2],
        authority: trail_authority[2]
    }
]

module.exports = trail_checkpoints