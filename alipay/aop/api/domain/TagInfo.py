#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TagInfo(object):

    def __init__(self):
        self._pre_identity = None
        self._tag_key = None
        self._tag_value = None

    @property
    def pre_identity(self):
        return self._pre_identity

    @pre_identity.setter
    def pre_identity(self, value):
        self._pre_identity = value
    @property
    def tag_key(self):
        return self._tag_key

    @tag_key.setter
    def tag_key(self, value):
        self._tag_key = value
    @property
    def tag_value(self):
        return self._tag_value

    @tag_value.setter
    def tag_value(self, value):
        self._tag_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.pre_identity:
            if hasattr(self.pre_identity, 'to_alipay_dict'):
                params['pre_identity'] = self.pre_identity.to_alipay_dict()
            else:
                params['pre_identity'] = self.pre_identity
        if self.tag_key:
            if hasattr(self.tag_key, 'to_alipay_dict'):
                params['tag_key'] = self.tag_key.to_alipay_dict()
            else:
                params['tag_key'] = self.tag_key
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
        o = TagInfo()
        if 'pre_identity' in d:
            o.pre_identity = d['pre_identity']
        if 'tag_key' in d:
            o.tag_key = d['tag_key']
        if 'tag_value' in d:
            o.tag_value = d['tag_value']
        return o


