#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseRelationFriendsQueryModel(object):

    def __init__(self):
        self._get_type = None
        self._include_self = None

    @property
    def get_type(self):
        return self._get_type

    @get_type.setter
    def get_type(self, value):
        self._get_type = value
    @property
    def include_self(self):
        return self._include_self

    @include_self.setter
    def include_self(self, value):
        self._include_self = value


    def to_alipay_dict(self):
        params = dict()
        if self.get_type:
            if hasattr(self.get_type, 'to_alipay_dict'):
                params['get_type'] = self.get_type.to_alipay_dict()
            else:
                params['get_type'] = self.get_type
        if self.include_self:
            if hasattr(self.include_self, 'to_alipay_dict'):
                params['include_self'] = self.include_self.to_alipay_dict()
            else:
                params['include_self'] = self.include_self
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseRelationFriendsQueryModel()
        if 'get_type' in d:
            o.get_type = d['get_type']
        if 'include_self' in d:
            o.include_self = d['include_self']
        return o


