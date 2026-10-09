#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndustryInvoiceGasStationInfo import IndustryInvoiceGasStationInfo


class IndustryInvoiceRefinedOilGasStation(object):

    def __init__(self):
        self._gas_card_invoice_no_list = None
        self._gas_card_invoice_stage = None
        self._gas_station_list = None

    @property
    def gas_card_invoice_no_list(self):
        return self._gas_card_invoice_no_list

    @gas_card_invoice_no_list.setter
    def gas_card_invoice_no_list(self, value):
        if isinstance(value, list):
            self._gas_card_invoice_no_list = list()
            for i in value:
                self._gas_card_invoice_no_list.append(i)
    @property
    def gas_card_invoice_stage(self):
        return self._gas_card_invoice_stage

    @gas_card_invoice_stage.setter
    def gas_card_invoice_stage(self, value):
        self._gas_card_invoice_stage = value
    @property
    def gas_station_list(self):
        return self._gas_station_list

    @gas_station_list.setter
    def gas_station_list(self, value):
        if isinstance(value, list):
            self._gas_station_list = list()
            for i in value:
                if isinstance(i, IndustryInvoiceGasStationInfo):
                    self._gas_station_list.append(i)
                else:
                    self._gas_station_list.append(IndustryInvoiceGasStationInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.gas_card_invoice_no_list:
            if isinstance(self.gas_card_invoice_no_list, list):
                for i in range(0, len(self.gas_card_invoice_no_list)):
                    element = self.gas_card_invoice_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gas_card_invoice_no_list[i] = element.to_alipay_dict()
            if hasattr(self.gas_card_invoice_no_list, 'to_alipay_dict'):
                params['gas_card_invoice_no_list'] = self.gas_card_invoice_no_list.to_alipay_dict()
            else:
                params['gas_card_invoice_no_list'] = self.gas_card_invoice_no_list
        if self.gas_card_invoice_stage:
            if hasattr(self.gas_card_invoice_stage, 'to_alipay_dict'):
                params['gas_card_invoice_stage'] = self.gas_card_invoice_stage.to_alipay_dict()
            else:
                params['gas_card_invoice_stage'] = self.gas_card_invoice_stage
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
        o = IndustryInvoiceRefinedOilGasStation()
        if 'gas_card_invoice_no_list' in d:
            o.gas_card_invoice_no_list = d['gas_card_invoice_no_list']
        if 'gas_card_invoice_stage' in d:
            o.gas_card_invoice_stage = d['gas_card_invoice_stage']
        if 'gas_station_list' in d:
            o.gas_station_list = d['gas_station_list']
        return o


