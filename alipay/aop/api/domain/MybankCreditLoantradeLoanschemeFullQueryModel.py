#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MyBkAccountVO import MyBkAccountVO


class MybankCreditLoantradeLoanschemeFullQueryModel(object):

    def __init__(self):
        self._alipay_id = None
        self._apply_amt = None
        self._apply_date = None
        self._credit_no = None
        self._cust_group = None
        self._ip_id = None
        self._ip_role_id = None
        self._loan_policy_code = None
        self._loan_term = None
        self._loan_term_unit = None
        self._promo_tools = None
        self._repay_mode = None
        self._sale_pd_code = None
        self._trans_in_account = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
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
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def cust_group(self):
        return self._cust_group

    @cust_group.setter
    def cust_group(self, value):
        self._cust_group = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
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
    def promo_tools(self):
        return self._promo_tools

    @promo_tools.setter
    def promo_tools(self, value):
        if isinstance(value, list):
            self._promo_tools = list()
            for i in value:
                self._promo_tools.append(i)
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value
    @property
    def trans_in_account(self):
        return self._trans_in_account

    @trans_in_account.setter
    def trans_in_account(self, value):
        if isinstance(value, MyBkAccountVO):
            self._trans_in_account = value
        else:
            self._trans_in_account = MyBkAccountVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.credit_no:
            if hasattr(self.credit_no, 'to_alipay_dict'):
                params['credit_no'] = self.credit_no.to_alipay_dict()
            else:
                params['credit_no'] = self.credit_no
        if self.cust_group:
            if hasattr(self.cust_group, 'to_alipay_dict'):
                params['cust_group'] = self.cust_group.to_alipay_dict()
            else:
                params['cust_group'] = self.cust_group
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.loan_policy_code:
            if hasattr(self.loan_policy_code, 'to_alipay_dict'):
                params['loan_policy_code'] = self.loan_policy_code.to_alipay_dict()
            else:
                params['loan_policy_code'] = self.loan_policy_code
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
        if self.promo_tools:
            if isinstance(self.promo_tools, list):
                for i in range(0, len(self.promo_tools)):
                    element = self.promo_tools[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_tools[i] = element.to_alipay_dict()
            if hasattr(self.promo_tools, 'to_alipay_dict'):
                params['promo_tools'] = self.promo_tools.to_alipay_dict()
            else:
                params['promo_tools'] = self.promo_tools
        if self.repay_mode:
            if hasattr(self.repay_mode, 'to_alipay_dict'):
                params['repay_mode'] = self.repay_mode.to_alipay_dict()
            else:
                params['repay_mode'] = self.repay_mode
        if self.sale_pd_code:
            if hasattr(self.sale_pd_code, 'to_alipay_dict'):
                params['sale_pd_code'] = self.sale_pd_code.to_alipay_dict()
            else:
                params['sale_pd_code'] = self.sale_pd_code
        if self.trans_in_account:
            if hasattr(self.trans_in_account, 'to_alipay_dict'):
                params['trans_in_account'] = self.trans_in_account.to_alipay_dict()
            else:
                params['trans_in_account'] = self.trans_in_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeLoanschemeFullQueryModel()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'credit_no' in d:
            o.credit_no = d['credit_no']
        if 'cust_group' in d:
            o.cust_group = d['cust_group']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'loan_policy_code' in d:
            o.loan_policy_code = d['loan_policy_code']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'promo_tools' in d:
            o.promo_tools = d['promo_tools']
        if 'repay_mode' in d:
            o.repay_mode = d['repay_mode']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'trans_in_account' in d:
            o.trans_in_account = d['trans_in_account']
        return o


