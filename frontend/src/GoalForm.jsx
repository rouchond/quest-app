import React, {useState} from 'react'
import {BASE_URL} from '../../keys'

function GoalForm({existingGoal = {}, updateCallback}){
    
    const [name, setName] = useState("");
    const [desc, setDesc] = useState("");
    const [color, setColor] = useState("");

    const updating = Object.entries(existingGoal).length !== 0;

    const onSubmit = async (e) => {
        e.preventDefault();

        const data = {
            name,
            desc,
            color
        };

        const url = BASE_URL + (updating ? 
            "/update_goal/" + existingGoal.id
            :
            "/create_goal"
        );

        const options = {
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
        <>
            <form onSubmit={onSubmit}>
                <div>
                    <label htmlFor="name">Goal Name: </label>
                    <input 
                    type="text"
                    id="name"
                    value={name} 
                    onChange={(e) => setName(e.target.value)}/>
                </div>
                <div>
                    <label htmlFor="desc">Goal Description: </label>
                    <input 
                    type="text"
                    id="desc"
                    value={desc} 
                    onChange={(e) => setDesc(e.target.value)}/>
                </div>
                <div>
                    <label htmlFor="color">Goal Color: </label>
                    <input 
                    type="text"
                    id="color"
                    value={color} 
                    onChange={(e) => setColor(e.target.value)}/>
                </div>
                <button type="submit">{updating ? "Update" : "Create"}</button>
            </form>
        </>
    );
}

export default GoalForm