#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MakeCallRequest import MakeCallRequest


class AnttechOceanbaseObglobalMakecallCreateModel(object):

    def __init__(self):
        self._make_call_request = None

    @property
    def make_call_request(self):
        return self._make_call_request

    @make_call_request.setter
    def make_call_request(self, value):
        if isinstance(value, MakeCallRequest):
            self._make_call_request = value
        else:
            self._make_call_request = MakeCallRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.make_call_request:
            if hasattr(self.make_call_request, 'to_alipay_dict'):
                params['make_call_request'] = self.make_call_request.to_alipay_dict()
            else:
                params['make_call_request'] = self.make_call_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalMakecallCreateModel()
        if 'make_call_request' in d:
            o.make_call_request = d['make_call_request']
        return o


