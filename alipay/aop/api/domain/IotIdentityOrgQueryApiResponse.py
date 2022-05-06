#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotIdentityOrgQueryApiResponse(object):

    def __init__(self):
        self._group_id = None
        self._logic_group_id = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def logic_group_id(self):
        return self._logic_group_id

    @logic_group_id.setter
    def logic_group_id(self, value):
        self._logic_group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.logic_group_id:
            if hasattr(self.logic_group_id, 'to_alipay_dict'):
                params['logic_group_id'] = self.logic_group_id.to_alipay_dict()
            else:
                params['logic_group_id'] = self.logic_group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotIdentityOrgQueryApiResponse()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'logic_group_id' in d:
            o.logic_group_id = d['logic_group_id']
        return o


