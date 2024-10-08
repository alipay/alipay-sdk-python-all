#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo


class AnttechBlockchainFinanceEnergySystemCreateModel(object):

    def __init__(self):
        self._adjustable = None
        self._operate_date = None
        self._owner_entity = None
        self._product_agreement_code = None
        self._rated_power_sum = None
        self._response_level = None
        self._station_id = None
        self._system_id = None
        self._system_info = None
        self._system_name = None
        self._system_status = None
        self._system_type = None

    @property
    def adjustable(self):
        return self._adjustable

    @adjustable.setter
    def adjustable(self, value):
        self._adjustable = value
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
    def rated_power_sum(self):
        return self._rated_power_sum

    @rated_power_sum.setter
    def rated_power_sum(self, value):
        self._rated_power_sum = value
    @property
    def response_level(self):
        return self._response_level

    @response_level.setter
    def response_level(self, value):
        self._response_level = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def system_id(self):
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        self._system_id = value
    @property
    def system_info(self):
        return self._system_info

    @system_info.setter
    def system_info(self, value):
        self._system_info = value
    @property
    def system_name(self):
        return self._system_name

    @system_name.setter
    def system_name(self, value):
        self._system_name = value
    @property
    def system_status(self):
        return self._system_status

    @system_status.setter
    def system_status(self, value):
        self._system_status = value
    @property
    def system_type(self):
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        self._system_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjustable:
            if hasattr(self.adjustable, 'to_alipay_dict'):
                params['adjustable'] = self.adjustable.to_alipay_dict()
            else:
                params['adjustable'] = self.adjustable
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
        if self.rated_power_sum:
            if hasattr(self.rated_power_sum, 'to_alipay_dict'):
                params['rated_power_sum'] = self.rated_power_sum.to_alipay_dict()
            else:
                params['rated_power_sum'] = self.rated_power_sum
        if self.response_level:
            if hasattr(self.response_level, 'to_alipay_dict'):
                params['response_level'] = self.response_level.to_alipay_dict()
            else:
                params['response_level'] = self.response_level
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.system_id:
            if hasattr(self.system_id, 'to_alipay_dict'):
                params['system_id'] = self.system_id.to_alipay_dict()
            else:
                params['system_id'] = self.system_id
        if self.system_info:
            if hasattr(self.system_info, 'to_alipay_dict'):
                params['system_info'] = self.system_info.to_alipay_dict()
            else:
                params['system_info'] = self.system_info
        if self.system_name:
            if hasattr(self.system_name, 'to_alipay_dict'):
                params['system_name'] = self.system_name.to_alipay_dict()
            else:
                params['system_name'] = self.system_name
        if self.system_status:
            if hasattr(self.system_status, 'to_alipay_dict'):
                params['system_status'] = self.system_status.to_alipay_dict()
            else:
                params['system_status'] = self.system_status
        if self.system_type:
            if hasattr(self.system_type, 'to_alipay_dict'):
                params['system_type'] = self.system_type.to_alipay_dict()
            else:
                params['system_type'] = self.system_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergySystemCreateModel()
        if 'adjustable' in d:
            o.adjustable = d['adjustable']
        if 'operate_date' in d:
            o.operate_date = d['operate_date']
        if 'owner_entity' in d:
            o.owner_entity = d['owner_entity']
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        if 'rated_power_sum' in d:
            o.rated_power_sum = d['rated_power_sum']
        if 'response_level' in d:
            o.response_level = d['response_level']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'system_id' in d:
            o.system_id = d['system_id']
        if 'system_info' in d:
            o.system_info = d['system_info']
        if 'system_name' in d:
            o.system_name = d['system_name']
        if 'system_status' in d:
            o.system_status = d['system_status']
        if 'system_type' in d:
            o.system_type = d['system_type']
        return o


