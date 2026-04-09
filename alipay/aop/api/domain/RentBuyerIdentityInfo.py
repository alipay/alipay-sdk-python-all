#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentBuyerIdentityInfo(object):

    def __init__(self):
        self._buyer_name = None
        self._id_number = None
        self._tel_number = None

    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value
    @property
    def tel_number(self):
        return self._tel_number

    @tel_number.setter
    def tel_number(self, value):
        self._tel_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.id_number:
            if hasattr(self.id_number, 'to_alipay_dict'):
                params['id_number'] = self.id_number.to_alipay_dict()
            else:
                params['id_number'] = self.id_number
        if self.tel_number:
            if hasattr(self.tel_number, 'to_alipay_dict'):
                params['tel_number'] = self.tel_number.to_alipay_dict()
            else:
                params['tel_number'] = self.tel_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentBuyerIdentityInfo()
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'tel_number' in d:
            o.tel_number = d['tel_number']
        return o


