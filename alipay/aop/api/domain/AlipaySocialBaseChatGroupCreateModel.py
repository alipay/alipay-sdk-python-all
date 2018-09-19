#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseChatGroupCreateModel(object):

    def __init__(self):
        self._client_id = None
        self._group_name = None

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
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
        o = AlipaySocialBaseChatGroupCreateModel()
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        return o


