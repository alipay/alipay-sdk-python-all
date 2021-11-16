#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DriverCarInfo import DriverCarInfo


class AlipayCommerceTransportTaxiDriverinfoModifyModel(object):

    def __init__(self):
        self._biz_no = None
        self._driver_car_info = None
        self._driver_user_id = None
        self._request_time = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def driver_car_info(self):
        return self._driver_car_info

    @driver_car_info.setter
    def driver_car_info(self, value):
        if isinstance(value, DriverCarInfo):
            self._driver_car_info = value
        else:
            self._driver_car_info = DriverCarInfo.from_alipay_dict(value)
    @property
    def driver_user_id(self):
        return self._driver_user_id

    @driver_user_id.setter
    def driver_user_id(self, value):
        self._driver_user_id = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.driver_car_info:
            if hasattr(self.driver_car_info, 'to_alipay_dict'):
                params['driver_car_info'] = self.driver_car_info.to_alipay_dict()
            else:
                params['driver_car_info'] = self.driver_car_info
        if self.driver_user_id:
            if hasattr(self.driver_user_id, 'to_alipay_dict'):
                params['driver_user_id'] = self.driver_user_id.to_alipay_dict()
            else:
                params['driver_user_id'] = self.driver_user_id
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
        o = AlipayCommerceTransportTaxiDriverinfoModifyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'driver_car_info' in d:
            o.driver_car_info = d['driver_car_info']
        if 'driver_user_id' in d:
            o.driver_user_id = d['driver_user_id']
        if 'request_time' in d:
            o.request_time = d['request_time']
        return o


