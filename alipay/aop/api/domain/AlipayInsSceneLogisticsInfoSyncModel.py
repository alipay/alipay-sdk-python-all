#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsSyncDataDTO import LogisticsSyncDataDTO


class AlipayInsSceneLogisticsInfoSyncModel(object):

    def __init__(self):
        self._biz_no = None
        self._isv_identity = None
        self._mail_no = None
        self._sync_data = None
        self._sync_type = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def isv_identity(self):
        return self._isv_identity

    @isv_identity.setter
    def isv_identity(self, value):
        self._isv_identity = value
    @property
    def mail_no(self):
        return self._mail_no

    @mail_no.setter
    def mail_no(self, value):
        self._mail_no = value
    @property
    def sync_data(self):
        return self._sync_data

    @sync_data.setter
    def sync_data(self, value):
        if isinstance(value, LogisticsSyncDataDTO):
            self._sync_data = value
        else:
            self._sync_data = LogisticsSyncDataDTO.from_alipay_dict(value)
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.isv_identity:
            if hasattr(self.isv_identity, 'to_alipay_dict'):
                params['isv_identity'] = self.isv_identity.to_alipay_dict()
            else:
                params['isv_identity'] = self.isv_identity
        if self.mail_no:
            if hasattr(self.mail_no, 'to_alipay_dict'):
                params['mail_no'] = self.mail_no.to_alipay_dict()
            else:
                params['mail_no'] = self.mail_no
        if self.sync_data:
            if hasattr(self.sync_data, 'to_alipay_dict'):
                params['sync_data'] = self.sync_data.to_alipay_dict()
            else:
                params['sync_data'] = self.sync_data
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneLogisticsInfoSyncModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'isv_identity' in d:
            o.isv_identity = d['isv_identity']
        if 'mail_no' in d:
            o.mail_no = d['mail_no']
        if 'sync_data' in d:
            o.sync_data = d['sync_data']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


