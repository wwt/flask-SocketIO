import React from 'react';
import './UserDisplay.css'

const UserDisplay = (props) => {
    return (
        <div className="User">
            <h3>{props.firstName} {props.lastName}</h3>
            <p>Location: {props.office}</p>
            <p>Email: {props.email}</p>
            <p>Phone: {props.mobile}</p>
        </div>
    )
}

export default UserDisplay;