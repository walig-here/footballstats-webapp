import { useMutation } from "@apollo/client";
import { Button, Icon, TextField } from "actify";
import { useState } from "react";
import {GET_TOKENS_MUTATION} from '../../api_client';
import {ACCESS_TOKEN, REFRESH_TOKEN} from '../../constants';
import { LoadingView } from "../../views/utilities/LoadingView";
import { useContext } from "react";
import { UserContext } from "../../App";
import { Body } from "../Body";
import { useNavigate } from "react-router";


export default function LoginForm() {
    const navigate = useNavigate();
    const user = useContext(UserContext);
    const [password, setPassword] = useState("");
    const [login, setLogin] = useState("");
    const [getTokensMutation, {loading, error}] = useMutation(GET_TOKENS_MUTATION);

    const tryLogin = async () => {
        user.logoutFunction();
        try {
            const {data} = await getTokensMutation({variables: {
                username: login, password: password
            }});
            user.setUsername(data.tokenAuth.payload.username);
            localStorage.setItem(ACCESS_TOKEN, data.tokenAuth.token);
            localStorage.setItem(REFRESH_TOKEN, data.tokenAuth.refreshToken);
            navigate("/");
        } catch (caughtError) {
            console.log(`Error occurred while trying to log in. Error:\n${caughtError}`);
        }
        setPassword("");
        setLogin("");
    }

    if (loading)
        return <LoadingView/>

    return (
        <div className="flex flex-col space-y-4">
            {error && <Body text={error.message} style='text-error'/>}
            <TextField 
                variant="outlined"
                label="Login"
                value={login}
                onChange={(value) => {setLogin(value)}}
            />
            {error && <Body text={error.message} style='text-error'/>}
            <TextField 
                variant="outlined" 
                label="Hasło" 
                type="password"
                value={password}
                onChange={(value) => {setPassword(value)}}
            />
            <Button 
                variant="filled"
                onPress={() => tryLogin()}
            >
                <Icon>login</Icon>
                Zaloguj się
            </Button>
        </div>
    )
}