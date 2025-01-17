import "../styles/components/background.css"

export function Background({children}) {
    return (
        <div className="background h-screen">
            {children}
        </div>
    )
}