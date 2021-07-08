import React, { useState, useEffect } from 'react';

function Gector(props){
    let [text, setText] = useState("")


    useEffect(()=>{
        if(props.result){
            setText (props.result.text);
        }
    });

    return <div>{text}</div>


}

export default Gector
