#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyRarenameMatchModel(object):

    def __init__(self):
        self._principal_id = None
        self._scene = None
        self._source_name = None
        self._target_name = None

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
    def source_name(self):
        return self._source_name

    @source_name.setter
    def source_name(self, value):
        self._source_name = value
    @property
    def target_name(self):
        return self._target_name

    @target_name.setter
    def target_name(self, value):
        self._target_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.source_name:
            if hasattr(self.source_name, 'to_alipay_dict'):
                params['source_name'] = self.source_name.to_alipay_dict()
            else:
                params['source_name'] = self.source_name
        if self.target_name:
            if hasattr(self.target_name, 'to_alipay_dict'):
                params['target_name'] = self.target_name.to_alipay_dict()
            else:
                params['target_name'] = self.target_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertifyRarenameMatchModel()
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'source_name' in d:
            o.source_name = d['source_name']
        if 'target_name' in d:
            o.target_name = d['target_name']
        return o


