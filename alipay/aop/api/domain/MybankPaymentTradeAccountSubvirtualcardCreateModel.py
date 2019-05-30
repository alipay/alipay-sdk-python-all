#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeAccountSubvirtualcardCreateModel(object):

    def __init__(self):
        self._member_id = None
        self._prim_card_name = None
        self._prim_card_no = None

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def prim_card_name(self):
        return self._prim_card_name

    @prim_card_name.setter
    def prim_card_name(self, value):
        self._prim_card_name = value
    @property
    def prim_card_no(self):
        return self._prim_card_no

    @prim_card_no.setter
    def prim_card_no(self, value):
        self._prim_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.prim_card_name:
            if hasattr(self.prim_card_name, 'to_alipay_dict'):
                params['prim_card_name'] = self.prim_card_name.to_alipay_dict()
            else:
                params['prim_card_name'] = self.prim_card_name
        if self.prim_card_no:
            if hasattr(self.prim_card_no, 'to_alipay_dict'):
                params['prim_card_no'] = self.prim_card_no.to_alipay_dict()
            else:
                params['prim_card_no'] = self.prim_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeAccountSubvirtualcardCreateModel()
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'prim_card_name' in d:
            o.prim_card_name = d['prim_card_name']
        if 'prim_card_no' in d:
            o.prim_card_no = d['prim_card_no']
        return o


