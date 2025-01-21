import { Autocomplete, Button, Icon, IconButton, SegmentedButton } from 'actify'
import ContentView from '../../components/ContentView';
import { CREATE_MATCH_MUTATION, LoginRequired, requestMutation } from '../../api_client';
import { useEffect, useState } from 'react';
import { MatchOwnDataForm } from '../../components/forms/MatchOwnDataForm';
import Section from '../../components/Section';
import { LeagueForm } from '../../components/forms/LeagueForm';
import { NewExistingSelection } from '../../components/NewExistingSelection';
import { LeagueSelector } from '../../components/selections/LeagueSelector';
import { SeasonForm } from '../../components/forms/SeasonForm';
import { SeasonSelector } from '../../components/selections/SeasonSelector';
import { TeamSelector } from '../../components/selections/TeamSelector';
import { AddPlayerToMatchForm } from '../../components/forms/AddPlayerToMatchForm';
import { useMutation } from '@apollo/client';
import { LoadingView } from '../utilities/LoadingView';
import { Body } from '../../components/Body';
import { serializeTeamPlayers } from '../../data_processing';

function AddPlayerForm({minutesPlayed, playerKey, setMinutesPlayed, setPlayerKey, onDelete}) {
    return (
        <Section
            title={"Dodaj zawodnika do meczu"}
            subtitle={"Wybierz zawodnika i określ jego czas gry"}
            topRightContent={
                <Button onPress={onDelete} variant='filled'>
                    <Icon>delete</Icon>
                </Button>
            }
        >
            <AddPlayerToMatchForm
                minutesPlayed={minutesPlayed}
                playerKey={playerKey}
                setMinutesPlayed={setMinutesPlayed}
                setPlayerKey={setPlayerKey}
            />
        </Section>
    )
}

export default function AddMatchView() {
    const [createMatchMutation, {data, loading, error}] = useMutation(CREATE_MATCH_MUTATION)
    const [ownData, setOwnData] = useState(null);
    const [league, setLeague] = useState("");
    const [season, setSeason] = useState("");
    const [homeTeam, setHomeTeam] = useState("");
    const [awayTeam, setAwayTeam] = useState("");
    const [homeTeamPlayers, setHomeTeamPlayers] = useState({
        formId: 1, players: []
    });
    const [awayTeamPlayers, setAwayTeamPlayers] = useState({
        formId: 1, players: []
    });

    const addPlayer = (home) => {
        const newPlayer = {
            key: home ? homeTeamPlayers.formId : awayTeamPlayers.formId,
            playerId: "",
            minutesPlayed: "0",
        };
        if (home){
            setHomeTeamPlayers(prev => ({
                formId: prev.formId + 1,
                players: [newPlayer, ...prev.players]
            }));
        }
        else {
            setAwayTeamPlayers(prev => ({
                formId: prev.formId + 1,
                players: [newPlayer, ...prev.players]
            }));
        }
    };
    const removePlayer = (home, key) => {
        if (home) {
            setHomeTeamPlayers(prev => ({
                ...prev,
                players: prev.players.filter(player => player.key != key)
            }));
        } else {
            setAwayTeamPlayers(prev => ({
                ...prev,
                players: prev.players.filter(player => player.key != key)
            }));
        }
    }

    const canShowSubmitButton = () => {
        return [
            ownData, league, season, homeTeam, awayTeam, 
            homeTeamPlayers.players.length,
            awayTeamPlayers.players.length,
            homeTeamPlayers.players.every(player => Object.values(player).every(Boolean)),
            awayTeamPlayers.players.every(player => Object.values(player).every(Boolean)),
        ].every(Boolean);
    }

    const createMatch = async () => {
        await requestMutation(
            {
                gameDate: ownData.date,
                leagueSeasonId: Number.parseInt(season),
                homeTeamId: Number.parseInt(homeTeam),
                awayTeamId: Number.parseInt(awayTeam),
                homeTeamPlayers: serializeTeamPlayers(homeTeamPlayers.players),
                awayTeamPlayers: serializeTeamPlayers(awayTeamPlayers.players)
            },
            createMatchMutation,
            "Dodano mecz",
            "Nie udało się dodać meczu!",
            "createMatch"
        )
    }

    if (loading)
        return <LoadingView/>;
    if (error){
        console.log(error)
    }

    return (
        <LoginRequired>
            <ContentView title={"Dodawanie meczu"}>
                {
                    (error || data?.createMatch?.errors?.length > 0)
                    &&
                    <Body 
                        text={
                            data?.createMatch?.errors ? 
                            data.createMatch.errors.map(err => err.messages.join("\n")) : 
                            error.cause.message
                        }
                        style={"text-error"}
                    />
                }
                <Section 
                    title={"Dane meczu"} 
                    subtitle={"Wprowadź dane nowego meczu"} 
                    iconName={"description"}
                    key="match-form"
                >
                    <MatchOwnDataForm matchOwnData={ownData} setMatchOwnData={setOwnData}/>
                    <LeagueSelector
                        nameIsKey={false}
                        leagueKey={league}
                        setLeagueKey={leagueId => setLeague(leagueId)}
                        setSeasonKey={seasonId => setSeason(seasonId)}
                        seasonKey={season}
                    />
                    <TeamSelector
                        label={"Drużyna gospodarzy"}
                        nameIsKey={false}
                        teamKey={homeTeam}
                        setTeamKey={teamId => setHomeTeam(teamId)}
                    />
                    <TeamSelector
                        label={"Drużyna gości"}
                        nameIsKey={false}
                        teamKey={awayTeam}
                        setTeamKey={teamId => setAwayTeam(teamId)}
                    />
                </Section>
                <Section
                    title={"Zawodnicy drużyny gospodarzy"}
                    iconName={"group"}
                    subtitle={"Zdefiniuj przynajmniej jednego zawodnika reprezentującego drużynę gospodarzy."}
                >
                    <Button 
                        variant='outlined'
                        onPress={() => addPlayer(true)}
                    >
                        <Icon>add_circle</Icon>
                        Dodaj zawodnika
                    </Button>{
                    homeTeamPlayers.players.map(playerData => (
                        <AddPlayerForm
                            onDelete={() => removePlayer(true, playerData.key)}
                            minutesPlayed={playerData.minutesPlayed}
                            key={playerData.key}
                            playerKey={playerData.playerId}
                            setMinutesPlayed={
                                (newMinutesPlayed) => setHomeTeamPlayers(prev => ({
                                    ...prev,
                                    players: prev.players.map(player => (
                                        player.key === playerData.key ?
                                        {...player, minutesPlayed: newMinutesPlayed}:
                                        player
                                    ))}
                                ))
                            }
                            setPlayerKey={
                                (newPlayerKey) => setHomeTeamPlayers(prev => ({
                                    ...prev,
                                    players: prev.players.map(player => (
                                        player.key === playerData.key ?
                                        {...player, playerId: newPlayerKey}:
                                        player
                                    ))}
                                ))
                            }
                        />
                    ))
                }</Section>
                <Section
                    title={"Zawodnicy drużyny gości"}
                    iconName={"group"}
                    subtitle={"Zdefiniuj przynajmniej jednego zawodnika reprezentującego drużynę gości."}
                >
                    <Button 
                        variant='outlined'
                        onPress={() => addPlayer(false)}
                    >
                        <Icon>add_circle</Icon>
                        Dodaj zawodnika
                    </Button>{
                    awayTeamPlayers.players.map(playerData => (
                        <AddPlayerForm
                            onDelete={() => removePlayer(false, playerData.key)}
                            minutesPlayed={playerData.minutesPlayed}
                            key={playerData.key}
                            playerKey={playerData.playerId}
                            setMinutesPlayed={
                                (newMinutesPlayed) => setAwayTeamPlayers(prev => ({
                                    ...prev,
                                    players: prev.players.map(player => (
                                        player.key === playerData.key ?
                                        {...player, minutesPlayed: newMinutesPlayed}:
                                        player
                                    ))}
                                ))
                            }
                            setPlayerKey={
                                (newPlayerKey) => setAwayTeamPlayers(prev => ({
                                    ...prev,
                                    players: prev.players.map(player => (
                                        player.key === playerData.key ?
                                        {...player, playerId: newPlayerKey}:
                                        player
                                    ))}
                                ))
                            }
                        />
                    ))
                }</Section>
                {
                    canShowSubmitButton() &&
                    <Button variant='filled' onPress={() => createMatch()}>
                        <Icon>check</Icon>
                        Dodaj mecz
                    </Button>
                }
            </ContentView>
        </LoginRequired>
    );
}