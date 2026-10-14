import { createContext } from 'react';

export interface User {
    id: number;
    name: string;
}

export interface AuthContextType {
    user: User | null;
    login: (name: string) => void;
    logout: () => void;
}

export const AuthContext = createContext<AuthContextType | undefined>(undefined);
