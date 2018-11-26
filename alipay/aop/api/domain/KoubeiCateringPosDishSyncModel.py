#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosDishModel import PosDishModel


class KoubeiCateringPosDishSyncModel(object):

    def __init__(self):
        self._pos_dish_model = None

    @property
    def pos_dish_model(self):
        return self._pos_dish_model

    @pos_dish_model.setter
    def pos_dish_model(self, value):
        if isinstance(value, PosDishModel):
            self._pos_dish_model = value
        else:
            self._pos_dish_model = PosDishModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.pos_dish_model:
            if hasattr(self.pos_dish_model, 'to_alipay_dict'):
                params['pos_dish_model'] = self.pos_dish_model.to_alipay_dict()
            else:
                params['pos_dish_model'] = self.pos_dish_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosDishSyncModel()
        if 'pos_dish_model' in d:
            o.pos_dish_model = d['pos_dish_model']
        return o


