#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntpaasRoleDeleteModel(object):

    def __init__(self):
        self._biz_scene = None
        self._ip_role_id = None
        self._join_rel_role_biz_platform = None
        self._operator_id = None
        self._rel_biz_typ = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def join_rel_role_biz_platform(self):
        return self._join_rel_role_biz_platform

    @join_rel_role_biz_platform.setter
    def join_rel_role_biz_platform(self, value):
        self._join_rel_role_biz_platform = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def rel_biz_typ(self):
        return self._rel_biz_typ

    @rel_biz_typ.setter
    def rel_biz_typ(self, value):
        self._rel_biz_typ = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.join_rel_role_biz_platform:
            if hasattr(self.join_rel_role_biz_platform, 'to_alipay_dict'):
                params['join_rel_role_biz_platform'] = self.join_rel_role_biz_platform.to_alipay_dict()
            else:
                params['join_rel_role_biz_platform'] = self.join_rel_role_biz_platform
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.rel_biz_typ:
            if hasattr(self.rel_biz_typ, 'to_alipay_dict'):
                params['rel_biz_typ'] = self.rel_biz_typ.to_alipay_dict()
            else:
                params['rel_biz_typ'] = self.rel_biz_typ
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntpaasRoleDeleteModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'join_rel_role_biz_platform' in d:
            o.join_rel_role_biz_platform = d['join_rel_role_biz_platform']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'rel_biz_typ' in d:
            o.rel_biz_typ = d['rel_biz_typ']
        return o


