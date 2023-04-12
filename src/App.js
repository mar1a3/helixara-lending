
import './App.css';
import Drawer from './components/Drawer';
import React from 'react';

function App() {
  const [itemDrawer, setItemDrawer] = React.useState(true)
  const changeVis =()=>{
    setItemDrawer(visible=>!visible)
  }
  return (
    <div className="App">
      {itemDrawer && <Drawer/>}
      {/* <button onClick= {changeVis}>Скрыть список</button> */}
    </div>
  );
}

export default App;
