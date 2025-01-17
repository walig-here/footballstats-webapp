import {Headline} from "./Headline"

export default function ContentView({children, title}) {
    return (
        <div className="p-4 h-screen bg-surface flex w-screen flex-col text-on-surface space-y-4">
            <Headline text={title} style="headline-large px-1 py-2"/>
            {children}
        </div>
    )
}