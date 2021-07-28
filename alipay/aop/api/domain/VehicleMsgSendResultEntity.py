#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleMsgSendResultEntity(object):

    def __init__(self):
        self._out_msg_id = None
        self._result = None
        self._success = None

    @property
    def out_msg_id(self):
        return self._out_msg_id

    @out_msg_id.setter
    def out_msg_id(self, value):
        self._out_msg_id = value
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
        if self.out_msg_id:
            if hasattr(self.out_msg_id, 'to_alipay_dict'):
                params['out_msg_id'] = self.out_msg_id.to_alipay_dict()
            else:
                params['out_msg_id'] = self.out_msg_id
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
        o = VehicleMsgSendResultEntity()
        if 'out_msg_id' in d:
            o.out_msg_id = d['out_msg_id']
        if 'result' in d:
            o.result = d['result']
        if 'success' in d:
            o.success = d['success']
        return o


