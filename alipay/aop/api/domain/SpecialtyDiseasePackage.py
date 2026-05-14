#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecialtyDiseasePackage(object):

    def __init__(self):
        self._fulfillment_valid_days = None
        self._service_package_desc = None
        self._service_package_id = None
        self._service_package_name = None
        self._service_package_price = None

    @property
    def fulfillment_valid_days(self):
        return self._fulfillment_valid_days

    @fulfillment_valid_days.setter
    def fulfillment_valid_days(self, value):
        self._fulfillment_valid_days = value
    @property
    def service_package_desc(self):
        return self._service_package_desc

    @service_package_desc.setter
    def service_package_desc(self, value):
        self._service_package_desc = value
    @property
    def service_package_id(self):
        return self._service_package_id

    @service_package_id.setter
    def service_package_id(self, value):
        self._service_package_id = value
    @property
    def service_package_name(self):
        return self._service_package_name

    @service_package_name.setter
    def service_package_name(self, value):
        self._service_package_name = value
    @property
    def service_package_price(self):
        return self._service_package_price

    @service_package_price.setter
    def service_package_price(self, value):
        self._service_package_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_valid_days:
            if hasattr(self.fulfillment_valid_days, 'to_alipay_dict'):
                params['fulfillment_valid_days'] = self.fulfillment_valid_days.to_alipay_dict()
            else:
                params['fulfillment_valid_days'] = self.fulfillment_valid_days
        if self.service_package_desc:
            if hasattr(self.service_package_desc, 'to_alipay_dict'):
                params['service_package_desc'] = self.service_package_desc.to_alipay_dict()
            else:
                params['service_package_desc'] = self.service_package_desc
        if self.service_package_id:
            if hasattr(self.service_package_id, 'to_alipay_dict'):
                params['service_package_id'] = self.service_package_id.to_alipay_dict()
            else:
                params['service_package_id'] = self.service_package_id
        if self.service_package_name:
            if hasattr(self.service_package_name, 'to_alipay_dict'):
                params['service_package_name'] = self.service_package_name.to_alipay_dict()
            else:
                params['service_package_name'] = self.service_package_name
        if self.service_package_price:
            if hasattr(self.service_package_price, 'to_alipay_dict'):
                params['service_package_price'] = self.service_package_price.to_alipay_dict()
            else:
                params['service_package_price'] = self.service_package_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecialtyDiseasePackage()
        if 'fulfillment_valid_days' in d:
            o.fulfillment_valid_days = d['fulfillment_valid_days']
        if 'service_package_desc' in d:
            o.service_package_desc = d['service_package_desc']
        if 'service_package_id' in d:
            o.service_package_id = d['service_package_id']
        if 'service_package_name' in d:
            o.service_package_name = d['service_package_name']
        if 'service_package_price' in d:
            o.service_package_price = d['service_package_price']
        return o


