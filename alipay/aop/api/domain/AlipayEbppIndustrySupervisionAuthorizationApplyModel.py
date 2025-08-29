#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySupervisionAuthorizationApplyModel(object):

    def __init__(self):
        self._apply_request_no = None
        self._authorization_list = None
        self._biz_scene = None
        self._merchant_alipay_open_id = None
        self._merchant_alipay_uid = None
        self._parent_ext_account_no = None

    @property
    def apply_request_no(self):
        return self._apply_request_no

    @apply_request_no.setter
    def apply_request_no(self, value):
        self._apply_request_no = value
    @property
    def authorization_list(self):
        return self._authorization_list

    @authorization_list.setter
    def authorization_list(self, value):
        if isinstance(value, list):
            self._authorization_list = list()
            for i in value:
                self._authorization_list.append(i)
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


    def to_alipay_dict(self):
        params = dict()
        if self.apply_request_no:
            if hasattr(self.apply_request_no, 'to_alipay_dict'):
                params['apply_request_no'] = self.apply_request_no.to_alipay_dict()
            else:
                params['apply_request_no'] = self.apply_request_no
        if self.authorization_list:
            if isinstance(self.authorization_list, list):
                for i in range(0, len(self.authorization_list)):
                    element = self.authorization_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authorization_list[i] = element.to_alipay_dict()
            if hasattr(self.authorization_list, 'to_alipay_dict'):
                params['authorization_list'] = self.authorization_list.to_alipay_dict()
            else:
                params['authorization_list'] = self.authorization_list
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySupervisionAuthorizationApplyModel()
        if 'apply_request_no' in d:
            o.apply_request_no = d['apply_request_no']
        if 'authorization_list' in d:
            o.authorization_list = d['authorization_list']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'merchant_alipay_open_id' in d:
            o.merchant_alipay_open_id = d['merchant_alipay_open_id']
        if 'merchant_alipay_uid' in d:
            o.merchant_alipay_uid = d['merchant_alipay_uid']
        if 'parent_ext_account_no' in d:
            o.parent_ext_account_no = d['parent_ext_account_no']
        return o


