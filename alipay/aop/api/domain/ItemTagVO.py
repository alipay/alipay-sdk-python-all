#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemTagVO(object):

    def __init__(self):
        self._tag_id = None
        self._tag_value = None

    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def tag_value(self):
        return self._tag_value

    @tag_value.setter
    def tag_value(self, value):
        self._tag_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
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
        o = ItemTagVO()
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'tag_value' in d:
            o.tag_value = d['tag_value']
        return o


