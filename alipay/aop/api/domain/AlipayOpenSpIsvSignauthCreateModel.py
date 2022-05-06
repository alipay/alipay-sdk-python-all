#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IsvAuthSceneInfo import IsvAuthSceneInfo


class AlipayOpenSpIsvSignauthCreateModel(object):

    def __init__(self):
        self._isv_auth_scene_infos = None
        self._merchant_logon_id = None
        self._need_app_auth = None
        self._sign_order_no = None

    @property
    def isv_auth_scene_infos(self):
        return self._isv_auth_scene_infos

    @isv_auth_scene_infos.setter
    def isv_auth_scene_infos(self, value):
        if isinstance(value, list):
            self._isv_auth_scene_infos = list()
            for i in value:
                if isinstance(i, IsvAuthSceneInfo):
                    self._isv_auth_scene_infos.append(i)
                else:
                    self._isv_auth_scene_infos.append(IsvAuthSceneInfo.from_alipay_dict(i))
    @property
    def merchant_logon_id(self):
        return self._merchant_logon_id

    @merchant_logon_id.setter
    def merchant_logon_id(self, value):
        self._merchant_logon_id = value
    @property
    def need_app_auth(self):
        return self._need_app_auth

    @need_app_auth.setter
    def need_app_auth(self, value):
        self._need_app_auth = value
    @property
    def sign_order_no(self):
        return self._sign_order_no

    @sign_order_no.setter
    def sign_order_no(self, value):
        self._sign_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_auth_scene_infos:
            if isinstance(self.isv_auth_scene_infos, list):
                for i in range(0, len(self.isv_auth_scene_infos)):
                    element = self.isv_auth_scene_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.isv_auth_scene_infos[i] = element.to_alipay_dict()
            if hasattr(self.isv_auth_scene_infos, 'to_alipay_dict'):
                params['isv_auth_scene_infos'] = self.isv_auth_scene_infos.to_alipay_dict()
            else:
                params['isv_auth_scene_infos'] = self.isv_auth_scene_infos
        if self.merchant_logon_id:
            if hasattr(self.merchant_logon_id, 'to_alipay_dict'):
                params['merchant_logon_id'] = self.merchant_logon_id.to_alipay_dict()
            else:
                params['merchant_logon_id'] = self.merchant_logon_id
        if self.need_app_auth:
            if hasattr(self.need_app_auth, 'to_alipay_dict'):
                params['need_app_auth'] = self.need_app_auth.to_alipay_dict()
            else:
                params['need_app_auth'] = self.need_app_auth
        if self.sign_order_no:
            if hasattr(self.sign_order_no, 'to_alipay_dict'):
                params['sign_order_no'] = self.sign_order_no.to_alipay_dict()
            else:
                params['sign_order_no'] = self.sign_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpIsvSignauthCreateModel()
        if 'isv_auth_scene_infos' in d:
            o.isv_auth_scene_infos = d['isv_auth_scene_infos']
        if 'merchant_logon_id' in d:
            o.merchant_logon_id = d['merchant_logon_id']
        if 'need_app_auth' in d:
            o.need_app_auth = d['need_app_auth']
        if 'sign_order_no' in d:
            o.sign_order_no = d['sign_order_no']
        return o


