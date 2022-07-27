const trail_warnings =[
    {
        id: 1,
        warning_info: "Muddy.",
        warning_severity_rating: 1
    },
    {
        id: 2,
        warning_info: "Coastal Cliffs.",
        warning_severity_rating: 3
    }
]

const trail_authority =[
    {
        id: 1,
        authority_name: "Cleveland Mountain Rescue Team.",
        authority_contact_number: "999"
    }
]

const trail_infos =[
    {
        id: 1,
        trail_name: "Cleveland Way.",
        length: "177",
        warnings: [trail_warnings[0], trail_warnings[1]],
    }
]

const trail_checkpoints = [
    { 
        id: 1, 
        info: trail_infos[0],
        authority: trail_authority[0]
    }
]

module.exports = trail_checkpoints