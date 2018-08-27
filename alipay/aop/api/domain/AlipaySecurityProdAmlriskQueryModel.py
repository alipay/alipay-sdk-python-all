#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndividualInfo import IndividualInfo


class AlipaySecurityProdAmlriskQueryModel(object):

    def __init__(self):
        self._business_address = None
        self._event_id = None
        self._individual_list = None
        self._legal_name = None
        self._merchant_id = None
        self._order_id = None
        self._registered_address = None
        self._registration_number = None

    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        self._business_address = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def individual_list(self):
        return self._individual_list

    @individual_list.setter
    def individual_list(self, value):
        if isinstance(value, list):
            self._individual_list = list()
            for i in value:
                if isinstance(i, IndividualInfo):
                    self._individual_list.append(i)
                else:
                    self._individual_list.append(IndividualInfo.from_alipay_dict(i))
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def registered_address(self):
        return self._registered_address

    @registered_address.setter
    def registered_address(self, value):
        self._registered_address = value
    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    def registration_number(self, value):
        self._registration_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_address:
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        if self.individual_list:
            if isinstance(self.individual_list, list):
                for i in range(0, len(self.individual_list)):
                    element = self.individual_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.individual_list[i] = element.to_alipay_dict()
            if hasattr(self.individual_list, 'to_alipay_dict'):
                params['individual_list'] = self.individual_list.to_alipay_dict()
            else:
                params['individual_list'] = self.individual_list
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.registered_address:
            if hasattr(self.registered_address, 'to_alipay_dict'):
                params['registered_address'] = self.registered_address.to_alipay_dict()
            else:
                params['registered_address'] = self.registered_address
        if self.registration_number:
            if hasattr(self.registration_number, 'to_alipay_dict'):
                params['registration_number'] = self.registration_number.to_alipay_dict()
            else:
                params['registration_number'] = self.registration_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdAmlriskQueryModel()
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'event_id' in d:
            o.event_id = d['event_id']
        if 'individual_list' in d:
            o.individual_list = d['individual_list']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'registered_address' in d:
            o.registered_address = d['registered_address']
        if 'registration_number' in d:
            o.registration_number = d['registration_number']
        return o


