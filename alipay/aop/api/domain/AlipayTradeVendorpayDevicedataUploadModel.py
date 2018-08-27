#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeVendorpayDevicedataUploadModel(object):

    def __init__(self):
        self._app_package_name = None
        self._ext_info = None
        self._imei = None
        self._imsi = None
        self._mac = None
        self._machine_type = None
        self._phone_sys_version = None
        self._public_key = None
        self._tidsource = None
        self._uuid = None
        self._vendor = None

    @property
    def app_package_name(self):
        return self._app_package_name

    @app_package_name.setter
    def app_package_name(self, value):
        self._app_package_name = value
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
    def imsi(self):
        return self._imsi

    @imsi.setter
    def imsi(self, value):
        self._imsi = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def machine_type(self):
        return self._machine_type

    @machine_type.setter
    def machine_type(self, value):
        self._machine_type = value
    @property
    def phone_sys_version(self):
        return self._phone_sys_version

    @phone_sys_version.setter
    def phone_sys_version(self, value):
        self._phone_sys_version = value
    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        self._public_key = value
    @property
    def tidsource(self):
        return self._tidsource

    @tidsource.setter
    def tidsource(self, value):
        self._tidsource = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value
    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        self._vendor = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_package_name:
            if hasattr(self.app_package_name, 'to_alipay_dict'):
                params['app_package_name'] = self.app_package_name.to_alipay_dict()
            else:
                params['app_package_name'] = self.app_package_name
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
        if self.imsi:
            if hasattr(self.imsi, 'to_alipay_dict'):
                params['imsi'] = self.imsi.to_alipay_dict()
            else:
                params['imsi'] = self.imsi
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.machine_type:
            if hasattr(self.machine_type, 'to_alipay_dict'):
                params['machine_type'] = self.machine_type.to_alipay_dict()
            else:
                params['machine_type'] = self.machine_type
        if self.phone_sys_version:
            if hasattr(self.phone_sys_version, 'to_alipay_dict'):
                params['phone_sys_version'] = self.phone_sys_version.to_alipay_dict()
            else:
                params['phone_sys_version'] = self.phone_sys_version
        if self.public_key:
            if hasattr(self.public_key, 'to_alipay_dict'):
                params['public_key'] = self.public_key.to_alipay_dict()
            else:
                params['public_key'] = self.public_key
        if self.tidsource:
            if hasattr(self.tidsource, 'to_alipay_dict'):
                params['tidsource'] = self.tidsource.to_alipay_dict()
            else:
                params['tidsource'] = self.tidsource
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        if self.vendor:
            if hasattr(self.vendor, 'to_alipay_dict'):
                params['vendor'] = self.vendor.to_alipay_dict()
            else:
                params['vendor'] = self.vendor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeVendorpayDevicedataUploadModel()
        if 'app_package_name' in d:
            o.app_package_name = d['app_package_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'imei' in d:
            o.imei = d['imei']
        if 'imsi' in d:
            o.imsi = d['imsi']
        if 'mac' in d:
            o.mac = d['mac']
        if 'machine_type' in d:
            o.machine_type = d['machine_type']
        if 'phone_sys_version' in d:
            o.phone_sys_version = d['phone_sys_version']
        if 'public_key' in d:
            o.public_key = d['public_key']
        if 'tidsource' in d:
            o.tidsource = d['tidsource']
        if 'uuid' in d:
            o.uuid = d['uuid']
        if 'vendor' in d:
            o.vendor = d['vendor']
        return o


