#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFDrugInfo(object):

    def __init__(self):
        self._approve_number = None
        self._drug_duration = None
        self._drug_duration_unit = None
        self._drug_frequency = None
        self._drug_name = None
        self._drug_quantity = None
        self._drug_quantity_unit = None
        self._drug_route = None
        self._drug_specification = None
        self._drug_taboo = None
        self._factory = None
        self._once_dosage = None
        self._once_dosage_unit = None
        self._partner_drug_id = None
        self._product_name = None
        self._rx = None
        self._take_mode = None
        self._user_time = None

    @property
    def approve_number(self):
        return self._approve_number

    @approve_number.setter
    def approve_number(self, value):
        self._approve_number = value
    @property
    def drug_duration(self):
        return self._drug_duration

    @drug_duration.setter
    def drug_duration(self, value):
        self._drug_duration = value
    @property
    def drug_duration_unit(self):
        return self._drug_duration_unit

    @drug_duration_unit.setter
    def drug_duration_unit(self, value):
        self._drug_duration_unit = value
    @property
    def drug_frequency(self):
        return self._drug_frequency

    @drug_frequency.setter
    def drug_frequency(self, value):
        self._drug_frequency = value
    @property
    def drug_name(self):
        return self._drug_name

    @drug_name.setter
    def drug_name(self, value):
        self._drug_name = value
    @property
    def drug_quantity(self):
        return self._drug_quantity

    @drug_quantity.setter
    def drug_quantity(self, value):
        self._drug_quantity = value
    @property
    def drug_quantity_unit(self):
        return self._drug_quantity_unit

    @drug_quantity_unit.setter
    def drug_quantity_unit(self, value):
        self._drug_quantity_unit = value
    @property
    def drug_route(self):
        return self._drug_route

    @drug_route.setter
    def drug_route(self, value):
        self._drug_route = value
    @property
    def drug_specification(self):
        return self._drug_specification

    @drug_specification.setter
    def drug_specification(self, value):
        self._drug_specification = value
    @property
    def drug_taboo(self):
        return self._drug_taboo

    @drug_taboo.setter
    def drug_taboo(self, value):
        self._drug_taboo = value
    @property
    def factory(self):
        return self._factory

    @factory.setter
    def factory(self, value):
        self._factory = value
    @property
    def once_dosage(self):
        return self._once_dosage

    @once_dosage.setter
    def once_dosage(self, value):
        self._once_dosage = value
    @property
    def once_dosage_unit(self):
        return self._once_dosage_unit

    @once_dosage_unit.setter
    def once_dosage_unit(self, value):
        self._once_dosage_unit = value
    @property
    def partner_drug_id(self):
        return self._partner_drug_id

    @partner_drug_id.setter
    def partner_drug_id(self, value):
        self._partner_drug_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def rx(self):
        return self._rx

    @rx.setter
    def rx(self, value):
        self._rx = value
    @property
    def take_mode(self):
        return self._take_mode

    @take_mode.setter
    def take_mode(self, value):
        self._take_mode = value
    @property
    def user_time(self):
        return self._user_time

    @user_time.setter
    def user_time(self, value):
        self._user_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.approve_number:
            if hasattr(self.approve_number, 'to_alipay_dict'):
                params['approve_number'] = self.approve_number.to_alipay_dict()
            else:
                params['approve_number'] = self.approve_number
        if self.drug_duration:
            if hasattr(self.drug_duration, 'to_alipay_dict'):
                params['drug_duration'] = self.drug_duration.to_alipay_dict()
            else:
                params['drug_duration'] = self.drug_duration
        if self.drug_duration_unit:
            if hasattr(self.drug_duration_unit, 'to_alipay_dict'):
                params['drug_duration_unit'] = self.drug_duration_unit.to_alipay_dict()
            else:
                params['drug_duration_unit'] = self.drug_duration_unit
        if self.drug_frequency:
            if hasattr(self.drug_frequency, 'to_alipay_dict'):
                params['drug_frequency'] = self.drug_frequency.to_alipay_dict()
            else:
                params['drug_frequency'] = self.drug_frequency
        if self.drug_name:
            if hasattr(self.drug_name, 'to_alipay_dict'):
                params['drug_name'] = self.drug_name.to_alipay_dict()
            else:
                params['drug_name'] = self.drug_name
        if self.drug_quantity:
            if hasattr(self.drug_quantity, 'to_alipay_dict'):
                params['drug_quantity'] = self.drug_quantity.to_alipay_dict()
            else:
                params['drug_quantity'] = self.drug_quantity
        if self.drug_quantity_unit:
            if hasattr(self.drug_quantity_unit, 'to_alipay_dict'):
                params['drug_quantity_unit'] = self.drug_quantity_unit.to_alipay_dict()
            else:
                params['drug_quantity_unit'] = self.drug_quantity_unit
        if self.drug_route:
            if hasattr(self.drug_route, 'to_alipay_dict'):
                params['drug_route'] = self.drug_route.to_alipay_dict()
            else:
                params['drug_route'] = self.drug_route
        if self.drug_specification:
            if hasattr(self.drug_specification, 'to_alipay_dict'):
                params['drug_specification'] = self.drug_specification.to_alipay_dict()
            else:
                params['drug_specification'] = self.drug_specification
        if self.drug_taboo:
            if hasattr(self.drug_taboo, 'to_alipay_dict'):
                params['drug_taboo'] = self.drug_taboo.to_alipay_dict()
            else:
                params['drug_taboo'] = self.drug_taboo
        if self.factory:
            if hasattr(self.factory, 'to_alipay_dict'):
                params['factory'] = self.factory.to_alipay_dict()
            else:
                params['factory'] = self.factory
        if self.once_dosage:
            if hasattr(self.once_dosage, 'to_alipay_dict'):
                params['once_dosage'] = self.once_dosage.to_alipay_dict()
            else:
                params['once_dosage'] = self.once_dosage
        if self.once_dosage_unit:
            if hasattr(self.once_dosage_unit, 'to_alipay_dict'):
                params['once_dosage_unit'] = self.once_dosage_unit.to_alipay_dict()
            else:
                params['once_dosage_unit'] = self.once_dosage_unit
        if self.partner_drug_id:
            if hasattr(self.partner_drug_id, 'to_alipay_dict'):
                params['partner_drug_id'] = self.partner_drug_id.to_alipay_dict()
            else:
                params['partner_drug_id'] = self.partner_drug_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.rx:
            if hasattr(self.rx, 'to_alipay_dict'):
                params['rx'] = self.rx.to_alipay_dict()
            else:
                params['rx'] = self.rx
        if self.take_mode:
            if hasattr(self.take_mode, 'to_alipay_dict'):
                params['take_mode'] = self.take_mode.to_alipay_dict()
            else:
                params['take_mode'] = self.take_mode
        if self.user_time:
            if hasattr(self.user_time, 'to_alipay_dict'):
                params['user_time'] = self.user_time.to_alipay_dict()
            else:
                params['user_time'] = self.user_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFDrugInfo()
        if 'approve_number' in d:
            o.approve_number = d['approve_number']
        if 'drug_duration' in d:
            o.drug_duration = d['drug_duration']
        if 'drug_duration_unit' in d:
            o.drug_duration_unit = d['drug_duration_unit']
        if 'drug_frequency' in d:
            o.drug_frequency = d['drug_frequency']
        if 'drug_name' in d:
            o.drug_name = d['drug_name']
        if 'drug_quantity' in d:
            o.drug_quantity = d['drug_quantity']
        if 'drug_quantity_unit' in d:
            o.drug_quantity_unit = d['drug_quantity_unit']
        if 'drug_route' in d:
            o.drug_route = d['drug_route']
        if 'drug_specification' in d:
            o.drug_specification = d['drug_specification']
        if 'drug_taboo' in d:
            o.drug_taboo = d['drug_taboo']
        if 'factory' in d:
            o.factory = d['factory']
        if 'once_dosage' in d:
            o.once_dosage = d['once_dosage']
        if 'once_dosage_unit' in d:
            o.once_dosage_unit = d['once_dosage_unit']
        if 'partner_drug_id' in d:
            o.partner_drug_id = d['partner_drug_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'rx' in d:
            o.rx = d['rx']
        if 'take_mode' in d:
            o.take_mode = d['take_mode']
        if 'user_time' in d:
            o.user_time = d['user_time']
        return o


