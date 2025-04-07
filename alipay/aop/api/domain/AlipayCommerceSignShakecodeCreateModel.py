#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSignShakecodeCreateModel(object):

    def __init__(self):
        self._biz_linked_id = None
        self._type = None

    @property
    def biz_linked_id(self):
        return self._biz_linked_id

    @biz_linked_id.setter
    def biz_linked_id(self, value):
        self._biz_linked_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_linked_id:
            if hasattr(self.biz_linked_id, 'to_alipay_dict'):
                params['biz_linked_id'] = self.biz_linked_id.to_alipay_dict()
            else:
                params['biz_linked_id'] = self.biz_linked_id
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
        o = AlipayCommerceSignShakecodeCreateModel()
        if 'biz_linked_id' in d:
            o.biz_linked_id = d['biz_linked_id']
        if 'type' in d:
            o.type = d['type']
        return o


