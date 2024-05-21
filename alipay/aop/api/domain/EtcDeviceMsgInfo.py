#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtcDeviceCardCheckInfo import EtcDeviceCardCheckInfo


class EtcDeviceMsgInfo(object):

    def __init__(self):
        self._active_status = None
        self._battery_percent = None
        self._bios_version = None
        self._biz_time = None
        self._card_no = None
        self._device_no = None
        self._device_status = None
        self._device_version = None
        self._error_list = None
        self._etc_switch_status = None
        self._fourth_generation_signal_percent = None
        self._gps_signal_percent = None
        self._interval = None
        self._sku_code = None
        self._sound_status = None

    @property
    def active_status(self):
        return self._active_status

    @active_status.setter
    def active_status(self, value):
        self._active_status = value
    @property
    def battery_percent(self):
        return self._battery_percent

    @battery_percent.setter
    def battery_percent(self, value):
        self._battery_percent = value
    @property
    def bios_version(self):
        return self._bios_version

    @bios_version.setter
    def bios_version(self, value):
        self._bios_version = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def device_version(self):
        return self._device_version

    @device_version.setter
    def device_version(self, value):
        self._device_version = value
    @property
    def error_list(self):
        return self._error_list

    @error_list.setter
    def error_list(self, value):
        if isinstance(value, list):
            self._error_list = list()
            for i in value:
                if isinstance(i, EtcDeviceCardCheckInfo):
                    self._error_list.append(i)
                else:
                    self._error_list.append(EtcDeviceCardCheckInfo.from_alipay_dict(i))
    @property
    def etc_switch_status(self):
        return self._etc_switch_status

    @etc_switch_status.setter
    def etc_switch_status(self, value):
        self._etc_switch_status = value
    @property
    def fourth_generation_signal_percent(self):
        return self._fourth_generation_signal_percent

    @fourth_generation_signal_percent.setter
    def fourth_generation_signal_percent(self, value):
        self._fourth_generation_signal_percent = value
    @property
    def gps_signal_percent(self):
        return self._gps_signal_percent

    @gps_signal_percent.setter
    def gps_signal_percent(self, value):
        self._gps_signal_percent = value
    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value
    @property
    def sound_status(self):
        return self._sound_status

    @sound_status.setter
    def sound_status(self, value):
        self._sound_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_status:
            if hasattr(self.active_status, 'to_alipay_dict'):
                params['active_status'] = self.active_status.to_alipay_dict()
            else:
                params['active_status'] = self.active_status
        if self.battery_percent:
            if hasattr(self.battery_percent, 'to_alipay_dict'):
                params['battery_percent'] = self.battery_percent.to_alipay_dict()
            else:
                params['battery_percent'] = self.battery_percent
        if self.bios_version:
            if hasattr(self.bios_version, 'to_alipay_dict'):
                params['bios_version'] = self.bios_version.to_alipay_dict()
            else:
                params['bios_version'] = self.bios_version
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.device_status:
            if hasattr(self.device_status, 'to_alipay_dict'):
                params['device_status'] = self.device_status.to_alipay_dict()
            else:
                params['device_status'] = self.device_status
        if self.device_version:
            if hasattr(self.device_version, 'to_alipay_dict'):
                params['device_version'] = self.device_version.to_alipay_dict()
            else:
                params['device_version'] = self.device_version
        if self.error_list:
            if isinstance(self.error_list, list):
                for i in range(0, len(self.error_list)):
                    element = self.error_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.error_list[i] = element.to_alipay_dict()
            if hasattr(self.error_list, 'to_alipay_dict'):
                params['error_list'] = self.error_list.to_alipay_dict()
            else:
                params['error_list'] = self.error_list
        if self.etc_switch_status:
            if hasattr(self.etc_switch_status, 'to_alipay_dict'):
                params['etc_switch_status'] = self.etc_switch_status.to_alipay_dict()
            else:
                params['etc_switch_status'] = self.etc_switch_status
        if self.fourth_generation_signal_percent:
            if hasattr(self.fourth_generation_signal_percent, 'to_alipay_dict'):
                params['fourth_generation_signal_percent'] = self.fourth_generation_signal_percent.to_alipay_dict()
            else:
                params['fourth_generation_signal_percent'] = self.fourth_generation_signal_percent
        if self.gps_signal_percent:
            if hasattr(self.gps_signal_percent, 'to_alipay_dict'):
                params['gps_signal_percent'] = self.gps_signal_percent.to_alipay_dict()
            else:
                params['gps_signal_percent'] = self.gps_signal_percent
        if self.interval:
            if hasattr(self.interval, 'to_alipay_dict'):
                params['interval'] = self.interval.to_alipay_dict()
            else:
                params['interval'] = self.interval
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        if self.sound_status:
            if hasattr(self.sound_status, 'to_alipay_dict'):
                params['sound_status'] = self.sound_status.to_alipay_dict()
            else:
                params['sound_status'] = self.sound_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcDeviceMsgInfo()
        if 'active_status' in d:
            o.active_status = d['active_status']
        if 'battery_percent' in d:
            o.battery_percent = d['battery_percent']
        if 'bios_version' in d:
            o.bios_version = d['bios_version']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'device_status' in d:
            o.device_status = d['device_status']
        if 'device_version' in d:
            o.device_version = d['device_version']
        if 'error_list' in d:
            o.error_list = d['error_list']
        if 'etc_switch_status' in d:
            o.etc_switch_status = d['etc_switch_status']
        if 'fourth_generation_signal_percent' in d:
            o.fourth_generation_signal_percent = d['fourth_generation_signal_percent']
        if 'gps_signal_percent' in d:
            o.gps_signal_percent = d['gps_signal_percent']
        if 'interval' in d:
            o.interval = d['interval']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        if 'sound_status' in d:
            o.sound_status = d['sound_status']
        return o


