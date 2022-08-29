#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeductInfo import DeductInfo


class CustomerDefineVoucherInfo(object):

    def __init__(self):
        self._deduct_info = None

    @property
    def deduct_info(self):
        return self._deduct_info

    @deduct_info.setter
    def deduct_info(self, value):
        if isinstance(value, DeductInfo):
            self._deduct_info = value
        else:
            self._deduct_info = DeductInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_info:
            if hasattr(self.deduct_info, 'to_alipay_dict'):
                params['deduct_info'] = self.deduct_info.to_alipay_dict()
            else:
                params['deduct_info'] = self.deduct_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerDefineVoucherInfo()
        if 'deduct_info' in d:
            o.deduct_info = d['deduct_info']
        return o


