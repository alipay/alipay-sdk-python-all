#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalGuideCardDTO import MedicalGuideCardDTO


class MedicalGuideContentDTO(object):

    def __init__(self):
        self._card = None
        self._text = None

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, value):
        if isinstance(value, MedicalGuideCardDTO):
            self._card = value
        else:
            self._card = MedicalGuideCardDTO.from_alipay_dict(value)
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.card:
            if hasattr(self.card, 'to_alipay_dict'):
                params['card'] = self.card.to_alipay_dict()
            else:
                params['card'] = self.card
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalGuideContentDTO()
        if 'card' in d:
            o.card = d['card']
        if 'text' in d:
            o.text = d['text']
        return o


