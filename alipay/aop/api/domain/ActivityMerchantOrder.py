#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityMerchantOrder(object):

    def __init__(self):
        self._activity_type = None
        self._audit_result = None
        self._fail_reason = None
        self._order_id = None
        self._rate = None

    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def audit_result(self):
        return self._audit_result

    @audit_result.setter
    def audit_result(self, value):
        self._audit_result = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.audit_result:
            if hasattr(self.audit_result, 'to_alipay_dict'):
                params['audit_result'] = self.audit_result.to_alipay_dict()
            else:
                params['audit_result'] = self.audit_result
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityMerchantOrder()
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'audit_result' in d:
            o.audit_result = d['audit_result']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'rate' in d:
            o.rate = d['rate']
        return o


