#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenMarketingActionDTO(object):

    def __init__(self):
        self._action_id = None
        self._action_name = None
        self._action_type = None

    @property
    def action_id(self):
        return self._action_id

    @action_id.setter
    def action_id(self, value):
        self._action_id = value
    @property
    def action_name(self):
        return self._action_name

    @action_name.setter
    def action_name(self, value):
        self._action_name = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_id:
            if hasattr(self.action_id, 'to_alipay_dict'):
                params['action_id'] = self.action_id.to_alipay_dict()
            else:
                params['action_id'] = self.action_id
        if self.action_name:
            if hasattr(self.action_name, 'to_alipay_dict'):
                params['action_name'] = self.action_name.to_alipay_dict()
            else:
                params['action_name'] = self.action_name
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenMarketingActionDTO()
        if 'action_id' in d:
            o.action_id = d['action_id']
        if 'action_name' in d:
            o.action_name = d['action_name']
        if 'action_type' in d:
            o.action_type = d['action_type']
        return o


