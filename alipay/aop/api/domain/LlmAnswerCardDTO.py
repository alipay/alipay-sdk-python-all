#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardDataInfoDTO import CardDataInfoDTO


class LlmAnswerCardDTO(object):

    def __init__(self):
        self._card_answer = None
        self._card_data = None
        self._card_type = None

    @property
    def card_answer(self):
        return self._card_answer

    @card_answer.setter
    def card_answer(self, value):
        self._card_answer = value
    @property
    def card_data(self):
        return self._card_data

    @card_data.setter
    def card_data(self, value):
        if isinstance(value, list):
            self._card_data = list()
            for i in value:
                if isinstance(i, CardDataInfoDTO):
                    self._card_data.append(i)
                else:
                    self._card_data.append(CardDataInfoDTO.from_alipay_dict(i))
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_answer:
            if hasattr(self.card_answer, 'to_alipay_dict'):
                params['card_answer'] = self.card_answer.to_alipay_dict()
            else:
                params['card_answer'] = self.card_answer
        if self.card_data:
            if isinstance(self.card_data, list):
                for i in range(0, len(self.card_data)):
                    element = self.card_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_data[i] = element.to_alipay_dict()
            if hasattr(self.card_data, 'to_alipay_dict'):
                params['card_data'] = self.card_data.to_alipay_dict()
            else:
                params['card_data'] = self.card_data
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
        o = LlmAnswerCardDTO()
        if 'card_answer' in d:
            o.card_answer = d['card_answer']
        if 'card_data' in d:
            o.card_data = d['card_data']
        if 'card_type' in d:
            o.card_type = d['card_type']
        return o


