#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDeviceInfo(object):

    def __init__(self):
        self._ext_info = None
        self._imei = None
        self._ip = None
        self._mac = None
        self._os_name = None
        self._os_version = None

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
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def os_name(self):
        return self._os_name

    @os_name.setter
    def os_name(self, value):
        self._os_name = value
    @property
    def os_version(self):
        return self._os_version

    @os_version.setter
    def os_version(self, value):
        self._os_version = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = self.ip.to_alipay_dict()
            else:
                params['ip'] = self.ip
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.os_name:
            if hasattr(self.os_name, 'to_alipay_dict'):
                params['os_name'] = self.os_name.to_alipay_dict()
            else:
                params['os_name'] = self.os_name
        if self.os_version:
            if hasattr(self.os_version, 'to_alipay_dict'):
                params['os_version'] = self.os_version.to_alipay_dict()
            else:
                params['os_version'] = self.os_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDeviceInfo()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'imei' in d:
            o.imei = d['imei']
        if 'ip' in d:
            o.ip = d['ip']
        if 'mac' in d:
            o.mac = d['mac']
        if 'os_name' in d:
            o.os_name = d['os_name']
        if 'os_version' in d:
            o.os_version = d['os_version']
        return o


