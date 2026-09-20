import { useState, useEffect } from 'react';
import axios from 'axios';

function getCookie(name){
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`)
  if (parts.length === 2) return parts.pop().split(";").shift();
  return null;

}

function App(){

  const [loggedIn, setLoggedIn] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [todos,setTodos] = useState([]);
  const [editingTodo, setEditingTodo] = useState(null);
  const [showModal, setShowModal] = useState(false);


  useEffect(()=>{
    const token = localStorage.getItem("access_token");
    if (token) {
      setLoggedIn(true);
      fetchTodos();
    }
  },[]);

  const handleLogin = async () => {
    try {
      const formData = new URLSearchParams();
      formData.append("username",email);
      formData.append("password",password);
      const res = await axios.post(
        `${BACKEND_URL}/auth/token`,
        formData,
        {
          headers: {"Content-Type": "application/x-www-form-urlencoded"},
        }
      );

      const token = res.data.access_token;
      if (token) {
        localStorage.setItem("access_token", token);
        setLoggedIn(true);
        fetchTodos();
      }
    } catch (err) {
      alert("Login failed");
      console.log(err);
    }
  };

  const fetchTodos= async() =>{
    const token = localStorage.getItem("access_token");
    if (!token) return;
    const res = await axios.get(`${BACKEND_URL}/todos/`,{
      headers:{
        Authorization: `Bearer ${token}`
      }
    });

    setTodos(res.data);

  };

  const openModal = (todo) => {
    setEditingTodo({...todo});  //clone to avoid instant ui changes
    setShowModal(true);
  }

  const editTodo = async() =>{
    const token = localStorage.getItem("access_token");
    if (!token) return;
    const res = await axios.put(
  `${BACKEND_URL}/todos/${editingTodo.id}`,
  {
    title: editingTodo.title,
    description: editingTodo.description,
    priority: editingTodo.priority,
    complete: editingTodo.complete
  },
  {
    headers: { Authorization: `Bearer ${token}` }
  }
);
    setShowModal(false);
    fetchTodos();

  };

if (!loggedIn) {
    return (
      <div style={{ padding: "20px" }}>
        <h2>Login</h2>

        <input
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{ display: "block", marginBottom: "10px" }}
        />

        <input
          placeholder="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ display: "block", marginBottom: "10px" }}
        />

        <button onClick={handleLogin}>Login</button>
      </div>
    );
  }

return (
  <div style={{ padding: "20px", fontFamily: "sans-serif",background: "beige"}}>
    <h1>TodoApp</h1>
    <ul>
      {todos.map(t => (
  <li key={t.id}>
    <strong>{t.title}</strong>
    <button onClick={() => openModal(t)}>Edit</button>
  </li>
))}
    </ul>
    {/* ---MOdal---*/}
    {showModal && (
      <div style={{ position: "fixed", top:"20%", bottom:"50%",transform: "translateX(-50%)",
                    background: "white", padding: "20px",border: "1px solid #ccc", borderRadius: "8px", width:"300px"}}>
        <h3> Edit Todo </h3>

        <label> Title </label>
        <input value={editingTodo.title} onChange={(e)=>{
          setEditingTodo({...editingTodo,title:e.target.value})
        }} style={{width: "100%", marginBottom: "10px"}}></input>

        <label> Description </label>
        <input value={editingTodo.description} onChange={(e)=>{
          setEditingTodo({...editingTodo,description:e.target.value})
        }} style={{width: "100%", marginBottom: "10px"}}></input>

        <label> Priority </label>
        <input type="integer" value={editingTodo.priority} onChange={(e)=>{
          setEditingTodo({...editingTodo,priority: Number(e.target.value)})
        }} style={{width: "100%", marginBottom: "10px"}}></input>

        <label> Complete 
        <input type="checkbox" checked={editingTodo.complete} onChange={(e)=>{
          setEditingTodo({...editingTodo,complete:e.target.checked})
        }} style={{ marginLeft: "10px"}}></input>
        </label>

        <div style={{ marginTop: "20px"}}>
        <button  onClick={editTodo}>Save</button>
        <button onClick={()=> setShowModal(false)} style={{marginLeft:"10px"}}> Cancel </button>
        </div>
      </div>

      )}
  </div>

  );


}


export default App;
