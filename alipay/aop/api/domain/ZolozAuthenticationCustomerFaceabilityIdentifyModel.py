#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FaceAbilityExtInfo import FaceAbilityExtInfo


class ZolozAuthenticationCustomerFaceabilityIdentifyModel(object):

    def __init__(self):
        self._ability = None
        self._alg_ver = None
        self._auth_img = None
        self._biz_id = None
        self._ext_info = None
        self._scene_code = None

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, value):
        self._ability = value
    @property
    def alg_ver(self):
        return self._alg_ver

    @alg_ver.setter
    def alg_ver(self, value):
        self._alg_ver = value
    @property
    def auth_img(self):
        return self._auth_img

    @auth_img.setter
    def auth_img(self, value):
        self._auth_img = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, FaceAbilityExtInfo):
            self._ext_info = value
        else:
            self._ext_info = FaceAbilityExtInfo.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability:
            if hasattr(self.ability, 'to_alipay_dict'):
                params['ability'] = self.ability.to_alipay_dict()
            else:
                params['ability'] = self.ability
        if self.alg_ver:
            if hasattr(self.alg_ver, 'to_alipay_dict'):
                params['alg_ver'] = self.alg_ver.to_alipay_dict()
            else:
                params['alg_ver'] = self.alg_ver
        if self.auth_img:
            if hasattr(self.auth_img, 'to_alipay_dict'):
                params['auth_img'] = self.auth_img.to_alipay_dict()
            else:
                params['auth_img'] = self.auth_img
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationCustomerFaceabilityIdentifyModel()
        if 'ability' in d:
            o.ability = d['ability']
        if 'alg_ver' in d:
            o.alg_ver = d['alg_ver']
        if 'auth_img' in d:
            o.auth_img = d['auth_img']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


