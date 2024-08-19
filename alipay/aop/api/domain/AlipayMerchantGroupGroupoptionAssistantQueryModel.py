#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupGroupoptionAssistantQueryModel(object):

    def __init__(self):
        self._excluded_content_id = None
        self._type = None

    @property
    def excluded_content_id(self):
        return self._excluded_content_id

    @excluded_content_id.setter
    def excluded_content_id(self, value):
        self._excluded_content_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.excluded_content_id:
            if hasattr(self.excluded_content_id, 'to_alipay_dict'):
                params['excluded_content_id'] = self.excluded_content_id.to_alipay_dict()
            else:
                params['excluded_content_id'] = self.excluded_content_id
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
        o = AlipayMerchantGroupGroupoptionAssistantQueryModel()
        if 'excluded_content_id' in d:
            o.excluded_content_id = d['excluded_content_id']
        if 'type' in d:
            o.type = d['type']
        return o


