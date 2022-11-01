#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardAssetInfo(object):

    def __init__(self):
        self._card_no = None
        self._card_pwd = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_pwd(self):
        return self._card_pwd

    @card_pwd.setter
    def card_pwd(self, value):
        self._card_pwd = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_pwd:
            if hasattr(self.card_pwd, 'to_alipay_dict'):
                params['card_pwd'] = self.card_pwd.to_alipay_dict()
            else:
                params['card_pwd'] = self.card_pwd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardAssetInfo()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_pwd' in d:
            o.card_pwd = d['card_pwd']
        return o


