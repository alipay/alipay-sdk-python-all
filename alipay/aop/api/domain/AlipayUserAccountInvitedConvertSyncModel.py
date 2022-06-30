#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountInvitedConvertSyncModel(object):

    def __init__(self):
        self._convert_tag = None
        self._out_biz_no = None
        self._scene_type = None
        self._user_id = None
        self._user_token = None

    @property
    def convert_tag(self):
        return self._convert_tag

    @convert_tag.setter
    def convert_tag(self, value):
        self._convert_tag = value
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
        if self.convert_tag:
            if hasattr(self.convert_tag, 'to_alipay_dict'):
                params['convert_tag'] = self.convert_tag.to_alipay_dict()
            else:
                params['convert_tag'] = self.convert_tag
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
        if 'convert_tag' in d:
            o.convert_tag = d['convert_tag']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_token' in d:
            o.user_token = d['user_token']
        return o


