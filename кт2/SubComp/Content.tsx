import { useState } from 'react';
import { useAuth } from '../CP2/useAuth';
import { DeepChild } from './deepChild.tsx';

export const Content = () => {
    const { user, login } = useAuth();
    const [name, setName] = useState('');

    return (
        <main>
            {user ? (
                <span>Ваша страница, {user.name}</span>
            ) : (
                <div>
                    <p>Войдите</p>
                    <input
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        placeholder="Имя"
                    />
                    <button
                        onClick={() => {
                            if (name.trim()) login(name.trim());
                        }}
                    >
                        Войти
                    </button>
                </div>
            )}
            <DeepChild />
        </main>
    );
};
