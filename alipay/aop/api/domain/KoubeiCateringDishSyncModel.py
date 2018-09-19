#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishInfo import KbdishInfo


class KoubeiCateringDishSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._kb_dish_info = None
        self._syn_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def kb_dish_info(self):
        return self._kb_dish_info

    @kb_dish_info.setter
    def kb_dish_info(self, value):
        if isinstance(value, KbdishInfo):
            self._kb_dish_info = value
        else:
            self._kb_dish_info = KbdishInfo.from_alipay_dict(value)
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
        if self.kb_dish_info:
            if hasattr(self.kb_dish_info, 'to_alipay_dict'):
                params['kb_dish_info'] = self.kb_dish_info.to_alipay_dict()
            else:
                params['kb_dish_info'] = self.kb_dish_info
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
        o = KoubeiCateringDishSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'kb_dish_info' in d:
            o.kb_dish_info = d['kb_dish_info']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        return o


