#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HealthCard import HealthCard


class HealthCardInfo(object):

    def __init__(self):
        self._cards = None
        self._receive_url = None

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if isinstance(value, list):
            self._cards = list()
            for i in value:
                if isinstance(i, HealthCard):
                    self._cards.append(i)
                else:
                    self._cards.append(HealthCard.from_alipay_dict(i))
    @property
    def receive_url(self):
        return self._receive_url

    @receive_url.setter
    def receive_url(self, value):
        self._receive_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.cards:
            if isinstance(self.cards, list):
                for i in range(0, len(self.cards)):
                    element = self.cards[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cards[i] = element.to_alipay_dict()
            if hasattr(self.cards, 'to_alipay_dict'):
                params['cards'] = self.cards.to_alipay_dict()
            else:
                params['cards'] = self.cards
        if self.receive_url:
            if hasattr(self.receive_url, 'to_alipay_dict'):
                params['receive_url'] = self.receive_url.to_alipay_dict()
            else:
                params['receive_url'] = self.receive_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthCardInfo()
        if 'cards' in d:
            o.cards = d['cards']
        if 'receive_url' in d:
            o.receive_url = d['receive_url']
        return o


