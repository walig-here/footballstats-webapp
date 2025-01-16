import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { ApolloProvider } from '@apollo/client'

import './styles/globals.css'
import Router from "./router/Router.jsx"
import {apiClient} from "./api_client.jsx"
import {Background} from "./components/Background.jsx"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ApolloProvider client={apiClient}>
      <Background>
        <Router/>
      </Background>
    </ApolloProvider>
  </StrictMode>
)
