#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardSecretDTO import CardSecretDTO


class VirtualInfoDTO(object):

    def __init__(self):
        self._card_secret = None
        self._virtual_use_jump_url = None

    @property
    def card_secret(self):
        return self._card_secret

    @card_secret.setter
    def card_secret(self, value):
        if isinstance(value, list):
            self._card_secret = list()
            for i in value:
                if isinstance(i, CardSecretDTO):
                    self._card_secret.append(i)
                else:
                    self._card_secret.append(CardSecretDTO.from_alipay_dict(i))
    @property
    def virtual_use_jump_url(self):
        return self._virtual_use_jump_url

    @virtual_use_jump_url.setter
    def virtual_use_jump_url(self, value):
        self._virtual_use_jump_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_secret:
            if isinstance(self.card_secret, list):
                for i in range(0, len(self.card_secret)):
                    element = self.card_secret[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_secret[i] = element.to_alipay_dict()
            if hasattr(self.card_secret, 'to_alipay_dict'):
                params['card_secret'] = self.card_secret.to_alipay_dict()
            else:
                params['card_secret'] = self.card_secret
        if self.virtual_use_jump_url:
            if hasattr(self.virtual_use_jump_url, 'to_alipay_dict'):
                params['virtual_use_jump_url'] = self.virtual_use_jump_url.to_alipay_dict()
            else:
                params['virtual_use_jump_url'] = self.virtual_use_jump_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VirtualInfoDTO()
        if 'card_secret' in d:
            o.card_secret = d['card_secret']
        if 'virtual_use_jump_url' in d:
            o.virtual_use_jump_url = d['virtual_use_jump_url']
        return o


