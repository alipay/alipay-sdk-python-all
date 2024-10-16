#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardUnit import CardUnit


class CardContentDTO(object):

    def __init__(self):
        self._card_list = None
        self._ext_info = None

    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, value):
        if isinstance(value, list):
            self._card_list = list()
            for i in value:
                if isinstance(i, CardUnit):
                    self._card_list.append(i)
                else:
                    self._card_list.append(CardUnit.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_list:
            if isinstance(self.card_list, list):
                for i in range(0, len(self.card_list)):
                    element = self.card_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_list[i] = element.to_alipay_dict()
            if hasattr(self.card_list, 'to_alipay_dict'):
                params['card_list'] = self.card_list.to_alipay_dict()
            else:
                params['card_list'] = self.card_list
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardContentDTO()
        if 'card_list' in d:
            o.card_list = d['card_list']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        return o


