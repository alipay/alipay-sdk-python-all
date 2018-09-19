#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosDeviceInfoVO(object):

    def __init__(self):
        self._decive_software_name = None
        self._device_app_cnt = None
        self._device_app_flow = None
        self._device_app_list = None
        self._device_company_name = None
        self._device_flow = None
        self._device_ip = None
        self._device_mac = None
        self._device_os_version = None
        self._device_status = None
        self._device_type = None
        self._device_version = None
        self._gmt_activate = None
        self._gmt_login = None
        self._gmt_production = None
        self._gmt_send = None
        self._gmt_unbundling = None
        self._gmt_update = None
        self._isv_name = None
        self._isv_pid = None
        self._shop_id = None
        self._sn_no = None

    @property
    def decive_software_name(self):
        return self._decive_software_name

    @decive_software_name.setter
    def decive_software_name(self, value):
        self._decive_software_name = value
    @property
    def device_app_cnt(self):
        return self._device_app_cnt

    @device_app_cnt.setter
    def device_app_cnt(self, value):
        self._device_app_cnt = value
    @property
    def device_app_flow(self):
        return self._device_app_flow

    @device_app_flow.setter
    def device_app_flow(self, value):
        self._device_app_flow = value
    @property
    def device_app_list(self):
        return self._device_app_list

    @device_app_list.setter
    def device_app_list(self, value):
        self._device_app_list = value
    @property
    def device_company_name(self):
        return self._device_company_name

    @device_company_name.setter
    def device_company_name(self, value):
        self._device_company_name = value
    @property
    def device_flow(self):
        return self._device_flow

    @device_flow.setter
    def device_flow(self, value):
        self._device_flow = value
    @property
    def device_ip(self):
        return self._device_ip

    @device_ip.setter
    def device_ip(self, value):
        self._device_ip = value
    @property
    def device_mac(self):
        return self._device_mac

    @device_mac.setter
    def device_mac(self, value):
        self._device_mac = value
    @property
    def device_os_version(self):
        return self._device_os_version

    @device_os_version.setter
    def device_os_version(self, value):
        self._device_os_version = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def device_version(self):
        return self._device_version

    @device_version.setter
    def device_version(self, value):
        self._device_version = value
    @property
    def gmt_activate(self):
        return self._gmt_activate

    @gmt_activate.setter
    def gmt_activate(self, value):
        self._gmt_activate = value
    @property
    def gmt_login(self):
        return self._gmt_login

    @gmt_login.setter
    def gmt_login(self, value):
        self._gmt_login = value
    @property
    def gmt_production(self):
        return self._gmt_production

    @gmt_production.setter
    def gmt_production(self, value):
        self._gmt_production = value
    @property
    def gmt_send(self):
        return self._gmt_send

    @gmt_send.setter
    def gmt_send(self, value):
        self._gmt_send = value
    @property
    def gmt_unbundling(self):
        return self._gmt_unbundling

    @gmt_unbundling.setter
    def gmt_unbundling(self, value):
        self._gmt_unbundling = value
    @property
    def gmt_update(self):
        return self._gmt_update

    @gmt_update.setter
    def gmt_update(self, value):
        self._gmt_update = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sn_no(self):
        return self._sn_no

    @sn_no.setter
    def sn_no(self, value):
        self._sn_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.decive_software_name:
            if hasattr(self.decive_software_name, 'to_alipay_dict'):
                params['decive_software_name'] = self.decive_software_name.to_alipay_dict()
            else:
                params['decive_software_name'] = self.decive_software_name
        if self.device_app_cnt:
            if hasattr(self.device_app_cnt, 'to_alipay_dict'):
                params['device_app_cnt'] = self.device_app_cnt.to_alipay_dict()
            else:
                params['device_app_cnt'] = self.device_app_cnt
        if self.device_app_flow:
            if hasattr(self.device_app_flow, 'to_alipay_dict'):
                params['device_app_flow'] = self.device_app_flow.to_alipay_dict()
            else:
                params['device_app_flow'] = self.device_app_flow
        if self.device_app_list:
            if hasattr(self.device_app_list, 'to_alipay_dict'):
                params['device_app_list'] = self.device_app_list.to_alipay_dict()
            else:
                params['device_app_list'] = self.device_app_list
        if self.device_company_name:
            if hasattr(self.device_company_name, 'to_alipay_dict'):
                params['device_company_name'] = self.device_company_name.to_alipay_dict()
            else:
                params['device_company_name'] = self.device_company_name
        if self.device_flow:
            if hasattr(self.device_flow, 'to_alipay_dict'):
                params['device_flow'] = self.device_flow.to_alipay_dict()
            else:
                params['device_flow'] = self.device_flow
        if self.device_ip:
            if hasattr(self.device_ip, 'to_alipay_dict'):
                params['device_ip'] = self.device_ip.to_alipay_dict()
            else:
                params['device_ip'] = self.device_ip
        if self.device_mac:
            if hasattr(self.device_mac, 'to_alipay_dict'):
                params['device_mac'] = self.device_mac.to_alipay_dict()
            else:
                params['device_mac'] = self.device_mac
        if self.device_os_version:
            if hasattr(self.device_os_version, 'to_alipay_dict'):
                params['device_os_version'] = self.device_os_version.to_alipay_dict()
            else:
                params['device_os_version'] = self.device_os_version
        if self.device_status:
            if hasattr(self.device_status, 'to_alipay_dict'):
                params['device_status'] = self.device_status.to_alipay_dict()
            else:
                params['device_status'] = self.device_status
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.device_version:
            if hasattr(self.device_version, 'to_alipay_dict'):
                params['device_version'] = self.device_version.to_alipay_dict()
            else:
                params['device_version'] = self.device_version
        if self.gmt_activate:
            if hasattr(self.gmt_activate, 'to_alipay_dict'):
                params['gmt_activate'] = self.gmt_activate.to_alipay_dict()
            else:
                params['gmt_activate'] = self.gmt_activate
        if self.gmt_login:
            if hasattr(self.gmt_login, 'to_alipay_dict'):
                params['gmt_login'] = self.gmt_login.to_alipay_dict()
            else:
                params['gmt_login'] = self.gmt_login
        if self.gmt_production:
            if hasattr(self.gmt_production, 'to_alipay_dict'):
                params['gmt_production'] = self.gmt_production.to_alipay_dict()
            else:
                params['gmt_production'] = self.gmt_production
        if self.gmt_send:
            if hasattr(self.gmt_send, 'to_alipay_dict'):
                params['gmt_send'] = self.gmt_send.to_alipay_dict()
            else:
                params['gmt_send'] = self.gmt_send
        if self.gmt_unbundling:
            if hasattr(self.gmt_unbundling, 'to_alipay_dict'):
                params['gmt_unbundling'] = self.gmt_unbundling.to_alipay_dict()
            else:
                params['gmt_unbundling'] = self.gmt_unbundling
        if self.gmt_update:
            if hasattr(self.gmt_update, 'to_alipay_dict'):
                params['gmt_update'] = self.gmt_update.to_alipay_dict()
            else:
                params['gmt_update'] = self.gmt_update
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sn_no:
            if hasattr(self.sn_no, 'to_alipay_dict'):
                params['sn_no'] = self.sn_no.to_alipay_dict()
            else:
                params['sn_no'] = self.sn_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosDeviceInfoVO()
        if 'decive_software_name' in d:
            o.decive_software_name = d['decive_software_name']
        if 'device_app_cnt' in d:
            o.device_app_cnt = d['device_app_cnt']
        if 'device_app_flow' in d:
            o.device_app_flow = d['device_app_flow']
        if 'device_app_list' in d:
            o.device_app_list = d['device_app_list']
        if 'device_company_name' in d:
            o.device_company_name = d['device_company_name']
        if 'device_flow' in d:
            o.device_flow = d['device_flow']
        if 'device_ip' in d:
            o.device_ip = d['device_ip']
        if 'device_mac' in d:
            o.device_mac = d['device_mac']
        if 'device_os_version' in d:
            o.device_os_version = d['device_os_version']
        if 'device_status' in d:
            o.device_status = d['device_status']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'device_version' in d:
            o.device_version = d['device_version']
        if 'gmt_activate' in d:
            o.gmt_activate = d['gmt_activate']
        if 'gmt_login' in d:
            o.gmt_login = d['gmt_login']
        if 'gmt_production' in d:
            o.gmt_production = d['gmt_production']
        if 'gmt_send' in d:
            o.gmt_send = d['gmt_send']
        if 'gmt_unbundling' in d:
            o.gmt_unbundling = d['gmt_unbundling']
        if 'gmt_update' in d:
            o.gmt_update = d['gmt_update']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sn_no' in d:
            o.sn_no = d['sn_no']
        return o


