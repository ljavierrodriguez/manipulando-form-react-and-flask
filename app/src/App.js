import { useEffect, useState } from "react";
import RegisterForm from "./components/RegisterForm";

const App = () => {

    const [users, setUsers] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [avatar, setAvatar] = useState('sin-foto.png');

    const handleSubmit = async e => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('name', name);
        formData.append('email', email);
        formData.append('avatar', avatar);

        
        const info = await registerFetch(formData);
        
        if(info.id){
            listUsers();
        }

    }

    const registerFetch = async data => {
        const resp = await fetch('https://5000-ljavierrodr-manipulando-dnq53i023n7.ws-us45.gitpod.io/api/register', { method: 'POST', body: data });
        const info = await resp.json();
        return info;
    }

    const listUsers = async () => {
        const resp = await fetch('https://5000-ljavierrodr-manipulando-dnq53i023n7.ws-us45.gitpod.io/api/users');
        const info = await resp.json();
        setUsers(info)
    }

    useEffect(() => {
        listUsers();
    }, [])

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-8 offset-md-2">
                    <RegisterForm handleSubmit={handleSubmit} name={name} email={email} avatar={avatar} setName={setName} setEmail={setEmail} setAvatar={setAvatar} />
                </div>
            </div>
            <div className="row">
                <div className="col-md-12">
                    <ul className="list-group">
                        {
                            users.map((user) => {
                                return <li key={user.id} className="list-group-item">
                                    { user.name } / { user.email } / <img src={user.avatar} width={40} height={40} className="rounded-circle mx-1" />
                                </li>
                            })
                        }
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default App;