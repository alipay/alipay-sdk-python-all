#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmSwItemDeleteModel(object):

    def __init__(self):
        self._item_codes = None
        self._syn_id = None

    @property
    def item_codes(self):
        return self._item_codes

    @item_codes.setter
    def item_codes(self, value):
        if isinstance(value, list):
            self._item_codes = list()
            for i in value:
                self._item_codes.append(i)
    @property
    def syn_id(self):
        return self._syn_id

    @syn_id.setter
    def syn_id(self, value):
        self._syn_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_codes:
            if isinstance(self.item_codes, list):
                for i in range(0, len(self.item_codes)):
                    element = self.item_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_codes[i] = element.to_alipay_dict()
            if hasattr(self.item_codes, 'to_alipay_dict'):
                params['item_codes'] = self.item_codes.to_alipay_dict()
            else:
                params['item_codes'] = self.item_codes
        if self.syn_id:
            if hasattr(self.syn_id, 'to_alipay_dict'):
                params['syn_id'] = self.syn_id.to_alipay_dict()
            else:
                params['syn_id'] = self.syn_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmSwItemDeleteModel()
        if 'item_codes' in d:
            o.item_codes = d['item_codes']
        if 'syn_id' in d:
            o.syn_id = d['syn_id']
        return o


