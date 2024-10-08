#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EntityAddress import EntityAddress
from alipay.aop.api.domain.EntityEnterpriseInfo import EntityEnterpriseInfo
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo


class AnttechBlockchainFinanceEnergyDeviceCreateModel(object):

    def __init__(self):
        self._address = None
        self._adjustable = None
        self._comm_module_no = None
        self._controller_only = None
        self._device_id = None
        self._device_info = None
        self._device_name = None
        self._device_type = None
        self._manufacturer = None
        self._measurable = None
        self._operate_date = None
        self._owner_entity = None
        self._product_agreement_code = None
        self._production_model = None
        self._rated_power = None
        self._rated_voltage = None
        self._response_level = None
        self._system_id = None
        self._timeable = None

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
    def adjustable(self):
        return self._adjustable

    @adjustable.setter
    def adjustable(self, value):
        self._adjustable = value
    @property
    def comm_module_no(self):
        return self._comm_module_no

    @comm_module_no.setter
    def comm_module_no(self, value):
        self._comm_module_no = value
    @property
    def controller_only(self):
        return self._controller_only

    @controller_only.setter
    def controller_only(self, value):
        self._controller_only = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        self._device_info = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if isinstance(value, EntityEnterpriseInfo):
            self._manufacturer = value
        else:
            self._manufacturer = EntityEnterpriseInfo.from_alipay_dict(value)
    @property
    def measurable(self):
        return self._measurable

    @measurable.setter
    def measurable(self, value):
        self._measurable = value
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
    def product_agreement_code(self):
        return self._product_agreement_code

    @product_agreement_code.setter
    def product_agreement_code(self, value):
        self._product_agreement_code = value
    @property
    def production_model(self):
        return self._production_model

    @production_model.setter
    def production_model(self, value):
        self._production_model = value
    @property
    def rated_power(self):
        return self._rated_power

    @rated_power.setter
    def rated_power(self, value):
        self._rated_power = value
    @property
    def rated_voltage(self):
        return self._rated_voltage

    @rated_voltage.setter
    def rated_voltage(self, value):
        self._rated_voltage = value
    @property
    def response_level(self):
        return self._response_level

    @response_level.setter
    def response_level(self, value):
        self._response_level = value
    @property
    def system_id(self):
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        self._system_id = value
    @property
    def timeable(self):
        return self._timeable

    @timeable.setter
    def timeable(self, value):
        self._timeable = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.adjustable:
            if hasattr(self.adjustable, 'to_alipay_dict'):
                params['adjustable'] = self.adjustable.to_alipay_dict()
            else:
                params['adjustable'] = self.adjustable
        if self.comm_module_no:
            if hasattr(self.comm_module_no, 'to_alipay_dict'):
                params['comm_module_no'] = self.comm_module_no.to_alipay_dict()
            else:
                params['comm_module_no'] = self.comm_module_no
        if self.controller_only:
            if hasattr(self.controller_only, 'to_alipay_dict'):
                params['controller_only'] = self.controller_only.to_alipay_dict()
            else:
                params['controller_only'] = self.controller_only
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.manufacturer:
            if hasattr(self.manufacturer, 'to_alipay_dict'):
                params['manufacturer'] = self.manufacturer.to_alipay_dict()
            else:
                params['manufacturer'] = self.manufacturer
        if self.measurable:
            if hasattr(self.measurable, 'to_alipay_dict'):
                params['measurable'] = self.measurable.to_alipay_dict()
            else:
                params['measurable'] = self.measurable
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
        if self.product_agreement_code:
            if hasattr(self.product_agreement_code, 'to_alipay_dict'):
                params['product_agreement_code'] = self.product_agreement_code.to_alipay_dict()
            else:
                params['product_agreement_code'] = self.product_agreement_code
        if self.production_model:
            if hasattr(self.production_model, 'to_alipay_dict'):
                params['production_model'] = self.production_model.to_alipay_dict()
            else:
                params['production_model'] = self.production_model
        if self.rated_power:
            if hasattr(self.rated_power, 'to_alipay_dict'):
                params['rated_power'] = self.rated_power.to_alipay_dict()
            else:
                params['rated_power'] = self.rated_power
        if self.rated_voltage:
            if hasattr(self.rated_voltage, 'to_alipay_dict'):
                params['rated_voltage'] = self.rated_voltage.to_alipay_dict()
            else:
                params['rated_voltage'] = self.rated_voltage
        if self.response_level:
            if hasattr(self.response_level, 'to_alipay_dict'):
                params['response_level'] = self.response_level.to_alipay_dict()
            else:
                params['response_level'] = self.response_level
        if self.system_id:
            if hasattr(self.system_id, 'to_alipay_dict'):
                params['system_id'] = self.system_id.to_alipay_dict()
            else:
                params['system_id'] = self.system_id
        if self.timeable:
            if hasattr(self.timeable, 'to_alipay_dict'):
                params['timeable'] = self.timeable.to_alipay_dict()
            else:
                params['timeable'] = self.timeable
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergyDeviceCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'adjustable' in d:
            o.adjustable = d['adjustable']
        if 'comm_module_no' in d:
            o.comm_module_no = d['comm_module_no']
        if 'controller_only' in d:
            o.controller_only = d['controller_only']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'measurable' in d:
            o.measurable = d['measurable']
        if 'operate_date' in d:
            o.operate_date = d['operate_date']
        if 'owner_entity' in d:
            o.owner_entity = d['owner_entity']
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        if 'production_model' in d:
            o.production_model = d['production_model']
        if 'rated_power' in d:
            o.rated_power = d['rated_power']
        if 'rated_voltage' in d:
            o.rated_voltage = d['rated_voltage']
        if 'response_level' in d:
            o.response_level = d['response_level']
        if 'system_id' in d:
            o.system_id = d['system_id']
        if 'timeable' in d:
            o.timeable = d['timeable']
        return o


