#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportIntelligentizeServicetaskQueryModel(object):

    def __init__(self):
        self._corp_id = None
        self._ext_param = None
        self._request_id = None
        self._service_task_id = None

    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def service_task_id(self):
        return self._service_task_id

    @service_task_id.setter
    def service_task_id(self, value):
        self._service_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.service_task_id:
            if hasattr(self.service_task_id, 'to_alipay_dict'):
                params['service_task_id'] = self.service_task_id.to_alipay_dict()
            else:
                params['service_task_id'] = self.service_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIntelligentizeServicetaskQueryModel()
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_task_id' in d:
            o.service_task_id = d['service_task_id']
        return o


