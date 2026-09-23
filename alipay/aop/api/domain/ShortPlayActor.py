#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShortPlayActor(object):

    def __init__(self):
        self._name = None
        self._photo_material_id = None
        self._profile = None
        self._role = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def photo_material_id(self):
        return self._photo_material_id

    @photo_material_id.setter
    def photo_material_id(self, value):
        self._photo_material_id = value
    @property
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, value):
        self._profile = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.photo_material_id:
            if hasattr(self.photo_material_id, 'to_alipay_dict'):
                params['photo_material_id'] = self.photo_material_id.to_alipay_dict()
            else:
                params['photo_material_id'] = self.photo_material_id
        if self.profile:
            if hasattr(self.profile, 'to_alipay_dict'):
                params['profile'] = self.profile.to_alipay_dict()
            else:
                params['profile'] = self.profile
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShortPlayActor()
        if 'name' in d:
            o.name = d['name']
        if 'photo_material_id' in d:
            o.photo_material_id = d['photo_material_id']
        if 'profile' in d:
            o.profile = d['profile']
        if 'role' in d:
            o.role = d['role']
        return o


