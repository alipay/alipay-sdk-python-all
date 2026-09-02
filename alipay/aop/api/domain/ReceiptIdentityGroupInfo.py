#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiptIdentityGroupInfo(object):

    def __init__(self):
        self._identity_group_id = None
        self._identity_group_name = None

    @property
    def identity_group_id(self):
        return self._identity_group_id

    @identity_group_id.setter
    def identity_group_id(self, value):
        self._identity_group_id = value
    @property
    def identity_group_name(self):
        return self._identity_group_name

    @identity_group_name.setter
    def identity_group_name(self, value):
        self._identity_group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_group_id:
            if hasattr(self.identity_group_id, 'to_alipay_dict'):
                params['identity_group_id'] = self.identity_group_id.to_alipay_dict()
            else:
                params['identity_group_id'] = self.identity_group_id
        if self.identity_group_name:
            if hasattr(self.identity_group_name, 'to_alipay_dict'):
                params['identity_group_name'] = self.identity_group_name.to_alipay_dict()
            else:
                params['identity_group_name'] = self.identity_group_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiptIdentityGroupInfo()
        if 'identity_group_id' in d:
            o.identity_group_id = d['identity_group_id']
        if 'identity_group_name' in d:
            o.identity_group_name = d['identity_group_name']
        return o


