import { useMutation, useQuery } from "@apollo/client";
import ContentView from "../../components/ContentView";
import {List} from "../../components/List";
import { GET_ADMINS_LIST, GRANT_PERMISSION, REMOVE_ADMIN, requestMutation, REVOKE_PERMISSION, SuperUserRequired } from "../../api_client";
import { ACCESS_TOKEN, ERROR_OCCURRED_TOAST, PermissionTypes, TOKEN_EXPIRED_ERROR } from "../../constants";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";
import { Checkbox, Divider, Icon, IconButton } from "actify";
import { useEffect, useState } from "react";
import {ConfirmModal} from "../../components/modals/ConfirmModal"
import { convertFiltersToBackendFormat, convertSortingToBackendFormat } from "../../data_processing";
import { toast } from "react-toastify";

const ALL_ADMINS_LIST_DESC = "Zarządzaj wszystkimi administratorami zarejestrowanymi w systemie.";
const CLOSED_MODAL_DATA = {
    open: false,
    onConfirm: () => {},
    message: null
};
const GET_LIST_QUERY = (page, filters, sorting) => {
    const [textualFilters] = convertFiltersToBackendFormat(filters);
    return [
        GET_ADMINS_LIST,
        {
            variables: {
                accessToken: localStorage.getItem(ACCESS_TOKEN),
                page: page - 1,
                textualFilters: textualFilters,
                sorting: convertSortingToBackendFormat(sorting)
            },
            fetchPolicy: "cache-and-network"
        }
    ]
};


function AdminListItem({user, onDelete, onEdit, onEditPermissionChange, onCreatePermissionChange, onDeletePermissionChange}) {
    return (
        <div>
            <div className="flex flex-row items-center px-2 py-4 place-content-between">
                <Body text={user.username} style={"text-base"}/>
                <div className="flex flex-row space-x-2.5 items-center">
                    <Checkbox 
                        isSelected={user.hasCreatePermission}
                        onChange={onCreatePermissionChange}
                    >Dodający</Checkbox>
                    <Checkbox
                        isSelected={user.hasModifyPermission}
                        onChange={onEditPermissionChange}
                    >Edytujący</Checkbox>
                    <Checkbox 
                        isSelected={user.hasDeletePermission}
                        onChange={onDeletePermissionChange}
                    >Usuwający</Checkbox>
                    <IconButton onPress={onDelete}>
                        <Icon className="text-on-surface-variant">delete</Icon>
                    </IconButton>
                </div>
            </div>
            <Divider/>
        </div>
    );
}


export default function AllAdminsListView() {
    const [page, setPage] = useState(1);
    const [filters, setFilters] = useState([]);
    const [sorting, setSorting] = useState({
        direction: "ASCENDING", 
        targetAttributeName: "login", 
        metric: {
            targetEventType: null,
            metricParams: []
        }
    })
    const [modalData, setModalData] = useState(CLOSED_MODAL_DATA);
    const listQuery = useQuery(...GET_LIST_QUERY(page, filters, sorting));

    const [deleteAdminMutation, deleteAdminMutationResponse] = useMutation(REMOVE_ADMIN);
    const [grantPermissionMutation, grantPermissionResponse] = useMutation(GRANT_PERMISSION);
    const [revokePermissionMutation, revokePermissionResponse] = useMutation(REVOKE_PERMISSION);

    const isLoading = [
        listQuery.loading, 
        deleteAdminMutationResponse.loading, 
        grantPermissionResponse.loading, 
        revokePermissionResponse.loading
    ].some(Boolean);
    const errors = [
        listQuery.error, 
        deleteAdminMutationResponse.error, 
        grantPermissionResponse.error, 
        revokePermissionResponse.error
    ];

    if (isLoading)
        return <LoadingView className="flex flex-col w-full h-full"/>;

    const openModal = (message, onConfirm) => {
        setModalData({
            open: true, onConfirm: onConfirm, message: message
        });
    };
    const closeModal = () => {
        setModalData(CLOSED_MODAL_DATA);
    };

    const deleteAdmin = async (username) => {
        await requestMutation(
            {username: username},
            deleteAdminMutation,
            "Usunięto administratora!",
            "Nie udało się usunąć administratora!"
        )
        listQuery.refetch();
    };

    const changePermission = async (hasPermission, username, permissionType) => {
        if (hasPermission)
            await requestMutation(
                {username: username, permission: permissionType},
                revokePermissionMutation,
                "Odebrano uprawnienie",
                "Nie udało się odebrać uprawnień"
            );
        else
            await requestMutation(
                {username: username, permission: permissionType},
                grantPermissionMutation,
                "Nadano uprawnienie",
                "Nie udało się nadać uprawnień"
            );
        listQuery.refetch();
    }

    const getItems = () => {
        if (listQuery.error){
            console.log(listQuery.error);
            if (listQuery.error.cause.message === TOKEN_EXPIRED_ERROR){
                return <Body text={"Uprawnienia wygasły, odśwież stronę, aby załadować zawartość!"}/>
            } else {
                return <Body text={listQuery.error}/>
            }
        }
        return listQuery.data.usersList.map(user => (
            <AdminListItem 
                key={user.id}
                user={user}
                onCreatePermissionChange={() => openModal(
                    `Czy chcesz zmienić uprawnienia "${user.username}"?`,
                    () => changePermission(
                        user.hasCreatePermission, user.username, PermissionTypes.CREATE
                    )
                )}
                onEditPermissionChange={() => openModal(
                    `Czy chcesz zmienić uprawnienia "${user.username}"?`,
                    () => changePermission(
                        user.hasModifyPermission, user.username, PermissionTypes.EDIT
                    )
                )}
                onDeletePermissionChange={() => openModal(
                    `Czy chcesz zmienić uprawnienia "${user.username}"?`,
                    () => changePermission(
                        user.hasDeletePermission, user.username, PermissionTypes.DELETE
                    )
                )}
                onDelete={() => openModal(
                    `Czy chcesz usunąć administratora "${user.username}"?`,
                    () => deleteAdmin(user.username)
                )}
            />
        ))
    }

    return (
        <SuperUserRequired>
            {
                modalData.open &&
                <ConfirmModal onConfirm={() => { closeModal(); modalData.onConfirm(); }} message={modalData.message} onClose={closeModal}/>
            }
            <ContentView title={"Administratorzy"}>
                <List
                    title={"Wszyscy administratorzy"} 
                    iconName={"shield_person"} 
                    subtitle={ALL_ADMINS_LIST_DESC}
                    setPage={setPage}
                    page={page}
                    maxPage={listQuery.data ? listQuery.data.usersListLength + 1 : 1}
                    filters={filters}
                    setFilters={(newFilter => setFilters(newFilter))}
                    filteringAttributes={listQuery.data ? listQuery.data.userFilteringAttributes : []}
                    metricFiltersDisabled={true}
                    sortingAttributes={listQuery.data ? listQuery.data.userSortingAttributes : []}
                    sorting={sorting}
                    setSorting={newSorting => setSorting(newSorting)}
                    metricSortingDisabled={true}
                >
                    {getItems()}
                </List>
            </ContentView>
        </SuperUserRequired>
    );
}