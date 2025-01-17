import { ApolloClient, InMemoryCache, gql, useMutation } from '@apollo/client';
import {useLocation, useNavigate} from 'react-router';

import * as constants from "./constants.js"
import { useEffect, useState } from 'react';
import { LoadingView } from './views/utilities/LoadingView.jsx';

export const REFRESH_TOKEN_MUTATION = gql`
    mutation(
        $refreshToken: String!
    ){
        refreshToken(refreshToken: $refreshToken){
            token
        }
    }
`

export const GET_TOKENS_MUTATION = gql`
    mutation($username: String!, $password: String!){
        tokenAuth(username: $username, password: $password){
            token,
            refreshToken,
            payload
        }
    }
`;

export const VERIFY_TOKEN_MUTATION = gql`
    mutation(
        $token: String!
    ){
        verifyToken(token: $token){
            payload
        }
    }
`;


export const REGISTER_USER_MUTATION = gql`
mutation($password: String!, $username: String!, $token: String!){
    registerUser(password: $password, username: $username, registrationToken: $token){
        ok,
        messages
    }
}
`

export const GENERATE_REGISTRATION_TOKEN = gql`
query($accessToken: String!){
  generateRegistrationToken(token: $accessToken)
}
`

export const CURRENT_USER = {
    name: null
}


export const apiClient = new ApolloClient({
    uri: constants.API_SERVER_URL,
    cache: new InMemoryCache(),
});


export function logOut() {
    localStorage.removeItem(constants.ACCESS_TOKEN);
    localStorage.removeItem(constants.REFRESH_TOKEN);
}


/**
 *  Wraps its child components and renders them to only the authenticated user.
 *  When user is not authenticated, then redirection to login page is performed.
 */
export function LoginRequired({children}) {
    const location = useLocation();
    const navigate = useNavigate()
    const [isAuthenticating, setIsAuthenticating] = useState(true);

    const [verifyToken] = useMutation(VERIFY_TOKEN_MUTATION);
    const [refreshAccessToken] = useMutation(REFRESH_TOKEN_MUTATION);

    async function tryRefreshToken(){
        const refreshToken = localStorage.getItem(constants.REFRESH_TOKEN);
        if (!refreshToken){
            return false;
        }
        try {
            const {data} = await refreshAccessToken({variables: {refreshToken: refreshToken}});
            localStorage.setItem(constants.ACCESS_TOKEN, data.refreshToken.token);
            return true;
        } catch (error) {
            return false;
        }
    }

    async function tryAuthenticate() {
        const accessToken = localStorage.getItem(constants.ACCESS_TOKEN);
        if (!accessToken) {
            return false;
        }
        try {
            await verifyToken({variables: {token: accessToken}});
            return true;
        } catch (error) {
            if (error.cause.message === constants.TOKEN_EXPIRED_ERROR) {
                const refreshed = await tryRefreshToken();
                if (refreshed) {
                    return await tryAuthenticate();
                }
            }
            return false;
        }
    }

    useEffect(() => {
        tryAuthenticate().then((isAuthenticated) => {
            setIsAuthenticating(false);
            if (!isAuthenticated)
                navigate(`${constants.LOGIN_PAGE_PATH}?redirect=${location.pathname}`);
        });
    }, []);

    if (isAuthenticating)
        return <LoadingView/>;

    return <>
        {children}
    </>;
}
