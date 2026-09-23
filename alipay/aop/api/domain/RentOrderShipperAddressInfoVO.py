#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentOrderShipperAddressInfoVO(object):

    def __init__(self):
        self._detailed_shipper_address = None
        self._shipper_name = None
        self._shipper_tel_number = None

    @property
    def detailed_shipper_address(self):
        return self._detailed_shipper_address

    @detailed_shipper_address.setter
    def detailed_shipper_address(self, value):
        self._detailed_shipper_address = value
    @property
    def shipper_name(self):
        return self._shipper_name

    @shipper_name.setter
    def shipper_name(self, value):
        self._shipper_name = value
    @property
    def shipper_tel_number(self):
        return self._shipper_tel_number

    @shipper_tel_number.setter
    def shipper_tel_number(self, value):
        self._shipper_tel_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.detailed_shipper_address:
            if hasattr(self.detailed_shipper_address, 'to_alipay_dict'):
                params['detailed_shipper_address'] = self.detailed_shipper_address.to_alipay_dict()
            else:
                params['detailed_shipper_address'] = self.detailed_shipper_address
        if self.shipper_name:
            if hasattr(self.shipper_name, 'to_alipay_dict'):
                params['shipper_name'] = self.shipper_name.to_alipay_dict()
            else:
                params['shipper_name'] = self.shipper_name
        if self.shipper_tel_number:
            if hasattr(self.shipper_tel_number, 'to_alipay_dict'):
                params['shipper_tel_number'] = self.shipper_tel_number.to_alipay_dict()
            else:
                params['shipper_tel_number'] = self.shipper_tel_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderShipperAddressInfoVO()
        if 'detailed_shipper_address' in d:
            o.detailed_shipper_address = d['detailed_shipper_address']
        if 'shipper_name' in d:
            o.shipper_name = d['shipper_name']
        if 'shipper_tel_number' in d:
            o.shipper_tel_number = d['shipper_tel_number']
        return o


