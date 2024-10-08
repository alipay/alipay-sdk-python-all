#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AcceptInfoVO(object):

    def __init__(self):
        self._accept_mode = None
        self._verify_result = None

    @property
    def accept_mode(self):
        return self._accept_mode

    @accept_mode.setter
    def accept_mode(self, value):
        self._accept_mode = value
    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_mode:
            if hasattr(self.accept_mode, 'to_alipay_dict'):
                params['accept_mode'] = self.accept_mode.to_alipay_dict()
            else:
                params['accept_mode'] = self.accept_mode
        if self.verify_result:
            if hasattr(self.verify_result, 'to_alipay_dict'):
                params['verify_result'] = self.verify_result.to_alipay_dict()
            else:
                params['verify_result'] = self.verify_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AcceptInfoVO()
        if 'accept_mode' in d:
            o.accept_mode = d['accept_mode']
        if 'verify_result' in d:
            o.verify_result = d['verify_result']
        return o


