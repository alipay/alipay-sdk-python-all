#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNsalesSubactivitySyncModel(object):

    def __init__(self):
        self._status = None
        self._sub_activity_id = None
        self._sync_memo = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_activity_id(self):
        return self._sub_activity_id

    @sub_activity_id.setter
    def sub_activity_id(self, value):
        self._sub_activity_id = value
    @property
    def sync_memo(self):
        return self._sync_memo

    @sync_memo.setter
    def sync_memo(self, value):
        self._sync_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_activity_id:
            if hasattr(self.sub_activity_id, 'to_alipay_dict'):
                params['sub_activity_id'] = self.sub_activity_id.to_alipay_dict()
            else:
                params['sub_activity_id'] = self.sub_activity_id
        if self.sync_memo:
            if hasattr(self.sync_memo, 'to_alipay_dict'):
                params['sync_memo'] = self.sync_memo.to_alipay_dict()
            else:
                params['sync_memo'] = self.sync_memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNsalesSubactivitySyncModel()
        if 'status' in d:
            o.status = d['status']
        if 'sub_activity_id' in d:
            o.sub_activity_id = d['sub_activity_id']
        if 'sync_memo' in d:
            o.sync_memo = d['sync_memo']
        return o


