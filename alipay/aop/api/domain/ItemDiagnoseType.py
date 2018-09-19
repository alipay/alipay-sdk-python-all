#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemDiagnoseType(object):

    def __init__(self):
        self._item_diagnose = None
        self._item_diagnose_desc = None

    @property
    def item_diagnose(self):
        return self._item_diagnose

    @item_diagnose.setter
    def item_diagnose(self, value):
        self._item_diagnose = value
    @property
    def item_diagnose_desc(self):
        return self._item_diagnose_desc

    @item_diagnose_desc.setter
    def item_diagnose_desc(self, value):
        self._item_diagnose_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_diagnose:
            if hasattr(self.item_diagnose, 'to_alipay_dict'):
                params['item_diagnose'] = self.item_diagnose.to_alipay_dict()
            else:
                params['item_diagnose'] = self.item_diagnose
        if self.item_diagnose_desc:
            if hasattr(self.item_diagnose_desc, 'to_alipay_dict'):
                params['item_diagnose_desc'] = self.item_diagnose_desc.to_alipay_dict()
            else:
                params['item_diagnose_desc'] = self.item_diagnose_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDiagnoseType()
        if 'item_diagnose' in d:
            o.item_diagnose = d['item_diagnose']
        if 'item_diagnose_desc' in d:
            o.item_diagnose_desc = d['item_diagnose_desc']
        return o


