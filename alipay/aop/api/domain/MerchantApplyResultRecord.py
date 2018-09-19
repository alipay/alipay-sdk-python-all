#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantApplyResultRecord(object):

    def __init__(self):
        self._prod_name = None
        self._prop_input_key = None
        self._result_msg = None
        self._result_status = None
        self._result_type = None

    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def prop_input_key(self):
        return self._prop_input_key

    @prop_input_key.setter
    def prop_input_key(self, value):
        self._prop_input_key = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.prop_input_key:
            if hasattr(self.prop_input_key, 'to_alipay_dict'):
                params['prop_input_key'] = self.prop_input_key.to_alipay_dict()
            else:
                params['prop_input_key'] = self.prop_input_key
        if self.result_msg:
            if hasattr(self.result_msg, 'to_alipay_dict'):
                params['result_msg'] = self.result_msg.to_alipay_dict()
            else:
                params['result_msg'] = self.result_msg
        if self.result_status:
            if hasattr(self.result_status, 'to_alipay_dict'):
                params['result_status'] = self.result_status.to_alipay_dict()
            else:
                params['result_status'] = self.result_status
        if self.result_type:
            if hasattr(self.result_type, 'to_alipay_dict'):
                params['result_type'] = self.result_type.to_alipay_dict()
            else:
                params['result_type'] = self.result_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantApplyResultRecord()
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prop_input_key' in d:
            o.prop_input_key = d['prop_input_key']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'result_status' in d:
            o.result_status = d['result_status']
        if 'result_type' in d:
            o.result_type = d['result_type']
        return o


