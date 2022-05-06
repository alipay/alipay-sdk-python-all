#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotIdentityFaceOutEventApiResponse(object):

    def __init__(self):
        self._fail_reason = None
        self._state = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotIdentityFaceOutEventApiResponse()
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'state' in d:
            o.state = d['state']
        return o


