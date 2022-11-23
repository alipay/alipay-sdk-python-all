#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaaSInvoker import SaaSInvoker
from alipay.aop.api.domain.InfoSecAnalyzeSyncContent import InfoSecAnalyzeSyncContent


class AlipaySecurityRiskContentAnalyzeSyncModel(object):

    def __init__(self):
        self._channel = None
        self._ext_info = None
        self._invoker = None
        self._req_msg_id = None
        self._request = None
        self._service_name = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def invoker(self):
        return self._invoker

    @invoker.setter
    def invoker(self, value):
        if isinstance(value, SaaSInvoker):
            self._invoker = value
        else:
            self._invoker = SaaSInvoker.from_alipay_dict(value)
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value
    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        if isinstance(value, InfoSecAnalyzeSyncContent):
            self._request = value
        else:
            self._request = InfoSecAnalyzeSyncContent.from_alipay_dict(value)
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.invoker:
            if hasattr(self.invoker, 'to_alipay_dict'):
                params['invoker'] = self.invoker.to_alipay_dict()
            else:
                params['invoker'] = self.invoker
        if self.req_msg_id:
            if hasattr(self.req_msg_id, 'to_alipay_dict'):
                params['req_msg_id'] = self.req_msg_id.to_alipay_dict()
            else:
                params['req_msg_id'] = self.req_msg_id
        if self.request:
            if hasattr(self.request, 'to_alipay_dict'):
                params['request'] = self.request.to_alipay_dict()
            else:
                params['request'] = self.request
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskContentAnalyzeSyncModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'invoker' in d:
            o.invoker = d['invoker']
        if 'req_msg_id' in d:
            o.req_msg_id = d['req_msg_id']
        if 'request' in d:
            o.request = d['request']
        if 'service_name' in d:
            o.service_name = d['service_name']
        return o


