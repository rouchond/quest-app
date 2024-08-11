import React, {useState} from 'react'

import QuestForm from './QuestForm.jsx'

function AddQuest(){

    const [isModalOpen, setModalOpen] = useState(false);

    const openCreateModal = () => {
        if (!isModalOpen) setModalOpen(true)
    }

    return(
        <>
        <button onClick={openCreateModal}>Add Quest</button>
        {isModalOpen && <div className="modal">
                <div className="modal-content">
                    <QuestForm/>
                </div>
            </div>}
        </>
    );
}

export default AddQuest;