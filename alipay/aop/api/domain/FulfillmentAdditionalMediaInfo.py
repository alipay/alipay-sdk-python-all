#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FulfillmentAdditionalMediaInfo(object):

    def __init__(self):
        self._origin_contract_file_id = None
        self._rent_contract_type = None
        self._type = None
        self._value = None

    @property
    def origin_contract_file_id(self):
        return self._origin_contract_file_id

    @origin_contract_file_id.setter
    def origin_contract_file_id(self, value):
        self._origin_contract_file_id = value
    @property
    def rent_contract_type(self):
        return self._rent_contract_type

    @rent_contract_type.setter
    def rent_contract_type(self, value):
        self._rent_contract_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.origin_contract_file_id:
            if hasattr(self.origin_contract_file_id, 'to_alipay_dict'):
                params['origin_contract_file_id'] = self.origin_contract_file_id.to_alipay_dict()
            else:
                params['origin_contract_file_id'] = self.origin_contract_file_id
        if self.rent_contract_type:
            if hasattr(self.rent_contract_type, 'to_alipay_dict'):
                params['rent_contract_type'] = self.rent_contract_type.to_alipay_dict()
            else:
                params['rent_contract_type'] = self.rent_contract_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentAdditionalMediaInfo()
        if 'origin_contract_file_id' in d:
            o.origin_contract_file_id = d['origin_contract_file_id']
        if 'rent_contract_type' in d:
            o.rent_contract_type = d['rent_contract_type']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


