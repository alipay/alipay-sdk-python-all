#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PostInfo(object):

    def __init__(self):
        self._customer_service_phone = None
        self._receiving_address = None
        self._receiving_unit = None
        self._supplementary_data_info = None

    @property
    def customer_service_phone(self):
        return self._customer_service_phone

    @customer_service_phone.setter
    def customer_service_phone(self, value):
        self._customer_service_phone = value
    @property
    def receiving_address(self):
        return self._receiving_address

    @receiving_address.setter
    def receiving_address(self, value):
        self._receiving_address = value
    @property
    def receiving_unit(self):
        return self._receiving_unit

    @receiving_unit.setter
    def receiving_unit(self, value):
        self._receiving_unit = value
    @property
    def supplementary_data_info(self):
        return self._supplementary_data_info

    @supplementary_data_info.setter
    def supplementary_data_info(self, value):
        self._supplementary_data_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_service_phone:
            if hasattr(self.customer_service_phone, 'to_alipay_dict'):
                params['customer_service_phone'] = self.customer_service_phone.to_alipay_dict()
            else:
                params['customer_service_phone'] = self.customer_service_phone
        if self.receiving_address:
            if hasattr(self.receiving_address, 'to_alipay_dict'):
                params['receiving_address'] = self.receiving_address.to_alipay_dict()
            else:
                params['receiving_address'] = self.receiving_address
        if self.receiving_unit:
            if hasattr(self.receiving_unit, 'to_alipay_dict'):
                params['receiving_unit'] = self.receiving_unit.to_alipay_dict()
            else:
                params['receiving_unit'] = self.receiving_unit
        if self.supplementary_data_info:
            if hasattr(self.supplementary_data_info, 'to_alipay_dict'):
                params['supplementary_data_info'] = self.supplementary_data_info.to_alipay_dict()
            else:
                params['supplementary_data_info'] = self.supplementary_data_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PostInfo()
        if 'customer_service_phone' in d:
            o.customer_service_phone = d['customer_service_phone']
        if 'receiving_address' in d:
            o.receiving_address = d['receiving_address']
        if 'receiving_unit' in d:
            o.receiving_unit = d['receiving_unit']
        if 'supplementary_data_info' in d:
            o.supplementary_data_info = d['supplementary_data_info']
        return o


