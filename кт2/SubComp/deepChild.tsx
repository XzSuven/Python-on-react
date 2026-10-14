import { useAuth } from '../CP2/useAuth';

export const DeepChild = () => {
    const { user } = useAuth();

    return (
        <div>
            глубокий файл внутри: {user ? user.name : 'нет пользователя'}
        </div>
    );
};
