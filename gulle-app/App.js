import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View, Button } from 'react-native';
import React, { useState } from 'react';
// importing native expo functions


export default function App() {

  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  // initializing the necessary variables

  const round = (number, decimalPlaces) => {
    return parseFloat(number.toFixed(decimalPlaces));
  };
  // function to round off the decimal places

  const conversion = () => {
      /*
      function that converts DD to DMS and vice versa, 
      depending if the input has "-" in it.
      */

    if (text.includes("-")){
      let dmsInput = text.split("-");
      let degrees = parseFloat(dmsInput[0]);
      let minutes = parseFloat(dmsInput[1]);
      let seconds = parseFloat(dmsInput[2]);
      let dd = degrees + (minutes/60) + (seconds/3600)

      setResult(round(dd,5));
    }

    else {
      let ddInput = text
      let degrees = Math.trunc(ddInput)
      let minutes = Math.abs((ddInput - degrees)*60)
      let minutesInt = Math.trunc(minutes)
      let seconds = Math.abs((minutesInt - minutes)*60)
      let dms = degrees + "° " + minutesInt + "' " + round(seconds,4) + "'' "

      setResult(dms)
    }
  };

  

  return (
    <View style={styles.mainbox}>

      <View style={styles.titlebox}>
      <Text style={styles.titletext}> DMS - DD CONVERTER </Text>
      <Text style={styles.text}>Use this handy calculator to convert 
      DMS to DD (and vice versa) with a press of a button!</Text>
      </View>

      <View style={styles.inputbox}>
      <Text style={styles.titletext}>Input:</Text>
      <TextInput
        style={styles.input}
        placeholder="Input goes here...."
        value={text}
        onChangeText={setText}
      />

      <Button title="Convert" onPress={conversion} />
      </View>

      <View style={styles.outputbox}>
      <Text style={styles.titletext}>Output:</Text>
      <Text style={styles.titletext}>{result}</Text>
      </View>

      <View style={styles.endbox}>
      <Text style={styles.text}>Please input DMS values in this format: DD-MM-SS.
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
