<template>
  <div id="app">
    <b-container fluid>
      <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>
        One of the parameters is empty. Can not submit
      </b-alert>
      <b-alert v-model="success" variant="success" dismissible>
        Data Retrieved Successfully
      </b-alert>
      <b-row>
        <b-col cols="2" bg-primary>
          <div>
            <b-form @submit="onSubmit" v-if="show">
              <b-form-group
                id="fieldset-1"
                description="Let us know your loan/mortgage amount."
                label="Principal Amount"
                label-for="input-1"
                :invalid-feedback="invalidPrincipalAmountFeedback"
                :valid-feedback="validPrincipalAmountFeedback"
                :state="principalAmountState"
              >
                <b-form-input id="input-1" v-model="principalAmount" :state="principalAmountState" type="number" trim></b-form-input>
              </b-form-group>

              <b-form-group
                id="fieldset-2"
                description="What is your interest rate?"
                label="Interest Rate"
                label-for="input-2"
                :invalid-feedback="invalidInterestRateFeedback"
                :valid-feedback="validInterestRateFeedback"
                :state="interestRateState"
              >
                <b-form-input id="input-2" v-model="interestRate" :state="interestRateState" type="number" trim></b-form-input>
              </b-form-group>

              <b-form-group
                id="fieldset-3"
                description="What is your payment period in years?"
                label="Payment Period"
                label-for="input-3"
                :invalid-feedback="invalidPaymentPeriodFeedback"
                :valid-feedback="validPaymentPeriodFeedback"
                :state="paymentPeriodState"
              >
                <b-form-input id="input-3" v-model="paymentPeriod" :state="paymentPeriodState" type="number" trim></b-form-input>
              </b-form-group>

              <b-form-group
                id="fieldset-4"
                description="What is your payment interval?"
                label="Payment Interval"
                label-for="input-4"
                :invalid-feedback="invalidPaymentIntervalFeedback"
                :valid-feedback="validPaymentIntervalFeedback"
                :state="paymentIntervalState"
              >
                <b-form-select v-model="paymentInterval" :options="options" class="mb-3">
                  <template slot="first">
                    <option :value="null" disabled>-- Please select an option --</option>
                  </template>
                </b-form-select>
              </b-form-group>

              <b-form-group
                id="fieldset-5"
                description="What is your payment start date?"
                label="Payment Start Date"
                label-for="input-5"
                :invalid-feedback="invalidPaymentStartDateFeedback"
                :valid-feedback="validPaymentStartDateFeedback"
                :state="paymentStartDateState"
              >
                <b-form-input id="input-3" v-model="paymentStartDate" :state="paymentStartDateState" type="date" trim></b-form-input>
              </b-form-group>

              <b-button type="submit" variant="primary">Submit</b-button>
            </b-form>
          </div>
        </b-col>
        <b-col cols="10">
          <div class="h-100" v-if="armotized">
            <div class="h-25">
              <div class="h-50">
                <b-row class="pt-5">
                  <b-col>
                    <span class="float-left pl-5">
                      <span class="font-weight-bold">Total Interest: </span>
                      <span class="font-weight-normal">{{ totalInterest }}</span>
                    </span>
                  </b-col>
                  <b-col>
                    <span class="float-left pl-5">
                      <span class="font-weight-bold">Total Payment: </span>
                      <span class="font-weight-normal">{{ totalPayment }}</span>
                    </span>
                  </b-col>
                  <b-col>
                    <span class="float-left pl-5">
                      <span class="font-weight-bold">Expected Payment: </span>
                      <span class="font-weight-normal">{{ expectedPayment }}</span>
                    </span>
                  </b-col>
                </b-row>
              </div>
              <div class="h-50">
                <b-row class="pt-4">
                  <b-col>
                    <span class="float-left pl-5">
                      <span class="font-weight-bold">No. Of Payments: </span>
                      <span class="font-weight-normal">{{ expectedNumberOfPayments }}</span>
                    </span>
                  </b-col>
                  <b-col>
                    <span class="float-left pl-5">
                      <span class="font-weight-bold">Expected Start Date: </span>
                      <span class="font-weight-normal">{{ expectedStartDate }}</span>
                    </span>
                  </b-col>
                  <b-col>
                    <span class="float-left pl-5">
                      <span class="font-weight-bold">Expected End Date: </span>
                      <span class="font-weight-normal">{{ expectedEndDate }}</span>
                    </span>
                  </b-col>
                </b-row>
              </div>
            </div>
            <div class="h-75">
              <div class="overflow-auto">
                <b-table
                  id="my-table"
                  striped
                  hover
                  fixed
                  :items="items"
                  :per-page="perPage"
                  :current-page="currentPage"
                  head-variant="dark"
                  table-variant="success"
                  caption-top
                  responsive
                  bordered
                >
                  <template slot="table-caption">
                    <div class="float-left">
                      <span class="font-weight-bold">Armotization Data</span>
                    </div>
                    <div class="float-right">
                      <b-button variant="outline-success" @click="downloadPdf">
                        <span class="font-weight-bold">Download</span>
                      </b-button>
                    </div>
                  </template>
                  <div slot="HEAD[]" class="text-nowrap" slot-scope="scope">{{ scope.label }}</div>
                  <div slot="[]" class="text-nowrap" slot-scope="scope">{{ scope.value }}</div>
                </b-table>
                <b-row>
                  <b-col>
                    <span class="mt-2 float-left">
                      <span class="font-weight-bold">Current Page: </span>
                      <span class="font-weight-normal">{{ currentPage }}</span>
                    </span>
                  </b-col>
                  <b-col>
                    <b-pagination
                    v-model="currentPage"
                    :total-rows="rows"
                    :per-page="perPage"
                    aria-controls="my-table"
                    align="right"
                  ></b-pagination>
                  </b-col>
                </b-row>
              </div>
            </div>
          </div>
          <div class="h-100" v-else>
            <div class="d-flex flex-row justify-content-center align-items-center h-100">
              <span class="font-weight-bold">
                No Armotized Data Yet.  
              </span>
              <span class="font-weight-bold"> 
              </span>
              <span class="font-weight-normal">
                Please fill in the form to continue.
              </span>
            </div>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import { mapState, mapActions, mapGetters, mapMutations } from 'vuex';

  import jsPDF from "jspdf";
  import 'jspdf-autotable';

  export default {
    data() {
      return {
        show: true,
        showDismissibleAlert: false,
        headerFields: ["dates", "beginning_balance", "ending_balance", "interest", "principal", "periodic_payment"],
        options: [
          { value: "Annualy", text: "Annualy" },
          { value: "Semi-Annualy", text: "Semi-Annualy" },
          { value: "Quarterly", text: "Quarterly" },
          { value: "Monthly", text: "Monthly" },
          { value: "Semi-Monthly", text: "Semi-Monthly" },
          { value: "Weekly", text: "Weekly" },
          { value: "Bi-Weekly", text: "Bi-Weekly" },
        ],
        perPage: 8,
        currentPage: 1,
      }
    },
    components: {
    },
    computed: {
      ...mapState([
        "postData"
      ]),
      ...mapGetters({
        success: "success",
        result: "resultData",
      }),
      totalInterest() {
        return this.result.total_interest
      },
      totalPayment() {
        return this.result.total_payment
      },
      expectedPayment() {
        return this.result.expected_payment
      },
      expectedStartDate() {
        return this.result.expected_start_date
      },
      expectedEndDate() {
        return this.result.expected_end_date
      },
      expectedNumberOfPayments() {
        return this.result.expected_number_of_payments
      },
      items() {
        return this.result.data
      },
      rows() {
        return this.items.length
      },
      armotized() {
        return this.result ? true : false
      },
      paymentInterval: {
          get() {
            return this.postData.paymentInterval
          },
          set(value) {
            this.update_post_data({...this.postData, paymentInterval:value})
          }
      },
      paymentStartDate: {
          get() {
            return this.postData.paymentStartDate
          },
          set(value) {
              this.update_post_data({...this.postData, paymentStartDate:value})
          }
      },
      interestRate: {
          get() {
            return this.postData.interestRate
          },
          set(value) {
              this.update_post_data({...this.postData, interestRate:value})
          }
      },
      paymentPeriod: {
          get() {
            return this.postData.paymentPeriod
          },
          set(value) {
              this.update_post_data({...this.postData, paymentPeriod:value})
          }
      },
      principalAmount: {
          get() {
            return this.postData.principalAmount
          },
          set(value) {
              this.update_post_data({...this.postData, principalAmount:value})
          }
      },
      principalAmountState() {
        return this.principalAmount > 0 ? true : false
      },
      interestRateState() {
        return this.interestRate > 0 && this.interestRate < 100 ? true : false
      },
      paymentPeriodState() {
        return this.paymentPeriod > 0 && this.paymentPeriod < 100 ? true : false
      },
      paymentIntervalState() {
        return this.paymentInterval ? true: false
      },
      paymentStartDateState() {
        return this.paymentStartDate ? true: false
      },
      invalidInterestRateFeedback() {
        if (this.interestRate === 0) {
          return "Nothing to calculate"
        } else if (this.interestRate > 0) {
          if (this.interestRate < 100) {
            return "We are in a good place"
          } else if (this.interestRate >= 100) {
            return "Unacceptable interest rate. Must be below 100"
          }
        } else {
          return "Please Enter Interest Rate"
        }
      },
      validInterestRateFeedback() {
        return this.interestRateState === true ? 'Thank you' : ''
      },
      invalidPrincipalAmountFeedback() {
        if (this.principalAmount === 0) {
          return "Nothing to calculate"
        } else if (this.principalAmount > 0) {
          return "Thats a good start"
        } else if (this.principalAmount > 1000000000) {
          return "You must be very rich"
        } else {
          return "Please Enter Principal Amount"
        }
      },
      validPrincipalAmountFeedback() {
        return this.principalAmountState === true ? 'Thank you' : ''
      },
      invalidPaymentPeriodFeedback() {
        if (this.paymentPeriod === 0) {
          return "Nothing to calculate"
        } else if (this.paymentPeriod > 0 && this.paymentPeriod < 100) {
          return ""
        } else if (this.paymentPeriod >= 100) {
          return "Why would it take you that long to pay a loan. Get serious."
        } else {
          return "Please Enter Payment Period"
        }
      },
      validPaymentPeriodFeedback() {
        return this.paymentPeriodState === true ? "We are in a good place son" : ''
      },
      invalidPaymentIntervalFeedback() {
        if (this.paymentInterval) {
          return ""
        } else {
          return "Please Select A Payment Interval"
        }
      },
      validPaymentIntervalFeedback() {
        return this.paymentIntervalState === true ? 'Thank you' : ''
      },
      invalidPaymentStartDateFeedback() {
        if (this.paymentStartDate) {
          return ""
        } else {
          return "Payment start date is required"
        }
      },
      validPaymentStartDateFeedback() {
        return this.paymentStartDateState === true ? 'Thank you' : ''
      },
    },
    methods: {
      ...mapActions([
          "sendPostData",
      ]),
      ...mapMutations({
        update_post_data: "SET_POST_DATA"
      }),
      onSubmit(evt) {
        evt.preventDefault()
        if (this.paymentPeriodState && this.paymentIntervalState && this.paymentStartDateState && this.principalAmountState && this.interestRateState) {
          // alert(JSON.stringify(this.postData))
          this.sendPostData(this.postData)
        } else {
          this.showDismissibleAlert = true
        }
      },
      downloadPdf() {
        let vm = this
        let pdfDate = new Date().toISOString().substr(0, 10)

        let columns = [
          {title: "Dates", dataKey: "dates"},
          {title: "Beginning Balance", dataKey: "beginning_balance"},
          {title: "Ending Balance", dataKey: "ending_balance"},
          {title: "Interest", dataKey: "interest"},
          {title: "Principal", dataKey: "principal"},
          {title: "Payment", dataKey: "periodic_payment"}
        ]

        let doc = new jsPDF("p", "pt")

        let pageHeight = doc.internal.pageSize.height || doc.internal.pageSize.getHeight()
        let pageWidth = doc.internal.pageSize.width || doc.internal.pageSize.getHeight()

        doc.setFontSize(12)
        doc.setFontStyle('bold')
        doc.setTextColor("#2980BA")
        doc.text(pdfDate.toString(), pageWidth-20, 20, {
          align: "right"
        })

        doc.setFontSize(26)
        doc.setFontStyle("bold")
        doc.setTextColor("#2980BA")
        doc.text("Armotization Report", pageWidth/2, 50, {
          align: "center"
        })

        doc.setFontSize(14)
        doc.setFontStyle('bold')
        doc.setTextColor("#2980BA")
        doc.text("Summary:", 40, 80, {
          align: "left"
        })

        let armotizationText = "Amortization is an accounting term that is the process of spreading out a loan into a series of fixed payments over time. You'll be paying off the loan's interest and principal periodically, although your total payment remains equal each period. Amortization schedule is a table that lists each regular payment on a mortgage/loan over fixed period of time and details how much will go toward each component of your mortgage/loan payment. Initially, most of your payment goes toward the interest rather than the principal. The schedule will show as the term of your loan progresses, a larger share of your payment goes toward paying down the principal until the loan is paid in full at the end of your term."

        let splitArmotizationText = doc.splitTextToSize(armotizationText, 700)

        doc.setFontSize(11)
        doc.setTextColor(40)
        doc.setFontStyle('normal')
        doc.text(40, 110, splitArmotizationText, {
          align: "left"
        })

        doc.setFontSize(14)
        doc.setFontStyle('bold')
        doc.setTextColor("#2980BA")
        doc.text("Statistical Data:", 40, 230, {
          align: "left"
        })
        
        doc.setFontSize(12)
        doc.setFontStyle('bold')
        doc.setTextColor("#2980BA")
        doc.text("Total Interest:", 40, 270, {
          align: "left"
        })

        doc.setFontSize(11)
        doc.setTextColor(40)
        doc.setFontStyle('normal')
        doc.text(vm.totalInterest.toString(), 125, 270, {
          align: "left"
        })

        doc.setFontSize(12);
        doc.setTextColor("#2980BA")
        doc.setFontStyle('bold')
        doc.text("Total Payment:", 220, 270, {
          align: "left"
        })

        doc.setFontSize(11);
        doc.setTextColor(40);
        doc.setFontStyle('normal')
        doc.text(vm.totalPayment.toString(), 310, 270, {
          align: "left"
        })


        doc.setFontSize(12)
        doc.setTextColor("#2980BA")
        doc.setFontStyle('bold')
        doc.text("Periodic Payment:", 400, 270, {
          align: "left"
        })

        doc.setFontSize(11)
        doc.setTextColor(40)
        doc.setFontStyle('normal')
        doc.text(vm.expectedPayment.toString(), 515, 270, {
          align: "left"
        })
        
        doc.setFontSize(12)
        doc.setTextColor("#2980BA")
        doc.setFontStyle('bold')
        doc.text("No. of Payments:", 40, 300, {
          align: "left"
        })

        doc.setFontSize(11)
        doc.setTextColor(40)
        doc.setFontStyle('normal')
        doc.text(vm.expectedNumberOfPayments.toString(), 145, 300, {
          align: "left"
        })

        doc.setFontSize(12)
        doc.setTextColor("#2980BA")
        doc.setFontStyle('bold')
        doc.text("Start Date:", 220, 300, {
          align: "left"
        })

        doc.setFontSize(11)
        doc.setTextColor(40)
        doc.setFontStyle('normal')
        doc.text(vm.expectedStartDate.toString(), 285, 300, {
          align: "left"
        })


        doc.setFontSize(12)
        doc.setTextColor("#2980BA")
        doc.setFontStyle('bold')
        doc.text("End date:", 400, 300, {
          align: "left"
        })

        doc.setFontSize(11)
        doc.setTextColor(40)
        doc.setFontStyle('normal')
        doc.text(vm.expectedEndDate.toString(), 460, 300, {
          align: "left"
        })

        doc.setFontSize(14)
        doc.setFontStyle('bold')
        doc.setTextColor("#2980BA")
        doc.text("Armotization Schedule/Table:", 40, 340, {
          align: "left"
        })
        
        doc.autoTable(columns, vm.items, 
          {
            margin: {
              top: 370
            }
          }
        )

        doc.save("armotization.pdf")
      }
    }
  }
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
