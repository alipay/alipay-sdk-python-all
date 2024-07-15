#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DailyCarRentalFee(object):

    def __init__(self):
        self._rent_fee = None
        self._rental_date = None

    @property
    def rent_fee(self):
        return self._rent_fee

    @rent_fee.setter
    def rent_fee(self, value):
        self._rent_fee = value
    @property
    def rental_date(self):
        return self._rental_date

    @rental_date.setter
    def rental_date(self, value):
        self._rental_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.rent_fee:
            if hasattr(self.rent_fee, 'to_alipay_dict'):
                params['rent_fee'] = self.rent_fee.to_alipay_dict()
            else:
                params['rent_fee'] = self.rent_fee
        if self.rental_date:
            if hasattr(self.rental_date, 'to_alipay_dict'):
                params['rental_date'] = self.rental_date.to_alipay_dict()
            else:
                params['rental_date'] = self.rental_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DailyCarRentalFee()
        if 'rent_fee' in d:
            o.rent_fee = d['rent_fee']
        if 'rental_date' in d:
            o.rental_date = d['rental_date']
        return o


