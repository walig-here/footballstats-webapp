import { useState, createContext } from "react";
import Router from "./router/Router.jsx"
import { DEFAULT_USERNAME, UNAUTHENTICATED_USERNAME, USERNAME } from "./constants.js";
import {logOut} from './api_client.jsx'

export const UserContext = createContext(null);
export const DateRangeContext = createContext(null);

export default function App() {
    const DEFAULT_USER = {
        username: localStorage.getItem(USERNAME) ? localStorage.getItem(USERNAME) : DEFAULT_USERNAME,
        logoutFunction: () => {
            setUser(previousUser => {
                return {
                    ...previousUser,
                    username: UNAUTHENTICATED_USERNAME,
                }
            });
            logOut();
            localStorage.removeItem(USERNAME);
        },
        setUsername: (newUsername) => {
            setUser(previousUser => {
                return {
                    ...previousUser,
                    username: newUsername,
                }
            });
            localStorage.setItem(USERNAME, newUsername);
        }
    };

    const [user, setUser] = useState(DEFAULT_USER);
    const [dateRange, setDateRange] = useState({
        minStartDate: null,
        maxEndDate: null,
        startDate: null,
        endDate: null
    });

    return (
        <DateRangeContext.Provider value={dateRange}>
            <UserContext.Provider value={user}>
                <Router/>
            </UserContext.Provider>
        </DateRangeContext.Provider>
    )
}