import React, { useState, useEffect } from 'react';

function TextGears(props){
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
        if(result && result.errors){
            wrongWordsList = []
            for (let i = 0; i < result.errors.length; i++) {
                if(result.errors[i].better[0]){
                    wrongWordsList.push( result.errors[i].better[0].value) ;
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
        if(!result["errors"]){
            return  <div key = "noError">There is No error.</div>
        }


        for (let i = 0; i < result.errors.length; i++) {
            tResult = [];
            offset = result.errors[i].offset
            len = result.errors[i]["length"]
            // tid = result.content.substring(offset, offset+len) + i ;

            newSetence.push(result.text.substring(oldOffset,offset))
            newSetence.push(<span className='wrong' key= {result.errors[i].bad} >{ buttonText[i] }</span>)
            oldOffset = offset+len;
            tResult.push("\t")
            tResult.push(result.text.substring(offset, offset+len ))  // offset lengh 계산!!!
            tResult.push("->")

            if( result.errors[i].better.length){
                for(let j=0; j< Math.min(result.errors[i].better.length,3); j++){
                    tResult.push(<button style={{margin: '0.3%'}} key={result.errors[i].better[j]} onClick={() => changeTextByClick(i, result.errors[i].better[j])} >{result.errors[i].better[j]}</button>);
                }
            }
            else{
                tResult.push(<button style={{margin: '0.3%'}} key={"nothing"} onClick={() => changeTextByClick(i, "")} >{"\t"}</button>);
            }

            // ignore = result.text.substring(offset, offset+len )
            tResult.push(<button style={ {float: 'right', margin: '0.3%', color: '#EB0000', borderColor  :  '#EB0000'}} key={ result.errors[i].bad + "n" } onClick={() => changeTextByClick(i, result.errors[i].bad )} >IGNORE</button>);
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
        buttonText = [];
        return <div></div>
    }
}

export default TextGears
