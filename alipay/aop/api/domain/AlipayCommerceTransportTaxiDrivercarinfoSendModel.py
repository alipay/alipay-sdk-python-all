#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DriverCarInfo import DriverCarInfo


class AlipayCommerceTransportTaxiDrivercarinfoSendModel(object):

    def __init__(self):
        self._driver_car_info_list = None
        self._request_time = None

    @property
    def driver_car_info_list(self):
        return self._driver_car_info_list

    @driver_car_info_list.setter
    def driver_car_info_list(self, value):
        if isinstance(value, list):
            self._driver_car_info_list = list()
            for i in value:
                if isinstance(i, DriverCarInfo):
                    self._driver_car_info_list.append(i)
                else:
                    self._driver_car_info_list.append(DriverCarInfo.from_alipay_dict(i))
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.driver_car_info_list:
            if isinstance(self.driver_car_info_list, list):
                for i in range(0, len(self.driver_car_info_list)):
                    element = self.driver_car_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.driver_car_info_list[i] = element.to_alipay_dict()
            if hasattr(self.driver_car_info_list, 'to_alipay_dict'):
                params['driver_car_info_list'] = self.driver_car_info_list.to_alipay_dict()
            else:
                params['driver_car_info_list'] = self.driver_car_info_list
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiDrivercarinfoSendModel()
        if 'driver_car_info_list' in d:
            o.driver_car_info_list = d['driver_car_info_list']
        if 'request_time' in d:
            o.request_time = d['request_time']
        return o


