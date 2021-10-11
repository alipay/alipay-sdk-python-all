#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeSubaccountBalanceQueryModel(object):

    def __init__(self):
        self._scene_code = None
        self._sub_card_no = None

    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sub_card_no(self):
        return self._sub_card_no

    @sub_card_no.setter
    def sub_card_no(self, value):
        self._sub_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sub_card_no:
            if hasattr(self.sub_card_no, 'to_alipay_dict'):
                params['sub_card_no'] = self.sub_card_no.to_alipay_dict()
            else:
                params['sub_card_no'] = self.sub_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeSubaccountBalanceQueryModel()
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sub_card_no' in d:
            o.sub_card_no = d['sub_card_no']
        return o


