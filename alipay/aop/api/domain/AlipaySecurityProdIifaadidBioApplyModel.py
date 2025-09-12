#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdIifaadidBioApplyModel(object):

    def __init__(self):
        self._biz_id = None
        self._did = None
        self._env_data = None
        self._ifaa_msg = None
        self._scene_code = None
        self._stock_name = None
        self._user_trans_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def did(self):
        return self._did

    @did.setter
    def did(self, value):
        self._did = value
    @property
    def env_data(self):
        return self._env_data

    @env_data.setter
    def env_data(self, value):
        self._env_data = value
    @property
    def ifaa_msg(self):
        return self._ifaa_msg

    @ifaa_msg.setter
    def ifaa_msg(self, value):
        self._ifaa_msg = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def stock_name(self):
        return self._stock_name

    @stock_name.setter
    def stock_name(self, value):
        self._stock_name = value
    @property
    def user_trans_id(self):
        return self._user_trans_id

    @user_trans_id.setter
    def user_trans_id(self, value):
        self._user_trans_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.did:
            if hasattr(self.did, 'to_alipay_dict'):
                params['did'] = self.did.to_alipay_dict()
            else:
                params['did'] = self.did
        if self.env_data:
            if hasattr(self.env_data, 'to_alipay_dict'):
                params['env_data'] = self.env_data.to_alipay_dict()
            else:
                params['env_data'] = self.env_data
        if self.ifaa_msg:
            if hasattr(self.ifaa_msg, 'to_alipay_dict'):
                params['ifaa_msg'] = self.ifaa_msg.to_alipay_dict()
            else:
                params['ifaa_msg'] = self.ifaa_msg
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.stock_name:
            if hasattr(self.stock_name, 'to_alipay_dict'):
                params['stock_name'] = self.stock_name.to_alipay_dict()
            else:
                params['stock_name'] = self.stock_name
        if self.user_trans_id:
            if hasattr(self.user_trans_id, 'to_alipay_dict'):
                params['user_trans_id'] = self.user_trans_id.to_alipay_dict()
            else:
                params['user_trans_id'] = self.user_trans_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdIifaadidBioApplyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'did' in d:
            o.did = d['did']
        if 'env_data' in d:
            o.env_data = d['env_data']
        if 'ifaa_msg' in d:
            o.ifaa_msg = d['ifaa_msg']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'stock_name' in d:
            o.stock_name = d['stock_name']
        if 'user_trans_id' in d:
            o.user_trans_id = d['user_trans_id']
        return o


