#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommerceAppUploadResponseData(object):

    def __init__(self):
        self._response = None
        self._time = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.response:
            if hasattr(self.response, 'to_alipay_dict'):
                params['response'] = self.response.to_alipay_dict()
            else:
                params['response'] = self.response
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommerceAppUploadResponseData()
        if 'response' in d:
            o.response = d['response']
        if 'time' in d:
            o.time = d['time']
        return o


