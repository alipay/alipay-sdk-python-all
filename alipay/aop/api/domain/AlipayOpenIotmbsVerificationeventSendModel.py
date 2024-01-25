#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsVerificationeventSendModel(object):

    def __init__(self):
        self._event = None
        self._event_params = None
        self._flow_id = None
        self._ftoken = None
        self._request_id = None
        self._sn = None

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def event_params(self):
        return self._event_params

    @event_params.setter
    def event_params(self, value):
        self._event_params = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        if self.event_params:
            if hasattr(self.event_params, 'to_alipay_dict'):
                params['event_params'] = self.event_params.to_alipay_dict()
            else:
                params['event_params'] = self.event_params
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsVerificationeventSendModel()
        if 'event' in d:
            o.event = d['event']
        if 'event_params' in d:
            o.event_params = d['event_params']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sn' in d:
            o.sn = d['sn']
        return o


