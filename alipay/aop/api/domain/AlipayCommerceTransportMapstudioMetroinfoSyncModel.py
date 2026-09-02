#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MetroInfoObject import MetroInfoObject


class AlipayCommerceTransportMapstudioMetroinfoSyncModel(object):

    def __init__(self):
        self._city_code = None
        self._metro_info_details = None
        self._metro_month = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def metro_info_details(self):
        return self._metro_info_details

    @metro_info_details.setter
    def metro_info_details(self, value):
        if isinstance(value, list):
            self._metro_info_details = list()
            for i in value:
                if isinstance(i, MetroInfoObject):
                    self._metro_info_details.append(i)
                else:
                    self._metro_info_details.append(MetroInfoObject.from_alipay_dict(i))
    @property
    def metro_month(self):
        return self._metro_month

    @metro_month.setter
    def metro_month(self, value):
        self._metro_month = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.metro_info_details:
            if isinstance(self.metro_info_details, list):
                for i in range(0, len(self.metro_info_details)):
                    element = self.metro_info_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.metro_info_details[i] = element.to_alipay_dict()
            if hasattr(self.metro_info_details, 'to_alipay_dict'):
                params['metro_info_details'] = self.metro_info_details.to_alipay_dict()
            else:
                params['metro_info_details'] = self.metro_info_details
        if self.metro_month:
            if hasattr(self.metro_month, 'to_alipay_dict'):
                params['metro_month'] = self.metro_month.to_alipay_dict()
            else:
                params['metro_month'] = self.metro_month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportMapstudioMetroinfoSyncModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'metro_info_details' in d:
            o.metro_info_details = d['metro_info_details']
        if 'metro_month' in d:
            o.metro_month = d['metro_month']
        return o


