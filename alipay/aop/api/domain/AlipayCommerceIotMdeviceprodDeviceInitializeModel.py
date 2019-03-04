#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMdeviceprodDeviceInitializeModel(object):

    def __init__(self):
        self._device_sn = None
        self._ext_info = None
        self._imei = None
        self._item_id = None
        self._mac = None
        self._net_type = None
        self._os_version = None
        self._plain_text = None
        self._sign_info = None
        self._supplier_id = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def net_type(self):
        return self._net_type

    @net_type.setter
    def net_type(self, value):
        self._net_type = value
    @property
    def os_version(self):
        return self._os_version

    @os_version.setter
    def os_version(self, value):
        self._os_version = value
    @property
    def plain_text(self):
        return self._plain_text

    @plain_text.setter
    def plain_text(self, value):
        self._plain_text = value
    @property
    def sign_info(self):
        return self._sign_info

    @sign_info.setter
    def sign_info(self, value):
        self._sign_info = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.net_type:
            if hasattr(self.net_type, 'to_alipay_dict'):
                params['net_type'] = self.net_type.to_alipay_dict()
            else:
                params['net_type'] = self.net_type
        if self.os_version:
            if hasattr(self.os_version, 'to_alipay_dict'):
                params['os_version'] = self.os_version.to_alipay_dict()
            else:
                params['os_version'] = self.os_version
        if self.plain_text:
            if hasattr(self.plain_text, 'to_alipay_dict'):
                params['plain_text'] = self.plain_text.to_alipay_dict()
            else:
                params['plain_text'] = self.plain_text
        if self.sign_info:
            if hasattr(self.sign_info, 'to_alipay_dict'):
                params['sign_info'] = self.sign_info.to_alipay_dict()
            else:
                params['sign_info'] = self.sign_info
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMdeviceprodDeviceInitializeModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'imei' in d:
            o.imei = d['imei']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mac' in d:
            o.mac = d['mac']
        if 'net_type' in d:
            o.net_type = d['net_type']
        if 'os_version' in d:
            o.os_version = d['os_version']
        if 'plain_text' in d:
            o.plain_text = d['plain_text']
        if 'sign_info' in d:
            o.sign_info = d['sign_info']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


