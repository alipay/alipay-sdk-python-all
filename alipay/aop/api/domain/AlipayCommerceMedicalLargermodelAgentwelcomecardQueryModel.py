#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalLargermodelAgentwelcomecardQueryModel(object):

    def __init__(self):
        self._agent_code = None
        self._open_id = None
        self._org_id = None
        self._out_user_id = None
        self._outer_user_type = None
        self._scene_code = None

    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def outer_user_type(self):
        return self._outer_user_type

    @outer_user_type.setter
    def outer_user_type(self, value):
        self._outer_user_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = self.agent_code.to_alipay_dict()
            else:
                params['agent_code'] = self.agent_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.outer_user_type:
            if hasattr(self.outer_user_type, 'to_alipay_dict'):
                params['outer_user_type'] = self.outer_user_type.to_alipay_dict()
            else:
                params['outer_user_type'] = self.outer_user_type
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
        o = AlipayCommerceMedicalLargermodelAgentwelcomecardQueryModel()
        if 'agent_code' in d:
            o.agent_code = d['agent_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'outer_user_type' in d:
            o.outer_user_type = d['outer_user_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


