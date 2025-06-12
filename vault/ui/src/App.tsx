import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { createClient } from '@supabase/supabase-js';

// Components
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Vault from './pages/Vault';
import Settings from './pages/Settings';
import Profile from './pages/Profile';

// Initialize Supabase client
const supabaseUrl = process.env.REACT_APP_SUPABASE_URL || '';
const supabaseKey = process.env.REACT_APP_SUPABASE_KEY || '';
export const supabase = createClient(supabaseUrl, supabaseKey);

// Initialize React Query
const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen bg-gray-100">
          <Navbar />
          <div className="flex">
            <Sidebar />
            <main className="flex-1 p-6">
              <Switch>
                <Route exact path="/" component={Dashboard} />
                <Route path="/vault" component={Vault} />
                <Route path="/settings" component={Settings} />
                <Route path="/profile" component={Profile} />
              </Switch>
            </main>
          </div>
        </div>
      </Router>
    </QueryClientProvider>
  );
}

export default App; 