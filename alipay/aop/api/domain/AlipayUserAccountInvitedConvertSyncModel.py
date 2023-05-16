#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountInvitedConvertSyncModel(object):

    def __init__(self):
        self._biz_ext_info = None
        self._convert_tag = None
        self._open_id = None
        self._out_biz_no = None
        self._scene_type = None
        self._user_id = None
        self._user_token = None

    @property
    def biz_ext_info(self):
        return self._biz_ext_info

    @biz_ext_info.setter
    def biz_ext_info(self, value):
        self._biz_ext_info = value
    @property
    def convert_tag(self):
        return self._convert_tag

    @convert_tag.setter
    def convert_tag(self, value):
        self._convert_tag = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_ext_info:
            if hasattr(self.biz_ext_info, 'to_alipay_dict'):
                params['biz_ext_info'] = self.biz_ext_info.to_alipay_dict()
            else:
                params['biz_ext_info'] = self.biz_ext_info
        if self.convert_tag:
            if hasattr(self.convert_tag, 'to_alipay_dict'):
                params['convert_tag'] = self.convert_tag.to_alipay_dict()
            else:
                params['convert_tag'] = self.convert_tag
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_token:
            if hasattr(self.user_token, 'to_alipay_dict'):
                params['user_token'] = self.user_token.to_alipay_dict()
            else:
                params['user_token'] = self.user_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountInvitedConvertSyncModel()
        if 'biz_ext_info' in d:
            o.biz_ext_info = d['biz_ext_info']
        if 'convert_tag' in d:
            o.convert_tag = d['convert_tag']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_token' in d:
            o.user_token = d['user_token']
        return o


