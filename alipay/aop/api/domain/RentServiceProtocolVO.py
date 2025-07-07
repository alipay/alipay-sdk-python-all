#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentServiceProtocolVO(object):

    def __init__(self):
        self._protocol_name = None
        self._protocol_path = None

    @property
    def protocol_name(self):
        return self._protocol_name

    @protocol_name.setter
    def protocol_name(self, value):
        self._protocol_name = value
    @property
    def protocol_path(self):
        return self._protocol_path

    @protocol_path.setter
    def protocol_path(self, value):
        self._protocol_path = value


    def to_alipay_dict(self):
        params = dict()
        if self.protocol_name:
            if hasattr(self.protocol_name, 'to_alipay_dict'):
                params['protocol_name'] = self.protocol_name.to_alipay_dict()
            else:
                params['protocol_name'] = self.protocol_name
        if self.protocol_path:
            if hasattr(self.protocol_path, 'to_alipay_dict'):
                params['protocol_path'] = self.protocol_path.to_alipay_dict()
            else:
                params['protocol_path'] = self.protocol_path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentServiceProtocolVO()
        if 'protocol_name' in d:
            o.protocol_name = d['protocol_name']
        if 'protocol_path' in d:
            o.protocol_path = d['protocol_path']
        return o


