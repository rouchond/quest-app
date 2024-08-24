// Note: Need to fix update button in goal form. 

import React, {useState, useEffect} from 'react'

import GoalForm from './GoalForm.jsx'

import {BASE_URL} from '../../keys.js'

function AddGoal(){

    const [goals, setGoals] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [currentGoal, setCurrentGoal] = useState({});

    useEffect(() => {
        fetchGoals();
    }, []);

    const fetchGoals = async () => {
        const response = await fetch(BASE_URL + "/goals");
        const data = await response.json();
        setGoals(data.goals);
    }

    const closeModal = () => {
        setIsModalOpen(false);
        setCurrentGoal({});
    }

    const openCreateModal = () => {
        if (!isModalOpen) setIsModalOpen(true);
    }

    const openEditModal = (goal) => {
        if (isModalOpen) return;
        setCurrentGoal(goal);
        setIsModalOpen(true);
    }

    const onUpdate = () => {
        closeModal();
        fetchGoals();
    }

    return(
        <>


            <button onClick={openCreateModal}>Add Goal</button>
            {isModalOpen && <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={closeModal}>&times;</span>
                        <GoalForm existingGoal={currentGoal} updateCallback={onUpdate}/>
                    </div>
                </div>
                }
        </>
    );
}

export default AddGoal;