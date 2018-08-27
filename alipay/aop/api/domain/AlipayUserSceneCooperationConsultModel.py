#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayUserPrincipalInfo import AlipayUserPrincipalInfo


class AlipayUserSceneCooperationConsultModel(object):

    def __init__(self):
        self._invite_scene = None
        self._partner_id = None
        self._pid = None
        self._principal = None
        self._scene = None

    @property
    def invite_scene(self):
        return self._invite_scene

    @invite_scene.setter
    def invite_scene(self, value):
        self._invite_scene = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        if isinstance(value, AlipayUserPrincipalInfo):
            self._principal = value
        else:
            self._principal = AlipayUserPrincipalInfo.from_alipay_dict(value)
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.invite_scene:
            if hasattr(self.invite_scene, 'to_alipay_dict'):
                params['invite_scene'] = self.invite_scene.to_alipay_dict()
            else:
                params['invite_scene'] = self.invite_scene
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserSceneCooperationConsultModel()
        if 'invite_scene' in d:
            o.invite_scene = d['invite_scene']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'principal' in d:
            o.principal = d['principal']
        if 'scene' in d:
            o.scene = d['scene']
        return o


