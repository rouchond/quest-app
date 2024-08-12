import React, {useState} from 'react'
import BASE_URL from '../../keys'

function QuestForm(existingQuest = {}, updateCallback){
    
    const [questName, setName] = useState("");
    const [questDesc, setDesc] = useState("");
    const [questColor, setColor] = useState("");

    const updating = Object.entries(existingQuest).length !== 0;

    const onSubmit = async (e) => {
        e.preventDefault();

        const data = {
            name,
            desc,
            color
        };

        const url = BASE_URL + (updating ? 
            "/update_goal/" + existingQuest.id
            :
            "create_goal"
        );

        const config = {
            method: updating ? "PUT" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        };

        const response = await fetch(url, options);
        if (response.status != 201 && response.status != 200){
            const data = response.json();
            alert(data.message);
        }
        else{
            updateCallback();
        }
    }

    return(
        <></>
    );
}

export default QuestForm