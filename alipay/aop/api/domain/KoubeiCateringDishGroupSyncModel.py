#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishGroupInfo import KbdishGroupInfo


class KoubeiCateringDishGroupSyncModel(object):

    def __init__(self):
        self._kb_dish_group = None
        self._syn_type = None

    @property
    def kb_dish_group(self):
        return self._kb_dish_group

    @kb_dish_group.setter
    def kb_dish_group(self, value):
        if isinstance(value, KbdishGroupInfo):
            self._kb_dish_group = value
        else:
            self._kb_dish_group = KbdishGroupInfo.from_alipay_dict(value)
    @property
    def syn_type(self):
        return self._syn_type

    @syn_type.setter
    def syn_type(self, value):
        self._syn_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.kb_dish_group:
            if hasattr(self.kb_dish_group, 'to_alipay_dict'):
                params['kb_dish_group'] = self.kb_dish_group.to_alipay_dict()
            else:
                params['kb_dish_group'] = self.kb_dish_group
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
        o = KoubeiCateringDishGroupSyncModel()
        if 'kb_dish_group' in d:
            o.kb_dish_group = d['kb_dish_group']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        return o


