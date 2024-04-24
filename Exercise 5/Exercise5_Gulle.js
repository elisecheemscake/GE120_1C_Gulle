/* 
Exercise 4
Jo Elise G. Gulle
2023-06414
*/

//creating the needed functions
function degreesToRadians(num) {
    value = num * Math.PI / 180
    return value
}

function getLatitude(distance, azimuth) {
    /*
    Solves for the latitude of a given line.
    Input: distance, azimuth
    Return: latitude
    */

    latitude = -distance*Math.cos(degreesToRadians(azimuth))
    return latitude
}

function getDeparture(distance, azimuth) {
    /*
    Solves for the departure of a given line.
    Input: distance, azimuth
    Return: latitude
    */

    departure = -distance*Math.sin(degreesToRadians(azimuth))
    return departure
}

function azimuthToBearing(azimuth) {
    /*
    Converts azimuths into bearings.
    Input: azimuth (in DD)
    Return: bearing (in DD)
    */
    
    bearing = 0

    if ((azimuth > 0) && (azimuth < 90)) {
        bearing = ('S ' + azimuth.toFixed(3) + ' W')
    }

    else if ((azimuth > 90) && (azimuth < 180)) {
        bearing = ('N ' + ((180 - azimuth).toFixed(3)) + ' W')
    }

    else if ((azimuth > 180) && (azimuth < 270)) {
        bearing = ('N ' + ((azimuth - 180).toFixed(3)) + ' E')
    }

    else if ((azimuth > 270) && (azimuth < 360)) {
        bearing = ('S ' + ((360 - azimuth).toFixed(3)) + ' E')
    }

    else if (azimuth == 0) {
        bearing = 'Due South'
    }

    else if (azimuth == 90) {
        bearing = 'Due West'
    }

    else if (azimuth == 180) {
        bearing = 'Due North'
    }

    else if (azimuth == 270) {
        bearing = 'Due East'
    }

    return bearing
}

//creating an array containing the given data
var rawdata = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562]
]




//initializing the necessary variables
var lines = []
var adjLines = []
var linesCorr = []
var sumLat = 0
var sumDep = 0
var sumDist = 0
var sum_corrDep = 0
var sum_corrLat = 0




//for loop which gets the lat, dep, & bearing for each of the given lines
for (item in rawdata) {
    //this declares that a 'line' is a pair of two values in the array 'rawdata'
    let line = rawdata [item]

    //in that 'line', we declare that the distance is the first value and the azimuth is the second
    let distance = line [0]
    let azimuth = line [1]

    //getting the lat, dep, and bearing using the created functions
    bearing = azimuthToBearing(azimuth)
    latitude = getLatitude(distance, azimuth)
    departure = getDeparture(distance, azimuth)

    //adding to the summation of lat, dep, and distance for each iteration
    sumLat = sumLat + latitude
    sumDep = sumDep + departure
    sumDist = sumDist + distance

    //creating an array with the needed information and adding it to the mother array 'lines'
    const newLine = {
        Distance: distance,
        Bearing: bearing,
        Latitude: latitude.toPrecision(5),
        Departure: departure.toPrecision(5),
    }

    lines.push(newLine)

}




//printing out the table of lines, along with lec, rec, and other needed information
console.log("-------------------- TRAVERSE COMPUTATION --------------------")
console.table(lines)

console.log("SUMMATION OF LATITUDE: ", sumLat.toPrecision(5))
console.log("SUMMATION OF DEPARTURE: ", sumDep.toPrecision(5))
console.log("SUMMATION OF DISTANCE: ", sumDist.toPrecision(5))

console.log()
lec = Math.sqrt((sumLat**2) + (sumDep**2))
console.log("LEC: ", lec)

rec = sumDist/lec
console.log("REC: 1:", rec)




//for loop to get the lat and dep corrections
for (item in rawdata) {
    //telling the computer that distance is the first element in each line in the array
    let line = rawdata [item]
    let distance = line [0]

    //getting the lat and dep corrections
    corrDep = -sumDep*(distance/sumDist)
    corrLat = -sumLat*(distance/sumDist)
    
    //adding to the running counter for both lat and dep corrections
    sum_corrDep = sum_corrDep + corrDep
    sum_corrLat = sum_corrLat + corrLat
    
    //creating an array with the needed information and adding it to the mother array 'linesCorr'
    const lat_dep_Corr = {
        LatitudeCorrection: corrLat.toPrecision(5),
        DepartureCorrection: corrDep.toPrecision(5),
    }
    
    linesCorr.push(lat_dep_Corr)
}



//for loop to add the lat and dep corrections to lat and dep
for (let item in lines) {
    //defining latitude and departure
    let line = lines[item]
    let latitude = parseFloat(line.Latitude) //convert latitude to a number
    let departure = parseFloat(line.Departure) //convert departure to a number

    //check if latitude and departure are valid numbers
    if (!isNaN(latitude) && !isNaN(departure)) {
        // Adding the corrections to lat and dep
        let adjDep = departure + sum_corrDep
        let adjLat = latitude + sum_corrLat

        //creating an array with the needed information and adding it to the mother array 'adjLines'
        const line_adjusted = {
            AdjustedLatitude: adjLat.toPrecision(5),
            AdjustedDeparture: adjDep.toPrecision(5),
        }

        adjLines.push(line_adjusted)
    } else {
        console.error('Invalid latitude or departure value:', latitude, departure);
    }
}




console.log()
console.log("---------- LAT AND DEP CORRECTIONS ----------")
console.table(linesCorr)
console.log("SUMMATION OF LATITUDE CORRECTIONS: ", sum_corrLat.toPrecision(5))
console.log("SUMMATION OF DEPARTURE CORRECTIONS: ", sum_corrDep.toPrecision(5))

console.log()
console.log("---------- ADJUSTED LAT AND DEP ----------")
console.table(adjLines)
