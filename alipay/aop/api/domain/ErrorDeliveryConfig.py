#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryConfig import DeliveryConfig


class ErrorDeliveryConfig(object):

    def __init__(self):
        self._delivery_config = None
        self._error_code = None
        self._error_msg = None

    @property
    def delivery_config(self):
        return self._delivery_config

    @delivery_config.setter
    def delivery_config(self, value):
        if isinstance(value, DeliveryConfig):
            self._delivery_config = value
        else:
            self._delivery_config = DeliveryConfig.from_alipay_dict(value)
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_config:
            if hasattr(self.delivery_config, 'to_alipay_dict'):
                params['delivery_config'] = self.delivery_config.to_alipay_dict()
            else:
                params['delivery_config'] = self.delivery_config
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ErrorDeliveryConfig()
        if 'delivery_config' in d:
            o.delivery_config = d['delivery_config']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        return o


