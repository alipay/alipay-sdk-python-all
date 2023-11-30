#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalGuideCardData import MedicalGuideCardData


class MedicalGuideCardDTO(object):

    def __init__(self):
        self._card_data = None
        self._template_code = None

    @property
    def card_data(self):
        return self._card_data

    @card_data.setter
    def card_data(self, value):
        if isinstance(value, MedicalGuideCardData):
            self._card_data = value
        else:
            self._card_data = MedicalGuideCardData.from_alipay_dict(value)
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_data:
            if hasattr(self.card_data, 'to_alipay_dict'):
                params['card_data'] = self.card_data.to_alipay_dict()
            else:
                params['card_data'] = self.card_data
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalGuideCardDTO()
        if 'card_data' in d:
            o.card_data = d['card_data']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


