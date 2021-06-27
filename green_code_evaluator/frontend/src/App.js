import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Chart from './components/Chart';
import Header from './components/Header';
import Presentation from './components/Presentation';
import GreenCode from './components/GreenCode';
import ChartCPU from './components/ChartCPU';
import Memory from './components/Memory';
import UnusedImport from './components/UnusedImport';

const App = () => (
  <div >
    <Header />
    <Switch>
      <Route path='/green-code-about' component={GreenCode}/>
      <Route path='/total-time' component={Chart} />
      <Route path='/cpu' component={ChartCPU} />
      <Route path='/unused' component={UnusedImport} />
      <Route path='/memory' component={Memory} />
      <Route path='/' component={Presentation} />
    </Switch>
  </div>
);

export default App;