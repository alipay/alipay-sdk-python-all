#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseBsnAssignModel(object):

    def __init__(self):
        self._aliuid = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._bsn = None

    @property
    def aliuid(self):
        return self._aliuid

    @aliuid.setter
    def aliuid(self, value):
        self._aliuid = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def bsn(self):
        return self._bsn

    @bsn.setter
    def bsn(self, value):
        self._bsn = value


    def to_alipay_dict(self):
        params = dict()
        if self.aliuid:
            if hasattr(self.aliuid, 'to_alipay_dict'):
                params['aliuid'] = self.aliuid.to_alipay_dict()
            else:
                params['aliuid'] = self.aliuid
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.bsn:
            if hasattr(self.bsn, 'to_alipay_dict'):
                params['bsn'] = self.bsn.to_alipay_dict()
            else:
                params['bsn'] = self.bsn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseBsnAssignModel()
        if 'aliuid' in d:
            o.aliuid = d['aliuid']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'bsn' in d:
            o.bsn = d['bsn']
        return o


