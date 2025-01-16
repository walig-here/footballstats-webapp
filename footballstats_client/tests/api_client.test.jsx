import {test, expect,} from 'vitest'
import {render, screen, waitFor } from '@testing-library/react'
import { MockedProvider } from "@apollo/client/testing";

import * as api from "../src/api_client.jsx"
import * as constants from "../src/constants.js"
import { BrowserRouter, Route, Routes } from 'react-router';
import LoginAndRegistrationView from '../src/views/utilities/LoginAndRegistrationView.jsx';

const VALID_ACCESS_TOKEN = "valid-access-token";
const EXPIRED_ACCESS_TOKEN = "expired-access-token";
const VALID_REFRESH_TOKEN = "valid-refresh-token";
const EXPIRED_REFRESH_TOKEN = "expired-refresh-token";
const INVALID_ACCESS_TOKEN = "invalid-access-token";

const GRAPH_QL_MOCKS = [
    {
        request: {
            query: api.VERIFY_TOKEN_MUTATION,
            variables: {
                token: EXPIRED_ACCESS_TOKEN,
            }
        },
        result: {
            errors: [
                {
                    message: constants.TOKEN_EXPIRED_ERROR,
                }
            ],
            data: {
                verifyToken: null,
            }
        },
        maxUsageCount: Number.POSITIVE_INFINITY
    },
    {
        request: {
            query: api.VERIFY_TOKEN_MUTATION,
            variables: {
                token: INVALID_ACCESS_TOKEN,
            }
        },
        result: {
            errors: [
                {
                    message: constants.INVALID_ACCESS_TOKEN,
                }
            ],
            data: {
                verifyToken: null,
            }
        },
        maxUsageCount: Number.POSITIVE_INFINITY
    },
    {
        request: {
            query: api.VERIFY_TOKEN_MUTATION,
            variables: {
                token: VALID_ACCESS_TOKEN,
            }
        },
        result: {
            data: {
                verifyToken: {
                    payload: {
                        username: "owner",
                        exp: 1737049033,
                        origIat: 1737048733
                    }
                },
            }
        },
        maxUsageCount: Number.POSITIVE_INFINITY
    },
    {
        request: {
            query: api.REFRESH_TOKEN_MUTATION,
            variables: {
                refreshToken: VALID_REFRESH_TOKEN,
            }
        },
        result: {
            data: {
                refreshToken: {
                    token: VALID_ACCESS_TOKEN,
                }
            }
        },
        maxUsageCount: Number.POSITIVE_INFINITY
    },
    {
        request: {
            query: api.REFRESH_TOKEN_MUTATION,
            variables: {
                refreshToken: EXPIRED_REFRESH_TOKEN,
            }
        },
        result: {
            errors: [
                {
                    message: constants.TOKEN_EXPIRED_ERROR,
                }
            ],
            data: {
                refreshToken: null,
            }
        },
        maxUsageCount: Number.POSITIVE_INFINITY
    },
];

test('LoginRequired -> when user is authenticated then render children', async () => {
    localStorage.setItem(constants.ACCESS_TOKEN, VALID_ACCESS_TOKEN);
    localStorage.setItem(constants.REFRESH_TOKEN, VALID_REFRESH_TOKEN);

    render(
        <BrowserRouter>
            <Routes>
                <Route path="" element={
                    <MockedProvider mocks={GRAPH_QL_MOCKS} addTypename={false}>
                        <api.LoginRequired>
                            <div data-testid='div'></div>
                        </api.LoginRequired>
                    </MockedProvider>
                }/>
                <Route path="auth/login" element={<LoginAndRegistrationView/>}/>
            </Routes>
        </BrowserRouter>
    );

    await waitFor(() => {
        expect(screen.getByTestId('div')).toBeInTheDocument();
    })
});

test('LoginRequired -> when user has expired access token but valid refresh token then render children', async () => {
    localStorage.setItem(constants.ACCESS_TOKEN, EXPIRED_ACCESS_TOKEN);
    localStorage.setItem(constants.REFRESH_TOKEN, VALID_REFRESH_TOKEN);

    render(
        <BrowserRouter>
            <Routes>
                <Route path="" element={
                    <MockedProvider mocks={GRAPH_QL_MOCKS} addTypename={false}>
                        <api.LoginRequired>
                            <div data-testid='div'></div>
                        </api.LoginRequired>
                    </MockedProvider>
                }/>
                <Route path="auth/login" element={<LoginAndRegistrationView/>}/>
            </Routes>
        </BrowserRouter>
    );

    await waitFor(() => {
        expect(screen.getByTestId('div')).toBeInTheDocument();
    });
});

test('LoginRequired -> when user has expired access token and expired refresh token then redirect to login page', async () => {
    localStorage.setItem(constants.ACCESS_TOKEN, EXPIRED_ACCESS_TOKEN);
    localStorage.setItem(constants.REFRESH_TOKEN, EXPIRED_REFRESH_TOKEN);

    render(
        <BrowserRouter>
            <Routes>
                <Route path="" element={
                    <MockedProvider mocks={GRAPH_QL_MOCKS} addTypename={false}>
                        <api.LoginRequired>
                            <div data-testid='div'></div>
                        </api.LoginRequired>
                    </MockedProvider>
                }/>
                <Route path="auth/login" element={<LoginAndRegistrationView/>}/>
            </Routes>
        </BrowserRouter>
    );

    await waitFor(() => {
        expect(screen.getByTestId('loginView')).toBeInTheDocument();
    });
});

test('LoginRequired -> when user has invalid access token and valid refresh token then redirect to login page', async () => {
    localStorage.setItem(constants.ACCESS_TOKEN, INVALID_ACCESS_TOKEN);
    localStorage.setItem(constants.REFRESH_TOKEN, VALID_REFRESH_TOKEN);

    render(
        <BrowserRouter>
            <Routes>
                <Route path="" element={
                    <MockedProvider mocks={GRAPH_QL_MOCKS} addTypename={false}>
                        <api.LoginRequired>
                            <div data-testid='div'></div>
                        </api.LoginRequired>
                    </MockedProvider>
                }/>
                <Route path="auth/login" element={<LoginAndRegistrationView/>}/>
            </Routes>
        </BrowserRouter>
    );

    await waitFor(() => {
        expect(screen.getByTestId('loginView')).toBeInTheDocument();
    });
});

test('LoginRequired -> when user has never authenticated then redirect to login page', async () => {
    render(
        <BrowserRouter>
            <Routes>
                <Route path="" element={
                    <MockedProvider mocks={GRAPH_QL_MOCKS} addTypename={false}>
                        <api.LoginRequired>
                            <div data-testid='div'></div>
                        </api.LoginRequired>
                    </MockedProvider>
                }/>
                <Route path="auth/login" element={<LoginAndRegistrationView/>}/>
            </Routes>
        </BrowserRouter>
    );

    await waitFor(() => {
        expect(screen.getByTestId('loginView')).toBeInTheDocument();
    });
});