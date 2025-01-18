import { Button, Icon, TextField } from "actify";
import { useState } from "react";
import {REGISTER_USER_MUTATION} from '../../api_client';
import { useMutation } from "@apollo/client";
import { LoadingView } from "../../views/utilities/LoadingView";
import { Body } from "../Body";
import * as utils from "../../data_processing"
import { useNavigate } from "react-router";
import { toast } from "react-toastify";


export default function RegisterForm() {
    const navigation = useNavigate();
    const [performRegisterMutation, {loading}] = useMutation(REGISTER_USER_MUTATION);
    const [form, setForm] = useState({
        login: "",
        loginError: null,
        password: "",
        passwordError: null,
        token: "",
        tokenError: null,
        formError: null,
    });

    const registerUser = async () => {
        const [loginValid, loginError] = utils.validateUsername(form.login);
        const [passwordValid, passwordError] = utils.validatePassword(form.password);
        const [tokenValid, tokenError] = utils.validateTextInput(form.token);
        if (![loginValid, passwordValid, tokenValid].every(Boolean)) {
            setForm(oldForm => ({
                ...oldForm,
                loginError: loginError,
                passwordError: passwordError,
                tokenError: tokenError
            }))
            return;
        }
        
        try {
            const {data} = await performRegisterMutation({variables: {
                username: form.login, password: form.password, token: form.token
            }});
            console.log(data);
            if (!data.registerUser.ok)
                setForm(oldForm => ({
                    ...oldForm,
                    formError: data.registerUser.messages[0],
                    loginError: loginError,
                    passwordError: loginError,
                    tokenError: loginError
                }));
            else {
                setForm(oldForm => ({
                    ...oldForm,
                    login: form.login,
                    password: form.password,
                    token: form.token,
                }));
                toast.success("Zarejestrowano administratora!");
                navigation("/");
            }
        } catch (err) {
            console.log(`Error occurred while registering user. Error:\n${err}`);
            return;
        }
    }

    if (loading)
        return <LoadingView/>;

    return (
        <div className="flex flex-col space-y-4">
            {form.formError && <Body text={form.formError} style='text-error'/>}
            {form.loginError && <Body text={form.loginError} style='text-error'/>}
            <TextField 
                variant="outlined"
                label="Login"
                value={form.login}
                onChange={(newLogin) => setForm(oldForm => ({
                    ...oldForm,
                    login: newLogin
                }))}
            />
            {form.passwordError && <Body text={form.passwordError} style='text-error'/>}
            <TextField 
                variant="outlined" 
                label="Hasło" 
                type="password"
                value={form.password}
                onChange={(newPassword) => setForm(oldForm => ({
                    ...oldForm,
                    password: newPassword
                }))}
            />
            {form.tokenError && <Body text={form.tokenError} style='text-error'/>}
            <TextField 
                variant="outlined" 
                label="Token rejestracji"
                value={form.token}
                onChange={(newToken) => setForm(oldForm => ({
                    ...oldForm,
                    token: newToken
                }))}
            />
            <Button 
                variant="filled"
                onPress={() => {registerUser()}}
            >
                <Icon>person_add</Icon>
                Zarejestruj się
            </Button>
        </div>
    );
}