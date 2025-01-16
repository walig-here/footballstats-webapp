import { CircularProgress } from 'actify'
import {Headline} from '../../components/Headline.jsx'


export function LoadingView() {
    return (
        <div
            className='w-full flex-col justify-items-center place-content-center gap-y-14'
        >
            <Headline data-testid='headline' text={"Ładowanie"} style={"headline-large"}/>
            <CircularProgress
                data-testid='loading-circle'
                aria-label="circular progress"
                isIndeterminate={true}
                size='xl'
            />
        </div>
    )
}