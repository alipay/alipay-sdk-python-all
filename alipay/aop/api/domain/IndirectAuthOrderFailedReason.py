#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectAuthOrderFailedReason(object):

    def __init__(self):
        self._fail_param = None
        self._fail_reason = None

    @property
    def fail_param(self):
        return self._fail_param

    @fail_param.setter
    def fail_param(self, value):
        self._fail_param = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_param:
            if hasattr(self.fail_param, 'to_alipay_dict'):
                params['fail_param'] = self.fail_param.to_alipay_dict()
            else:
                params['fail_param'] = self.fail_param
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectAuthOrderFailedReason()
        if 'fail_param' in d:
            o.fail_param = d['fail_param']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        return o


