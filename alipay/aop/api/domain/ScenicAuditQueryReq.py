#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenicAuditQueryReq(object):

    def __init__(self):
        self._scenic_app_id = None
        self._scenic_id = None

    @property
    def scenic_app_id(self):
        return self._scenic_app_id

    @scenic_app_id.setter
    def scenic_app_id(self, value):
        self._scenic_app_id = value
    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.scenic_app_id:
            if hasattr(self.scenic_app_id, 'to_alipay_dict'):
                params['scenic_app_id'] = self.scenic_app_id.to_alipay_dict()
            else:
                params['scenic_app_id'] = self.scenic_app_id
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenicAuditQueryReq()
        if 'scenic_app_id' in d:
            o.scenic_app_id = d['scenic_app_id']
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        return o


