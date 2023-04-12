import React from 'react';

// функциональный компонент
const Drawer=()=>{
    const [numbers, setNumbers] = React.useState([1,2,3,4,5,6,7,8])
    const addRandNum = () =>{
    const randNumber = Math.round(Math.random()*10)
    const newArr = [...numbers, randNumber]
    setNumbers(newArr)
    }

    React.useEffect(()=>{
        console.log('компонент обновился')
    },[numbers])
    return(
        <div className='ul-list'>
            <div className='ul-list-block'>
             <ul>
                 {numbers.map((num, index)=> (
                   <li key={index}>{num}</li> 
                ))}
            </ul>
            </div>
            <button onClick={addRandNum}>Добавьте число</button>
            
        </div>
    )
}

// классовый Компонент

// class Drawer extends React.Component{
// state = {
//     numbers: [1,2,5],
// };
//  addRandomNumber =  () =>{
//     const RandNumber = Math.round(Math.random()*10)
//     this.setState({
//         numbers: [...this.state.numbers, RandNumber]
//     })
// }
// render(){
//     return(
//         <div>
//             <ul>
//                 {this.state.numbers.map((num, index)=> (
//                    <li key={index}>{num}</li> 
//                 ))}
//             </ul>
//             <button onClick={this.addRandomNumber}>Добавьте число</button>
//         </div>
//     )
// }
// }
export default Drawer;