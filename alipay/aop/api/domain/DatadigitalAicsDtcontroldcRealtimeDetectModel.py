#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDtcontroldcRealtimeDetectModel(object):

    def __init__(self):
        self._agent_id = None
        self._context = None
        self._service_source = None
        self._tenant = None
        self._text = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
    @property
    def service_source(self):
        return self._service_source

    @service_source.setter
    def service_source(self, value):
        self._service_source = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.service_source:
            if hasattr(self.service_source, 'to_alipay_dict'):
                params['service_source'] = self.service_source.to_alipay_dict()
            else:
                params['service_source'] = self.service_source
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDtcontroldcRealtimeDetectModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'context' in d:
            o.context = d['context']
        if 'service_source' in d:
            o.service_source = d['service_source']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'text' in d:
            o.text = d['text']
        return o


