#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarViolationInfoPushModel(object):

    def __init__(self):
        self._deal_type = None
        self._push_type = None
        self._vi_address = None
        self._vi_fine = None
        self._vi_handled = None
        self._vi_number = None
        self._vi_point = None
        self._vi_time = None
        self._vi_type = None

    @property
    def deal_type(self):
        return self._deal_type

    @deal_type.setter
    def deal_type(self, value):
        self._deal_type = value
    @property
    def push_type(self):
        return self._push_type

    @push_type.setter
    def push_type(self, value):
        self._push_type = value
    @property
    def vi_address(self):
        return self._vi_address

    @vi_address.setter
    def vi_address(self, value):
        self._vi_address = value
    @property
    def vi_fine(self):
        return self._vi_fine

    @vi_fine.setter
    def vi_fine(self, value):
        self._vi_fine = value
    @property
    def vi_handled(self):
        return self._vi_handled

    @vi_handled.setter
    def vi_handled(self, value):
        self._vi_handled = value
    @property
    def vi_number(self):
        return self._vi_number

    @vi_number.setter
    def vi_number(self, value):
        self._vi_number = value
    @property
    def vi_point(self):
        return self._vi_point

    @vi_point.setter
    def vi_point(self, value):
        self._vi_point = value
    @property
    def vi_time(self):
        return self._vi_time

    @vi_time.setter
    def vi_time(self, value):
        self._vi_time = value
    @property
    def vi_type(self):
        return self._vi_type

    @vi_type.setter
    def vi_type(self, value):
        self._vi_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.deal_type:
            if hasattr(self.deal_type, 'to_alipay_dict'):
                params['deal_type'] = self.deal_type.to_alipay_dict()
            else:
                params['deal_type'] = self.deal_type
        if self.push_type:
            if hasattr(self.push_type, 'to_alipay_dict'):
                params['push_type'] = self.push_type.to_alipay_dict()
            else:
                params['push_type'] = self.push_type
        if self.vi_address:
            if hasattr(self.vi_address, 'to_alipay_dict'):
                params['vi_address'] = self.vi_address.to_alipay_dict()
            else:
                params['vi_address'] = self.vi_address
        if self.vi_fine:
            if hasattr(self.vi_fine, 'to_alipay_dict'):
                params['vi_fine'] = self.vi_fine.to_alipay_dict()
            else:
                params['vi_fine'] = self.vi_fine
        if self.vi_handled:
            if hasattr(self.vi_handled, 'to_alipay_dict'):
                params['vi_handled'] = self.vi_handled.to_alipay_dict()
            else:
                params['vi_handled'] = self.vi_handled
        if self.vi_number:
            if hasattr(self.vi_number, 'to_alipay_dict'):
                params['vi_number'] = self.vi_number.to_alipay_dict()
            else:
                params['vi_number'] = self.vi_number
        if self.vi_point:
            if hasattr(self.vi_point, 'to_alipay_dict'):
                params['vi_point'] = self.vi_point.to_alipay_dict()
            else:
                params['vi_point'] = self.vi_point
        if self.vi_time:
            if hasattr(self.vi_time, 'to_alipay_dict'):
                params['vi_time'] = self.vi_time.to_alipay_dict()
            else:
                params['vi_time'] = self.vi_time
        if self.vi_type:
            if hasattr(self.vi_type, 'to_alipay_dict'):
                params['vi_type'] = self.vi_type.to_alipay_dict()
            else:
                params['vi_type'] = self.vi_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarViolationInfoPushModel()
        if 'deal_type' in d:
            o.deal_type = d['deal_type']
        if 'push_type' in d:
            o.push_type = d['push_type']
        if 'vi_address' in d:
            o.vi_address = d['vi_address']
        if 'vi_fine' in d:
            o.vi_fine = d['vi_fine']
        if 'vi_handled' in d:
            o.vi_handled = d['vi_handled']
        if 'vi_number' in d:
            o.vi_number = d['vi_number']
        if 'vi_point' in d:
            o.vi_point = d['vi_point']
        if 'vi_time' in d:
            o.vi_time = d['vi_time']
        if 'vi_type' in d:
            o.vi_type = d['vi_type']
        return o


