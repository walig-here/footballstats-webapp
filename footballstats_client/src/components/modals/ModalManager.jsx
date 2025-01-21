import { createContext, useState } from "react";
import { ConfirmModal } from "./ConfirmModal";

export const ModalContext = createContext(null);

export function ModalManager({children}) {
    const [modalData, setModalData] = useState({
        open: false,
        onConfirm: () => {},
        message: null,
        openModal: (message, onConfirm) => {
            setModalData(
                prev => ({...prev, onConfirm: onConfirm, message: message, open: true})
            );
        },
        closeModal: () => {
            setModalData(prev => ({...prev, open: false}));
        }
    });

    return (
        <ModalContext.Provider value={modalData}>
            {
                modalData.open && 
                <ConfirmModal 
                    message={modalData.message}
                    onClose={() => modalData.closeModal()}
                    onConfirm={() => {modalData.closeModal(); modalData.onConfirm();}}
                />
            }
            {children}
        </ModalContext.Provider>
    )
}