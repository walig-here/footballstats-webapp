import { ApolloClient, InMemoryCache, gql, useMutation } from '@apollo/client';
import {data, useLocation, useNavigate} from 'react-router';

import * as constants from "./constants.js"
import { useEffect, useState } from 'react';
import { LoadingView } from './views/utilities/LoadingView.jsx';
import { getMatchEventWithName, getMetricWithName, isAuthenticated, isOwner } from './data_processing.js';
import { toast } from 'react-toastify';

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

function calculateTeamMetricForDataSeries(dataSeries, metricName) {
  let queryBody = ``;
  dataSeries.forEach(dataPoint => {
    queryBody += `
      ${dataPoint.stringify()}: team(id: $teamId){
        calculateMetric(
          startDate: $startDate,
          endDate: $endDate,
          match: $match,
          metric: {
            metricType: ${getMetricWithName(metricName)},
            targetMatchEvent: ${getMatchEventWithName(dataPoint.eventName)},
            metricParams: [${dataPoint.stringifyParams()}]
          }
        )
      }`;
  });
  
  return gql`
  query(
    $teamId: Int!
    $startDate: Date!,
    $endDate: Date!,
    $match: Int!,
  ){
    ${queryBody}
  }`
}
export const QUERY_TEAM_CALCULATE_METRIC_FOR_DATA_SERIES = (teamId, startDate, endDate, match, team, metricName, dataSeries) => [
  calculateTeamMetricForDataSeries(dataSeries, metricName),
  {
    variables: {
      teamId: teamId,
      startDate: startDate,
      endDate: endDate,
      match: match,
    }
  }
]

function calculatePlayerMetricForDataSeries(dataSeries, metricName) {
  let queryBody = ``;
  dataSeries.forEach(dataPoint => {
    queryBody += `
      ${dataPoint.stringify()}: player(id: $playerId){
        calculateMetric(
          startDate: $startDate,
          endDate: $endDate,
          match: $match,
          team: $team,
          metric: {
            metricType: ${getMetricWithName(metricName)},
            targetMatchEvent: ${getMatchEventWithName(dataPoint.eventName)},
            metricParams: [${dataPoint.stringifyParams()}]
          }
        )
      }`;
  });
  
  return gql`
  query(
    $playerId: Int!
    $startDate: Date!,
    $endDate: Date!,
    $match: Int!,
    $team: Int!,
  ){
    ${queryBody}
  }`
}
export const QUERY_PLAYER_CALCULATE_METRIC_FOR_DATA_SERIES = (playerId, startDate, endDate, match, team, metricName, dataSeries) => [
  calculatePlayerMetricForDataSeries(dataSeries, metricName),
  {
    variables: {
      playerId: playerId,
      startDate: startDate,
      endDate: endDate,
      match: match,
      team: team,
    }
  }
]

function calculatePlayerMetricHistoryForDataSeries(dataSeries, metricName) {
  let queryBody = ``;
  dataSeries.forEach(dataPoint => {
    queryBody += `
      ${dataPoint.stringify()}: player(id: $playerId){
        metricHistory(
          startDate: $startDate,
          endDate: $endDate,
          metric: {
            metricType: ${getMetricWithName(metricName)},
            targetMatchEvent: ${getMatchEventWithName(dataPoint.eventName)},
            metricParams: [${dataPoint.stringifyParams()}]
          }
        ) {
          value,
          time
        }
      }`;
  });
  
  return gql`
  query(
    $playerId: Int!
    $startDate: Date!,
    $endDate: Date!,
  ){
    ${queryBody}
  }`
}
export const QUERY_PLAYER_METRIC_HISTORY_FOR_DATA_SERIES = (playerId, startDate, endDate, metricName, dataSeries) => [
  calculatePlayerMetricHistoryForDataSeries(dataSeries, metricName),
  {
    variables: {
      playerId: playerId,
      startDate: startDate,
      endDate: endDate,
    }
  }
]

function calculateTeamMetricHistoryForDataSeries(dataSeries, metricName) {
  let queryBody = ``;
  dataSeries.forEach(dataPoint => {
    queryBody += `
      ${dataPoint.stringify()}: team(id: $teamId){
        metricHistory(
          startDate: $startDate,
          endDate: $endDate,
          metric: {
            metricType: ${getMetricWithName(metricName)},
            targetMatchEvent: ${getMatchEventWithName(dataPoint.eventName)},
            metricParams: [${dataPoint.stringifyParams()}]
          }
        ) {
          value,
          time
        }
      }`;
  });
  
  return gql`
  query(
    $teamId: Int!
    $startDate: Date!,
    $endDate: Date!,
  ){
    ${queryBody}
  }`
}
export const QUERY_TEAM_METRIC_HISTORY_FOR_DATA_SERIES = (teamId, startDate, endDate, metricName, dataSeries) => [
  calculateTeamMetricHistoryForDataSeries(dataSeries, metricName),
  {
    variables: {
      teamId: teamId,
      startDate: startDate,
      endDate: endDate,
    }
  }
]

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

export const GET_DATE_RANGE = gql`
{
  dataDateRange
}
`

export const GET_TEAM = gql`
query (
  $id: Int!
) {
  team(id: $id) {
    name,
    countryOfOrigin {
      name
    }
  }
}`;
export const buildTeamQuery = (id) => [
  GET_TEAM,
  {
    variables: {id: id}
  }
];

export const GET_PLAYER = gql`
query (
  $id: Int!
) {
  player(id: $id) {
    name,
    surname,
    nickname,
    countryOfOrigin {
      name
    }
  }
}
`;
export const buildPlayerQuery = (id) => [
  GET_PLAYER,
  {
    variables: {id: id}
  }
];

export const GET_MATCH = gql`
query(
  $id: Int!,
){
  match(id: $id){
    gameDate,
    teamsScores{
      score,
      teamId,
      teamName
    },
    leagueSeason {
      name,
      league {
        name,
        countryOfOrigin {
          id,
          name
        }
      }
    },
    events {
      occurrenceMinute,
      eventType {
        name
      },
      player {
        name,
        surname,
      }
    }
  }
}
`

export const GET_MATCH_CRUCIAL_DATA = gql`
query(
  $id: Int!,
){
  match(id: $id){
    gameDate,
    teamsScores{
      score,
      teamId,
      teamName
    },
  }
}
`

export const GET_PLAYERS = gql`
query(
  $page: Int!,
  $textualFilters: [TextualFilterType],
  $metricFilters: [MetricFilterType],
  $sorting: SortingType,
  $startDate: Date!,
  $endDate: Date!
  $match: Int,
  $team: Int
){
  playersList(
    page: $page, 
    textualFilters: $textualFilters, 
    sorting: $sorting,
    metricFilters: $metricFilters,
    startDate: $startDate,
    endDate: $endDate,
    playingInMatch: $match,
    representingTeam: $team
  ) {
    id,
    name,
    surname,
    nickname,
    countryOfOrigin {
      name
    }
  },
  playerListLength: playersList(
    page: -1, 
    textualFilters: $textualFilters, 
    metricFilters: $metricFilters,
    startDate: $startDate
    endDate: $endDate,
    playingInMatch: $match,
    representingTeam: $team
  ) {
    id
  },
  playerSortingAttributes,
  playerFilteringAttributes,
}
`

export const GET_TEAMS = gql`
query(
  $page: Int!,
  $textualFilters: [TextualFilterType],
  $metricFilters: [MetricFilterType],
  $sorting: SortingType,
  $startDate: Date!,
  $endDate: Date!,
  $matchId: Int,
  $playerId: Int
){
  teamsList(
    page: $page, 
    textualFilters: $textualFilters, 
    sorting: $sorting,
    metricFilters: $metricFilters,
    startDate: $startDate
    endDate: $endDate,
    playingInMatch: $matchId,
    representedByPlayer: $playerId
  ) {
    id,
    name,
    countryOfOrigin {
      name
    }
  },
  teamsListLength: teamsList(
    page: -1, 
    textualFilters: $textualFilters, 
    metricFilters: $metricFilters,
    startDate: $startDate
    endDate: $endDate,
    playingInMatch: $matchId,
    representedByPlayer: $playerId
  ) {
    id
  },
  teamSortingAttributes,
  teamFilteringAttributes,
}
`

export const GET_MATCHES = gql`
query(
  $page: Int!,
  $textualFilters: [TextualFilterType],
  $metricFilters: [MetricFilterType],
  $sorting: SortingType,
  $startDate: Date!,
  $endDate: Date!
  $teamId: Int,
  $playerId: Int
){
  matchesList(
    page: $page, 
    textualFilters: $textualFilters, 
    sorting: $sorting,
    metricFilters: $metricFilters,
    startDate: $startDate
    endDate: $endDate,
    teamInvolved: $teamId,
    playerInvolved: $playerId
  ) {
    id,
    gameDate,
    teamsScores{
      score,
      teamName
    },
    leagueSeason {
      league {
        name
      }
    }
  },
  matchSortingAttributes,
  matchFilteringAttributes,
  matchListLength: matchesList(
    page: -1, 
    textualFilters: $textualFilters, 
    metricFilters: $metricFilters,
    startDate: $startDate
    endDate: $endDate,
    teamInvolved: $teamId,
    playerInvolved: $playerId
  ) {
    id
  }
}
`

export const GET_ADMINS_LIST = gql`
query(
  $accessToken: String!,
  $page: Int!,
  $textualFilters: [TextualFilterType],
  $sorting: SortingType,
){
  usersList(
    page: $page, 
    token: $accessToken, 
    textualFilters: $textualFilters, 
    sorting: $sorting
  ) {
    id,
    username,
    hasCreatePermission,
    hasModifyPermission,
    hasDeletePermission
  },
  usersListLength(token: $accessToken),
  userFilteringAttributes,
  userSortingAttributes
}
`

export const REMOVE_ADMIN = gql`
mutation(
  $accessToken: String!,
  $username: String!
){
  removeUser(token: $accessToken, username: $username){
    ok,
    messages
  }
}
`

export const GRANT_PERMISSION = gql`
mutation(
  $accessToken: String!,
  $username: String!,
  $permission: PermissionType!
){
  grantPermission(token: $accessToken, username: $username, permission: $permission){
    ok,
    messages
  }
}
`

export const REVOKE_PERMISSION = gql`
mutation(
  $accessToken: String!,
  $username: String!,
  $permission: PermissionType!
){
  revokePermission(token: $accessToken, username: $username, permission: $permission){
    ok,
    messages
  }
}
`

export const USER_FILTERING_ATTRIBUTES = gql`
{
  userFilteringAttributes
}
`

const GET_ALL_USERNAMES = gql`
query(
  $accessToken: String!,
){
  usersList(
    page: -1,
    token: $accessToken,
	) {
    username,
  },
}
`

const GET_ALL_PLAYERS_NAMES = gql`
query(
  $startDate: Date!,
  $endDate: Date!,
){
  playersList(
    startDate: $startDate,
    endDate: $endDate,
    page: -1,
	) {
    id,
    name
  },
}
`

const GET_ALL_PLAYERS_SURNAMES = gql`
query(
  $startDate: Date!,
  $endDate: Date!,
){
  playersList(
    startDate: $startDate,
    endDate: $endDate,
    page: -1,
  ) {
    id,
    surname
  },
}
`

export const GET_ALL_TEAMS = gql`
query(
  $startDate: Date!,
  $endDate: Date!,
){
  teamsList(
    startDate: $startDate,
    endDate: $endDate,
    page: -1,
	) {
    id,
    name
  },
}
`

export const GET_ALL_COUNTRIES = gql`
{
  countryList{
    id,
  	name  
  }
}
`

export const GET_ALL_LEAGUES = gql`
{
  leaguesList{
    id,
  	name  
  }
}
`

export const GET_ALL_EVENT_TYPES = gql`
{
  eventTypesList{
    id,
    name
  }
}
`


export const CURRENT_USER = {
    name: null
}


export const apiClient = new ApolloClient({
    uri: constants.API_SERVER_URL,
    cache: new InMemoryCache(),
});


export async function requestMutation(variables, mutation, successMessage, errorMessage){
    const accessToken = localStorage.getItem(constants.ACCESS_TOKEN);
    try{
        await mutation({variables: {
            accessToken: accessToken, ...variables
        }});
        toast.success(successMessage);
    } catch (error) {
        console.log(`Error occurred while executing mutation. Error\n${error}`);
        toast.error(errorMessage);
    }
}


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

export function SuperUserRequired({children}) {
    const navigate = useNavigate();
    const [isAuthorizing, setIsAuthorizing] = useState(true);

    useEffect(() => {
        if (!isOwner(localStorage.getItem(constants.USERNAME))){
            navigate(constants.UNAUTHORIZED_PAGE);
        }
        setIsAuthorizing(false);
    });

    if (isAuthorizing)
        return <LoadingView/>;

    return (
        <LoginRequired>
            {children}
        </LoginRequired>
    )
}


export async function getAllPlayersNames(startDate, endDate) {
    try {
        const response = await apiClient.query({
            query: GET_ALL_PLAYERS_NAMES,
            variables: {startDate: startDate, endDate: endDate}
        });
        return response.data.playersList.map((player) => player.name);
    } catch (error) {
        console.log(error)
        return [];
    }
}

export async function getAllPlayersSurnames(startDate, endDate) {
    try {
        const response = await apiClient.query({
            query: GET_ALL_PLAYERS_SURNAMES,
            variables: {startDate: startDate, endDate: endDate}
        });
        return response.data.playersList.map((player) => player.surname);
    } catch (error) {
        console.log(error)
        return [];
    }
}


export async function getAllUsernames() {
    try {
        const response = await apiClient.query({
            query: GET_ALL_USERNAMES,
            variables: {accessToken: localStorage.getItem(constants.ACCESS_TOKEN)}
        });
        return response.data.usersList.map((user) => user.username);
    } catch (error) {
        console.log(error)
        return [];
    }
}

export async function getAllTeamsNames(startDate, endDate) {
    try {
        const response = await apiClient.query({
            query: GET_ALL_TEAMS,
            variables: {startDate: startDate, endDate: endDate}
        });
        return response.data.teamsList.map((team) => team.name);
    } catch (error) {
        console.log(error)
        return [];
    }
}

export async function getAllCountriesNames() {
    try {
        const response = await apiClient.query({query: GET_ALL_COUNTRIES,});
        return response.data.countryList.map((country) => country.name);
    } catch (error) {
        console.log(error)
        return [];
    }
}

export async function getAllLeagueNames() {
    try {
        const response = await apiClient.query({query: GET_ALL_LEAGUES,});
        return response.data.leaguesList.map((league) => league.name);
    } catch (error) {
        console.log(error)
        return [];
    }
}

export async function getAllEventTypes() {
    try {
        const response = await apiClient.query({query: GET_ALL_EVENT_TYPES,});
        return response.data.eventTypesList;
    } catch (error) {
        console.log(error)
        return [];
    }
}