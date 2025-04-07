#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryPoint import DeliveryPoint
from alipay.aop.api.domain.DistanceMarkupRuleDTO import DistanceMarkupRuleDTO
from alipay.aop.api.domain.TimeMarkupRuleDTO import TimeMarkupRuleDTO


class Delivery(object):

    def __init__(self):
        self._app_delivery_code = None
        self._delivery_point_list = None
        self._delivery_price = None
        self._delivery_radius = None
        self._distance_markup_rule_list = None
        self._distance_markup_state = None
        self._start_price = None
        self._time_markup_rule_list = None
        self._time_markup_state = None
        self._times_name = None

    @property
    def app_delivery_code(self):
        return self._app_delivery_code

    @app_delivery_code.setter
    def app_delivery_code(self, value):
        self._app_delivery_code = value
    @property
    def delivery_point_list(self):
        return self._delivery_point_list

    @delivery_point_list.setter
    def delivery_point_list(self, value):
        if isinstance(value, list):
            self._delivery_point_list = list()
            for i in value:
                if isinstance(i, DeliveryPoint):
                    self._delivery_point_list.append(i)
                else:
                    self._delivery_point_list.append(DeliveryPoint.from_alipay_dict(i))
    @property
    def delivery_price(self):
        return self._delivery_price

    @delivery_price.setter
    def delivery_price(self, value):
        self._delivery_price = value
    @property
    def delivery_radius(self):
        return self._delivery_radius

    @delivery_radius.setter
    def delivery_radius(self, value):
        self._delivery_radius = value
    @property
    def distance_markup_rule_list(self):
        return self._distance_markup_rule_list

    @distance_markup_rule_list.setter
    def distance_markup_rule_list(self, value):
        if isinstance(value, list):
            self._distance_markup_rule_list = list()
            for i in value:
                if isinstance(i, DistanceMarkupRuleDTO):
                    self._distance_markup_rule_list.append(i)
                else:
                    self._distance_markup_rule_list.append(DistanceMarkupRuleDTO.from_alipay_dict(i))
    @property
    def distance_markup_state(self):
        return self._distance_markup_state

    @distance_markup_state.setter
    def distance_markup_state(self, value):
        self._distance_markup_state = value
    @property
    def start_price(self):
        return self._start_price

    @start_price.setter
    def start_price(self, value):
        self._start_price = value
    @property
    def time_markup_rule_list(self):
        return self._time_markup_rule_list

    @time_markup_rule_list.setter
    def time_markup_rule_list(self, value):
        if isinstance(value, list):
            self._time_markup_rule_list = list()
            for i in value:
                if isinstance(i, TimeMarkupRuleDTO):
                    self._time_markup_rule_list.append(i)
                else:
                    self._time_markup_rule_list.append(TimeMarkupRuleDTO.from_alipay_dict(i))
    @property
    def time_markup_state(self):
        return self._time_markup_state

    @time_markup_state.setter
    def time_markup_state(self, value):
        self._time_markup_state = value
    @property
    def times_name(self):
        return self._times_name

    @times_name.setter
    def times_name(self, value):
        self._times_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_delivery_code:
            if hasattr(self.app_delivery_code, 'to_alipay_dict'):
                params['app_delivery_code'] = self.app_delivery_code.to_alipay_dict()
            else:
                params['app_delivery_code'] = self.app_delivery_code
        if self.delivery_point_list:
            if isinstance(self.delivery_point_list, list):
                for i in range(0, len(self.delivery_point_list)):
                    element = self.delivery_point_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_point_list[i] = element.to_alipay_dict()
            if hasattr(self.delivery_point_list, 'to_alipay_dict'):
                params['delivery_point_list'] = self.delivery_point_list.to_alipay_dict()
            else:
                params['delivery_point_list'] = self.delivery_point_list
        if self.delivery_price:
            if hasattr(self.delivery_price, 'to_alipay_dict'):
                params['delivery_price'] = self.delivery_price.to_alipay_dict()
            else:
                params['delivery_price'] = self.delivery_price
        if self.delivery_radius:
            if hasattr(self.delivery_radius, 'to_alipay_dict'):
                params['delivery_radius'] = self.delivery_radius.to_alipay_dict()
            else:
                params['delivery_radius'] = self.delivery_radius
        if self.distance_markup_rule_list:
            if isinstance(self.distance_markup_rule_list, list):
                for i in range(0, len(self.distance_markup_rule_list)):
                    element = self.distance_markup_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.distance_markup_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.distance_markup_rule_list, 'to_alipay_dict'):
                params['distance_markup_rule_list'] = self.distance_markup_rule_list.to_alipay_dict()
            else:
                params['distance_markup_rule_list'] = self.distance_markup_rule_list
        if self.distance_markup_state:
            if hasattr(self.distance_markup_state, 'to_alipay_dict'):
                params['distance_markup_state'] = self.distance_markup_state.to_alipay_dict()
            else:
                params['distance_markup_state'] = self.distance_markup_state
        if self.start_price:
            if hasattr(self.start_price, 'to_alipay_dict'):
                params['start_price'] = self.start_price.to_alipay_dict()
            else:
                params['start_price'] = self.start_price
        if self.time_markup_rule_list:
            if isinstance(self.time_markup_rule_list, list):
                for i in range(0, len(self.time_markup_rule_list)):
                    element = self.time_markup_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_markup_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.time_markup_rule_list, 'to_alipay_dict'):
                params['time_markup_rule_list'] = self.time_markup_rule_list.to_alipay_dict()
            else:
                params['time_markup_rule_list'] = self.time_markup_rule_list
        if self.time_markup_state:
            if hasattr(self.time_markup_state, 'to_alipay_dict'):
                params['time_markup_state'] = self.time_markup_state.to_alipay_dict()
            else:
                params['time_markup_state'] = self.time_markup_state
        if self.times_name:
            if hasattr(self.times_name, 'to_alipay_dict'):
                params['times_name'] = self.times_name.to_alipay_dict()
            else:
                params['times_name'] = self.times_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Delivery()
        if 'app_delivery_code' in d:
            o.app_delivery_code = d['app_delivery_code']
        if 'delivery_point_list' in d:
            o.delivery_point_list = d['delivery_point_list']
        if 'delivery_price' in d:
            o.delivery_price = d['delivery_price']
        if 'delivery_radius' in d:
            o.delivery_radius = d['delivery_radius']
        if 'distance_markup_rule_list' in d:
            o.distance_markup_rule_list = d['distance_markup_rule_list']
        if 'distance_markup_state' in d:
            o.distance_markup_state = d['distance_markup_state']
        if 'start_price' in d:
            o.start_price = d['start_price']
        if 'time_markup_rule_list' in d:
            o.time_markup_rule_list = d['time_markup_rule_list']
        if 'time_markup_state' in d:
            o.time_markup_state = d['time_markup_state']
        if 'times_name' in d:
            o.times_name = d['times_name']
        return o


