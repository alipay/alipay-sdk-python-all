#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LendDrawdown(object):

    def __init__(self):
        self._fin_drawdown_no = None
        self._fin_org = None
        self._fund_rate = None
        self._loan_amt = None
        self._loan_date = None
        self._loan_rate = None
        self._loan_term = None
        self._loan_term_unit = None
        self._loan_type = None
        self._mortgage_rate = None
        self._org_drawdown_no = None
        self._product_code = None
        self._repay_type = None
        self._service_fee_rate = None
        self._valuate_price = None

    @property
    def fin_drawdown_no(self):
        return self._fin_drawdown_no

    @fin_drawdown_no.setter
    def fin_drawdown_no(self, value):
        self._fin_drawdown_no = value
    @property
    def fin_org(self):
        return self._fin_org

    @fin_org.setter
    def fin_org(self, value):
        self._fin_org = value
    @property
    def fund_rate(self):
        return self._fund_rate

    @fund_rate.setter
    def fund_rate(self, value):
        self._fund_rate = value
    @property
    def loan_amt(self):
        return self._loan_amt

    @loan_amt.setter
    def loan_amt(self, value):
        self._loan_amt = value
    @property
    def loan_date(self):
        return self._loan_date

    @loan_date.setter
    def loan_date(self, value):
        self._loan_date = value
    @property
    def loan_rate(self):
        return self._loan_rate

    @loan_rate.setter
    def loan_rate(self, value):
        self._loan_rate = value
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
    def loan_type(self):
        return self._loan_type

    @loan_type.setter
    def loan_type(self, value):
        self._loan_type = value
    @property
    def mortgage_rate(self):
        return self._mortgage_rate

    @mortgage_rate.setter
    def mortgage_rate(self, value):
        self._mortgage_rate = value
    @property
    def org_drawdown_no(self):
        return self._org_drawdown_no

    @org_drawdown_no.setter
    def org_drawdown_no(self, value):
        self._org_drawdown_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value
    @property
    def service_fee_rate(self):
        return self._service_fee_rate

    @service_fee_rate.setter
    def service_fee_rate(self, value):
        self._service_fee_rate = value
    @property
    def valuate_price(self):
        return self._valuate_price

    @valuate_price.setter
    def valuate_price(self, value):
        self._valuate_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.fin_drawdown_no:
            if hasattr(self.fin_drawdown_no, 'to_alipay_dict'):
                params['fin_drawdown_no'] = self.fin_drawdown_no.to_alipay_dict()
            else:
                params['fin_drawdown_no'] = self.fin_drawdown_no
        if self.fin_org:
            if hasattr(self.fin_org, 'to_alipay_dict'):
                params['fin_org'] = self.fin_org.to_alipay_dict()
            else:
                params['fin_org'] = self.fin_org
        if self.fund_rate:
            if hasattr(self.fund_rate, 'to_alipay_dict'):
                params['fund_rate'] = self.fund_rate.to_alipay_dict()
            else:
                params['fund_rate'] = self.fund_rate
        if self.loan_amt:
            if hasattr(self.loan_amt, 'to_alipay_dict'):
                params['loan_amt'] = self.loan_amt.to_alipay_dict()
            else:
                params['loan_amt'] = self.loan_amt
        if self.loan_date:
            if hasattr(self.loan_date, 'to_alipay_dict'):
                params['loan_date'] = self.loan_date.to_alipay_dict()
            else:
                params['loan_date'] = self.loan_date
        if self.loan_rate:
            if hasattr(self.loan_rate, 'to_alipay_dict'):
                params['loan_rate'] = self.loan_rate.to_alipay_dict()
            else:
                params['loan_rate'] = self.loan_rate
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.loan_term_unit:
            if hasattr(self.loan_term_unit, 'to_alipay_dict'):
                params['loan_term_unit'] = self.loan_term_unit.to_alipay_dict()
            else:
                params['loan_term_unit'] = self.loan_term_unit
        if self.loan_type:
            if hasattr(self.loan_type, 'to_alipay_dict'):
                params['loan_type'] = self.loan_type.to_alipay_dict()
            else:
                params['loan_type'] = self.loan_type
        if self.mortgage_rate:
            if hasattr(self.mortgage_rate, 'to_alipay_dict'):
                params['mortgage_rate'] = self.mortgage_rate.to_alipay_dict()
            else:
                params['mortgage_rate'] = self.mortgage_rate
        if self.org_drawdown_no:
            if hasattr(self.org_drawdown_no, 'to_alipay_dict'):
                params['org_drawdown_no'] = self.org_drawdown_no.to_alipay_dict()
            else:
                params['org_drawdown_no'] = self.org_drawdown_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
        if self.service_fee_rate:
            if hasattr(self.service_fee_rate, 'to_alipay_dict'):
                params['service_fee_rate'] = self.service_fee_rate.to_alipay_dict()
            else:
                params['service_fee_rate'] = self.service_fee_rate
        if self.valuate_price:
            if hasattr(self.valuate_price, 'to_alipay_dict'):
                params['valuate_price'] = self.valuate_price.to_alipay_dict()
            else:
                params['valuate_price'] = self.valuate_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LendDrawdown()
        if 'fin_drawdown_no' in d:
            o.fin_drawdown_no = d['fin_drawdown_no']
        if 'fin_org' in d:
            o.fin_org = d['fin_org']
        if 'fund_rate' in d:
            o.fund_rate = d['fund_rate']
        if 'loan_amt' in d:
            o.loan_amt = d['loan_amt']
        if 'loan_date' in d:
            o.loan_date = d['loan_date']
        if 'loan_rate' in d:
            o.loan_rate = d['loan_rate']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'loan_type' in d:
            o.loan_type = d['loan_type']
        if 'mortgage_rate' in d:
            o.mortgage_rate = d['mortgage_rate']
        if 'org_drawdown_no' in d:
            o.org_drawdown_no = d['org_drawdown_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        if 'service_fee_rate' in d:
            o.service_fee_rate = d['service_fee_rate']
        if 'valuate_price' in d:
            o.valuate_price = d['valuate_price']
        return o


