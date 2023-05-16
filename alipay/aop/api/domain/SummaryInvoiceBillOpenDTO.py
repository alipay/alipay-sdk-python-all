#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SummaryInvoiceBillOpenDTO(object):

    def __init__(self):
        self._bill_no = None
        self._biz_out_no = None
        self._buyer_open_id = None
        self._buyer_user_id = None
        self._pay_type = None
        self._related_pay_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def biz_out_no(self):
        return self._biz_out_no

    @biz_out_no.setter
    def biz_out_no(self, value):
        self._biz_out_no = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def related_pay_no(self):
        return self._related_pay_no

    @related_pay_no.setter
    def related_pay_no(self, value):
        self._related_pay_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.biz_out_no:
            if hasattr(self.biz_out_no, 'to_alipay_dict'):
                params['biz_out_no'] = self.biz_out_no.to_alipay_dict()
            else:
                params['biz_out_no'] = self.biz_out_no
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.related_pay_no:
            if hasattr(self.related_pay_no, 'to_alipay_dict'):
                params['related_pay_no'] = self.related_pay_no.to_alipay_dict()
            else:
                params['related_pay_no'] = self.related_pay_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SummaryInvoiceBillOpenDTO()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'biz_out_no' in d:
            o.biz_out_no = d['biz_out_no']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'related_pay_no' in d:
            o.related_pay_no = d['related_pay_no']
        return o


