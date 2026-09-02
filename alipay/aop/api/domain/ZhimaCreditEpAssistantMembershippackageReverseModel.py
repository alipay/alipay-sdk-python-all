#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAssistantMembershippackageReverseModel(object):

    def __init__(self):
        self._origin_order_no = None
        self._out_biz_no = None
        self._reverse_reason = None

    @property
    def origin_order_no(self):
        return self._origin_order_no

    @origin_order_no.setter
    def origin_order_no(self, value):
        self._origin_order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def reverse_reason(self):
        return self._reverse_reason

    @reverse_reason.setter
    def reverse_reason(self, value):
        self._reverse_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.origin_order_no:
            if hasattr(self.origin_order_no, 'to_alipay_dict'):
                params['origin_order_no'] = self.origin_order_no.to_alipay_dict()
            else:
                params['origin_order_no'] = self.origin_order_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.reverse_reason:
            if hasattr(self.reverse_reason, 'to_alipay_dict'):
                params['reverse_reason'] = self.reverse_reason.to_alipay_dict()
            else:
                params['reverse_reason'] = self.reverse_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAssistantMembershippackageReverseModel()
        if 'origin_order_no' in d:
            o.origin_order_no = d['origin_order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'reverse_reason' in d:
            o.reverse_reason = d['reverse_reason']
        return o


