#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportChargerChargerbindinfoSyncModel(object):

    def __init__(self):
        self._bind_qrcode = None
        self._bind_status = None
        self._bind_time = None
        self._connector_type = None
        self._current_output_type = None
        self._equip_id = None
        self._equip_imei = None
        self._equip_name = None
        self._equip_sn = None
        self._equip_status = None
        self._equip_type_no = None
        self._operator_id = None
        self._operator_uid = None
        self._rated_current = None
        self._rated_power = None
        self._rated_voltage = None
        self._unbind_time = None

    @property
    def bind_qrcode(self):
        return self._bind_qrcode

    @bind_qrcode.setter
    def bind_qrcode(self, value):
        self._bind_qrcode = value
    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def bind_time(self):
        return self._bind_time

    @bind_time.setter
    def bind_time(self, value):
        self._bind_time = value
    @property
    def connector_type(self):
        return self._connector_type

    @connector_type.setter
    def connector_type(self, value):
        self._connector_type = value
    @property
    def current_output_type(self):
        return self._current_output_type

    @current_output_type.setter
    def current_output_type(self, value):
        self._current_output_type = value
    @property
    def equip_id(self):
        return self._equip_id

    @equip_id.setter
    def equip_id(self, value):
        self._equip_id = value
    @property
    def equip_imei(self):
        return self._equip_imei

    @equip_imei.setter
    def equip_imei(self, value):
        self._equip_imei = value
    @property
    def equip_name(self):
        return self._equip_name

    @equip_name.setter
    def equip_name(self, value):
        self._equip_name = value
    @property
    def equip_sn(self):
        return self._equip_sn

    @equip_sn.setter
    def equip_sn(self, value):
        self._equip_sn = value
    @property
    def equip_status(self):
        return self._equip_status

    @equip_status.setter
    def equip_status(self, value):
        self._equip_status = value
    @property
    def equip_type_no(self):
        return self._equip_type_no

    @equip_type_no.setter
    def equip_type_no(self, value):
        self._equip_type_no = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_uid(self):
        return self._operator_uid

    @operator_uid.setter
    def operator_uid(self, value):
        self._operator_uid = value
    @property
    def rated_current(self):
        return self._rated_current

    @rated_current.setter
    def rated_current(self, value):
        self._rated_current = value
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
    def unbind_time(self):
        return self._unbind_time

    @unbind_time.setter
    def unbind_time(self, value):
        self._unbind_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_qrcode:
            if hasattr(self.bind_qrcode, 'to_alipay_dict'):
                params['bind_qrcode'] = self.bind_qrcode.to_alipay_dict()
            else:
                params['bind_qrcode'] = self.bind_qrcode
        if self.bind_status:
            if hasattr(self.bind_status, 'to_alipay_dict'):
                params['bind_status'] = self.bind_status.to_alipay_dict()
            else:
                params['bind_status'] = self.bind_status
        if self.bind_time:
            if hasattr(self.bind_time, 'to_alipay_dict'):
                params['bind_time'] = self.bind_time.to_alipay_dict()
            else:
                params['bind_time'] = self.bind_time
        if self.connector_type:
            if hasattr(self.connector_type, 'to_alipay_dict'):
                params['connector_type'] = self.connector_type.to_alipay_dict()
            else:
                params['connector_type'] = self.connector_type
        if self.current_output_type:
            if hasattr(self.current_output_type, 'to_alipay_dict'):
                params['current_output_type'] = self.current_output_type.to_alipay_dict()
            else:
                params['current_output_type'] = self.current_output_type
        if self.equip_id:
            if hasattr(self.equip_id, 'to_alipay_dict'):
                params['equip_id'] = self.equip_id.to_alipay_dict()
            else:
                params['equip_id'] = self.equip_id
        if self.equip_imei:
            if hasattr(self.equip_imei, 'to_alipay_dict'):
                params['equip_imei'] = self.equip_imei.to_alipay_dict()
            else:
                params['equip_imei'] = self.equip_imei
        if self.equip_name:
            if hasattr(self.equip_name, 'to_alipay_dict'):
                params['equip_name'] = self.equip_name.to_alipay_dict()
            else:
                params['equip_name'] = self.equip_name
        if self.equip_sn:
            if hasattr(self.equip_sn, 'to_alipay_dict'):
                params['equip_sn'] = self.equip_sn.to_alipay_dict()
            else:
                params['equip_sn'] = self.equip_sn
        if self.equip_status:
            if hasattr(self.equip_status, 'to_alipay_dict'):
                params['equip_status'] = self.equip_status.to_alipay_dict()
            else:
                params['equip_status'] = self.equip_status
        if self.equip_type_no:
            if hasattr(self.equip_type_no, 'to_alipay_dict'):
                params['equip_type_no'] = self.equip_type_no.to_alipay_dict()
            else:
                params['equip_type_no'] = self.equip_type_no
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_uid:
            if hasattr(self.operator_uid, 'to_alipay_dict'):
                params['operator_uid'] = self.operator_uid.to_alipay_dict()
            else:
                params['operator_uid'] = self.operator_uid
        if self.rated_current:
            if hasattr(self.rated_current, 'to_alipay_dict'):
                params['rated_current'] = self.rated_current.to_alipay_dict()
            else:
                params['rated_current'] = self.rated_current
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
        if self.unbind_time:
            if hasattr(self.unbind_time, 'to_alipay_dict'):
                params['unbind_time'] = self.unbind_time.to_alipay_dict()
            else:
                params['unbind_time'] = self.unbind_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerChargerbindinfoSyncModel()
        if 'bind_qrcode' in d:
            o.bind_qrcode = d['bind_qrcode']
        if 'bind_status' in d:
            o.bind_status = d['bind_status']
        if 'bind_time' in d:
            o.bind_time = d['bind_time']
        if 'connector_type' in d:
            o.connector_type = d['connector_type']
        if 'current_output_type' in d:
            o.current_output_type = d['current_output_type']
        if 'equip_id' in d:
            o.equip_id = d['equip_id']
        if 'equip_imei' in d:
            o.equip_imei = d['equip_imei']
        if 'equip_name' in d:
            o.equip_name = d['equip_name']
        if 'equip_sn' in d:
            o.equip_sn = d['equip_sn']
        if 'equip_status' in d:
            o.equip_status = d['equip_status']
        if 'equip_type_no' in d:
            o.equip_type_no = d['equip_type_no']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_uid' in d:
            o.operator_uid = d['operator_uid']
        if 'rated_current' in d:
            o.rated_current = d['rated_current']
        if 'rated_power' in d:
            o.rated_power = d['rated_power']
        if 'rated_voltage' in d:
            o.rated_voltage = d['rated_voltage']
        if 'unbind_time' in d:
            o.unbind_time = d['unbind_time']
        return o


