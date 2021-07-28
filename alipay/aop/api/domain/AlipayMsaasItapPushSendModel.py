#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DevicePushPayload import DevicePushPayload


class AlipayMsaasItapPushSendModel(object):

    def __init__(self):
        self._payload = None
        self._request_id = None
        self._user_id = None

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        if isinstance(value, list):
            self._payload = list()
            for i in value:
                if isinstance(i, DevicePushPayload):
                    self._payload.append(i)
                else:
                    self._payload.append(DevicePushPayload.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.payload:
            if isinstance(self.payload, list):
                for i in range(0, len(self.payload)):
                    element = self.payload[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payload[i] = element.to_alipay_dict()
            if hasattr(self.payload, 'to_alipay_dict'):
                params['payload'] = self.payload.to_alipay_dict()
            else:
                params['payload'] = self.payload
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasItapPushSendModel()
        if 'payload' in d:
            o.payload = d['payload']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


