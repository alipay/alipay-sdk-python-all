#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AftersaleServiceTag(object):

    def __init__(self):
        self._service_tag_code = None
        self._service_tag_name = None

    @property
    def service_tag_code(self):
        return self._service_tag_code

    @service_tag_code.setter
    def service_tag_code(self, value):
        self._service_tag_code = value
    @property
    def service_tag_name(self):
        return self._service_tag_name

    @service_tag_name.setter
    def service_tag_name(self, value):
        self._service_tag_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_tag_code:
            if hasattr(self.service_tag_code, 'to_alipay_dict'):
                params['service_tag_code'] = self.service_tag_code.to_alipay_dict()
            else:
                params['service_tag_code'] = self.service_tag_code
        if self.service_tag_name:
            if hasattr(self.service_tag_name, 'to_alipay_dict'):
                params['service_tag_name'] = self.service_tag_name.to_alipay_dict()
            else:
                params['service_tag_name'] = self.service_tag_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftersaleServiceTag()
        if 'service_tag_code' in d:
            o.service_tag_code = d['service_tag_code']
        if 'service_tag_name' in d:
            o.service_tag_name = d['service_tag_name']
        return o


