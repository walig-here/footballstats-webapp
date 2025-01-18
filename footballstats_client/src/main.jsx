import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { ApolloProvider } from '@apollo/client'

import './styles/globals.css'
import App from "./App.jsx"
import {apiClient} from "./api_client.jsx"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ApolloProvider client={apiClient}>
        <App/>
    </ApolloProvider>
  </StrictMode>
)
