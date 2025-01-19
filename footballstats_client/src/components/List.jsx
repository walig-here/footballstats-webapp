import { Button, Icon, IconButton, Pagination } from "actify";
import Section from "./Section";
import { Body } from "./Body";
import { useState } from "react";
import Filters from "./filtering/Filters";
import { SortingPanel } from "./sorting/SortingPanel";

export function List({
    children, 
    iconName, 
    title, 
    subtitle, 
    closable, 
    onClose, 
    page, 
    maxPage, 
    setPage, 
    filters, 
    setFilters, 
    filteringAttributes,
    metricFiltersDisabled,
    metricSortingDisabled,
    sortingAttributes,
    sorting,
    setSorting
}){
    const [filteringPanelVisible, setFilteringPanelVisible] = useState();
    const [sortingPanelVisible, setSortingPanelVisible] = useState();

    const sortAndFilterButtons = (
        <div className="flex flex-row space-x-2.5">
            <Button 
                variant="filled"
                onPress={() => setSortingPanelVisible(prev => !prev)}
                isDisabled={sortingPanelVisible || filteringPanelVisible}
            >
                <Icon>sort</Icon>
                Sortuj
            </Button>
            <Button 
                variant="filled" 
                onPress={() => setFilteringPanelVisible(prev => !prev)}
                isDisabled={filteringPanelVisible || sortingPanelVisible}
            >
                <Icon>filter_list</Icon>
                Filtruj
            </Button>
            {
                closable &&
                <Button 
                    variant="tonal" 
                    onPress={() => onClose()}
                >
                    <Icon>close</Icon>
                </Button>
            }
        </div>
    )

    return (
    <div className="flex flex-row space-x-6">
        <Section 
            title={title}
            iconName={iconName} 
            subtitle={subtitle}
            topRightContent={sortAndFilterButtons}
            className="w-full"
        >
            <div className="flex flex-col">
                {children.length === 0 ? <Body text={"Brak wpisów!"}/> : children}
                <div className="flex flex-row items-center pt-4">
                    <IconButton onPress={() => setPage(1)}>
                        <Icon>first_page</Icon>
                    </IconButton>
                    <IconButton onPress={() => setPage(prevPage => prevPage > 1 ? prevPage - 1 : 1)}>
                        <Icon>navigate_before</Icon>
                    </IconButton>
                    <Body text={children.length === 0 ? "0 z 0" : `${page} z ${maxPage}`}/>
                    <IconButton onPress={() => setPage(prevPage => prevPage !== maxPage ? prevPage + 1 : maxPage)}>
                        <Icon>navigate_next</Icon>
                    </IconButton>
                    <IconButton onPress={() => setPage(maxPage)}>
                        <Icon>last_page</Icon>
                    </IconButton>
                </div>
            </div>
        </Section>
        {   
            filteringPanelVisible && 
            <Filters 
                onClose={() => setFilteringPanelVisible(false)}
                filters={filters}
                setFilters={setFilters}
                filteringAttributes={filteringAttributes}
                metricFiltersDisabled={metricFiltersDisabled}
            />
        }
        {
            sortingPanelVisible &&
            <SortingPanel
                sortingAttributes={sortingAttributes}
                sortingCriteria={sorting}
                setSortingCriteria={setSorting}
                metricCriteriaDisabled={metricFiltersDisabled}
                onClose={() => setSortingPanelVisible(false)}
            />
        }
    </div>
    )
}