#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCookInfo import KbdishCookInfo


class KoubeiCateringDishCookSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._kb_dish_cook = None
        self._syn_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def kb_dish_cook(self):
        return self._kb_dish_cook

    @kb_dish_cook.setter
    def kb_dish_cook(self, value):
        if isinstance(value, KbdishCookInfo):
            self._kb_dish_cook = value
        else:
            self._kb_dish_cook = KbdishCookInfo.from_alipay_dict(value)
    @property
    def syn_type(self):
        return self._syn_type

    @syn_type.setter
    def syn_type(self, value):
        self._syn_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.kb_dish_cook:
            if hasattr(self.kb_dish_cook, 'to_alipay_dict'):
                params['kb_dish_cook'] = self.kb_dish_cook.to_alipay_dict()
            else:
                params['kb_dish_cook'] = self.kb_dish_cook
        if self.syn_type:
            if hasattr(self.syn_type, 'to_alipay_dict'):
                params['syn_type'] = self.syn_type.to_alipay_dict()
            else:
                params['syn_type'] = self.syn_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishCookSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'kb_dish_cook' in d:
            o.kb_dish_cook = d['kb_dish_cook']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        return o


