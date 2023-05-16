#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrMoneyDTO import IndrMoneyDTO


class AlipayOverseasOpenIndramountPreconsultModel(object):

    def __init__(self):
        self._original_amount = None
        self._scene_type = None

    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        if isinstance(value, IndrMoneyDTO):
            self._original_amount = value
        else:
            self._original_amount = IndrMoneyDTO.from_alipay_dict(value)
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.original_amount:
            if hasattr(self.original_amount, 'to_alipay_dict'):
                params['original_amount'] = self.original_amount.to_alipay_dict()
            else:
                params['original_amount'] = self.original_amount
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndramountPreconsultModel()
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


