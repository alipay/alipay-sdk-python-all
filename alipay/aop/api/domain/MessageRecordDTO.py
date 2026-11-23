#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MessageRecordDTO(object):

    def __init__(self):
        self._send_result = None
        self._uuid = None

    @property
    def send_result(self):
        return self._send_result

    @send_result.setter
    def send_result(self, value):
        self._send_result = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.send_result:
            if hasattr(self.send_result, 'to_alipay_dict'):
                params['send_result'] = self.send_result.to_alipay_dict()
            else:
                params['send_result'] = self.send_result
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MessageRecordDTO()
        if 'send_result' in d:
            o.send_result = d['send_result']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


