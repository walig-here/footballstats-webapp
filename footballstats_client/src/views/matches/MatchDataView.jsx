import { useNavigate, useParams } from "react-router";
import ContentView from "../../components/ContentView";
import { useMutation, useQuery } from "@apollo/client";
import { GET_MATCH, REMOVE_EVENT_FROM_MATCH, requestMutation } from "../../api_client";
import { LoadingView } from "../utilities/LoadingView";
import { Button, Divider, Icon, TabItem, Tabs } from "actify";
import { DataRangeControl } from "../../components/DataRangeControl";
import { useContext, useEffect, useState } from "react";
import Section from "../../components/Section";
import { Body } from "../../components/Body";
import { ListItem } from "../../components/ListItem";
import { ModalContext } from "../../components/modals/ModalManager";

const GET_MATCH_QUERY = (matchId) => [
    GET_MATCH,
    {variables: {id: matchId}, fetchPolicy: "network-only"}
];

function MatchDataView() {
    const navigate = useNavigate();
    const {id} = useParams();
    const [currentTab, setCurrentTab] = useState(`/match/${id}/data`);
    const {loading, data, error, refetch} = useQuery(...GET_MATCH_QUERY(Number.parseInt(id)));
    const modalContext = useContext(ModalContext);
    const [removeEventMutation, removeEventResponse] = useMutation(REMOVE_EVENT_FROM_MATCH);


    useEffect(() => {
        navigate(currentTab);
    }, [currentTab])

    const removeEvent = (eventId) => {
        requestMutation(
            {eventId: Number.parseInt(eventId)},
            removeEventMutation,
            "Usunięto zdarzenie!",
            "Nie udało się usunąć zdarzenia!",
            "removeEventFromMatch"
        )
        refetch({fetchPolicy: "network-only"});
    }

    if (loading || removeEventResponse.loading)
        return <LoadingView/>;

    if (error)
        console.log(error);
    if (error){
        return <ContentView title={"Mecz nie istnieje"}></ContentView>;
    }

    return (
        <ContentView title={`${data.match.teamsScores[0].teamName} vs ${data.match.teamsScores[1].teamName}`}>
            <Tabs onSelectionChange={(e) => setCurrentTab(e)}>
                <TabItem title={"Dane"} key={`/match/${id}/data`}></TabItem>
                <TabItem title={"Uczestnicy"} key={`/match/${id}/participants`}></TabItem>
            </Tabs>
            <Section 
                title={data.match.leagueSeason.league.name}
                subtitle={data.match.leagueSeason.name}
                topRightContent={
                    <Body text={data.match.leagueSeason.league.countryOfOrigin.name}/>
                }
            >
                <div className="flex flex-row space-x-16 place-items-center justify-center">
                    <div className="w-1/3 place-items-center">
                        <Body 
                            text={data.match.teamsScores[0].teamName}
                            style="text-base font-medium"
                        />
                    </div>
                    <div className="flex flex-col place-items-center w-1/3">
                        <Body 
                            text={`${data.match.teamsScores[0].score} : ${data.match.teamsScores[1].score}`}
                            style="text-on-surface text-5xl"
                        />
                        <Body 
                            text={data.match.gameDate}
                            style="text-on-surface-variant text-base font-medium"
                        />
                    </div>
                    <div className="w-1/3 place-items-center">
                        <Body 
                            text={data.match.teamsScores[1].teamName}
                            style="text-base font-medium"
                        />
                    </div>
                </div>
            </Section>
            <Section
                title={"Zdarzenia z meczu"}
                iconName={"local_activity"}
                subtitle={"Przeglądaj chronologiczny spis zdarzeń, które wystąpiły w meczu."}
                topRightContent={
                    <Button
                        variant="filled"
                        onPress={() => setCurrentTab(`/form/add_event/${id}`)}
                    >
                        <Icon>add_circle</Icon>
                        Dodaj zdarzenie
                    </Button>
                }
            >
                {
                    data.match.events.map((event) => (
                        <ListItem
                            topText={`${event.occurrenceMinute} '`}
                            mainText={event.eventType.name}
                            bottomText={`${event.player.name} ${event.player.surname}`}
                            key={event.id}
                            onDelete={() => modalContext.openModal(
                                "Czy na pewno chcesz usunąć zdarzenie?",
                                () => removeEvent(event.id)
                            )}
                        />
                    ))
                }
            </Section>
        </ContentView>
    );
}

export default MatchDataView;