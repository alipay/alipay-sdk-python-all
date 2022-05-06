#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillAccountdailyQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_product_code = None
        self._bill_user_account_no = None
        self._bill_user_id = None
        self._date = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_product_code(self):
        return self._agreement_product_code

    @agreement_product_code.setter
    def agreement_product_code(self, value):
        self._agreement_product_code = value
    @property
    def bill_user_account_no(self):
        return self._bill_user_account_no

    @bill_user_account_no.setter
    def bill_user_account_no(self, value):
        self._bill_user_account_no = value
    @property
    def bill_user_id(self):
        return self._bill_user_id

    @bill_user_id.setter
    def bill_user_id(self, value):
        self._bill_user_id = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_product_code:
            if hasattr(self.agreement_product_code, 'to_alipay_dict'):
                params['agreement_product_code'] = self.agreement_product_code.to_alipay_dict()
            else:
                params['agreement_product_code'] = self.agreement_product_code
        if self.bill_user_account_no:
            if hasattr(self.bill_user_account_no, 'to_alipay_dict'):
                params['bill_user_account_no'] = self.bill_user_account_no.to_alipay_dict()
            else:
                params['bill_user_account_no'] = self.bill_user_account_no
        if self.bill_user_id:
            if hasattr(self.bill_user_id, 'to_alipay_dict'):
                params['bill_user_id'] = self.bill_user_id.to_alipay_dict()
            else:
                params['bill_user_id'] = self.bill_user_id
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillAccountdailyQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_product_code' in d:
            o.agreement_product_code = d['agreement_product_code']
        if 'bill_user_account_no' in d:
            o.bill_user_account_no = d['bill_user_account_no']
        if 'bill_user_id' in d:
            o.bill_user_id = d['bill_user_id']
        if 'date' in d:
            o.date = d['date']
        return o


