#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsSnVerifyFailDetail(object):

    def __init__(self):
        self._fail_reason = None
        self._sn_id = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def sn_id(self):
        return self._sn_id

    @sn_id.setter
    def sn_id(self, value):
        self._sn_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.sn_id:
            if hasattr(self.sn_id, 'to_alipay_dict'):
                params['sn_id'] = self.sn_id.to_alipay_dict()
            else:
                params['sn_id'] = self.sn_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsSnVerifyFailDetail()
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'sn_id' in d:
            o.sn_id = d['sn_id']
        return o


