#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinLendServiceInfo(object):

    def __init__(self):
        self._service_type = None
        self._service_type_version = None

    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def service_type_version(self):
        return self._service_type_version

    @service_type_version.setter
    def service_type_version(self, value):
        self._service_type_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.service_type_version:
            if hasattr(self.service_type_version, 'to_alipay_dict'):
                params['service_type_version'] = self.service_type_version.to_alipay_dict()
            else:
                params['service_type_version'] = self.service_type_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinLendServiceInfo()
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'service_type_version' in d:
            o.service_type_version = d['service_type_version']
        return o


