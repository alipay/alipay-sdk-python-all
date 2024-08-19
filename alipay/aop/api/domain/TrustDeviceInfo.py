#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChargeConnectorInfo import ChargeConnectorInfo
from alipay.aop.api.domain.EntityEnterpriseInfo import EntityEnterpriseInfo


class TrustDeviceInfo(object):

    def __init__(self):
        self._adjustable = None
        self._charge_device_type = None
        self._connector_infos = None
        self._device_type = None
        self._electric_account = None
        self._electric_meter_no = None
        self._manufacturer = None
        self._operate_status = None
        self._rated_power = None

    @property
    def adjustable(self):
        return self._adjustable

    @adjustable.setter
    def adjustable(self, value):
        self._adjustable = value
    @property
    def charge_device_type(self):
        return self._charge_device_type

    @charge_device_type.setter
    def charge_device_type(self, value):
        self._charge_device_type = value
    @property
    def connector_infos(self):
        return self._connector_infos

    @connector_infos.setter
    def connector_infos(self, value):
        if isinstance(value, list):
            self._connector_infos = list()
            for i in value:
                if isinstance(i, ChargeConnectorInfo):
                    self._connector_infos.append(i)
                else:
                    self._connector_infos.append(ChargeConnectorInfo.from_alipay_dict(i))
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def electric_account(self):
        return self._electric_account

    @electric_account.setter
    def electric_account(self, value):
        self._electric_account = value
    @property
    def electric_meter_no(self):
        return self._electric_meter_no

    @electric_meter_no.setter
    def electric_meter_no(self, value):
        self._electric_meter_no = value
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
    def operate_status(self):
        return self._operate_status

    @operate_status.setter
    def operate_status(self, value):
        self._operate_status = value
    @property
    def rated_power(self):
        return self._rated_power

    @rated_power.setter
    def rated_power(self, value):
        self._rated_power = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjustable:
            if hasattr(self.adjustable, 'to_alipay_dict'):
                params['adjustable'] = self.adjustable.to_alipay_dict()
            else:
                params['adjustable'] = self.adjustable
        if self.charge_device_type:
            if hasattr(self.charge_device_type, 'to_alipay_dict'):
                params['charge_device_type'] = self.charge_device_type.to_alipay_dict()
            else:
                params['charge_device_type'] = self.charge_device_type
        if self.connector_infos:
            if isinstance(self.connector_infos, list):
                for i in range(0, len(self.connector_infos)):
                    element = self.connector_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.connector_infos[i] = element.to_alipay_dict()
            if hasattr(self.connector_infos, 'to_alipay_dict'):
                params['connector_infos'] = self.connector_infos.to_alipay_dict()
            else:
                params['connector_infos'] = self.connector_infos
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.electric_account:
            if hasattr(self.electric_account, 'to_alipay_dict'):
                params['electric_account'] = self.electric_account.to_alipay_dict()
            else:
                params['electric_account'] = self.electric_account
        if self.electric_meter_no:
            if hasattr(self.electric_meter_no, 'to_alipay_dict'):
                params['electric_meter_no'] = self.electric_meter_no.to_alipay_dict()
            else:
                params['electric_meter_no'] = self.electric_meter_no
        if self.manufacturer:
            if hasattr(self.manufacturer, 'to_alipay_dict'):
                params['manufacturer'] = self.manufacturer.to_alipay_dict()
            else:
                params['manufacturer'] = self.manufacturer
        if self.operate_status:
            if hasattr(self.operate_status, 'to_alipay_dict'):
                params['operate_status'] = self.operate_status.to_alipay_dict()
            else:
                params['operate_status'] = self.operate_status
        if self.rated_power:
            if hasattr(self.rated_power, 'to_alipay_dict'):
                params['rated_power'] = self.rated_power.to_alipay_dict()
            else:
                params['rated_power'] = self.rated_power
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrustDeviceInfo()
        if 'adjustable' in d:
            o.adjustable = d['adjustable']
        if 'charge_device_type' in d:
            o.charge_device_type = d['charge_device_type']
        if 'connector_infos' in d:
            o.connector_infos = d['connector_infos']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'electric_account' in d:
            o.electric_account = d['electric_account']
        if 'electric_meter_no' in d:
            o.electric_meter_no = d['electric_meter_no']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'operate_status' in d:
            o.operate_status = d['operate_status']
        if 'rated_power' in d:
            o.rated_power = d['rated_power']
        return o


