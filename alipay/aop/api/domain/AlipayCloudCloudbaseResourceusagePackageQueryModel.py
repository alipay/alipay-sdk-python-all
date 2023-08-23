#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourceusagePackageQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._fee_item_code = None

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
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseResourceusagePackageQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        return o


