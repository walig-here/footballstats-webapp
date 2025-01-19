import { useState, createContext, useEffect } from "react";
import Router from "./router/Router.jsx"
import { DEFAULT_USERNAME, UNAUTHENTICATED_USERNAME, USERNAME } from "./constants.js";
import {ToastContainer} from 'react-toastify';
import {GET_DATE_RANGE, logOut} from './api_client.jsx'
import { useQuery } from "@apollo/client";
import { LoadingView } from "./views/utilities/LoadingView.jsx";

export const UserContext = createContext(null);
export const DateRangeContext = createContext(null);

export default function App() {
    const serverDateRange = useQuery(GET_DATE_RANGE);
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
        minStartDate: "0001-01-01",
        maxEndDate: "9999-01-01",
        startDate: "0001-01-01",
        endDate: "9999-01-01",
        setRange: (start, end) => { 
            setDateRange(prev => ({...prev, startDate: start, endDate: end})) 
        }
    });

    useEffect(() => {
        if (serverDateRange.error || !serverDateRange.data)
            return;
        console.log(serverDateRange)

        const newStartDate = (
            dateRange.startDate >= serverDateRange.data.dataDateRange[0] ?
            dateRange.startDate : serverDateRange.data.dataDateRange[0]
        );
        const newEndDate = (
            dateRange.endDate <= serverDateRange.data.dataDateRange[1] ?
            dateRange.endDate : serverDateRange.data.dataDateRange[1]
        )
        setDateRange(prev => ({
            ...prev,
            startDate: newStartDate,
            endDate: newEndDate,
            minStartDate: serverDateRange.data.dataDateRange[0],
            maxEndDate: serverDateRange.data.dataDateRange[1]
        }));
    }, [serverDateRange.data])

    if (serverDateRange.loading)
        return <LoadingView/>

    return (
        <DateRangeContext.Provider value={dateRange}>
            <ToastContainer position="top-right"/>
            <UserContext.Provider value={user}>
                <Router/>
            </UserContext.Provider>
        </DateRangeContext.Provider>
    )
}