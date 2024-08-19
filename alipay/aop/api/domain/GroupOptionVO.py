#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupOptionVO(object):

    def __init__(self):
        self._forbidden = None
        self._group_id = None
        self._group_name = None

    @property
    def forbidden(self):
        return self._forbidden

    @forbidden.setter
    def forbidden(self, value):
        self._forbidden = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.forbidden:
            if hasattr(self.forbidden, 'to_alipay_dict'):
                params['forbidden'] = self.forbidden.to_alipay_dict()
            else:
                params['forbidden'] = self.forbidden
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupOptionVO()
        if 'forbidden' in d:
            o.forbidden = d['forbidden']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        return o


