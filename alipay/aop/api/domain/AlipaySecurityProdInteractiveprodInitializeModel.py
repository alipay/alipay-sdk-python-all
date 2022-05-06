#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdInteractiveprodInitializeModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_request_params = None
        self._need_consult = None
        self._scene_id = None
        self._tenant_id = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_request_params(self):
        return self._biz_request_params

    @biz_request_params.setter
    def biz_request_params(self, value):
        self._biz_request_params = value
    @property
    def need_consult(self):
        return self._need_consult

    @need_consult.setter
    def need_consult(self, value):
        self._need_consult = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_request_params:
            if hasattr(self.biz_request_params, 'to_alipay_dict'):
                params['biz_request_params'] = self.biz_request_params.to_alipay_dict()
            else:
                params['biz_request_params'] = self.biz_request_params
        if self.need_consult:
            if hasattr(self.need_consult, 'to_alipay_dict'):
                params['need_consult'] = self.need_consult.to_alipay_dict()
            else:
                params['need_consult'] = self.need_consult
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
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
        o = AlipaySecurityProdInteractiveprodInitializeModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_request_params' in d:
            o.biz_request_params = d['biz_request_params']
        if 'need_consult' in d:
            o.need_consult = d['need_consult']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


