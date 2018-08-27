#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MyBkAccountVO import MyBkAccountVO
from alipay.aop.api.domain.LoanChargeInfo import LoanChargeInfo
from alipay.aop.api.domain.InstallmentValue import InstallmentValue


class MybankCreditLoantradeLoanschemeQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeLoanschemeQueryResponse, self).__init__()
        self._account_vo = None
        self._alert_amt = None
        self._charge_info_list = None
        self._credit_expire_date = None
        self._credit_lmt_amt = None
        self._credit_no = None
        self._credit_source = None
        self._credit_start_date = None
        self._int_rate = None
        self._loan_policy_code = None
        self._loan_term = None
        self._loan_term_unit = None
        self._loanable_amt = None
        self._repay_mode_list = None
        self._sale_pd_code = None
        self._water_amt = None

    @property
    def account_vo(self):
        return self._account_vo

    @account_vo.setter
    def account_vo(self, value):
        if isinstance(value, list):
            self._account_vo = list()
            for i in value:
                if isinstance(i, MyBkAccountVO):
                    self._account_vo.append(i)
                else:
                    self._account_vo.append(MyBkAccountVO.from_alipay_dict(i))
    @property
    def alert_amt(self):
        return self._alert_amt

    @alert_amt.setter
    def alert_amt(self, value):
        self._alert_amt = value
    @property
    def charge_info_list(self):
        return self._charge_info_list

    @charge_info_list.setter
    def charge_info_list(self, value):
        if isinstance(value, list):
            self._charge_info_list = list()
            for i in value:
                if isinstance(i, LoanChargeInfo):
                    self._charge_info_list.append(i)
                else:
                    self._charge_info_list.append(LoanChargeInfo.from_alipay_dict(i))
    @property
    def credit_expire_date(self):
        return self._credit_expire_date

    @credit_expire_date.setter
    def credit_expire_date(self, value):
        self._credit_expire_date = value
    @property
    def credit_lmt_amt(self):
        return self._credit_lmt_amt

    @credit_lmt_amt.setter
    def credit_lmt_amt(self, value):
        self._credit_lmt_amt = value
    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def credit_source(self):
        return self._credit_source

    @credit_source.setter
    def credit_source(self, value):
        self._credit_source = value
    @property
    def credit_start_date(self):
        return self._credit_start_date

    @credit_start_date.setter
    def credit_start_date(self, value):
        self._credit_start_date = value
    @property
    def int_rate(self):
        return self._int_rate

    @int_rate.setter
    def int_rate(self, value):
        self._int_rate = value
    @property
    def loan_policy_code(self):
        return self._loan_policy_code

    @loan_policy_code.setter
    def loan_policy_code(self, value):
        self._loan_policy_code = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def loan_term_unit(self):
        return self._loan_term_unit

    @loan_term_unit.setter
    def loan_term_unit(self, value):
        self._loan_term_unit = value
    @property
    def loanable_amt(self):
        return self._loanable_amt

    @loanable_amt.setter
    def loanable_amt(self, value):
        self._loanable_amt = value
    @property
    def repay_mode_list(self):
        return self._repay_mode_list

    @repay_mode_list.setter
    def repay_mode_list(self, value):
        if isinstance(value, InstallmentValue):
            self._repay_mode_list = value
        else:
            self._repay_mode_list = InstallmentValue.from_alipay_dict(value)
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value
    @property
    def water_amt(self):
        return self._water_amt

    @water_amt.setter
    def water_amt(self, value):
        self._water_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeLoanschemeQueryResponse, self).parse_response_content(response_content)
        if 'account_vo' in response:
            self.account_vo = response['account_vo']
        if 'alert_amt' in response:
            self.alert_amt = response['alert_amt']
        if 'charge_info_list' in response:
            self.charge_info_list = response['charge_info_list']
        if 'credit_expire_date' in response:
            self.credit_expire_date = response['credit_expire_date']
        if 'credit_lmt_amt' in response:
            self.credit_lmt_amt = response['credit_lmt_amt']
        if 'credit_no' in response:
            self.credit_no = response['credit_no']
        if 'credit_source' in response:
            self.credit_source = response['credit_source']
        if 'credit_start_date' in response:
            self.credit_start_date = response['credit_start_date']
        if 'int_rate' in response:
            self.int_rate = response['int_rate']
        if 'loan_policy_code' in response:
            self.loan_policy_code = response['loan_policy_code']
        if 'loan_term' in response:
            self.loan_term = response['loan_term']
        if 'loan_term_unit' in response:
            self.loan_term_unit = response['loan_term_unit']
        if 'loanable_amt' in response:
            self.loanable_amt = response['loanable_amt']
        if 'repay_mode_list' in response:
            self.repay_mode_list = response['repay_mode_list']
        if 'sale_pd_code' in response:
            self.sale_pd_code = response['sale_pd_code']
        if 'water_amt' in response:
            self.water_amt = response['water_amt']
