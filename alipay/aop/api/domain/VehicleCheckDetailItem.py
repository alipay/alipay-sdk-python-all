#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleCheckDetailItem(object):

    def __init__(self):
        self._check_item_code = None
        self._check_item_result = None

    @property
    def check_item_code(self):
        return self._check_item_code

    @check_item_code.setter
    def check_item_code(self, value):
        self._check_item_code = value
    @property
    def check_item_result(self):
        return self._check_item_result

    @check_item_result.setter
    def check_item_result(self, value):
        self._check_item_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_item_code:
            if hasattr(self.check_item_code, 'to_alipay_dict'):
                params['check_item_code'] = self.check_item_code.to_alipay_dict()
            else:
                params['check_item_code'] = self.check_item_code
        if self.check_item_result:
            if hasattr(self.check_item_result, 'to_alipay_dict'):
                params['check_item_result'] = self.check_item_result.to_alipay_dict()
            else:
                params['check_item_result'] = self.check_item_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleCheckDetailItem()
        if 'check_item_code' in d:
            o.check_item_code = d['check_item_code']
        if 'check_item_result' in d:
            o.check_item_result = d['check_item_result']
        return o


