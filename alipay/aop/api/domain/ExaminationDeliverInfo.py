#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExaminationDeliverInfo(object):

    def __init__(self):
        self._address = None
        self._carrier_order_no = None
        self._phone = None
        self._user_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def carrier_order_no(self):
        return self._carrier_order_no

    @carrier_order_no.setter
    def carrier_order_no(self, value):
        self._carrier_order_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.carrier_order_no:
            if hasattr(self.carrier_order_no, 'to_alipay_dict'):
                params['carrier_order_no'] = self.carrier_order_no.to_alipay_dict()
            else:
                params['carrier_order_no'] = self.carrier_order_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationDeliverInfo()
        if 'address' in d:
            o.address = d['address']
        if 'carrier_order_no' in d:
            o.carrier_order_no = d['carrier_order_no']
        if 'phone' in d:
            o.phone = d['phone']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


