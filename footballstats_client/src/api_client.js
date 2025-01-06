import { gql } from '@apollo/client'

import API_SERVER_URL from "./constants.js"


const apiClient = new ApolloClient({
    uri: API_SERVER_URL,
    cache: new InMemoryCache(),
});

GET_LIST_OF_PLAYERS = gql``

GET_LIST_OF_TEAMS = gql``

GET_LIST_OF_MATCHES = gql``