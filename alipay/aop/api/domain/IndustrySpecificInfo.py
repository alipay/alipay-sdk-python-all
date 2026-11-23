#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceGasStationInfoDTO import InvoiceGasStationInfoDTO


class IndustrySpecificInfo(object):

    def __init__(self):
        self._gas_station_list = None

    @property
    def gas_station_list(self):
        return self._gas_station_list

    @gas_station_list.setter
    def gas_station_list(self, value):
        if isinstance(value, list):
            self._gas_station_list = list()
            for i in value:
                if isinstance(i, InvoiceGasStationInfoDTO):
                    self._gas_station_list.append(i)
                else:
                    self._gas_station_list.append(InvoiceGasStationInfoDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.gas_station_list:
            if isinstance(self.gas_station_list, list):
                for i in range(0, len(self.gas_station_list)):
                    element = self.gas_station_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gas_station_list[i] = element.to_alipay_dict()
            if hasattr(self.gas_station_list, 'to_alipay_dict'):
                params['gas_station_list'] = self.gas_station_list.to_alipay_dict()
            else:
                params['gas_station_list'] = self.gas_station_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustrySpecificInfo()
        if 'gas_station_list' in d:
            o.gas_station_list = d['gas_station_list']
        return o


