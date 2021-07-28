#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BaseOpenApiResponseHeaderDTO(object):

    def __init__(self):
        self._status_code = None

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BaseOpenApiResponseHeaderDTO()
        if 'status_code' in d:
            o.status_code = d['status_code']
        return o


