#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberDTO(object):

    def __init__(self):
        self._id = None
        self._unique_name = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def unique_name(self):
        return self._unique_name

    @unique_name.setter
    def unique_name(self, value):
        self._unique_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.unique_name:
            if hasattr(self.unique_name, 'to_alipay_dict'):
                params['unique_name'] = self.unique_name.to_alipay_dict()
            else:
                params['unique_name'] = self.unique_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberDTO()
        if 'id' in d:
            o.id = d['id']
        if 'unique_name' in d:
            o.unique_name = d['unique_name']
        return o


