#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfimMqSyncModel(object):

    def __init__(self):
        self._msg_body = None
        self._open_id = None
        self._routing_key = None

    @property
    def msg_body(self):
        return self._msg_body

    @msg_body.setter
    def msg_body(self, value):
        self._msg_body = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def routing_key(self):
        return self._routing_key

    @routing_key.setter
    def routing_key(self, value):
        self._routing_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_body:
            if hasattr(self.msg_body, 'to_alipay_dict'):
                params['msg_body'] = self.msg_body.to_alipay_dict()
            else:
                params['msg_body'] = self.msg_body
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.routing_key:
            if hasattr(self.routing_key, 'to_alipay_dict'):
                params['routing_key'] = self.routing_key.to_alipay_dict()
            else:
                params['routing_key'] = self.routing_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfimMqSyncModel()
        if 'msg_body' in d:
            o.msg_body = d['msg_body']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'routing_key' in d:
            o.routing_key = d['routing_key']
        return o


