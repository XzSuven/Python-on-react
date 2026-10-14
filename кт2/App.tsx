import "react";
import {AuthProvider} from "./CP2/AuthProvider.tsx";
import {Header} from "./SubComp/Header.tsx";
import {Content} from "./SubComp/Content.tsx";
// import Practise from "./components/practise.tsx";
// import StateEx from "./components/StateEx.tsx";
// import type { Task } from './types.ts'
// import TaskBoard from "./components/TaskBoard";
// import ShoppingList from "./components/212121.tsx";
// import Effect from "./components/StateEx.tsx";

function App(){
    return (
        <>
            {/*<TaskBoard tasks={tasks} />*/}
            {/*<ShoppingList/>*/}
            {/*<Effect />*/}
            {/*<StateEx/>*/}
            {/*<Practise/>*/}
            <AuthProvider>
                <Header/>
                <Content/>
            </AuthProvider>
        </>
    );
}

export default App;