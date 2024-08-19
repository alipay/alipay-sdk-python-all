#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrustDeviceInfo import TrustDeviceInfo
from alipay.aop.api.domain.EntityAddress import EntityAddress
from alipay.aop.api.domain.EntityEnterpriseInfo import EntityEnterpriseInfo
from alipay.aop.api.domain.EntityEnterpriseInfo import EntityEnterpriseInfo
from alipay.aop.api.domain.TrustStationInfo import TrustStationInfo
from alipay.aop.api.domain.TrustSystemInfo import TrustSystemInfo


class AnttechBlockchainFinanceEnergyEntityCreateModel(object):

    def __init__(self):
        self._contact_name = None
        self._contact_number = None
        self._device_info = None
        self._entity_address = None
        self._entity_name = None
        self._entity_type = None
        self._operate_date = None
        self._operator_enterprise = None
        self._out_entity_id = None
        self._owner_enterprise = None
        self._parent_out_entity_id = None
        self._product_agreement_code = None
        self._station_info = None
        self._system_info = None

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
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, TrustDeviceInfo):
            self._device_info = value
        else:
            self._device_info = TrustDeviceInfo.from_alipay_dict(value)
    @property
    def entity_address(self):
        return self._entity_address

    @entity_address.setter
    def entity_address(self, value):
        if isinstance(value, EntityAddress):
            self._entity_address = value
        else:
            self._entity_address = EntityAddress.from_alipay_dict(value)
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def operate_date(self):
        return self._operate_date

    @operate_date.setter
    def operate_date(self, value):
        self._operate_date = value
    @property
    def operator_enterprise(self):
        return self._operator_enterprise

    @operator_enterprise.setter
    def operator_enterprise(self, value):
        if isinstance(value, EntityEnterpriseInfo):
            self._operator_enterprise = value
        else:
            self._operator_enterprise = EntityEnterpriseInfo.from_alipay_dict(value)
    @property
    def out_entity_id(self):
        return self._out_entity_id

    @out_entity_id.setter
    def out_entity_id(self, value):
        self._out_entity_id = value
    @property
    def owner_enterprise(self):
        return self._owner_enterprise

    @owner_enterprise.setter
    def owner_enterprise(self, value):
        if isinstance(value, EntityEnterpriseInfo):
            self._owner_enterprise = value
        else:
            self._owner_enterprise = EntityEnterpriseInfo.from_alipay_dict(value)
    @property
    def parent_out_entity_id(self):
        return self._parent_out_entity_id

    @parent_out_entity_id.setter
    def parent_out_entity_id(self, value):
        self._parent_out_entity_id = value
    @property
    def product_agreement_code(self):
        return self._product_agreement_code

    @product_agreement_code.setter
    def product_agreement_code(self, value):
        self._product_agreement_code = value
    @property
    def station_info(self):
        return self._station_info

    @station_info.setter
    def station_info(self, value):
        if isinstance(value, TrustStationInfo):
            self._station_info = value
        else:
            self._station_info = TrustStationInfo.from_alipay_dict(value)
    @property
    def system_info(self):
        return self._system_info

    @system_info.setter
    def system_info(self, value):
        if isinstance(value, TrustSystemInfo):
            self._system_info = value
        else:
            self._system_info = TrustSystemInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.entity_address:
            if hasattr(self.entity_address, 'to_alipay_dict'):
                params['entity_address'] = self.entity_address.to_alipay_dict()
            else:
                params['entity_address'] = self.entity_address
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.operate_date:
            if hasattr(self.operate_date, 'to_alipay_dict'):
                params['operate_date'] = self.operate_date.to_alipay_dict()
            else:
                params['operate_date'] = self.operate_date
        if self.operator_enterprise:
            if hasattr(self.operator_enterprise, 'to_alipay_dict'):
                params['operator_enterprise'] = self.operator_enterprise.to_alipay_dict()
            else:
                params['operator_enterprise'] = self.operator_enterprise
        if self.out_entity_id:
            if hasattr(self.out_entity_id, 'to_alipay_dict'):
                params['out_entity_id'] = self.out_entity_id.to_alipay_dict()
            else:
                params['out_entity_id'] = self.out_entity_id
        if self.owner_enterprise:
            if hasattr(self.owner_enterprise, 'to_alipay_dict'):
                params['owner_enterprise'] = self.owner_enterprise.to_alipay_dict()
            else:
                params['owner_enterprise'] = self.owner_enterprise
        if self.parent_out_entity_id:
            if hasattr(self.parent_out_entity_id, 'to_alipay_dict'):
                params['parent_out_entity_id'] = self.parent_out_entity_id.to_alipay_dict()
            else:
                params['parent_out_entity_id'] = self.parent_out_entity_id
        if self.product_agreement_code:
            if hasattr(self.product_agreement_code, 'to_alipay_dict'):
                params['product_agreement_code'] = self.product_agreement_code.to_alipay_dict()
            else:
                params['product_agreement_code'] = self.product_agreement_code
        if self.station_info:
            if hasattr(self.station_info, 'to_alipay_dict'):
                params['station_info'] = self.station_info.to_alipay_dict()
            else:
                params['station_info'] = self.station_info
        if self.system_info:
            if hasattr(self.system_info, 'to_alipay_dict'):
                params['system_info'] = self.system_info.to_alipay_dict()
            else:
                params['system_info'] = self.system_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergyEntityCreateModel()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'entity_address' in d:
            o.entity_address = d['entity_address']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'operate_date' in d:
            o.operate_date = d['operate_date']
        if 'operator_enterprise' in d:
            o.operator_enterprise = d['operator_enterprise']
        if 'out_entity_id' in d:
            o.out_entity_id = d['out_entity_id']
        if 'owner_enterprise' in d:
            o.owner_enterprise = d['owner_enterprise']
        if 'parent_out_entity_id' in d:
            o.parent_out_entity_id = d['parent_out_entity_id']
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        if 'station_info' in d:
            o.station_info = d['station_info']
        if 'system_info' in d:
            o.system_info = d['system_info']
        return o


