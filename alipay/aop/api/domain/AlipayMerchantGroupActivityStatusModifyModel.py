#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupActivityStatusModifyModel(object):

    def __init__(self):
        self._group_activity_id = None
        self._status = None

    @property
    def group_activity_id(self):
        return self._group_activity_id

    @group_activity_id.setter
    def group_activity_id(self, value):
        self._group_activity_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_activity_id:
            if hasattr(self.group_activity_id, 'to_alipay_dict'):
                params['group_activity_id'] = self.group_activity_id.to_alipay_dict()
            else:
                params['group_activity_id'] = self.group_activity_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupActivityStatusModifyModel()
        if 'group_activity_id' in d:
            o.group_activity_id = d['group_activity_id']
        if 'status' in d:
            o.status = d['status']
        return o


