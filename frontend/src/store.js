import Vue from "vue";
import Vuex from "vuex";

import axios from "axios";

Vue.use(Vuex,axios);

export default new Vuex.Store({
  state: {
    postData: {
      interestRate: 0,
      paymentPeriod: 0,
      principalAmount: 0,
      paymentInterval: null,
      paymentStartDate: null
    },
    resultData: null,
    success: false
  },
  getters: {
    success: state => state.success,
    resultData: state => state.resultData,
  },
  mutations: {
    SET_SUCCESS: (state) => {
      state.success = !state.success
    },
    SET_POST_DATA: (state, payload) =>{
      state.postData = Object.assign({}, state.postData, payload)
    },
    CLEAR_FORM_DATA: (state) => {
      state.postData = Object.assign({}, state.postData, {
        interestRate: 0,
        paymentPeriod: 0,
        principalAmount: 0,
        paymentInterval: null,
        paymentStartDate: null
      })
    },
    UPDATE_RESULT_DATA: (state, payload) => {
      state.resultData = payload
    }
  },
  actions: {
    sendPostData: ({commit}, payload) =>{
      let formData = new URLSearchParams()

      formData.append("interval", payload.paymentInterval)
      formData.append("start_date", payload.paymentStartDate)
      formData.append("interest_rate", payload.interestRate)
      formData.append("payment_period", payload.paymentPeriod)
      formData.append("principal_amount", payload.principalAmount)

      axios({
        method: "post",
        url: "http://localhost:8001/api/armotization",
        headers: {"content-type": "application/x-www-form-urlencoded"},
        data: formData
      })
      .then(res => {
        commit("CLEAR_FORM_DATA")
        commit("SET_SUCCESS")
        commit("UPDATE_RESULT_DATA", res.data)
      })
      .catch(err => {
        console.error(err)
      })
    }
  }
});
