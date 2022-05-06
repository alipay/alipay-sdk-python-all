#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtLinktypeQueryModel(object):

    def __init__(self):
        self._scene_type_code = None
        self._tnt_inst_id = None

    @property
    def scene_type_code(self):
        return self._scene_type_code

    @scene_type_code.setter
    def scene_type_code(self, value):
        self._scene_type_code = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_type_code:
            if hasattr(self.scene_type_code, 'to_alipay_dict'):
                params['scene_type_code'] = self.scene_type_code.to_alipay_dict()
            else:
                params['scene_type_code'] = self.scene_type_code
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtLinktypeQueryModel()
        if 'scene_type_code' in d:
            o.scene_type_code = d['scene_type_code']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


