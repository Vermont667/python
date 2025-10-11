import { useState } from 'react';
import './App.css';
// import Counter from './Counter';
// import Person from './Person';
// import Modal from './Modal';
// import Item from './Item';
import Task from './Task';
import Form from './Form';


function App() {

  let [tasks, setTasks] = useState([
    {
      text: 'Выучить JavaScript',
      done: false
    },
    {
      text: 'Познакомиться с React',
      done: false
    },
    {
      text: 'Устроиться на работу',
      done: false
    },
  ])

  let addTask = text => {
    let newTask = [...tasks, { text }];
    setTasks(newTask)
  }

  let doneTask = index => {
    if (tasks[index].done === false) {
      let newTask = [...tasks];
      newTask[index].done = true;
      setTasks(newTask)
    } else {
      let newTask = [...tasks]
      newTask[index].done = false;
      setTasks(newTask)
    };
  }

  let deleteTask = index => {
    let newTask = [...tasks];
    newTask.splice(index, 1);
    setTasks(newTask);
  }

  return (

    <div className="App">
      {
        console.log(tasks)

      }
      <div className='task-list'>
        {/* <Counter />
      <Person /> */}
        {/* <Modal /> */}
        {/* <Item /> */}
        {
          tasks.map((task, index) =>
            <Task
              key={index}
              task={task}
              doneTask={doneTask}
              index={index}
              deleteTask={deleteTask}
            />
          )
        }
        <Form addTask={addTask} />
      </div>
    </div>
  );
}

export default App;
