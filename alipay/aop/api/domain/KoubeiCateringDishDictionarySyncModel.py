#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishDictionary import KbdishDictionary


class KoubeiCateringDishDictionarySyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._kb_dish_dictionary = None
        self._syn_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def kb_dish_dictionary(self):
        return self._kb_dish_dictionary

    @kb_dish_dictionary.setter
    def kb_dish_dictionary(self, value):
        if isinstance(value, KbdishDictionary):
            self._kb_dish_dictionary = value
        else:
            self._kb_dish_dictionary = KbdishDictionary.from_alipay_dict(value)
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
        if self.kb_dish_dictionary:
            if hasattr(self.kb_dish_dictionary, 'to_alipay_dict'):
                params['kb_dish_dictionary'] = self.kb_dish_dictionary.to_alipay_dict()
            else:
                params['kb_dish_dictionary'] = self.kb_dish_dictionary
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
        o = KoubeiCateringDishDictionarySyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'kb_dish_dictionary' in d:
            o.kb_dish_dictionary = d['kb_dish_dictionary']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        return o


