#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySupervisionAccountQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._merchant_alipay_open_id = None
        self._merchant_alipay_uid = None
        self._parent_ext_account_no = None
        self._sub_account_type = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def merchant_alipay_open_id(self):
        return self._merchant_alipay_open_id

    @merchant_alipay_open_id.setter
    def merchant_alipay_open_id(self, value):
        self._merchant_alipay_open_id = value
    @property
    def merchant_alipay_uid(self):
        return self._merchant_alipay_uid

    @merchant_alipay_uid.setter
    def merchant_alipay_uid(self, value):
        self._merchant_alipay_uid = value
    @property
    def parent_ext_account_no(self):
        return self._parent_ext_account_no

    @parent_ext_account_no.setter
    def parent_ext_account_no(self, value):
        self._parent_ext_account_no = value
    @property
    def sub_account_type(self):
        return self._sub_account_type

    @sub_account_type.setter
    def sub_account_type(self, value):
        self._sub_account_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.merchant_alipay_open_id:
            if hasattr(self.merchant_alipay_open_id, 'to_alipay_dict'):
                params['merchant_alipay_open_id'] = self.merchant_alipay_open_id.to_alipay_dict()
            else:
                params['merchant_alipay_open_id'] = self.merchant_alipay_open_id
        if self.merchant_alipay_uid:
            if hasattr(self.merchant_alipay_uid, 'to_alipay_dict'):
                params['merchant_alipay_uid'] = self.merchant_alipay_uid.to_alipay_dict()
            else:
                params['merchant_alipay_uid'] = self.merchant_alipay_uid
        if self.parent_ext_account_no:
            if hasattr(self.parent_ext_account_no, 'to_alipay_dict'):
                params['parent_ext_account_no'] = self.parent_ext_account_no.to_alipay_dict()
            else:
                params['parent_ext_account_no'] = self.parent_ext_account_no
        if self.sub_account_type:
            if hasattr(self.sub_account_type, 'to_alipay_dict'):
                params['sub_account_type'] = self.sub_account_type.to_alipay_dict()
            else:
                params['sub_account_type'] = self.sub_account_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySupervisionAccountQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'merchant_alipay_open_id' in d:
            o.merchant_alipay_open_id = d['merchant_alipay_open_id']
        if 'merchant_alipay_uid' in d:
            o.merchant_alipay_uid = d['merchant_alipay_uid']
        if 'parent_ext_account_no' in d:
            o.parent_ext_account_no = d['parent_ext_account_no']
        if 'sub_account_type' in d:
            o.sub_account_type = d['sub_account_type']
        return o


