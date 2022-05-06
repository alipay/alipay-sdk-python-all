#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignPartyOpenApiDTO import SignPartyOpenApiDTO


class SignPartyGroupOpenApiDTO(object):

    def __init__(self):
        self._sign_parties = None

    @property
    def sign_parties(self):
        return self._sign_parties

    @sign_parties.setter
    def sign_parties(self, value):
        if isinstance(value, list):
            self._sign_parties = list()
            for i in value:
                if isinstance(i, SignPartyOpenApiDTO):
                    self._sign_parties.append(i)
                else:
                    self._sign_parties.append(SignPartyOpenApiDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.sign_parties:
            if isinstance(self.sign_parties, list):
                for i in range(0, len(self.sign_parties)):
                    element = self.sign_parties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_parties[i] = element.to_alipay_dict()
            if hasattr(self.sign_parties, 'to_alipay_dict'):
                params['sign_parties'] = self.sign_parties.to_alipay_dict()
            else:
                params['sign_parties'] = self.sign_parties
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignPartyGroupOpenApiDTO()
        if 'sign_parties' in d:
            o.sign_parties = d['sign_parties']
        return o


