#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArMonthlyBillDTO import ArMonthlyBillDTO


class AlipayBossFncInvoicereceiptCreateModel(object):

    def __init__(self):
        self._event_code = None
        self._event_type = None
        self._monthly_bill = None
        self._msg_id = None
        self._out_biz_type = None

    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def monthly_bill(self):
        return self._monthly_bill

    @monthly_bill.setter
    def monthly_bill(self, value):
        if isinstance(value, ArMonthlyBillDTO):
            self._monthly_bill = value
        else:
            self._monthly_bill = ArMonthlyBillDTO.from_alipay_dict(value)
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.monthly_bill:
            if hasattr(self.monthly_bill, 'to_alipay_dict'):
                params['monthly_bill'] = self.monthly_bill.to_alipay_dict()
            else:
                params['monthly_bill'] = self.monthly_bill
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoicereceiptCreateModel()
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'monthly_bill' in d:
            o.monthly_bill = d['monthly_bill']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        return o


