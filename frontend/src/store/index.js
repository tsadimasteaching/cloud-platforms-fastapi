import { createStore } from "vuex";

import Jobs from './modules/jobs';
import users from './modules/users';

export default createStore({
  modules: {
    jobs,
    users,
  }
});