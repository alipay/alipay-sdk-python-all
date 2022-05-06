#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillAccountlogQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_product_code = None
        self._alipay_order_no = None
        self._bill_user_id = None
        self._end_time = None
        self._merchant_order_no = None
        self._page_no = None
        self._page_size = None
        self._start_time = None
        self._trans_code = None

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
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def bill_user_id(self):
        return self._bill_user_id

    @bill_user_id.setter
    def bill_user_id(self, value):
        self._bill_user_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def trans_code(self):
        return self._trans_code

    @trans_code.setter
    def trans_code(self, value):
        self._trans_code = value


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
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.bill_user_id:
            if hasattr(self.bill_user_id, 'to_alipay_dict'):
                params['bill_user_id'] = self.bill_user_id.to_alipay_dict()
            else:
                params['bill_user_id'] = self.bill_user_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.trans_code:
            if hasattr(self.trans_code, 'to_alipay_dict'):
                params['trans_code'] = self.trans_code.to_alipay_dict()
            else:
                params['trans_code'] = self.trans_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillAccountlogQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_product_code' in d:
            o.agreement_product_code = d['agreement_product_code']
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'bill_user_id' in d:
            o.bill_user_id = d['bill_user_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'trans_code' in d:
            o.trans_code = d['trans_code']
        return o


