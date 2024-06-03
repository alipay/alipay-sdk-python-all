#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupBuyInfo(object):

    def __init__(self):
        self._group_id = None
        self._group_status = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_status(self):
        return self._group_status

    @group_status.setter
    def group_status(self, value):
        self._group_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_status:
            if hasattr(self.group_status, 'to_alipay_dict'):
                params['group_status'] = self.group_status.to_alipay_dict()
            else:
                params['group_status'] = self.group_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupBuyInfo()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_status' in d:
            o.group_status = d['group_status']
        return o


