#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceDeployorderResultSendModel(object):

    def __init__(self):
        self._record_id = None
        self._result = None
        self._success = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDeployorderResultSendModel()
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'result' in d:
            o.result = d['result']
        if 'success' in d:
            o.success = d['success']
        return o


