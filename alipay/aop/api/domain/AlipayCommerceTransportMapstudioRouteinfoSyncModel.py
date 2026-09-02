#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RouteInfoObject import RouteInfoObject


class AlipayCommerceTransportMapstudioRouteinfoSyncModel(object):

    def __init__(self):
        self._city_code = None
        self._route_info_details = None
        self._route_score_month = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def route_info_details(self):
        return self._route_info_details

    @route_info_details.setter
    def route_info_details(self, value):
        if isinstance(value, list):
            self._route_info_details = list()
            for i in value:
                if isinstance(i, RouteInfoObject):
                    self._route_info_details.append(i)
                else:
                    self._route_info_details.append(RouteInfoObject.from_alipay_dict(i))
    @property
    def route_score_month(self):
        return self._route_score_month

    @route_score_month.setter
    def route_score_month(self, value):
        self._route_score_month = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.route_info_details:
            if isinstance(self.route_info_details, list):
                for i in range(0, len(self.route_info_details)):
                    element = self.route_info_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.route_info_details[i] = element.to_alipay_dict()
            if hasattr(self.route_info_details, 'to_alipay_dict'):
                params['route_info_details'] = self.route_info_details.to_alipay_dict()
            else:
                params['route_info_details'] = self.route_info_details
        if self.route_score_month:
            if hasattr(self.route_score_month, 'to_alipay_dict'):
                params['route_score_month'] = self.route_score_month.to_alipay_dict()
            else:
                params['route_score_month'] = self.route_score_month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportMapstudioRouteinfoSyncModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'route_info_details' in d:
            o.route_info_details = d['route_info_details']
        if 'route_score_month' in d:
            o.route_score_month = d['route_score_month']
        return o


