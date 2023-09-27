#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardExtendParamsDTO(object):

    def __init__(self):
        self._open_wallet = None

    @property
    def open_wallet(self):
        return self._open_wallet

    @open_wallet.setter
    def open_wallet(self, value):
        self._open_wallet = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_wallet:
            if hasattr(self.open_wallet, 'to_alipay_dict'):
                params['open_wallet'] = self.open_wallet.to_alipay_dict()
            else:
                params['open_wallet'] = self.open_wallet
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardExtendParamsDTO()
        if 'open_wallet' in d:
            o.open_wallet = d['open_wallet']
        return o


