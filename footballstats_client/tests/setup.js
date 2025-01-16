import {afterEach, beforeEach, vi} from 'vitest';
import {cleanup} from '@testing-library/react';
import "@testing-library/jest-dom/vitest";

const mockLocalStorage = () => {
    let storage = {};

    return {
        getItem: (key) => (key in storage ? storage[key] : null),
        setItem: (key, value) => {
            storage[key] = `${value}`;
        },
        removeItem: (key) => {
            delete storage[key];
        },
        clear: () => {
            storage = {};
        },
        storage: storage
    };
};


beforeEach(() => {
    vi.stubGlobal('localStorage', mockLocalStorage());
});


afterEach(() => {
    cleanup();
    vi.unstubAllGlobals();
    mockLocalStorage().clear();
});