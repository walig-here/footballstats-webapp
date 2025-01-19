import { Card, Divider, Icon } from "actify";
import { Title } from "./Title";
import { Body } from "./Body";



export default function Section({children, topRightContent, title, subtitle, iconName, className}) {
    return (
        <Card variant="outlined" className={`p-4 flex flex-col space-y-3 ${className}`}>
            <div className="flex flex-row place-content-between pb-3">
                <div className="flex flex-row space-x-3">
                    {iconName && <Icon>{iconName}</Icon>}
                    <div>
                        <Title text={title} style={"title-medium"}/>
                        <Body text={subtitle}/>
                    </div>
                </div>
                <div>
                    {topRightContent}
                </div>
            </div>
            <Divider/>
            <div className="pt-4 flex flex-col space-y-4">
                {children}
            </div>
        </Card>
    );
}