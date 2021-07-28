#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignCardInfo(object):

    def __init__(self):
        self._card_no_en = None
        self._first_eight_card_no = None

    @property
    def card_no_en(self):
        return self._card_no_en

    @card_no_en.setter
    def card_no_en(self, value):
        self._card_no_en = value
    @property
    def first_eight_card_no(self):
        return self._first_eight_card_no

    @first_eight_card_no.setter
    def first_eight_card_no(self, value):
        self._first_eight_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no_en:
            if hasattr(self.card_no_en, 'to_alipay_dict'):
                params['card_no_en'] = self.card_no_en.to_alipay_dict()
            else:
                params['card_no_en'] = self.card_no_en
        if self.first_eight_card_no:
            if hasattr(self.first_eight_card_no, 'to_alipay_dict'):
                params['first_eight_card_no'] = self.first_eight_card_no.to_alipay_dict()
            else:
                params['first_eight_card_no'] = self.first_eight_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignCardInfo()
        if 'card_no_en' in d:
            o.card_no_en = d['card_no_en']
        if 'first_eight_card_no' in d:
            o.first_eight_card_no = d['first_eight_card_no']
        return o


