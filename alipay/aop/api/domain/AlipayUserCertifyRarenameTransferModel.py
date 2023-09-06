#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyRarenameTransferModel(object):

    def __init__(self):
        self._name = None
        self._principal_id = None
        self._scene = None
        self._target_encode_type = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def target_encode_type(self):
        return self._target_encode_type

    @target_encode_type.setter
    def target_encode_type(self, value):
        self._target_encode_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.target_encode_type:
            if hasattr(self.target_encode_type, 'to_alipay_dict'):
                params['target_encode_type'] = self.target_encode_type.to_alipay_dict()
            else:
                params['target_encode_type'] = self.target_encode_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertifyRarenameTransferModel()
        if 'name' in d:
            o.name = d['name']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'target_encode_type' in d:
            o.target_encode_type = d['target_encode_type']
        return o


