#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignApproveOpenApiDTO(object):

    def __init__(self):
        self._process_ids = None
        self._process_type = None

    @property
    def process_ids(self):
        return self._process_ids

    @process_ids.setter
    def process_ids(self, value):
        if isinstance(value, list):
            self._process_ids = list()
            for i in value:
                self._process_ids.append(i)
    @property
    def process_type(self):
        return self._process_type

    @process_type.setter
    def process_type(self, value):
        self._process_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.process_ids:
            if isinstance(self.process_ids, list):
                for i in range(0, len(self.process_ids)):
                    element = self.process_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.process_ids[i] = element.to_alipay_dict()
            if hasattr(self.process_ids, 'to_alipay_dict'):
                params['process_ids'] = self.process_ids.to_alipay_dict()
            else:
                params['process_ids'] = self.process_ids
        if self.process_type:
            if hasattr(self.process_type, 'to_alipay_dict'):
                params['process_type'] = self.process_type.to_alipay_dict()
            else:
                params['process_type'] = self.process_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignApproveOpenApiDTO()
        if 'process_ids' in d:
            o.process_ids = d['process_ids']
        if 'process_type' in d:
            o.process_type = d['process_type']
        return o


