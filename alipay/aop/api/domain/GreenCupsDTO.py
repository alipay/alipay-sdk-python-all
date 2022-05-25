#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GreenCupsDTO(object):

    def __init__(self):
        self._cup_type = None
        self._cups_amount = None

    @property
    def cup_type(self):
        return self._cup_type

    @cup_type.setter
    def cup_type(self, value):
        self._cup_type = value
    @property
    def cups_amount(self):
        return self._cups_amount

    @cups_amount.setter
    def cups_amount(self, value):
        self._cups_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.cup_type:
            if hasattr(self.cup_type, 'to_alipay_dict'):
                params['cup_type'] = self.cup_type.to_alipay_dict()
            else:
                params['cup_type'] = self.cup_type
        if self.cups_amount:
            if hasattr(self.cups_amount, 'to_alipay_dict'):
                params['cups_amount'] = self.cups_amount.to_alipay_dict()
            else:
                params['cups_amount'] = self.cups_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GreenCupsDTO()
        if 'cup_type' in d:
            o.cup_type = d['cup_type']
        if 'cups_amount' in d:
            o.cups_amount = d['cups_amount']
        return o


