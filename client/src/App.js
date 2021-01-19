import './App.css';
import './components/UserList'
import UserList from './components/UserList';
import CreateNewUser from './components/CreateNewUser';


function App() {
  return (
    <div>
      <h1>Users</h1>
      <CreateNewUser></CreateNewUser>
      <div className="App">
        <UserList></UserList>
      </div>
    </div>
  );
}

export default App;
