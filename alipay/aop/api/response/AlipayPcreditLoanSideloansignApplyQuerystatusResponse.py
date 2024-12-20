#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanSideloansignApplyQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloansignApplyQuerystatusResponse, self).__init__()
        self._credit_quota = None
        self._credit_status = None
        self._credit_time = None
        self._end_time = None
        self._fail_reason_code = None
        self._fail_reason_message = None
        self._fund_supplier_code = None
        self._institution_credit_apply_no = None
        self._next_available_apply_time = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None
        self._start_time = None

    @property
    def credit_quota(self):
        return self._credit_quota

    @credit_quota.setter
    def credit_quota(self, value):
        self._credit_quota = value
    @property
    def credit_status(self):
        return self._credit_status

    @credit_status.setter
    def credit_status(self, value):
        self._credit_status = value
    @property
    def credit_time(self):
        return self._credit_time

    @credit_time.setter
    def credit_time(self, value):
        self._credit_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
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
    def fund_supplier_code(self):
        return self._fund_supplier_code

    @fund_supplier_code.setter
    def fund_supplier_code(self, value):
        self._fund_supplier_code = value
    @property
    def institution_credit_apply_no(self):
        return self._institution_credit_apply_no

    @institution_credit_apply_no.setter
    def institution_credit_apply_no(self, value):
        self._institution_credit_apply_no = value
    @property
    def next_available_apply_time(self):
        return self._next_available_apply_time

    @next_available_apply_time.setter
    def next_available_apply_time(self, value):
        self._next_available_apply_time = value
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
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloansignApplyQuerystatusResponse, self).parse_response_content(response_content)
        if 'credit_quota' in response:
            self.credit_quota = response['credit_quota']
        if 'credit_status' in response:
            self.credit_status = response['credit_status']
        if 'credit_time' in response:
            self.credit_time = response['credit_time']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'fail_reason_code' in response:
            self.fail_reason_code = response['fail_reason_code']
        if 'fail_reason_message' in response:
            self.fail_reason_message = response['fail_reason_message']
        if 'fund_supplier_code' in response:
            self.fund_supplier_code = response['fund_supplier_code']
        if 'institution_credit_apply_no' in response:
            self.institution_credit_apply_no = response['institution_credit_apply_no']
        if 'next_available_apply_time' in response:
            self.next_available_apply_time = response['next_available_apply_time']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
        if 'start_time' in response:
            self.start_time = response['start_time']
