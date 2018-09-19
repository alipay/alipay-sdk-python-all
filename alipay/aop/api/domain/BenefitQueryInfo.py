#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitQueryInfo(object):

    def __init__(self):
        self._benefit_desc = None
        self._benefit_name = None
        self._beneft_price = None
        self._end_time = None
        self._other_infos = None
        self._person_limit = None
        self._start_time = None
        self._total_quantity = None

    @property
    def benefit_desc(self):
        return self._benefit_desc

    @benefit_desc.setter
    def benefit_desc(self, value):
        self._benefit_desc = value
    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def beneft_price(self):
        return self._beneft_price

    @beneft_price.setter
    def beneft_price(self, value):
        self._beneft_price = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def other_infos(self):
        return self._other_infos

    @other_infos.setter
    def other_infos(self, value):
        self._other_infos = value
    @property
    def person_limit(self):
        return self._person_limit

    @person_limit.setter
    def person_limit(self, value):
        self._person_limit = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def total_quantity(self):
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, value):
        self._total_quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_desc:
            if hasattr(self.benefit_desc, 'to_alipay_dict'):
                params['benefit_desc'] = self.benefit_desc.to_alipay_dict()
            else:
                params['benefit_desc'] = self.benefit_desc
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.beneft_price:
            if hasattr(self.beneft_price, 'to_alipay_dict'):
                params['beneft_price'] = self.beneft_price.to_alipay_dict()
            else:
                params['beneft_price'] = self.beneft_price
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.other_infos:
            if hasattr(self.other_infos, 'to_alipay_dict'):
                params['other_infos'] = self.other_infos.to_alipay_dict()
            else:
                params['other_infos'] = self.other_infos
        if self.person_limit:
            if hasattr(self.person_limit, 'to_alipay_dict'):
                params['person_limit'] = self.person_limit.to_alipay_dict()
            else:
                params['person_limit'] = self.person_limit
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.total_quantity:
            if hasattr(self.total_quantity, 'to_alipay_dict'):
                params['total_quantity'] = self.total_quantity.to_alipay_dict()
            else:
                params['total_quantity'] = self.total_quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitQueryInfo()
        if 'benefit_desc' in d:
            o.benefit_desc = d['benefit_desc']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'beneft_price' in d:
            o.beneft_price = d['beneft_price']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'other_infos' in d:
            o.other_infos = d['other_infos']
        if 'person_limit' in d:
            o.person_limit = d['person_limit']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'total_quantity' in d:
            o.total_quantity = d['total_quantity']
        return o


