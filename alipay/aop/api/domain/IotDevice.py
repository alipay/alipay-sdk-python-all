#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotDevice(object):

    def __init__(self):
        self._bluetooth_mac = None
        self._control_url = None
        self._device_id = None
        self._device_name = None
        self._model_id = None
        self._sn = None
        self._wifi_mac = None

    @property
    def bluetooth_mac(self):
        return self._bluetooth_mac

    @bluetooth_mac.setter
    def bluetooth_mac(self, value):
        self._bluetooth_mac = value
    @property
    def control_url(self):
        return self._control_url

    @control_url.setter
    def control_url(self, value):
        self._control_url = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def wifi_mac(self):
        return self._wifi_mac

    @wifi_mac.setter
    def wifi_mac(self, value):
        self._wifi_mac = value


    def to_alipay_dict(self):
        params = dict()
        if self.bluetooth_mac:
            if hasattr(self.bluetooth_mac, 'to_alipay_dict'):
                params['bluetooth_mac'] = self.bluetooth_mac.to_alipay_dict()
            else:
                params['bluetooth_mac'] = self.bluetooth_mac
        if self.control_url:
            if hasattr(self.control_url, 'to_alipay_dict'):
                params['control_url'] = self.control_url.to_alipay_dict()
            else:
                params['control_url'] = self.control_url
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.wifi_mac:
            if hasattr(self.wifi_mac, 'to_alipay_dict'):
                params['wifi_mac'] = self.wifi_mac.to_alipay_dict()
            else:
                params['wifi_mac'] = self.wifi_mac
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotDevice()
        if 'bluetooth_mac' in d:
            o.bluetooth_mac = d['bluetooth_mac']
        if 'control_url' in d:
            o.control_url = d['control_url']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'sn' in d:
            o.sn = d['sn']
        if 'wifi_mac' in d:
            o.wifi_mac = d['wifi_mac']
        return o


