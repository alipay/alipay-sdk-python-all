#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalOrderRefundApproveModel(object):

    def __init__(self):
        self._action_type = None
        self._order_no = None
        self._reason = None
        self._reason_code = None
        self._refund_no = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def refund_no(self):
        return self._refund_no

    @refund_no.setter
    def refund_no(self, value):
        self._refund_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.refund_no:
            if hasattr(self.refund_no, 'to_alipay_dict'):
                params['refund_no'] = self.refund_no.to_alipay_dict()
            else:
                params['refund_no'] = self.refund_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOrderRefundApproveModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'reason' in d:
            o.reason = d['reason']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'refund_no' in d:
            o.refund_no = d['refund_no']
        return o


