#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PushChannelDTO(object):

    def __init__(self):
        self._business_id = None
        self._push_type = None
        self._template_params = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def push_type(self):
        return self._push_type

    @push_type.setter
    def push_type(self, value):
        self._push_type = value
    @property
    def template_params(self):
        return self._template_params

    @template_params.setter
    def template_params(self, value):
        self._template_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.push_type:
            if hasattr(self.push_type, 'to_alipay_dict'):
                params['push_type'] = self.push_type.to_alipay_dict()
            else:
                params['push_type'] = self.push_type
        if self.template_params:
            if hasattr(self.template_params, 'to_alipay_dict'):
                params['template_params'] = self.template_params.to_alipay_dict()
            else:
                params['template_params'] = self.template_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PushChannelDTO()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'push_type' in d:
            o.push_type = d['push_type']
        if 'template_params' in d:
            o.template_params = d['template_params']
        return o


