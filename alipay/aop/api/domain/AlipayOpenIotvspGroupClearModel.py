#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotvspGroupClearModel(object):

    def __init__(self):
        self._biz_id = None
        self._isv_pid = None
        self._org_out_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def org_out_id(self):
        return self._org_out_id

    @org_out_id.setter
    def org_out_id(self, value):
        self._org_out_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.org_out_id:
            if hasattr(self.org_out_id, 'to_alipay_dict'):
                params['org_out_id'] = self.org_out_id.to_alipay_dict()
            else:
                params['org_out_id'] = self.org_out_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotvspGroupClearModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'org_out_id' in d:
            o.org_out_id = d['org_out_id']
        return o


