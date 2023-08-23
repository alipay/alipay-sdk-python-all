#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiveInfoDto(object):

    def __init__(self):
        self._address = None
        self._postcode = None
        self._receive = None
        self._telephone = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def postcode(self):
        return self._postcode

    @postcode.setter
    def postcode(self, value):
        self._postcode = value
    @property
    def receive(self):
        return self._receive

    @receive.setter
    def receive(self, value):
        self._receive = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.postcode:
            if hasattr(self.postcode, 'to_alipay_dict'):
                params['postcode'] = self.postcode.to_alipay_dict()
            else:
                params['postcode'] = self.postcode
        if self.receive:
            if hasattr(self.receive, 'to_alipay_dict'):
                params['receive'] = self.receive.to_alipay_dict()
            else:
                params['receive'] = self.receive
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiveInfoDto()
        if 'address' in d:
            o.address = d['address']
        if 'postcode' in d:
            o.postcode = d['postcode']
        if 'receive' in d:
            o.receive = d['receive']
        if 'telephone' in d:
            o.telephone = d['telephone']
        return o


