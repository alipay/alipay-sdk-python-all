#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenNumberRangeValue import OpenNumberRangeValue


class OpenCrowdOperationOptionRequest(object):

    def __init__(self):
        self._number_range_option_value = None
        self._option_code = None
        self._option_value_id_list = None
        self._option_value_list = None

    @property
    def number_range_option_value(self):
        return self._number_range_option_value

    @number_range_option_value.setter
    def number_range_option_value(self, value):
        if isinstance(value, OpenNumberRangeValue):
            self._number_range_option_value = value
        else:
            self._number_range_option_value = OpenNumberRangeValue.from_alipay_dict(value)
    @property
    def option_code(self):
        return self._option_code

    @option_code.setter
    def option_code(self, value):
        self._option_code = value
    @property
    def option_value_id_list(self):
        return self._option_value_id_list

    @option_value_id_list.setter
    def option_value_id_list(self, value):
        self._option_value_id_list = value
    @property
    def option_value_list(self):
        return self._option_value_list

    @option_value_list.setter
    def option_value_list(self, value):
        self._option_value_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.number_range_option_value:
            if hasattr(self.number_range_option_value, 'to_alipay_dict'):
                params['number_range_option_value'] = self.number_range_option_value.to_alipay_dict()
            else:
                params['number_range_option_value'] = self.number_range_option_value
        if self.option_code:
            if hasattr(self.option_code, 'to_alipay_dict'):
                params['option_code'] = self.option_code.to_alipay_dict()
            else:
                params['option_code'] = self.option_code
        if self.option_value_id_list:
            if hasattr(self.option_value_id_list, 'to_alipay_dict'):
                params['option_value_id_list'] = self.option_value_id_list.to_alipay_dict()
            else:
                params['option_value_id_list'] = self.option_value_id_list
        if self.option_value_list:
            if hasattr(self.option_value_list, 'to_alipay_dict'):
                params['option_value_list'] = self.option_value_list.to_alipay_dict()
            else:
                params['option_value_list'] = self.option_value_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenCrowdOperationOptionRequest()
        if 'number_range_option_value' in d:
            o.number_range_option_value = d['number_range_option_value']
        if 'option_code' in d:
            o.option_code = d['option_code']
        if 'option_value_id_list' in d:
            o.option_value_id_list = d['option_value_id_list']
        if 'option_value_list' in d:
            o.option_value_list = d['option_value_list']
        return o


