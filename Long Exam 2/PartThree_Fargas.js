/*
    Dear Sir Dom,
    Though you said we didn't have to code, I decided to use my code from Lab 6 to serve as a template
    for this portion of the test. I also reused code from my Lab 5 to make the convertToBearing function.
    Additionally, I also want to say that I uploaded my Lab 6 ~20 minutes before the exam. The 
    commit message on some of the expo files says "In progress", but they're for submission na po, 
    di ko lang po mapalitan huhu. I hope that's okay.

*/

/*
    (Given the following specifications for this design, what React Native components do you suggest
    are needed to develop this app, and how will you implement them?)

    We know that we need TextInput, Text, and Button at the very least. As you can see below, I decided
    to split the screen into four boxes. The two middle boxes hold the 'meat' of the app; the second
    box from the top contains the text field and the button to convert. The third box displays the 
    output. 

    It is made very simple so that the user will not get confused. I made it similar to most conversion
    calculators that you can find online. I also hope that the colors, text, and layout help guide 
    the user's eyes to the focus of the app.

*/

import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View, Button } from 'react-native';
import React, { useState } from 'react';
// importing native expo functions


export default function App() {

  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [inter1, setInter1] = useState('');
  const [inter2, setInter2] = useState('');
  // initializing the necessary variables

  const convertToBearing = () => {
    const DMStoDD = () => {
    /*
    function that converts DMS to DD.
    */

    let dmsInput = text.split("-");
    let degrees = parseFloat(dmsInput[0]);
    let minutes = parseFloat(dmsInput[1]);
    let seconds = parseFloat(dmsInput[2]);
    let dd = degrees + (minutes/60) + (seconds/3600)

    setInter1(dd);
  };

    const convertToBearingDD = () => {
    /*
    Converts azimuths into bearings.
    Input: azimuth (in DD)
    Return: bearing (in DD)
    */

    let inter1 = azimuth

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

    setInter2(bearing)
  };

  

  const DDtoDMS = () => {
    /*
    function that converts DD to DMS.
    */

    let ddInput = inter2
    let degrees = Math.trunc(ddInput)
    let minutes = Math.abs((ddInput - degrees)*60)
    let minutesInt = Math.trunc(minutes)
    let seconds = Math.abs((minutesInt - minutes)*60)
    let dms = degrees + "° " + minutesInt + "' " + round(seconds,4) + "'' "

    setResult(dms)
  };
}
  /*
    This entire thing feels very convoluted and I don't feel like this is the best way, 
    but the entire convertToBearing megafunction is meant to first convert the input to DD,
    get the bearing, then finally convert it back to DMS. I don't think I'm allowed to use my phone,
    so I wasn't able to see if my code works or not. Hopefully gagana huhu
  */

  return (
    <View style={styles.mainbox}>

      <View style={styles.titlebox}>
      <Text style={styles.titletext}> AZIMUTH TO BEARING CONVERTER </Text>
      <Text style={styles.text}>Use this handy calculator to convert 
      azimuths to bearings with a press of a button!</Text>
      </View>

      <View style={styles.inputbox}>
      <Text style={styles.titletext}>Input:</Text>
      <TextInput
        style={styles.input}
        placeholder="Input goes here...."
        value={text}
        onChangeText={setText}
      />

      <Button 
        title="Convert" 
        onPress={convertToBearing}
        />
      </View>

      <View style={styles.outputbox}>
      <Text style={styles.titletext}>Output:</Text>
      <Text style={styles.titletext}>{result}</Text>
      </View>

      <View style={styles.endbox}>
      <Text style={styles.text}>Please input azimuth values in this format: DD-MM-SS. Note that this
      calculator works only for azimuths from the south, not the north.
      If the calculator doesn't show the expected result, please double check how you entered the values.
      </Text>
      </View>

      <StatusBar style="auto" />
    </View>

  );
}

// stylesheet containing all of the styles used
const styles = StyleSheet.create({
  mainbox: {
    flex: 1,
    backgroundColor: '#dad7cd',
    alignItems: 'center',
    justifyContent: 'center',
  },

  titletext: {
    fontSize: 24,
    fontWeight: '600'
  },

  input: {
    height: 40,
    borderColor: 'white',
    borderWidth: 1,
    width: '100%',
    padding: 8,
    marginBottom: 16,
  },

  titlebox: {
    flex: 1,
    width: '100%',
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 15,
    backgroundColor: '#a3b18a',
  },

  inputbox: {
    flex: 1,
    width: '100%',
    backgroundColor: '#fff',
    alignItems: 'left',
    justifyContent: 'center',
    paddingHorizontal: 15,
    backgroundColor: '#588157',
  },

  outputbox: {
    flex: 1,
    width: '100%',
    backgroundColor: '#fff',
    alignItems: 'left',
    justifyContent: 'center',
    paddingHorizontal: 15,
    backgroundColor: '#588157',
  },

  endbox: {
    flex: 1,
    width: '100%',
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 15,
    backgroundColor: '#3a5a40',
  },
});

