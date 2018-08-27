#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanApplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanApplyQueryResponse, self).__init__()
        self._apply_amt = None
        self._apply_date = None
        self._ar_no = None
        self._cert_no = None
        self._cert_type = None
        self._credit_no = None
        self._daily_int_rate = None
        self._due_date = None
        self._encash_org = None
        self._loan_apply_no = None
        self._need_prepayment_fee = None
        self._payment_dt = None
        self._repay_mode = None
        self._status = None
        self._term = None
        self._term_unit = None
        self._user_name = None

    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        self._apply_amt = value
    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def daily_int_rate(self):
        return self._daily_int_rate

    @daily_int_rate.setter
    def daily_int_rate(self, value):
        self._daily_int_rate = value
    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def encash_org(self):
        return self._encash_org

    @encash_org.setter
    def encash_org(self, value):
        self._encash_org = value
    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value
    @property
    def need_prepayment_fee(self):
        return self._need_prepayment_fee

    @need_prepayment_fee.setter
    def need_prepayment_fee(self, value):
        self._need_prepayment_fee = value
    @property
    def payment_dt(self):
        return self._payment_dt

    @payment_dt.setter
    def payment_dt(self, value):
        self._payment_dt = value
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value
    @property
    def term_unit(self):
        return self._term_unit

    @term_unit.setter
    def term_unit(self, value):
        self._term_unit = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanApplyQueryResponse, self).parse_response_content(response_content)
        if 'apply_amt' in response:
            self.apply_amt = response['apply_amt']
        if 'apply_date' in response:
            self.apply_date = response['apply_date']
        if 'ar_no' in response:
            self.ar_no = response['ar_no']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'credit_no' in response:
            self.credit_no = response['credit_no']
        if 'daily_int_rate' in response:
            self.daily_int_rate = response['daily_int_rate']
        if 'due_date' in response:
            self.due_date = response['due_date']
        if 'encash_org' in response:
            self.encash_org = response['encash_org']
        if 'loan_apply_no' in response:
            self.loan_apply_no = response['loan_apply_no']
        if 'need_prepayment_fee' in response:
            self.need_prepayment_fee = response['need_prepayment_fee']
        if 'payment_dt' in response:
            self.payment_dt = response['payment_dt']
        if 'repay_mode' in response:
            self.repay_mode = response['repay_mode']
        if 'status' in response:
            self.status = response['status']
        if 'term' in response:
            self.term = response['term']
        if 'term_unit' in response:
            self.term_unit = response['term_unit']
        if 'user_name' in response:
            self.user_name = response['user_name']
