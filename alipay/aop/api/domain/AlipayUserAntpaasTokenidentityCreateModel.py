#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntpaasTokenidentityCreateModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_scene = None
        self._ext_info = None
        self._ext_info_id = None
        self._mobile = None
        self._user_type = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def ext_info_id(self):
        return self._ext_info_id

    @ext_info_id.setter
    def ext_info_id(self, value):
        self._ext_info_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.ext_info_id:
            if hasattr(self.ext_info_id, 'to_alipay_dict'):
                params['ext_info_id'] = self.ext_info_id.to_alipay_dict()
            else:
                params['ext_info_id'] = self.ext_info_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntpaasTokenidentityCreateModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'ext_info_id' in d:
            o.ext_info_id = d['ext_info_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


