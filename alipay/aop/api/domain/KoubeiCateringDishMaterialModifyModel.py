#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishMaterialInfo import KbdishMaterialInfo


class KoubeiCateringDishMaterialModifyModel(object):

    def __init__(self):
        self._kb_dish_material_info = None

    @property
    def kb_dish_material_info(self):
        return self._kb_dish_material_info

    @kb_dish_material_info.setter
    def kb_dish_material_info(self, value):
        if isinstance(value, KbdishMaterialInfo):
            self._kb_dish_material_info = value
        else:
            self._kb_dish_material_info = KbdishMaterialInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.kb_dish_material_info:
            if hasattr(self.kb_dish_material_info, 'to_alipay_dict'):
                params['kb_dish_material_info'] = self.kb_dish_material_info.to_alipay_dict()
            else:
                params['kb_dish_material_info'] = self.kb_dish_material_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishMaterialModifyModel()
        if 'kb_dish_material_info' in d:
            o.kb_dish_material_info = d['kb_dish_material_info']
        return o


