#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RepayLoanDetail import RepayLoanDetail


class AlipayPcreditLoanSideloanrepayResultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanrepayResultQueryResponse, self).__init__()
        self._fail_reason_code = None
        self._fail_reason_message = None
        self._institution_repayment_no = None
        self._repaid_interest = None
        self._repaid_penalty = None
        self._repaid_principal = None
        self._repaid_time = None
        self._repaid_total_amount = None
        self._repay_apply_no = None
        self._repay_initiator = None
        self._repay_loan_detail_list = None
        self._repay_status = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None

    @property
    def fail_reason_code(self):
        return self._fail_reason_code

    @fail_reason_code.setter
    def fail_reason_code(self, value):
        self._fail_reason_code = value
    @property
    def fail_reason_message(self):
        return self._fail_reason_message

    @fail_reason_message.setter
    def fail_reason_message(self, value):
        self._fail_reason_message = value
    @property
    def institution_repayment_no(self):
        return self._institution_repayment_no

    @institution_repayment_no.setter
    def institution_repayment_no(self, value):
        self._institution_repayment_no = value
    @property
    def repaid_interest(self):
        return self._repaid_interest

    @repaid_interest.setter
    def repaid_interest(self, value):
        self._repaid_interest = value
    @property
    def repaid_penalty(self):
        return self._repaid_penalty

    @repaid_penalty.setter
    def repaid_penalty(self, value):
        self._repaid_penalty = value
    @property
    def repaid_principal(self):
        return self._repaid_principal

    @repaid_principal.setter
    def repaid_principal(self, value):
        self._repaid_principal = value
    @property
    def repaid_time(self):
        return self._repaid_time

    @repaid_time.setter
    def repaid_time(self, value):
        self._repaid_time = value
    @property
    def repaid_total_amount(self):
        return self._repaid_total_amount

    @repaid_total_amount.setter
    def repaid_total_amount(self, value):
        self._repaid_total_amount = value
    @property
    def repay_apply_no(self):
        return self._repay_apply_no

    @repay_apply_no.setter
    def repay_apply_no(self, value):
        self._repay_apply_no = value
    @property
    def repay_initiator(self):
        return self._repay_initiator

    @repay_initiator.setter
    def repay_initiator(self, value):
        self._repay_initiator = value
    @property
    def repay_loan_detail_list(self):
        return self._repay_loan_detail_list

    @repay_loan_detail_list.setter
    def repay_loan_detail_list(self, value):
        if isinstance(value, list):
            self._repay_loan_detail_list = list()
            for i in value:
                if isinstance(i, RepayLoanDetail):
                    self._repay_loan_detail_list.append(i)
                else:
                    self._repay_loan_detail_list.append(RepayLoanDetail.from_alipay_dict(i))
    @property
    def repay_status(self):
        return self._repay_status

    @repay_status.setter
    def repay_status(self, value):
        self._repay_status = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_sub_code(self):
        return self._return_sub_code

    @return_sub_code.setter
    def return_sub_code(self, value):
        self._return_sub_code = value
    @property
    def return_sub_message(self):
        return self._return_sub_message

    @return_sub_message.setter
    def return_sub_message(self, value):
        self._return_sub_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloanrepayResultQueryResponse, self).parse_response_content(response_content)
        if 'fail_reason_code' in response:
            self.fail_reason_code = response['fail_reason_code']
        if 'fail_reason_message' in response:
            self.fail_reason_message = response['fail_reason_message']
        if 'institution_repayment_no' in response:
            self.institution_repayment_no = response['institution_repayment_no']
        if 'repaid_interest' in response:
            self.repaid_interest = response['repaid_interest']
        if 'repaid_penalty' in response:
            self.repaid_penalty = response['repaid_penalty']
        if 'repaid_principal' in response:
            self.repaid_principal = response['repaid_principal']
        if 'repaid_time' in response:
            self.repaid_time = response['repaid_time']
        if 'repaid_total_amount' in response:
            self.repaid_total_amount = response['repaid_total_amount']
        if 'repay_apply_no' in response:
            self.repay_apply_no = response['repay_apply_no']
        if 'repay_initiator' in response:
            self.repay_initiator = response['repay_initiator']
        if 'repay_loan_detail_list' in response:
            self.repay_loan_detail_list = response['repay_loan_detail_list']
        if 'repay_status' in response:
            self.repay_status = response['repay_status']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
