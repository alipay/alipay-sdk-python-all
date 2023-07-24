#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelAccountSyncaplusApplyModel(object):

    def __init__(self):
        self._aplus_owner_id = None
        self._cn_owner_id = None

    @property
    def aplus_owner_id(self):
        return self._aplus_owner_id

    @aplus_owner_id.setter
    def aplus_owner_id(self, value):
        self._aplus_owner_id = value
    @property
    def cn_owner_id(self):
        return self._cn_owner_id

    @cn_owner_id.setter
    def cn_owner_id(self, value):
        self._cn_owner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aplus_owner_id:
            if hasattr(self.aplus_owner_id, 'to_alipay_dict'):
                params['aplus_owner_id'] = self.aplus_owner_id.to_alipay_dict()
            else:
                params['aplus_owner_id'] = self.aplus_owner_id
        if self.cn_owner_id:
            if hasattr(self.cn_owner_id, 'to_alipay_dict'):
                params['cn_owner_id'] = self.cn_owner_id.to_alipay_dict()
            else:
                params['cn_owner_id'] = self.cn_owner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelAccountSyncaplusApplyModel()
        if 'aplus_owner_id' in d:
            o.aplus_owner_id = d['aplus_owner_id']
        if 'cn_owner_id' in d:
            o.cn_owner_id = d['cn_owner_id']
        return o


