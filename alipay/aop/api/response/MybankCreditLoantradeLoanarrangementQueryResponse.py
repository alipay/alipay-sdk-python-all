#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InstRepayPlan import InstRepayPlan
from alipay.aop.api.domain.InstallmentMetaInfo import InstallmentMetaInfo
from alipay.aop.api.domain.InstallmentMetaInfo import InstallmentMetaInfo


class MybankCreditLoantradeLoanarrangementQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeLoanarrangementQueryResponse, self).__init__()
        self._ar_status = None
        self._encash_amt = None
        self._end_date = None
        self._installment_repay_plans = None
        self._interest = None
        self._interest_rates = None
        self._loan_ar_no = None
        self._loan_term = None
        self._ovd_days = None
        self._overdue_interest_penalty = None
        self._overdue_principal_penalty = None
        self._principal = None
        self._repay_modes = None
        self._start_date = None

    @property
    def ar_status(self):
        return self._ar_status

    @ar_status.setter
    def ar_status(self, value):
        self._ar_status = value
    @property
    def encash_amt(self):
        return self._encash_amt

    @encash_amt.setter
    def encash_amt(self, value):
        self._encash_amt = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def installment_repay_plans(self):
        return self._installment_repay_plans

    @installment_repay_plans.setter
    def installment_repay_plans(self, value):
        if isinstance(value, list):
            self._installment_repay_plans = list()
            for i in value:
                if isinstance(i, InstRepayPlan):
                    self._installment_repay_plans.append(i)
                else:
                    self._installment_repay_plans.append(InstRepayPlan.from_alipay_dict(i))
    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value
    @property
    def interest_rates(self):
        return self._interest_rates

    @interest_rates.setter
    def interest_rates(self, value):
        if isinstance(value, list):
            self._interest_rates = list()
            for i in value:
                if isinstance(i, InstallmentMetaInfo):
                    self._interest_rates.append(i)
                else:
                    self._interest_rates.append(InstallmentMetaInfo.from_alipay_dict(i))
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def ovd_days(self):
        return self._ovd_days

    @ovd_days.setter
    def ovd_days(self, value):
        self._ovd_days = value
    @property
    def overdue_interest_penalty(self):
        return self._overdue_interest_penalty

    @overdue_interest_penalty.setter
    def overdue_interest_penalty(self, value):
        self._overdue_interest_penalty = value
    @property
    def overdue_principal_penalty(self):
        return self._overdue_principal_penalty

    @overdue_principal_penalty.setter
    def overdue_principal_penalty(self, value):
        self._overdue_principal_penalty = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def repay_modes(self):
        return self._repay_modes

    @repay_modes.setter
    def repay_modes(self, value):
        if isinstance(value, list):
            self._repay_modes = list()
            for i in value:
                if isinstance(i, InstallmentMetaInfo):
                    self._repay_modes.append(i)
                else:
                    self._repay_modes.append(InstallmentMetaInfo.from_alipay_dict(i))
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, list):
            self._start_date = list()
            for i in value:
                self._start_date.append(i)

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeLoanarrangementQueryResponse, self).parse_response_content(response_content)
        if 'ar_status' in response:
            self.ar_status = response['ar_status']
        if 'encash_amt' in response:
            self.encash_amt = response['encash_amt']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'installment_repay_plans' in response:
            self.installment_repay_plans = response['installment_repay_plans']
        if 'interest' in response:
            self.interest = response['interest']
        if 'interest_rates' in response:
            self.interest_rates = response['interest_rates']
        if 'loan_ar_no' in response:
            self.loan_ar_no = response['loan_ar_no']
        if 'loan_term' in response:
            self.loan_term = response['loan_term']
        if 'ovd_days' in response:
            self.ovd_days = response['ovd_days']
        if 'overdue_interest_penalty' in response:
            self.overdue_interest_penalty = response['overdue_interest_penalty']
        if 'overdue_principal_penalty' in response:
            self.overdue_principal_penalty = response['overdue_principal_penalty']
        if 'principal' in response:
            self.principal = response['principal']
        if 'repay_modes' in response:
            self.repay_modes = response['repay_modes']
        if 'start_date' in response:
            self.start_date = response['start_date']
