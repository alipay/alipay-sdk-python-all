#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchAgentframeworkWarrenqQueryModel(object):

    def __init__(self):
        self._input = None
        self._service_id = None
        self._tags = None

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        self._input = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value


    def to_alipay_dict(self):
        params = dict()
        if self.input:
            if hasattr(self.input, 'to_alipay_dict'):
                params['input'] = self.input.to_alipay_dict()
            else:
                params['input'] = self.input
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchAgentframeworkWarrenqQueryModel()
        if 'input' in d:
            o.input = d['input']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'tags' in d:
            o.tags = d['tags']
        return o


