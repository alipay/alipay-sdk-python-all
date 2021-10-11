#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthBalanceQueryModel(object):

    def __init__(self):
        self._biz_ext_id = None
        self._biz_ext_info = None
        self._biz_ext_type = None
        self._biz_type = None
        self._inst_id = None
        self._product_id = None
        self._scene_id = None
        self._submit_no = None
        self._user_id = None

    @property
    def biz_ext_id(self):
        return self._biz_ext_id

    @biz_ext_id.setter
    def biz_ext_id(self, value):
        self._biz_ext_id = value
    @property
    def biz_ext_info(self):
        return self._biz_ext_info

    @biz_ext_info.setter
    def biz_ext_info(self, value):
        self._biz_ext_info = value
    @property
    def biz_ext_type(self):
        return self._biz_ext_type

    @biz_ext_type.setter
    def biz_ext_type(self, value):
        self._biz_ext_type = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def submit_no(self):
        return self._submit_no

    @submit_no.setter
    def submit_no(self, value):
        self._submit_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_ext_id:
            if hasattr(self.biz_ext_id, 'to_alipay_dict'):
                params['biz_ext_id'] = self.biz_ext_id.to_alipay_dict()
            else:
                params['biz_ext_id'] = self.biz_ext_id
        if self.biz_ext_info:
            if hasattr(self.biz_ext_info, 'to_alipay_dict'):
                params['biz_ext_info'] = self.biz_ext_info.to_alipay_dict()
            else:
                params['biz_ext_info'] = self.biz_ext_info
        if self.biz_ext_type:
            if hasattr(self.biz_ext_type, 'to_alipay_dict'):
                params['biz_ext_type'] = self.biz_ext_type.to_alipay_dict()
            else:
                params['biz_ext_type'] = self.biz_ext_type
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.submit_no:
            if hasattr(self.submit_no, 'to_alipay_dict'):
                params['submit_no'] = self.submit_no.to_alipay_dict()
            else:
                params['submit_no'] = self.submit_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthBalanceQueryModel()
        if 'biz_ext_id' in d:
            o.biz_ext_id = d['biz_ext_id']
        if 'biz_ext_info' in d:
            o.biz_ext_info = d['biz_ext_info']
        if 'biz_ext_type' in d:
            o.biz_ext_type = d['biz_ext_type']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'submit_no' in d:
            o.submit_no = d['submit_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


