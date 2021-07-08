import React, { useState } from 'react'
// import logo from './logo.svg';

import './App.css';
import GrammarBot from './API/GrammarBot';
import LanguageTool from './API/LanguageTool';
import LanguageToolPy from './API/LanguageToolPy';
import TextGears from './API/TextGears';
import ProWritingAid from './API/ProWritingAid';
import Gector from './API/Gector';

import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button'

function App() {
    // const ref = React.useRef();

    let [text, setText] = useState("");
    let [noText, setNoText] = useState("문자을 입력해주세요.");
    const [loading, setLoading] = useState(false);

    let [grammarBotTime, setGrammarBotTime] = useState(0);
    let [resultGrammarBot, setResultGrammarBot] = useState(null);

    let [languageToolTime, setLanguageToolTime] = useState(0);
    let [resultLanguageTool, setResultLanguageTool] = useState(null);

    let [languageToolPyTime, setLanguageToolPyTime] = useState(0);
    let [resultLanguageToolPy, setResultLanguageToolPy] = useState(null);

    let [textGearsTime, setTextGearsTime] = useState(0);
    let [resultTextGears, setResultTextGears] = useState(null);

    let [proWritingAidTime, setProWritingAidTime] = useState(0);
    let [resultProWritingAid, setResultProWritingAid] = useState(null);

    let [gectorTime, setGectorTime] = useState(0);
    let [resultGector, setResultGector] = useState(null);
    // let [result, setResult] = useState("");

    const clear = () =>{
        setGrammarBotTime(0);
        setResultGrammarBot(null);
        setLanguageToolTime(0);
        setResultLanguageTool(null);
        setTextGearsTime(0);
        setResultTextGears(null);
        setLanguageToolPyTime(0);
        setResultLanguageToolPy(null);
        setProWritingAidTime(0);
        setResultProWritingAid(null);
        setGectorTime(0);
        setResultGector(null);
    }

    const clearAll = () => {
        setText("");
        setNoText("문자을 입력해주세요.")
        clear();
    }


    // const deleteSpan = () =>{
    //     var text = document.getElementById('input').innerText;
    //     text = text.replace(/<span*\'>/gi, "");
    //     text = text.replace(/<\/span>/gi, "");
    //     document.getElementById("input").innerHTML = text;
    //
    //     return text;
    // }

    const postGrammarbot = () => {
        const data= { text : text };

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
            },
            body : JSON.stringify(data)
        };

        fetch('/api/grammarbot', requestOptions)
            .then(response => response.json())
            .then( (result) => {
                setResultGrammarBot(result)
                setGrammarBotTime(result['time'])

            })
            .catch(error => {
                console.error(error);
            });
            // unregister()
    }

    const postLanguageTool = () => {
        const data= { text : text };

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
            },
            body : JSON.stringify(data)
        };

        fetch('/api/languagetool', requestOptions)
            .then(response => response.json())
            .then( (result) => {
                setResultLanguageTool(result)
                setLanguageToolTime(result['time'])
            })
            .catch(error => {
                setResultLanguageTool(null)
                console.error(error);
            });
            // unregister()
    }

    const postLanguageToolpY = () => {
        const data= { text : text };

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
            },
            body : JSON.stringify(data)
        };

        fetch('/api/languagetoolpy', requestOptions)
            .then(response => response.json())
            .then( (result) => {
                console.log(result)
                setResultLanguageToolPy(result)
                setLanguageToolPyTime(result['time'])
            })
            .catch(error => {
                console.error(error);
            });
            // unregister()
    }

    const postTextGears = () => {
        const data= { text : text };

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
            },
            body : JSON.stringify(data)
        };

        fetch('/api/textGears', requestOptions)
            .then(response => response.json())
            .then( (result) => {
                setResultTextGears(result)
                setTextGearsTime(result['time'])
                // console.log("textGears", result)
            })
            .catch(error => {
                console.error(error);
            });
            // unregister(
    }

    const postProWritingGaid = () => {
        const data= { text : text };

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
            },
            body : JSON.stringify(data)
        };

        fetch('/api/proWritingAid', requestOptions)
            .then(response => response.json())
            .then( (result) => {
                setResultProWritingAid(result)
                setProWritingAidTime(result['time'])
                // console.log("proWritingAid" , result)
            })
            .catch(error => {
                console.error(error);
            });
            // unregister(
    }

    const postGector = () => {
        const data= { text : text };

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
            },
            body : JSON.stringify(data)
        };

        fetch('/api/gector', requestOptions)
            .then(response => response.json())
            .then( (result) => {
                // console.log(result)
                setResultGector(result)
                setGectorTime(result['time'])
                // console.log("proWritingAid" , result)
            })
            .catch(error => {
                console.error(error);
            });
            // unregister(
    }

    const  post = () =>{
        postGrammarbot();
        postLanguageTool()
        postTextGears();
        postProWritingGaid()
        postLanguageToolpY()
        postGector()
    }

     const postData = async ()  =>{
         if( !text ){
             setNoText("빈칸은 허용되지 않습니다.")
             console.log("No DATA")
             return;
         }

         await clear();
         setLoading(true);
         try {
             post();
         } catch (e) {
             Error(e)
         }finally{
             setLoading(false)
         }
    }
    const handleChange = (event) => {
        setText(event.target.value)
    }

  return (
    <div className="App">
        <div id='wrapper'>
            <div id="inputPanel">
                <textarea id='input' value={text} onChange={handleChange} placeholder={noText}/>
                <div id='buttonPanel'>
                    <Button disabled={loading} variant="secondary" size='sm' onClick={ ()=> clearAll() } style={{float  : 'right', margin: "2.5%"}} >Clear</Button>
                    <Button disabled={loading} variant="secondary" size='sm' onClick={ () => postData() } style={{float  : 'right', margin: "2.5%", display:'inlin-block'}} >Submit</Button>
                </div>
            </div>

            <div id="apiPanel">
                <div className="apis">
                    <div style={{margin:'0% 0% 3% 0%'}}>Grammar Bot<span style={{float:"right"}}>{grammarBotTime} ms</span></div>
                    <GrammarBot result = {resultGrammarBot}/>
                </div>

                <div className="apis">
                    <div style={{margin:'0% 0% 3% 0%'}}>Language Tool<span style={{float:"right"}}>{languageToolTime} ms</span></div>
                    <LanguageTool result = {resultLanguageTool}/>
                </div>

                <div className="apis">
                    <div style={{margin:'0% 0% 3% 0%'}}>Text Gears<span style={{float:"right"}}>{textGearsTime} ms</span></div>
                    <TextGears result = {resultTextGears}/>
                </div>

                <div className="apis">
                    <div style={{margin:'0% 0% 3% 0%'}}>Language Tool Python<span style={{float:"right"}}>{languageToolPyTime} ms</span></div>
                    <LanguageToolPy result = {resultLanguageToolPy}/>
                </div>

                <div className="apis">
                    <div style={{margin:'0% 0% 3% 0%'}}>Pro Writing Aid<span style={{float:"right"}}>{proWritingAidTime} ms</span></div>
                    <ProWritingAid result = {resultProWritingAid}/>
                </div>

                <div className="apis">
                    <div style={{margin:'0% 0% 3% 0%'}}>Gector<span style={{float:"right"}}>{gectorTime} ms</span></div>
                    <Gector result = {resultGector}/>
                </div>
            </div>
        </div>
    </div>
  );
}

export default App;
