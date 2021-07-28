#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozAuthenticationSmilefaceSendmeSendModel(object):

    def __init__(self):
        self._biz_type = None
        self._camp_id = None
        self._ext_info = None
        self._ftoken = None
        self._mini_app_id = None
        self._path = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationSmilefaceSendmeSendModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'path' in d:
            o.path = d['path']
        return o


