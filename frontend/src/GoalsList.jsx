import { BASE_URL } from "../../keys";

function GoalsList({goals, updateGoal, updateCallBack}){
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`${BASE_URL}/delete_goal/${id}`, options);
            if (response.status === 200) {
                updateCallBack();
            }
            else {
                console.error("Failed to delete");
            }
        }
        catch (error) {
            alert(error);
        }
    }

    return(
        <>
            <div>
                <h2>Goals</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Goal Name</th>
                            <th>Goal Desc</th>
                            <th>Goal Color</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {goals.map((goal) => (
                            <tr key={goal.id}>
                                <td>{goal.name}</td>
                                <td>{goal.desc}</td>
                                <td>{goal.color}</td>
                                <td>
                                    <button onClick={() => updateGoal(goal)}>Update</button>
                                    <button onClick={() => onDelete(goal.id)}>Delete</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    )
}


export default GoalsList