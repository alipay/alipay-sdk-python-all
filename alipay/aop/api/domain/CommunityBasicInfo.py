#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommunityBasicInfo(object):

    def __init__(self):
        self._building_type = None
        self._complete_date = None
        self._development_enterprise = None
        self._electricity_type = None
        self._gas_cost = None
        self._greening_rate = None
        self._heating_cost = None
        self._heating_type = None
        self._management_company = None
        self._management_mobile = None
        self._parking_cost = None
        self._parking_number = None
        self._plot_ratio = None
        self._police_station_mobile = None
        self._police_station_name = None
        self._transaction_ownership = None
        self._water_type = None

    @property
    def building_type(self):
        return self._building_type

    @building_type.setter
    def building_type(self, value):
        self._building_type = value
    @property
    def complete_date(self):
        return self._complete_date

    @complete_date.setter
    def complete_date(self, value):
        self._complete_date = value
    @property
    def development_enterprise(self):
        return self._development_enterprise

    @development_enterprise.setter
    def development_enterprise(self, value):
        self._development_enterprise = value
    @property
    def electricity_type(self):
        return self._electricity_type

    @electricity_type.setter
    def electricity_type(self, value):
        self._electricity_type = value
    @property
    def gas_cost(self):
        return self._gas_cost

    @gas_cost.setter
    def gas_cost(self, value):
        self._gas_cost = value
    @property
    def greening_rate(self):
        return self._greening_rate

    @greening_rate.setter
    def greening_rate(self, value):
        self._greening_rate = value
    @property
    def heating_cost(self):
        return self._heating_cost

    @heating_cost.setter
    def heating_cost(self, value):
        self._heating_cost = value
    @property
    def heating_type(self):
        return self._heating_type

    @heating_type.setter
    def heating_type(self, value):
        self._heating_type = value
    @property
    def management_company(self):
        return self._management_company

    @management_company.setter
    def management_company(self, value):
        self._management_company = value
    @property
    def management_mobile(self):
        return self._management_mobile

    @management_mobile.setter
    def management_mobile(self, value):
        self._management_mobile = value
    @property
    def parking_cost(self):
        return self._parking_cost

    @parking_cost.setter
    def parking_cost(self, value):
        self._parking_cost = value
    @property
    def parking_number(self):
        return self._parking_number

    @parking_number.setter
    def parking_number(self, value):
        self._parking_number = value
    @property
    def plot_ratio(self):
        return self._plot_ratio

    @plot_ratio.setter
    def plot_ratio(self, value):
        self._plot_ratio = value
    @property
    def police_station_mobile(self):
        return self._police_station_mobile

    @police_station_mobile.setter
    def police_station_mobile(self, value):
        self._police_station_mobile = value
    @property
    def police_station_name(self):
        return self._police_station_name

    @police_station_name.setter
    def police_station_name(self, value):
        self._police_station_name = value
    @property
    def transaction_ownership(self):
        return self._transaction_ownership

    @transaction_ownership.setter
    def transaction_ownership(self, value):
        self._transaction_ownership = value
    @property
    def water_type(self):
        return self._water_type

    @water_type.setter
    def water_type(self, value):
        self._water_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.building_type:
            if hasattr(self.building_type, 'to_alipay_dict'):
                params['building_type'] = self.building_type.to_alipay_dict()
            else:
                params['building_type'] = self.building_type
        if self.complete_date:
            if hasattr(self.complete_date, 'to_alipay_dict'):
                params['complete_date'] = self.complete_date.to_alipay_dict()
            else:
                params['complete_date'] = self.complete_date
        if self.development_enterprise:
            if hasattr(self.development_enterprise, 'to_alipay_dict'):
                params['development_enterprise'] = self.development_enterprise.to_alipay_dict()
            else:
                params['development_enterprise'] = self.development_enterprise
        if self.electricity_type:
            if hasattr(self.electricity_type, 'to_alipay_dict'):
                params['electricity_type'] = self.electricity_type.to_alipay_dict()
            else:
                params['electricity_type'] = self.electricity_type
        if self.gas_cost:
            if hasattr(self.gas_cost, 'to_alipay_dict'):
                params['gas_cost'] = self.gas_cost.to_alipay_dict()
            else:
                params['gas_cost'] = self.gas_cost
        if self.greening_rate:
            if hasattr(self.greening_rate, 'to_alipay_dict'):
                params['greening_rate'] = self.greening_rate.to_alipay_dict()
            else:
                params['greening_rate'] = self.greening_rate
        if self.heating_cost:
            if hasattr(self.heating_cost, 'to_alipay_dict'):
                params['heating_cost'] = self.heating_cost.to_alipay_dict()
            else:
                params['heating_cost'] = self.heating_cost
        if self.heating_type:
            if hasattr(self.heating_type, 'to_alipay_dict'):
                params['heating_type'] = self.heating_type.to_alipay_dict()
            else:
                params['heating_type'] = self.heating_type
        if self.management_company:
            if hasattr(self.management_company, 'to_alipay_dict'):
                params['management_company'] = self.management_company.to_alipay_dict()
            else:
                params['management_company'] = self.management_company
        if self.management_mobile:
            if hasattr(self.management_mobile, 'to_alipay_dict'):
                params['management_mobile'] = self.management_mobile.to_alipay_dict()
            else:
                params['management_mobile'] = self.management_mobile
        if self.parking_cost:
            if hasattr(self.parking_cost, 'to_alipay_dict'):
                params['parking_cost'] = self.parking_cost.to_alipay_dict()
            else:
                params['parking_cost'] = self.parking_cost
        if self.parking_number:
            if hasattr(self.parking_number, 'to_alipay_dict'):
                params['parking_number'] = self.parking_number.to_alipay_dict()
            else:
                params['parking_number'] = self.parking_number
        if self.plot_ratio:
            if hasattr(self.plot_ratio, 'to_alipay_dict'):
                params['plot_ratio'] = self.plot_ratio.to_alipay_dict()
            else:
                params['plot_ratio'] = self.plot_ratio
        if self.police_station_mobile:
            if hasattr(self.police_station_mobile, 'to_alipay_dict'):
                params['police_station_mobile'] = self.police_station_mobile.to_alipay_dict()
            else:
                params['police_station_mobile'] = self.police_station_mobile
        if self.police_station_name:
            if hasattr(self.police_station_name, 'to_alipay_dict'):
                params['police_station_name'] = self.police_station_name.to_alipay_dict()
            else:
                params['police_station_name'] = self.police_station_name
        if self.transaction_ownership:
            if hasattr(self.transaction_ownership, 'to_alipay_dict'):
                params['transaction_ownership'] = self.transaction_ownership.to_alipay_dict()
            else:
                params['transaction_ownership'] = self.transaction_ownership
        if self.water_type:
            if hasattr(self.water_type, 'to_alipay_dict'):
                params['water_type'] = self.water_type.to_alipay_dict()
            else:
                params['water_type'] = self.water_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommunityBasicInfo()
        if 'building_type' in d:
            o.building_type = d['building_type']
        if 'complete_date' in d:
            o.complete_date = d['complete_date']
        if 'development_enterprise' in d:
            o.development_enterprise = d['development_enterprise']
        if 'electricity_type' in d:
            o.electricity_type = d['electricity_type']
        if 'gas_cost' in d:
            o.gas_cost = d['gas_cost']
        if 'greening_rate' in d:
            o.greening_rate = d['greening_rate']
        if 'heating_cost' in d:
            o.heating_cost = d['heating_cost']
        if 'heating_type' in d:
            o.heating_type = d['heating_type']
        if 'management_company' in d:
            o.management_company = d['management_company']
        if 'management_mobile' in d:
            o.management_mobile = d['management_mobile']
        if 'parking_cost' in d:
            o.parking_cost = d['parking_cost']
        if 'parking_number' in d:
            o.parking_number = d['parking_number']
        if 'plot_ratio' in d:
            o.plot_ratio = d['plot_ratio']
        if 'police_station_mobile' in d:
            o.police_station_mobile = d['police_station_mobile']
        if 'police_station_name' in d:
            o.police_station_name = d['police_station_name']
        if 'transaction_ownership' in d:
            o.transaction_ownership = d['transaction_ownership']
        if 'water_type' in d:
            o.water_type = d['water_type']
        return o


