import { Button, Icon, IconButton } from 'actify';
import '../styles/components/TopBar.css';
import { Title } from './Title.jsx';
import "../styles/components/Title.css";

export default function TopBar({username, hideNavigation, logoutFunction}){
    const currentUserData = (
        username !== null ?
        <div className='flex flex-row items-center space-x-3 text-on-surface-variant'>
                <Title text={username} style="title-medium"/>
                <Button
                    onPress={() => {logoutFunction()}}
                    variant='filled' 
                    style={{fontFamily: "inter"}}
                >
                    <Icon>logout</Icon>
                    Wyloguj
                </Button>
        </div>
        :
        null
    )

    return (
        <div className="fixed bg-surface-container w-full flex flex-row items-center h-16 px-1 py-2 place-content-between">
            <div className='items-center flex-row flex gap-x-1'>
                <IconButton onPress={() => {hideNavigation()}}>
                    <Icon>menu</Icon>
                </IconButton>
                <Icon>sports_and_outdoors</Icon>
                <Title text={"FootballStats"} style="title-large"/>
            </div>
            {currentUserData}
        </div>
    );
}