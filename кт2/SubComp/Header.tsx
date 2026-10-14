import { useAuth } from '../CP2/useAuth';

export const Header = () => {
    const { user, logout } = useAuth();

    return (
        <header>
            {user ? (
                <>
                    Привет, {user.name} <button onClick={logout}>Выйти</button>
                </>
            ) : (
                <span>Гость</span>
            )}
        </header>
    );
};
