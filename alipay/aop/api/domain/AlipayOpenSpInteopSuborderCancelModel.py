#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpInteopSuborderCancelModel(object):

    def __init__(self):
        self._cancel_reason = None
        self._inteop_order_no = None
        self._sub_order_no = None

    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def sub_order_no(self):
        return self._sub_order_no

    @sub_order_no.setter
    def sub_order_no(self, value):
        self._sub_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.sub_order_no:
            if hasattr(self.sub_order_no, 'to_alipay_dict'):
                params['sub_order_no'] = self.sub_order_no.to_alipay_dict()
            else:
                params['sub_order_no'] = self.sub_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopSuborderCancelModel()
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'sub_order_no' in d:
            o.sub_order_no = d['sub_order_no']
        return o


