#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumerLoanTriggerActionExtInfo(object):

    def __init__(self):
        self._action_type = None
        self._entity_type = None
        self._out_biz_no = None
        self._paid_amount = None
        self._paid_time = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self._paid_amount = value
    @property
    def paid_time(self):
        return self._paid_time

    @paid_time.setter
    def paid_time(self, value):
        self._paid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.paid_amount:
            if hasattr(self.paid_amount, 'to_alipay_dict'):
                params['paid_amount'] = self.paid_amount.to_alipay_dict()
            else:
                params['paid_amount'] = self.paid_amount
        if self.paid_time:
            if hasattr(self.paid_time, 'to_alipay_dict'):
                params['paid_time'] = self.paid_time.to_alipay_dict()
            else:
                params['paid_time'] = self.paid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanTriggerActionExtInfo()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'paid_amount' in d:
            o.paid_amount = d['paid_amount']
        if 'paid_time' in d:
            o.paid_time = d['paid_time']
        return o


