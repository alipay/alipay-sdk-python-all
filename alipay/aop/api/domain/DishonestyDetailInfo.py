#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DishonestyDetailInfo(object):

    def __init__(self):
        self._behavior = None
        self._case_code = None
        self._enforce_court = None
        self._id_number = None
        self._name = None
        self._performance = None
        self._publish_date = None
        self._region = None

    @property
    def behavior(self):
        return self._behavior

    @behavior.setter
    def behavior(self, value):
        self._behavior = value
    @property
    def case_code(self):
        return self._case_code

    @case_code.setter
    def case_code(self, value):
        self._case_code = value
    @property
    def enforce_court(self):
        return self._enforce_court

    @enforce_court.setter
    def enforce_court(self, value):
        self._enforce_court = value
    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def performance(self):
        return self._performance

    @performance.setter
    def performance(self, value):
        self._performance = value
    @property
    def publish_date(self):
        return self._publish_date

    @publish_date.setter
    def publish_date(self, value):
        self._publish_date = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value


    def to_alipay_dict(self):
        params = dict()
        if self.behavior:
            if hasattr(self.behavior, 'to_alipay_dict'):
                params['behavior'] = self.behavior.to_alipay_dict()
            else:
                params['behavior'] = self.behavior
        if self.case_code:
            if hasattr(self.case_code, 'to_alipay_dict'):
                params['case_code'] = self.case_code.to_alipay_dict()
            else:
                params['case_code'] = self.case_code
        if self.enforce_court:
            if hasattr(self.enforce_court, 'to_alipay_dict'):
                params['enforce_court'] = self.enforce_court.to_alipay_dict()
            else:
                params['enforce_court'] = self.enforce_court
        if self.id_number:
            if hasattr(self.id_number, 'to_alipay_dict'):
                params['id_number'] = self.id_number.to_alipay_dict()
            else:
                params['id_number'] = self.id_number
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.performance:
            if hasattr(self.performance, 'to_alipay_dict'):
                params['performance'] = self.performance.to_alipay_dict()
            else:
                params['performance'] = self.performance
        if self.publish_date:
            if hasattr(self.publish_date, 'to_alipay_dict'):
                params['publish_date'] = self.publish_date.to_alipay_dict()
            else:
                params['publish_date'] = self.publish_date
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DishonestyDetailInfo()
        if 'behavior' in d:
            o.behavior = d['behavior']
        if 'case_code' in d:
            o.case_code = d['case_code']
        if 'enforce_court' in d:
            o.enforce_court = d['enforce_court']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'name' in d:
            o.name = d['name']
        if 'performance' in d:
            o.performance = d['performance']
        if 'publish_date' in d:
            o.publish_date = d['publish_date']
        if 'region' in d:
            o.region = d['region']
        return o


