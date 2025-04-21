#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardAftersalesQueryModel(object):

    def __init__(self):
        self._aftersales_id = None
        self._card_id = None

    @property
    def aftersales_id(self):
        return self._aftersales_id

    @aftersales_id.setter
    def aftersales_id(self, value):
        self._aftersales_id = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersales_id:
            if hasattr(self.aftersales_id, 'to_alipay_dict'):
                params['aftersales_id'] = self.aftersales_id.to_alipay_dict()
            else:
                params['aftersales_id'] = self.aftersales_id
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardAftersalesQueryModel()
        if 'aftersales_id' in d:
            o.aftersales_id = d['aftersales_id']
        if 'card_id' in d:
            o.card_id = d['card_id']
        return o


