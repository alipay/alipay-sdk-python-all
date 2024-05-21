#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalShopTag(object):

    def __init__(self):
        self._tag_type = None
        self._tag_value = None

    @property
    def tag_type(self):
        return self._tag_type

    @tag_type.setter
    def tag_type(self, value):
        self._tag_type = value
    @property
    def tag_value(self):
        return self._tag_value

    @tag_value.setter
    def tag_value(self, value):
        self._tag_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_type:
            if hasattr(self.tag_type, 'to_alipay_dict'):
                params['tag_type'] = self.tag_type.to_alipay_dict()
            else:
                params['tag_type'] = self.tag_type
        if self.tag_value:
            if hasattr(self.tag_value, 'to_alipay_dict'):
                params['tag_value'] = self.tag_value.to_alipay_dict()
            else:
                params['tag_value'] = self.tag_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalShopTag()
        if 'tag_type' in d:
            o.tag_type = d['tag_type']
        if 'tag_value' in d:
            o.tag_value = d['tag_value']
        return o


