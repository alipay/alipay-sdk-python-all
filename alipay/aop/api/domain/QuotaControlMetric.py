#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QuotaControlMetric(object):

    def __init__(self):
        self._fee_item_code = None
        self._fee_item_name = None
        self._package_quota = None
        self._unit_name = None

    @property
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def fee_item_name(self):
        return self._fee_item_name

    @fee_item_name.setter
    def fee_item_name(self, value):
        self._fee_item_name = value
    @property
    def package_quota(self):
        return self._package_quota

    @package_quota.setter
    def package_quota(self, value):
        self._package_quota = value
    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        if self.fee_item_name:
            if hasattr(self.fee_item_name, 'to_alipay_dict'):
                params['fee_item_name'] = self.fee_item_name.to_alipay_dict()
            else:
                params['fee_item_name'] = self.fee_item_name
        if self.package_quota:
            if hasattr(self.package_quota, 'to_alipay_dict'):
                params['package_quota'] = self.package_quota.to_alipay_dict()
            else:
                params['package_quota'] = self.package_quota
        if self.unit_name:
            if hasattr(self.unit_name, 'to_alipay_dict'):
                params['unit_name'] = self.unit_name.to_alipay_dict()
            else:
                params['unit_name'] = self.unit_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuotaControlMetric()
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        if 'fee_item_name' in d:
            o.fee_item_name = d['fee_item_name']
        if 'package_quota' in d:
            o.package_quota = d['package_quota']
        if 'unit_name' in d:
            o.unit_name = d['unit_name']
        return o


