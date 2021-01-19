import React from 'react';
import axios from 'axios';
import './UserDisplay.css'

export default class CreateNewUser extends React.Component {
  state = {
    firstName: '',
    lastName: '',
    office: '',
    email: '',
    mobile: ''
  }

  handleChange = event => {
    const value = event.target.value;
    this.setState({ 
      ...this.state,
      [event.target.name]: value, 
    })
  }

  handleSubmit = event => {
    event.preventDefault();

    const user = {
        firstName: this.state.firstName,
        lastName: this.state.lastName,
        office: this.state.office,
        email: this.state.email,
        mobile: this.state.mobile
    };

    axios.post(`http://localhost:5000/users`, user)
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }

  render() {
    return (
      <div className="AddUser">
        <form onSubmit={this.handleSubmit}>
          <div>
            <label>
              First Name
              <input className="TextBox" type="text" name="firstName" value={this.state.firstName} onChange={this.handleChange} />
            </label>
          </div>
          <div>
          <label>
            <br></br>Last Name
            <input className="TextBox" type="text" name="lastName" value={this.state.lastName} onChange={this.handleChange} />
          </label>
          </div>
          <div>
          <label>
          <br></br>Location
            <input className="TextBox" type="text" name="office" value={this.state.office} onChange={this.handleChange} />
          </label>
          </div>
          <div>
          <label>
          <br></br>Email
            <input className="TextBox" type="text" name="email" value={this.state.email} onChange={this.handleChange} />
          </label>
          </div>
          <div>
          <label>
          <br></br>Phone
            <input className="TextBox"type="text" name="mobile" value={this.state.mobile} onChange={this.handleChange} />
          </label>
          </div>
          <br></br>
          <button type="submit">Add User</button>
        </form>
      </div>
    )
  }
}