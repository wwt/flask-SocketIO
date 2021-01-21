import React, {useEffect} from 'react';
import UserDisplay from './UserDisplay';
import axios from 'axios';

import { socket } from '../App'

export default class UserList extends React.Component {
  state = {
    users: []
  }

  componentDidMount() {
    socket.on('userAddedResponse', (resp) => {
      const users = this.state.users;
      const userAdded = resp.data.data.user;
      users.push(userAdded)
      
      this.setState({ users })
    });

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