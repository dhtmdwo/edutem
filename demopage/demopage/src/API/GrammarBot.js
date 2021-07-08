import React, { useState, useEffect } from 'react';

function GrammarBot(props){
    var result = props.result ;
    var fResult = [];
    var mResult = [];
    var tResult = [];
    var offset;
    var oldOffset = 0;
    var len;
    var newSetence =[];
    var wrongWordsList = [];
    let [buttonText, setButtonText] = useState(wrongWordsList);

    function resetButtonText(){
        if(result && result.matches){
            wrongWordsList = []
            for (let i = 0; i < result.matches.length; i++) {
                if(result.matches[i].replacements[0]){
                    wrongWordsList.push( result.matches[i].replacements[0].value) ;
                }
            }
            setButtonText (wrongWordsList)
        }
    }

    function changeTextByClick(i, newWord){
        var newArr = [...buttonText];
        newArr[i] = newWord;
        setButtonText(newArr);
    }



    useEffect(()=>{
        resetButtonText()
    }, [props]);


    if(result){
        // <div style={{margin:'0%'}}>Grammar Bot<span style={{float:"right"}}>{grammarBotTime} ms</span></div>
        if(!result["matches"]){
            return  <div key = "noError">There is No error.</div>
        }


        for (let i = 0; i < result.matches.length; i++) {
            tResult = [];
            offset = result.matches[i].offset
            len = result.matches[i]["length"]
            // tid = result.content.substring(offset, offset+len) + i ;
            // if(result.matches[i].replacements[0]){
            //     buttonText.push(result.matches[i].replacements[0].value); // 좋지 않은 방식 바꾸어 주어야 함.!
            // }
            newSetence.push(result.text.substring(oldOffset,offset))
            newSetence.push(<span className='wrong' key= {result.text.substring(offset,offset+len)} >{ buttonText[i] }</span>)
            oldOffset = offset+len;
            tResult.push("\t")
            tResult.push(result.text.substring(offset, offset+len ))  // offset lengh 계산!!!
            tResult.push("->")

            for(let j=0; j< Math.min(result.matches[i].replacements.length,3); j++){
                tResult.push(<button style={{margin: '0.3%'}} key={result.matches[i].replacements[j].value} onClick={() => changeTextByClick(i, result.matches[i].replacements[j].value)} >{result.matches[i].replacements[j].value}</button>);
            }
            // ignore = result.text.substring(offset, offset+len )
            tResult.push(<button style={ {float: 'right', margin: '0.3%', color: '#EB0000', borderColor  :  '#EB0000'}} key={ result.text.substring(result.matches[i].offset, result.matches[i].offset + result.matches[i]["length"] ) + "n" } onClick={() => changeTextByClick(i, result.text.substring(result.matches[i].offset, result.matches[i].offset + result.matches[i]["length"]) )} >IGNORE</button>);
            // tResult.push(<button style={{flow: 'right', margin: '0.3%'}} key={ignore} onClick={() => console.log({ignore}) } >IGNORE</button>);
            mResult.push(<div style={{margin: '0.5%'}} key={i}>{tResult}</div>)
        }
        newSetence.push(result.text.substring(oldOffset))

        fResult.push(<div key="newSetence" >{newSetence}</div>)
        fResult.push(<div key="mResult" >{mResult}</div>)
    //
        return fResult;
    }
    else{
        // console.log("NOTHING")
        buttonText = [];
        return <div></div>
    }
}

export default GrammarBot
