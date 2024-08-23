#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferCarData import TransferCarData


class AlipayCommerceTransportCarsaleVehicleAddModel(object):

    def __init__(self):
        self._car_data = None

    @property
    def car_data(self):
        return self._car_data

    @car_data.setter
    def car_data(self, value):
        if isinstance(value, list):
            self._car_data = list()
            for i in value:
                if isinstance(i, TransferCarData):
                    self._car_data.append(i)
                else:
                    self._car_data.append(TransferCarData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.car_data:
            if isinstance(self.car_data, list):
                for i in range(0, len(self.car_data)):
                    element = self.car_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.car_data[i] = element.to_alipay_dict()
            if hasattr(self.car_data, 'to_alipay_dict'):
                params['car_data'] = self.car_data.to_alipay_dict()
            else:
                params['car_data'] = self.car_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportCarsaleVehicleAddModel()
        if 'car_data' in d:
            o.car_data = d['car_data']
        return o


