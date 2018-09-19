#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsObject(object):

    def __init__(self):
        self._insured_object_id = None
        self._insured_object_info = None
        self._type = None

    @property
    def insured_object_id(self):
        return self._insured_object_id

    @insured_object_id.setter
    def insured_object_id(self, value):
        self._insured_object_id = value
    @property
    def insured_object_info(self):
        return self._insured_object_info

    @insured_object_info.setter
    def insured_object_info(self, value):
        self._insured_object_info = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.insured_object_id:
            if hasattr(self.insured_object_id, 'to_alipay_dict'):
                params['insured_object_id'] = self.insured_object_id.to_alipay_dict()
            else:
                params['insured_object_id'] = self.insured_object_id
        if self.insured_object_info:
            if hasattr(self.insured_object_info, 'to_alipay_dict'):
                params['insured_object_info'] = self.insured_object_info.to_alipay_dict()
            else:
                params['insured_object_info'] = self.insured_object_info
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsObject()
        if 'insured_object_id' in d:
            o.insured_object_id = d['insured_object_id']
        if 'insured_object_info' in d:
            o.insured_object_info = d['insured_object_info']
        if 'type' in d:
            o.type = d['type']
        return o


