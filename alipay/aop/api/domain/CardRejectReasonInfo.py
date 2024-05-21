#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardRejectReasonInfo(object):

    def __init__(self):
        self._reject_item = None
        self._reject_reason = None

    @property
    def reject_item(self):
        return self._reject_item

    @reject_item.setter
    def reject_item(self, value):
        self._reject_item = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.reject_item:
            if hasattr(self.reject_item, 'to_alipay_dict'):
                params['reject_item'] = self.reject_item.to_alipay_dict()
            else:
                params['reject_item'] = self.reject_item
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardRejectReasonInfo()
        if 'reject_item' in d:
            o.reject_item = d['reject_item']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        return o


