#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessParams(object):

    def __init__(self):
        self._actual_order_time = None
        self._campus_card = None
        self._card_type = None

    @property
    def actual_order_time(self):
        return self._actual_order_time

    @actual_order_time.setter
    def actual_order_time(self, value):
        self._actual_order_time = value
    @property
    def campus_card(self):
        return self._campus_card

    @campus_card.setter
    def campus_card(self, value):
        self._campus_card = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_order_time:
            if hasattr(self.actual_order_time, 'to_alipay_dict'):
                params['actual_order_time'] = self.actual_order_time.to_alipay_dict()
            else:
                params['actual_order_time'] = self.actual_order_time
        if self.campus_card:
            if hasattr(self.campus_card, 'to_alipay_dict'):
                params['campus_card'] = self.campus_card.to_alipay_dict()
            else:
                params['campus_card'] = self.campus_card
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessParams()
        if 'actual_order_time' in d:
            o.actual_order_time = d['actual_order_time']
        if 'campus_card' in d:
            o.campus_card = d['campus_card']
        if 'card_type' in d:
            o.card_type = d['card_type']
        return o


