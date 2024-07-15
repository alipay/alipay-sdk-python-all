#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrivateChargingEquipment(object):

    def __init__(self):
        self._bind_qrcode = None
        self._connector_type = None
        self._current_output_type = None
        self._equip_id = None
        self._equip_imei_no = None
        self._equip_name = None
        self._equip_sn = None
        self._equip_type = None
        self._equip_type_no = None
        self._modes = None
        self._rated_current = None
        self._rated_power = None
        self._rated_voltage = None

    @property
    def bind_qrcode(self):
        return self._bind_qrcode

    @bind_qrcode.setter
    def bind_qrcode(self, value):
        self._bind_qrcode = value
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
    def equip_imei_no(self):
        return self._equip_imei_no

    @equip_imei_no.setter
    def equip_imei_no(self, value):
        self._equip_imei_no = value
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
    def equip_type(self):
        return self._equip_type

    @equip_type.setter
    def equip_type(self, value):
        self._equip_type = value
    @property
    def equip_type_no(self):
        return self._equip_type_no

    @equip_type_no.setter
    def equip_type_no(self, value):
        self._equip_type_no = value
    @property
    def modes(self):
        return self._modes

    @modes.setter
    def modes(self, value):
        if isinstance(value, list):
            self._modes = list()
            for i in value:
                self._modes.append(i)
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


    def to_alipay_dict(self):
        params = dict()
        if self.bind_qrcode:
            if hasattr(self.bind_qrcode, 'to_alipay_dict'):
                params['bind_qrcode'] = self.bind_qrcode.to_alipay_dict()
            else:
                params['bind_qrcode'] = self.bind_qrcode
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
        if self.equip_imei_no:
            if hasattr(self.equip_imei_no, 'to_alipay_dict'):
                params['equip_imei_no'] = self.equip_imei_no.to_alipay_dict()
            else:
                params['equip_imei_no'] = self.equip_imei_no
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
        if self.equip_type:
            if hasattr(self.equip_type, 'to_alipay_dict'):
                params['equip_type'] = self.equip_type.to_alipay_dict()
            else:
                params['equip_type'] = self.equip_type
        if self.equip_type_no:
            if hasattr(self.equip_type_no, 'to_alipay_dict'):
                params['equip_type_no'] = self.equip_type_no.to_alipay_dict()
            else:
                params['equip_type_no'] = self.equip_type_no
        if self.modes:
            if isinstance(self.modes, list):
                for i in range(0, len(self.modes)):
                    element = self.modes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.modes[i] = element.to_alipay_dict()
            if hasattr(self.modes, 'to_alipay_dict'):
                params['modes'] = self.modes.to_alipay_dict()
            else:
                params['modes'] = self.modes
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrivateChargingEquipment()
        if 'bind_qrcode' in d:
            o.bind_qrcode = d['bind_qrcode']
        if 'connector_type' in d:
            o.connector_type = d['connector_type']
        if 'current_output_type' in d:
            o.current_output_type = d['current_output_type']
        if 'equip_id' in d:
            o.equip_id = d['equip_id']
        if 'equip_imei_no' in d:
            o.equip_imei_no = d['equip_imei_no']
        if 'equip_name' in d:
            o.equip_name = d['equip_name']
        if 'equip_sn' in d:
            o.equip_sn = d['equip_sn']
        if 'equip_type' in d:
            o.equip_type = d['equip_type']
        if 'equip_type_no' in d:
            o.equip_type_no = d['equip_type_no']
        if 'modes' in d:
            o.modes = d['modes']
        if 'rated_current' in d:
            o.rated_current = d['rated_current']
        if 'rated_power' in d:
            o.rated_power = d['rated_power']
        if 'rated_voltage' in d:
            o.rated_voltage = d['rated_voltage']
        return o


