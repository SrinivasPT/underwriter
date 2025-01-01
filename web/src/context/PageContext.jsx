import React, { createContext, useReducer } from "react";

export const initialState = { data: {}, flags: {}, internal: {}, errors: {} };

// Create context
export const PageContext = createContext({
    state: {},
    dispatch: () => {},
});

// Reducer function
export const pageReducer = (draft, action) => {
    switch (action.type) {
        case "SET_DATA":
            draft.data = action.payload;
            break;
        default:
            break;
    }
};

// Context provider component
export const PageProvider = ({ children, state: initialState }) => {
    const [state, dispatch] = useReducer(pageReducer, initialState);

    return <PageContext.Provider value={{ state, dispatch }}>{children}</PageContext.Provider>;
};
