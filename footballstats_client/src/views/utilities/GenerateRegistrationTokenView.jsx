import { Button, Icon, TextField } from "actify";
import ContentView from "../../components/ContentView";
import Section from "../../components/Section";
import { Body } from "../../components/Body";
import { useState } from "react";
import { LoginRequired, GENERATE_REGISTRATION_TOKEN, apiClient } from "../../api_client";
import { LoadingView } from "./LoadingView";
import { ACCESS_TOKEN, NOT_AUTHORIZED, UNAUTHORIZED_PAGE } from "../../constants";
import { useNavigate } from "react-router";

const GENERATE_TOKENS_DESC = "Wygeneruj jednorazowy token pozwalający na zarejestrowanie konta administratora."
const GENERATE_TOKEN_MANUAL = "Wygenerowany token zostanie umieszczony w poniższym polu i skopiowany do twojego schowka. Zachowaj go w bezpiecznym miejscu, gdyż po odświeżeniu storny nie będzie on więcej dostępny!"

export default function GenerateRegistrationTokenView() {
    const navigate = useNavigate();
    const [token, setToken] = useState("");
    const [loadingQuery, setLoadingQuery] = useState(false);

    const generateToken = async () => {
        setLoadingQuery(true);
        const accessToken = localStorage.getItem(ACCESS_TOKEN);
        if (!accessToken){
            navigate(UNAUTHORIZED_PAGE);
            return;
        }
        try {
            const {data} = await apiClient.query(
                {query: GENERATE_REGISTRATION_TOKEN, variables: {accessToken: accessToken}}
            );
            setToken(data.generateRegistrationToken);
            navigator.clipboard.writeText(data.generateRegistrationToken);
        } catch (err) {
            console.log(`Error occurred while generating registration token. Error\n${err}`);
            if (err.cause.message === NOT_AUTHORIZED)
                navigate(UNAUTHORIZED_PAGE);
        }
        setLoadingQuery(false);
    }

    return (
        <LoginRequired>
            <ContentView title="Wygeneruj token rejestracji">
                <Section title={"Generator tokenów"} iconName="key_vertical" subtitle={GENERATE_TOKENS_DESC}>
                    {
                        loadingQuery ?
                        <LoadingView/>
                        :
                        <>
                            <Body text={GENERATE_TOKEN_MANUAL}/>
                            <TextField 
                                variant="outlined" 
                                label="Wygenerowany token"
                                value={token}
                                isReadOnly={true}
                            />
                            <Button variant="filled" onPress={() => generateToken()}>
                                <Icon>add_circle_outline</Icon>
                                Wygeneruj token
                            </Button>
                        </>
                    }
                </Section>
            </ContentView>
        </LoginRequired>
    );
}