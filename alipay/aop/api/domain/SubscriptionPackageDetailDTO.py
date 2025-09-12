#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubscriptionPackageDetailDTO(object):

    def __init__(self):
        self._package_amount = None
        self._package_id = None
        self._package_type = None
        self._package_unit = None
        self._package_value = None

    @property
    def package_amount(self):
        return self._package_amount

    @package_amount.setter
    def package_amount(self, value):
        self._package_amount = value
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value
    @property
    def package_type(self):
        return self._package_type

    @package_type.setter
    def package_type(self, value):
        self._package_type = value
    @property
    def package_unit(self):
        return self._package_unit

    @package_unit.setter
    def package_unit(self, value):
        self._package_unit = value
    @property
    def package_value(self):
        return self._package_value

    @package_value.setter
    def package_value(self, value):
        self._package_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.package_amount:
            if hasattr(self.package_amount, 'to_alipay_dict'):
                params['package_amount'] = self.package_amount.to_alipay_dict()
            else:
                params['package_amount'] = self.package_amount
        if self.package_id:
            if hasattr(self.package_id, 'to_alipay_dict'):
                params['package_id'] = self.package_id.to_alipay_dict()
            else:
                params['package_id'] = self.package_id
        if self.package_type:
            if hasattr(self.package_type, 'to_alipay_dict'):
                params['package_type'] = self.package_type.to_alipay_dict()
            else:
                params['package_type'] = self.package_type
        if self.package_unit:
            if hasattr(self.package_unit, 'to_alipay_dict'):
                params['package_unit'] = self.package_unit.to_alipay_dict()
            else:
                params['package_unit'] = self.package_unit
        if self.package_value:
            if hasattr(self.package_value, 'to_alipay_dict'):
                params['package_value'] = self.package_value.to_alipay_dict()
            else:
                params['package_value'] = self.package_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscriptionPackageDetailDTO()
        if 'package_amount' in d:
            o.package_amount = d['package_amount']
        if 'package_id' in d:
            o.package_id = d['package_id']
        if 'package_type' in d:
            o.package_type = d['package_type']
        if 'package_unit' in d:
            o.package_unit = d['package_unit']
        if 'package_value' in d:
            o.package_value = d['package_value']
        return o


