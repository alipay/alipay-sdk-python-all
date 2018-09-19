#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantDeviceHeartbeatUploadModel(object):

    def __init__(self):
        self._app_info = None
        self._exception_info = None
        self._extend_info = None
        self._hardware_version = None
        self._isv_app_id = None
        self._isv_pid = None
        self._isv_server_time = None
        self._lbs = None
        self._lbs_type = None
        self._mac = None
        self._manufacturer = None
        self._network_ip = None
        self._network_name = None
        self._network_type = None
        self._product = None
        self._shop_id = None
        self._sn_id = None
        self._soft_version = None
        self._sys_type = None
        self._sys_version = None
        self._time = None

    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, value):
        self._app_info = value
    @property
    def exception_info(self):
        return self._exception_info

    @exception_info.setter
    def exception_info(self, value):
        self._exception_info = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def hardware_version(self):
        return self._hardware_version

    @hardware_version.setter
    def hardware_version(self, value):
        self._hardware_version = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def isv_server_time(self):
        return self._isv_server_time

    @isv_server_time.setter
    def isv_server_time(self, value):
        self._isv_server_time = value
    @property
    def lbs(self):
        return self._lbs

    @lbs.setter
    def lbs(self, value):
        self._lbs = value
    @property
    def lbs_type(self):
        return self._lbs_type

    @lbs_type.setter
    def lbs_type(self, value):
        self._lbs_type = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    @property
    def network_ip(self):
        return self._network_ip

    @network_ip.setter
    def network_ip(self, value):
        self._network_ip = value
    @property
    def network_name(self):
        return self._network_name

    @network_name.setter
    def network_name(self, value):
        self._network_name = value
    @property
    def network_type(self):
        return self._network_type

    @network_type.setter
    def network_type(self, value):
        self._network_type = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sn_id(self):
        return self._sn_id

    @sn_id.setter
    def sn_id(self, value):
        self._sn_id = value
    @property
    def soft_version(self):
        return self._soft_version

    @soft_version.setter
    def soft_version(self, value):
        self._soft_version = value
    @property
    def sys_type(self):
        return self._sys_type

    @sys_type.setter
    def sys_type(self, value):
        self._sys_type = value
    @property
    def sys_version(self):
        return self._sys_version

    @sys_version.setter
    def sys_version(self, value):
        self._sys_version = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_info:
            if hasattr(self.app_info, 'to_alipay_dict'):
                params['app_info'] = self.app_info.to_alipay_dict()
            else:
                params['app_info'] = self.app_info
        if self.exception_info:
            if hasattr(self.exception_info, 'to_alipay_dict'):
                params['exception_info'] = self.exception_info.to_alipay_dict()
            else:
                params['exception_info'] = self.exception_info
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.hardware_version:
            if hasattr(self.hardware_version, 'to_alipay_dict'):
                params['hardware_version'] = self.hardware_version.to_alipay_dict()
            else:
                params['hardware_version'] = self.hardware_version
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.isv_server_time:
            if hasattr(self.isv_server_time, 'to_alipay_dict'):
                params['isv_server_time'] = self.isv_server_time.to_alipay_dict()
            else:
                params['isv_server_time'] = self.isv_server_time
        if self.lbs:
            if hasattr(self.lbs, 'to_alipay_dict'):
                params['lbs'] = self.lbs.to_alipay_dict()
            else:
                params['lbs'] = self.lbs
        if self.lbs_type:
            if hasattr(self.lbs_type, 'to_alipay_dict'):
                params['lbs_type'] = self.lbs_type.to_alipay_dict()
            else:
                params['lbs_type'] = self.lbs_type
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.manufacturer:
            if hasattr(self.manufacturer, 'to_alipay_dict'):
                params['manufacturer'] = self.manufacturer.to_alipay_dict()
            else:
                params['manufacturer'] = self.manufacturer
        if self.network_ip:
            if hasattr(self.network_ip, 'to_alipay_dict'):
                params['network_ip'] = self.network_ip.to_alipay_dict()
            else:
                params['network_ip'] = self.network_ip
        if self.network_name:
            if hasattr(self.network_name, 'to_alipay_dict'):
                params['network_name'] = self.network_name.to_alipay_dict()
            else:
                params['network_name'] = self.network_name
        if self.network_type:
            if hasattr(self.network_type, 'to_alipay_dict'):
                params['network_type'] = self.network_type.to_alipay_dict()
            else:
                params['network_type'] = self.network_type
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sn_id:
            if hasattr(self.sn_id, 'to_alipay_dict'):
                params['sn_id'] = self.sn_id.to_alipay_dict()
            else:
                params['sn_id'] = self.sn_id
        if self.soft_version:
            if hasattr(self.soft_version, 'to_alipay_dict'):
                params['soft_version'] = self.soft_version.to_alipay_dict()
            else:
                params['soft_version'] = self.soft_version
        if self.sys_type:
            if hasattr(self.sys_type, 'to_alipay_dict'):
                params['sys_type'] = self.sys_type.to_alipay_dict()
            else:
                params['sys_type'] = self.sys_type
        if self.sys_version:
            if hasattr(self.sys_version, 'to_alipay_dict'):
                params['sys_version'] = self.sys_version.to_alipay_dict()
            else:
                params['sys_version'] = self.sys_version
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantDeviceHeartbeatUploadModel()
        if 'app_info' in d:
            o.app_info = d['app_info']
        if 'exception_info' in d:
            o.exception_info = d['exception_info']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'hardware_version' in d:
            o.hardware_version = d['hardware_version']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'isv_server_time' in d:
            o.isv_server_time = d['isv_server_time']
        if 'lbs' in d:
            o.lbs = d['lbs']
        if 'lbs_type' in d:
            o.lbs_type = d['lbs_type']
        if 'mac' in d:
            o.mac = d['mac']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'network_ip' in d:
            o.network_ip = d['network_ip']
        if 'network_name' in d:
            o.network_name = d['network_name']
        if 'network_type' in d:
            o.network_type = d['network_type']
        if 'product' in d:
            o.product = d['product']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sn_id' in d:
            o.sn_id = d['sn_id']
        if 'soft_version' in d:
            o.soft_version = d['soft_version']
        if 'sys_type' in d:
            o.sys_type = d['sys_type']
        if 'sys_version' in d:
            o.sys_version = d['sys_version']
        if 'time' in d:
            o.time = d['time']
        return o


