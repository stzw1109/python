db.birds.deleteMany(
{
    sightings_count:{
        $lte: 10
        }
}

)