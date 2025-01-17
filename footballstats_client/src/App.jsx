import { useState, createContext } from "react";
import Router from "./router/Router.jsx"

export const UsernameContext = createContext(null);
export const DateRangeContext = createContext(null);

export default function App() {
    const [username, setUsername] = useState(null);
    const [dateRange, setDateRange] = useState({
        minStartDate: null,
        maxEndDate: null,
        startDate: null,
        endDate: null
    });

    return (
        <DateRangeContext.Provider value={dateRange}>
            <UsernameContext.Provider value={username}>
                <Router/>
            </UsernameContext.Provider>
        </DateRangeContext.Provider>
    )
}