#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EntityAddress import EntityAddress
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo


class AnttechBlockchainFinanceEnergyStationCreateModel(object):

    def __init__(self):
        self._address = None
        self._adjustable_duration_max = None
        self._adjustable_load_max = None
        self._construction = None
        self._contact_name = None
        self._contact_number = None
        self._demand_load_max = None
        self._electric_account = None
        self._operate_date = None
        self._owner_entity = None
        self._peak_shaving_load_max = None
        self._product_agreement_code = None
        self._rated_power = None
        self._service_tel = None
        self._station_id = None
        self._station_name = None
        self._station_type = None
        self._transformer_load_max = None
        self._transformer_load_min = None
        self._valley_filling_load_max = None
        self._virtual_account = None
        self._voltage_level = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, EntityAddress):
            self._address = value
        else:
            self._address = EntityAddress.from_alipay_dict(value)
    @property
    def adjustable_duration_max(self):
        return self._adjustable_duration_max

    @adjustable_duration_max.setter
    def adjustable_duration_max(self, value):
        self._adjustable_duration_max = value
    @property
    def adjustable_load_max(self):
        return self._adjustable_load_max

    @adjustable_load_max.setter
    def adjustable_load_max(self, value):
        self._adjustable_load_max = value
    @property
    def construction(self):
        return self._construction

    @construction.setter
    def construction(self, value):
        self._construction = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def demand_load_max(self):
        return self._demand_load_max

    @demand_load_max.setter
    def demand_load_max(self, value):
        self._demand_load_max = value
    @property
    def electric_account(self):
        return self._electric_account

    @electric_account.setter
    def electric_account(self, value):
        self._electric_account = value
    @property
    def operate_date(self):
        return self._operate_date

    @operate_date.setter
    def operate_date(self, value):
        self._operate_date = value
    @property
    def owner_entity(self):
        return self._owner_entity

    @owner_entity.setter
    def owner_entity(self, value):
        if isinstance(value, TrustEntityInfo):
            self._owner_entity = value
        else:
            self._owner_entity = TrustEntityInfo.from_alipay_dict(value)
    @property
    def peak_shaving_load_max(self):
        return self._peak_shaving_load_max

    @peak_shaving_load_max.setter
    def peak_shaving_load_max(self, value):
        self._peak_shaving_load_max = value
    @property
    def product_agreement_code(self):
        return self._product_agreement_code

    @product_agreement_code.setter
    def product_agreement_code(self, value):
        self._product_agreement_code = value
    @property
    def rated_power(self):
        return self._rated_power

    @rated_power.setter
    def rated_power(self, value):
        self._rated_power = value
    @property
    def service_tel(self):
        return self._service_tel

    @service_tel.setter
    def service_tel(self, value):
        self._service_tel = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def station_type(self):
        return self._station_type

    @station_type.setter
    def station_type(self, value):
        self._station_type = value
    @property
    def transformer_load_max(self):
        return self._transformer_load_max

    @transformer_load_max.setter
    def transformer_load_max(self, value):
        self._transformer_load_max = value
    @property
    def transformer_load_min(self):
        return self._transformer_load_min

    @transformer_load_min.setter
    def transformer_load_min(self, value):
        self._transformer_load_min = value
    @property
    def valley_filling_load_max(self):
        return self._valley_filling_load_max

    @valley_filling_load_max.setter
    def valley_filling_load_max(self, value):
        self._valley_filling_load_max = value
    @property
    def virtual_account(self):
        return self._virtual_account

    @virtual_account.setter
    def virtual_account(self, value):
        self._virtual_account = value
    @property
    def voltage_level(self):
        return self._voltage_level

    @voltage_level.setter
    def voltage_level(self, value):
        self._voltage_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.adjustable_duration_max:
            if hasattr(self.adjustable_duration_max, 'to_alipay_dict'):
                params['adjustable_duration_max'] = self.adjustable_duration_max.to_alipay_dict()
            else:
                params['adjustable_duration_max'] = self.adjustable_duration_max
        if self.adjustable_load_max:
            if hasattr(self.adjustable_load_max, 'to_alipay_dict'):
                params['adjustable_load_max'] = self.adjustable_load_max.to_alipay_dict()
            else:
                params['adjustable_load_max'] = self.adjustable_load_max
        if self.construction:
            if hasattr(self.construction, 'to_alipay_dict'):
                params['construction'] = self.construction.to_alipay_dict()
            else:
                params['construction'] = self.construction
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        if self.demand_load_max:
            if hasattr(self.demand_load_max, 'to_alipay_dict'):
                params['demand_load_max'] = self.demand_load_max.to_alipay_dict()
            else:
                params['demand_load_max'] = self.demand_load_max
        if self.electric_account:
            if hasattr(self.electric_account, 'to_alipay_dict'):
                params['electric_account'] = self.electric_account.to_alipay_dict()
            else:
                params['electric_account'] = self.electric_account
        if self.operate_date:
            if hasattr(self.operate_date, 'to_alipay_dict'):
                params['operate_date'] = self.operate_date.to_alipay_dict()
            else:
                params['operate_date'] = self.operate_date
        if self.owner_entity:
            if hasattr(self.owner_entity, 'to_alipay_dict'):
                params['owner_entity'] = self.owner_entity.to_alipay_dict()
            else:
                params['owner_entity'] = self.owner_entity
        if self.peak_shaving_load_max:
            if hasattr(self.peak_shaving_load_max, 'to_alipay_dict'):
                params['peak_shaving_load_max'] = self.peak_shaving_load_max.to_alipay_dict()
            else:
                params['peak_shaving_load_max'] = self.peak_shaving_load_max
        if self.product_agreement_code:
            if hasattr(self.product_agreement_code, 'to_alipay_dict'):
                params['product_agreement_code'] = self.product_agreement_code.to_alipay_dict()
            else:
                params['product_agreement_code'] = self.product_agreement_code
        if self.rated_power:
            if hasattr(self.rated_power, 'to_alipay_dict'):
                params['rated_power'] = self.rated_power.to_alipay_dict()
            else:
                params['rated_power'] = self.rated_power
        if self.service_tel:
            if hasattr(self.service_tel, 'to_alipay_dict'):
                params['service_tel'] = self.service_tel.to_alipay_dict()
            else:
                params['service_tel'] = self.service_tel
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        if self.station_type:
            if hasattr(self.station_type, 'to_alipay_dict'):
                params['station_type'] = self.station_type.to_alipay_dict()
            else:
                params['station_type'] = self.station_type
        if self.transformer_load_max:
            if hasattr(self.transformer_load_max, 'to_alipay_dict'):
                params['transformer_load_max'] = self.transformer_load_max.to_alipay_dict()
            else:
                params['transformer_load_max'] = self.transformer_load_max
        if self.transformer_load_min:
            if hasattr(self.transformer_load_min, 'to_alipay_dict'):
                params['transformer_load_min'] = self.transformer_load_min.to_alipay_dict()
            else:
                params['transformer_load_min'] = self.transformer_load_min
        if self.valley_filling_load_max:
            if hasattr(self.valley_filling_load_max, 'to_alipay_dict'):
                params['valley_filling_load_max'] = self.valley_filling_load_max.to_alipay_dict()
            else:
                params['valley_filling_load_max'] = self.valley_filling_load_max
        if self.virtual_account:
            if hasattr(self.virtual_account, 'to_alipay_dict'):
                params['virtual_account'] = self.virtual_account.to_alipay_dict()
            else:
                params['virtual_account'] = self.virtual_account
        if self.voltage_level:
            if hasattr(self.voltage_level, 'to_alipay_dict'):
                params['voltage_level'] = self.voltage_level.to_alipay_dict()
            else:
                params['voltage_level'] = self.voltage_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergyStationCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'adjustable_duration_max' in d:
            o.adjustable_duration_max = d['adjustable_duration_max']
        if 'adjustable_load_max' in d:
            o.adjustable_load_max = d['adjustable_load_max']
        if 'construction' in d:
            o.construction = d['construction']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'demand_load_max' in d:
            o.demand_load_max = d['demand_load_max']
        if 'electric_account' in d:
            o.electric_account = d['electric_account']
        if 'operate_date' in d:
            o.operate_date = d['operate_date']
        if 'owner_entity' in d:
            o.owner_entity = d['owner_entity']
        if 'peak_shaving_load_max' in d:
            o.peak_shaving_load_max = d['peak_shaving_load_max']
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        if 'rated_power' in d:
            o.rated_power = d['rated_power']
        if 'service_tel' in d:
            o.service_tel = d['service_tel']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'station_type' in d:
            o.station_type = d['station_type']
        if 'transformer_load_max' in d:
            o.transformer_load_max = d['transformer_load_max']
        if 'transformer_load_min' in d:
            o.transformer_load_min = d['transformer_load_min']
        if 'valley_filling_load_max' in d:
            o.valley_filling_load_max = d['valley_filling_load_max']
        if 'virtual_account' in d:
            o.virtual_account = d['virtual_account']
        if 'voltage_level' in d:
            o.voltage_level = d['voltage_level']
        return o


