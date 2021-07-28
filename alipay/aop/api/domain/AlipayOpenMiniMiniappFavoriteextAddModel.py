#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniMiniappFavoriteextAddModel(object):

    def __init__(self):
        self._biz_type = None
        self._extend_info = None
        self._mini_app_id = None
        self._principal_biz_type = None
        self._principal_ids = None
        self._principal_type = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def principal_biz_type(self):
        return self._principal_biz_type

    @principal_biz_type.setter
    def principal_biz_type(self, value):
        self._principal_biz_type = value
    @property
    def principal_ids(self):
        return self._principal_ids

    @principal_ids.setter
    def principal_ids(self, value):
        if isinstance(value, list):
            self._principal_ids = list()
            for i in value:
                self._principal_ids.append(i)
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.principal_biz_type:
            if hasattr(self.principal_biz_type, 'to_alipay_dict'):
                params['principal_biz_type'] = self.principal_biz_type.to_alipay_dict()
            else:
                params['principal_biz_type'] = self.principal_biz_type
        if self.principal_ids:
            if isinstance(self.principal_ids, list):
                for i in range(0, len(self.principal_ids)):
                    element = self.principal_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.principal_ids[i] = element.to_alipay_dict()
            if hasattr(self.principal_ids, 'to_alipay_dict'):
                params['principal_ids'] = self.principal_ids.to_alipay_dict()
            else:
                params['principal_ids'] = self.principal_ids
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
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
        o = AlipayOpenMiniMiniappFavoriteextAddModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'principal_biz_type' in d:
            o.principal_biz_type = d['principal_biz_type']
        if 'principal_ids' in d:
            o.principal_ids = d['principal_ids']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


