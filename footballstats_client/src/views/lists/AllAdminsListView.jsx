import { useMutation, useQuery } from "@apollo/client";
import ContentView from "../../components/ContentView";
import List from "../../components/List";
import { GET_ADMINS_LIST, GRANT_PERMISSION, REMOVE_ADMIN, REVOKE_PERMISSION, SuperUserRequired } from "../../api_client";
import { ACCESS_TOKEN, PermissionTypes } from "../../constants";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";
import { Checkbox, Divider, Icon, IconButton } from "actify";
import { useState } from "react";
import {ConfirmModal} from "../../components/modals/ConfirmModal"
import { toast } from "react-toastify";

const ALL_ADMINS_LIST_DESC = "Zarządzaj wszystkimi administratorami zarejestrowanymi w systemie.";

export default function AllAdminsListView() {
    const [page, setPage] = useState(1);
    const [deleteAdminMutation, {loading: loadingDeleteAdmin}] = useMutation(REMOVE_ADMIN);
    const [grantPermissionMutation, {loading: loadingGrantPermission}] = useMutation(GRANT_PERMISSION);
    const [revokePermissionMutation, {loading: loadingRemovePermission}] = useMutation(REVOKE_PERMISSION);
    const {data, loading: loadingList, error: errorLoadList, refetch: refetchList} = useQuery(
        GET_ADMINS_LIST,
        {
            variables: {
                accessToken: localStorage.getItem(ACCESS_TOKEN),
                page: page - 1,
                textualFilters: [],
                sorting: null
            },
            fetchPolicy: "cache-and-network"
        }
    );
    const [modalData, setModalData] = useState({
        open: false,
        onConfirm: () => {},
        message: null
    });

    if ([loadingList, loadingDeleteAdmin, loadingGrantPermission, loadingRemovePermission].some(Boolean))
        return <LoadingView className="flex flex-col w-full h-full"/>;

    const openModal = (message, onConfirm) => {
        setModalData({
            open: true, onConfirm: onConfirm, message: message
        });
    };
    const closeModal = () => {
        setModalData({
            open: false, onConfirm: () => {}, message: null
        });
    }

    const deleteAdmin = async (username) => {
        closeModal();
        const accessToken = localStorage.getItem(ACCESS_TOKEN);
        try{
            const {data} = await deleteAdminMutation({variables: {
                accessToken: accessToken, username: username
            }});
            refetchList();
            toast.success("Usunięto administratora!");
        } catch (error) {
            console.log(`Error occurred while deleting user ${username}. Error\m${error}`);
            toast.error("Nie udało się usunąć administratora!");
        }
    };
    const grantPermission = async (username, permission) => {
        closeModal();
        const accessToken = localStorage.getItem(ACCESS_TOKEN);
        try{
            const {data} = await grantPermissionMutation({variables: {
                accessToken: accessToken, username: username, permission: permission
            }});
            refetchList();
            toast.success("Nadano uprawnienie!");
        } catch (error) {
            console.log(`Error occurred while granting permission to user ${username}. Error\m${error}`);
            toast.error("Nie udało się nadać uprawnienia!");
        }
    };
    const revokePermission = async (username, permission) => {
        closeModal();
        const accessToken = localStorage.getItem(ACCESS_TOKEN);
        try{
            const {data} = await revokePermissionMutation({variables: {
                accessToken: accessToken, username: username, permission: permission
            }});
            refetchList();
            toast.success("Odebrano uprawnienie!");
        } catch (error) {
            console.log(`Error occurred while revoking permission to user ${username}. Error\m${error}`);
            toast.error("Nie udało się odebrać uprawnienia!");
        }
    };

    return (
        <SuperUserRequired>
            {
                modalData.open &&
                <ConfirmModal onConfirm={modalData.onConfirm} message={modalData.message} onClose={closeModal}/>
            }
            <ContentView title={"Administratorzy"}>
                <List 
                    title={"Wszyscy administratorzy"} 
                    iconName={"shield_person"} 
                    subtitle={ALL_ADMINS_LIST_DESC}
                    setPage={setPage}
                    page={page}
                    maxPage={data ? data.usersListLength + 1 : 1}
                >
                    {
                        !errorLoadList &&
                        data.usersList.map(user => (
                            <div key={user.id}>
                                <div className="flex flex-row items-center px-2 py-4 place-content-between">
                                    <Body text={user.username} style={"text-base"}/>
                                    <div className="flex flex-row space-x-2.5 items-center">
                                        <Checkbox 
                                            isSelected={user.hasCreatePermission}
                                            onChange={
                                                () => openModal(
                                                    `Czy chcesz zmienić uprawnienia "${user.username}" do dodawania?`,
                                                    () => !user.hasCreatePermission ? 
                                                    grantPermission(user.username, PermissionTypes.CREATE) :
                                                    revokePermission(user.username, PermissionTypes.CREATE)
                                                )
                                            }
                                        >
                                            Dodający
                                        </Checkbox>
                                        <Checkbox 
                                            isSelected={user.hasModifyPermission}
                                            onChange={
                                                () => openModal(
                                                    `Czy chcesz zmienić uprawnienia "${user.username}" do modyfikowania?`,
                                                    () => !user.hasModifyPermission ? 
                                                    grantPermission(user.username, PermissionTypes.EDIT) :
                                                    revokePermission(user.username, PermissionTypes.EDIT)
                                                )
                                            }
                                        >
                                            Edytujący
                                        </Checkbox>
                                        <Checkbox 
                                            isSelected={user.hasDeletePermission}
                                            onChange={
                                                () => openModal(
                                                    `Czy chcesz zmienić uprawnienia "${user.username}" do usuwania?`,
                                                    () => !user.hasDeletePermission ? 
                                                    grantPermission(user.username, PermissionTypes.DELETE) :
                                                    revokePermission(user.username, PermissionTypes.DELETE)
                                                )
                                            }
                                        >
                                            Usuwający
                                        </Checkbox>
                                        <IconButton onPress={
                                            () => openModal(
                                                `Czy chcesz usunąć administratora "${user.username}"?`,
                                                () => deleteAdmin(user.username)
                                            )
                                        }>
                                            <Icon className="text-on-surface-variant">delete</Icon>
                                        </IconButton>
                                    </div>
                                </div>
                                <Divider/>
                            </div>
                        ))
                    }
                </List>
            </ContentView>
        </SuperUserRequired>
    );
}