#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InstallmentMetaInfo import InstallmentMetaInfo
from alipay.aop.api.domain.InstallmentRepayPlan import InstallmentRepayPlan
from alipay.aop.api.domain.InstallmentMetaInfo import InstallmentMetaInfo


class MybankCreditLoantradeLoanarQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeLoanarQueryResponse, self).__init__()
        self._arg_status = None
        self._instal_int_rate = None
        self._installment_repay_plans = None
        self._loan_ar_no = None
        self._loan_term = None
        self._nom_int = None
        self._nom_prin = None
        self._ovd_int = None
        self._ovd_int_pen_int = None
        self._ovd_prin = None
        self._ovd_prin_pen_int = None
        self._repay_modes = None

    @property
    def arg_status(self):
        return self._arg_status

    @arg_status.setter
    def arg_status(self, value):
        self._arg_status = value
    @property
    def instal_int_rate(self):
        return self._instal_int_rate

    @instal_int_rate.setter
    def instal_int_rate(self, value):
        if isinstance(value, list):
            self._instal_int_rate = list()
            for i in value:
                if isinstance(i, InstallmentMetaInfo):
                    self._instal_int_rate.append(i)
                else:
                    self._instal_int_rate.append(InstallmentMetaInfo.from_alipay_dict(i))
    @property
    def installment_repay_plans(self):
        return self._installment_repay_plans

    @installment_repay_plans.setter
    def installment_repay_plans(self, value):
        if isinstance(value, list):
            self._installment_repay_plans = list()
            for i in value:
                if isinstance(i, InstallmentRepayPlan):
                    self._installment_repay_plans.append(i)
                else:
                    self._installment_repay_plans.append(InstallmentRepayPlan.from_alipay_dict(i))
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
    def nom_int(self):
        return self._nom_int

    @nom_int.setter
    def nom_int(self, value):
        self._nom_int = value
    @property
    def nom_prin(self):
        return self._nom_prin

    @nom_prin.setter
    def nom_prin(self, value):
        self._nom_prin = value
    @property
    def ovd_int(self):
        return self._ovd_int

    @ovd_int.setter
    def ovd_int(self, value):
        self._ovd_int = value
    @property
    def ovd_int_pen_int(self):
        return self._ovd_int_pen_int

    @ovd_int_pen_int.setter
    def ovd_int_pen_int(self, value):
        self._ovd_int_pen_int = value
    @property
    def ovd_prin(self):
        return self._ovd_prin

    @ovd_prin.setter
    def ovd_prin(self, value):
        self._ovd_prin = value
    @property
    def ovd_prin_pen_int(self):
        return self._ovd_prin_pen_int

    @ovd_prin_pen_int.setter
    def ovd_prin_pen_int(self, value):
        self._ovd_prin_pen_int = value
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

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeLoanarQueryResponse, self).parse_response_content(response_content)
        if 'arg_status' in response:
            self.arg_status = response['arg_status']
        if 'instal_int_rate' in response:
            self.instal_int_rate = response['instal_int_rate']
        if 'installment_repay_plans' in response:
            self.installment_repay_plans = response['installment_repay_plans']
        if 'loan_ar_no' in response:
            self.loan_ar_no = response['loan_ar_no']
        if 'loan_term' in response:
            self.loan_term = response['loan_term']
        if 'nom_int' in response:
            self.nom_int = response['nom_int']
        if 'nom_prin' in response:
            self.nom_prin = response['nom_prin']
        if 'ovd_int' in response:
            self.ovd_int = response['ovd_int']
        if 'ovd_int_pen_int' in response:
            self.ovd_int_pen_int = response['ovd_int_pen_int']
        if 'ovd_prin' in response:
            self.ovd_prin = response['ovd_prin']
        if 'ovd_prin_pen_int' in response:
            self.ovd_prin_pen_int = response['ovd_prin_pen_int']
        if 'repay_modes' in response:
            self.repay_modes = response['repay_modes']
