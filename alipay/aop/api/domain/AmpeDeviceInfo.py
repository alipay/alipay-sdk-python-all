#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmpeDeviceInfo(object):

    def __init__(self):
        self._card_height = None
        self._card_width = None

    @property
    def card_height(self):
        return self._card_height

    @card_height.setter
    def card_height(self, value):
        self._card_height = value
    @property
    def card_width(self):
        return self._card_width

    @card_width.setter
    def card_width(self, value):
        self._card_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_height:
            if hasattr(self.card_height, 'to_alipay_dict'):
                params['card_height'] = self.card_height.to_alipay_dict()
            else:
                params['card_height'] = self.card_height
        if self.card_width:
            if hasattr(self.card_width, 'to_alipay_dict'):
                params['card_width'] = self.card_width.to_alipay_dict()
            else:
                params['card_width'] = self.card_width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmpeDeviceInfo()
        if 'card_height' in d:
            o.card_height = d['card_height']
        if 'card_width' in d:
            o.card_width = d['card_width']
        return o


