import axios from 'axios';

const state = {
  Jobs: null,
  Job: null
};

const getters = {
  stateJobs: state => state.Jobs,
  stateJob: state => state.Job,
};

const actions = {
  async createJob({dispatch}, Job) {
    await axios.post('Jobs', Job);
    await dispatch('getJobs');
  },
  async getJobs({commit}) {
    let {data} = await axios.get('Jobs');
    commit('setJobs', data);
  },
  async viewJob({commit}, id) {
    let {data} = await axios.get(`Job/${id}`);
    commit('setJob', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateJob({}, Job) {
    await axios.patch(`Job/${Job.id}`, Job.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteJob({}, id) {
    await axios.delete(`Job/${id}`);
  }
};

const mutations = {
  setJobs(state, Jobs){
    state.Jobs = Jobs;
  },
  setJob(state, Job){
    state.Job = Job;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};