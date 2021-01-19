import React from 'react';
import UserDisplay from './UserDisplay';
import axios from 'axios';

export default class UserList extends React.Component {
  state = {
    users: []
  }

  componentDidMount() {
    axios.get(`http://localhost:5000/users`)
      .then(res => {
        const users = res.data.users;
        this.setState({ users });
      })
  }

  render() {
    return (
      <div>
        { this.state.users.map(user => <UserDisplay firstName={user.firstName} lastName={user.lastName} office={user.office} email={user.email} mobile={user.mobile}></UserDisplay>)}
      </div>
    )
  }
}