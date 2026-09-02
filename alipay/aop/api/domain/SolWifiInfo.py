#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SolWifiInfo(object):

    def __init__(self):
        self._cert_url = None
        self._enable_flag = None
        self._jump_url = None
        self._location_id = None
        self._location_name = None
        self._shop_id = None
        self._sms_cert_url = None
        self._spi_client_id = None
        self._wifi_bssid = None
        self._wifi_cipher = None
        self._wifi_id = None
        self._wifi_name = None
        self._wifi_type = None

    @property
    def cert_url(self):
        return self._cert_url

    @cert_url.setter
    def cert_url(self, value):
        self._cert_url = value
    @property
    def enable_flag(self):
        return self._enable_flag

    @enable_flag.setter
    def enable_flag(self, value):
        self._enable_flag = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def location_id(self):
        return self._location_id

    @location_id.setter
    def location_id(self, value):
        self._location_id = value
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sms_cert_url(self):
        return self._sms_cert_url

    @sms_cert_url.setter
    def sms_cert_url(self, value):
        self._sms_cert_url = value
    @property
    def spi_client_id(self):
        return self._spi_client_id

    @spi_client_id.setter
    def spi_client_id(self, value):
        self._spi_client_id = value
    @property
    def wifi_bssid(self):
        return self._wifi_bssid

    @wifi_bssid.setter
    def wifi_bssid(self, value):
        self._wifi_bssid = value
    @property
    def wifi_cipher(self):
        return self._wifi_cipher

    @wifi_cipher.setter
    def wifi_cipher(self, value):
        self._wifi_cipher = value
    @property
    def wifi_id(self):
        return self._wifi_id

    @wifi_id.setter
    def wifi_id(self, value):
        self._wifi_id = value
    @property
    def wifi_name(self):
        return self._wifi_name

    @wifi_name.setter
    def wifi_name(self, value):
        self._wifi_name = value
    @property
    def wifi_type(self):
        return self._wifi_type

    @wifi_type.setter
    def wifi_type(self, value):
        self._wifi_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_url:
            if hasattr(self.cert_url, 'to_alipay_dict'):
                params['cert_url'] = self.cert_url.to_alipay_dict()
            else:
                params['cert_url'] = self.cert_url
        if self.enable_flag:
            if hasattr(self.enable_flag, 'to_alipay_dict'):
                params['enable_flag'] = self.enable_flag.to_alipay_dict()
            else:
                params['enable_flag'] = self.enable_flag
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.location_id:
            if hasattr(self.location_id, 'to_alipay_dict'):
                params['location_id'] = self.location_id.to_alipay_dict()
            else:
                params['location_id'] = self.location_id
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sms_cert_url:
            if hasattr(self.sms_cert_url, 'to_alipay_dict'):
                params['sms_cert_url'] = self.sms_cert_url.to_alipay_dict()
            else:
                params['sms_cert_url'] = self.sms_cert_url
        if self.spi_client_id:
            if hasattr(self.spi_client_id, 'to_alipay_dict'):
                params['spi_client_id'] = self.spi_client_id.to_alipay_dict()
            else:
                params['spi_client_id'] = self.spi_client_id
        if self.wifi_bssid:
            if hasattr(self.wifi_bssid, 'to_alipay_dict'):
                params['wifi_bssid'] = self.wifi_bssid.to_alipay_dict()
            else:
                params['wifi_bssid'] = self.wifi_bssid
        if self.wifi_cipher:
            if hasattr(self.wifi_cipher, 'to_alipay_dict'):
                params['wifi_cipher'] = self.wifi_cipher.to_alipay_dict()
            else:
                params['wifi_cipher'] = self.wifi_cipher
        if self.wifi_id:
            if hasattr(self.wifi_id, 'to_alipay_dict'):
                params['wifi_id'] = self.wifi_id.to_alipay_dict()
            else:
                params['wifi_id'] = self.wifi_id
        if self.wifi_name:
            if hasattr(self.wifi_name, 'to_alipay_dict'):
                params['wifi_name'] = self.wifi_name.to_alipay_dict()
            else:
                params['wifi_name'] = self.wifi_name
        if self.wifi_type:
            if hasattr(self.wifi_type, 'to_alipay_dict'):
                params['wifi_type'] = self.wifi_type.to_alipay_dict()
            else:
                params['wifi_type'] = self.wifi_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SolWifiInfo()
        if 'cert_url' in d:
            o.cert_url = d['cert_url']
        if 'enable_flag' in d:
            o.enable_flag = d['enable_flag']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'location_id' in d:
            o.location_id = d['location_id']
        if 'location_name' in d:
            o.location_name = d['location_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sms_cert_url' in d:
            o.sms_cert_url = d['sms_cert_url']
        if 'spi_client_id' in d:
            o.spi_client_id = d['spi_client_id']
        if 'wifi_bssid' in d:
            o.wifi_bssid = d['wifi_bssid']
        if 'wifi_cipher' in d:
            o.wifi_cipher = d['wifi_cipher']
        if 'wifi_id' in d:
            o.wifi_id = d['wifi_id']
        if 'wifi_name' in d:
            o.wifi_name = d['wifi_name']
        if 'wifi_type' in d:
            o.wifi_type = d['wifi_type']
        return o


