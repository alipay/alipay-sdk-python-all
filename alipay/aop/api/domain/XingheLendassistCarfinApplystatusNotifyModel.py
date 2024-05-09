#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistCarfinApplystatusNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._credit_amt = None
        self._fin_drawdown_no = None
        self._fin_org = None
        self._loan_amt = None
        self._loan_date = None
        self._loan_rate = None
        self._loan_term = None
        self._loan_term_unit = None
        self._mortgage_rate = None
        self._org_drawdown_no = None
        self._out_apply_no = None
        self._refuse_code = None
        self._refuse_msg = None
        self._repay_type = None
        self._status = None
        self._valuate_price = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def credit_amt(self):
        return self._credit_amt

    @credit_amt.setter
    def credit_amt(self, value):
        self._credit_amt = value
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
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def valuate_price(self):
        return self._valuate_price

    @valuate_price.setter
    def valuate_price(self, value):
        self._valuate_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.credit_amt:
            if hasattr(self.credit_amt, 'to_alipay_dict'):
                params['credit_amt'] = self.credit_amt.to_alipay_dict()
            else:
                params['credit_amt'] = self.credit_amt
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
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        if self.refuse_msg:
            if hasattr(self.refuse_msg, 'to_alipay_dict'):
                params['refuse_msg'] = self.refuse_msg.to_alipay_dict()
            else:
                params['refuse_msg'] = self.refuse_msg
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = XingheLendassistCarfinApplystatusNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'credit_amt' in d:
            o.credit_amt = d['credit_amt']
        if 'fin_drawdown_no' in d:
            o.fin_drawdown_no = d['fin_drawdown_no']
        if 'fin_org' in d:
            o.fin_org = d['fin_org']
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
        if 'mortgage_rate' in d:
            o.mortgage_rate = d['mortgage_rate']
        if 'org_drawdown_no' in d:
            o.org_drawdown_no = d['org_drawdown_no']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        if 'refuse_msg' in d:
            o.refuse_msg = d['refuse_msg']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        if 'status' in d:
            o.status = d['status']
        if 'valuate_price' in d:
            o.valuate_price = d['valuate_price']
        return o


