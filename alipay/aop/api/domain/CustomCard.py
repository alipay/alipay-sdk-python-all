#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomCard(object):

    def __init__(self):
        self._card_body = None
        self._card_id = None

    @property
    def card_body(self):
        return self._card_body

    @card_body.setter
    def card_body(self, value):
        self._card_body = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_body:
            if hasattr(self.card_body, 'to_alipay_dict'):
                params['card_body'] = self.card_body.to_alipay_dict()
            else:
                params['card_body'] = self.card_body
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
        o = CustomCard()
        if 'card_body' in d:
            o.card_body = d['card_body']
        if 'card_id' in d:
            o.card_id = d['card_id']
        return o


