#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpeechRecordDetail(object):

    def __init__(self):
        self._alipay_plan_id = None
        self._device_address = None
        self._device_city = None
        self._device_district = None
        self._device_ip = None
        self._device_latitude = None
        self._device_longitude = None
        self._device_online_time = None
        self._device_os_version = None
        self._device_province = None
        self._device_sdk_version = None
        self._device_sn = None
        self._device_sound = None
        self._device_supplier_id = None
        self._out_plan_end_time = None
        self._out_plan_id = None
        self._out_plan_start_time = None
        self._scan_type = None
        self._smid = None
        self._speech_content = None
        self._speech_event = None
        self._speech_id = None
        self._speech_result = None
        self._speech_result_msg = None
        self._speech_scene = None
        self._speech_time = None
        self._trade_channel = None
        self._trade_no = None

    @property
    def alipay_plan_id(self):
        return self._alipay_plan_id

    @alipay_plan_id.setter
    def alipay_plan_id(self, value):
        self._alipay_plan_id = value
    @property
    def device_address(self):
        return self._device_address

    @device_address.setter
    def device_address(self, value):
        self._device_address = value
    @property
    def device_city(self):
        return self._device_city

    @device_city.setter
    def device_city(self, value):
        self._device_city = value
    @property
    def device_district(self):
        return self._device_district

    @device_district.setter
    def device_district(self, value):
        self._device_district = value
    @property
    def device_ip(self):
        return self._device_ip

    @device_ip.setter
    def device_ip(self, value):
        self._device_ip = value
    @property
    def device_latitude(self):
        return self._device_latitude

    @device_latitude.setter
    def device_latitude(self, value):
        self._device_latitude = value
    @property
    def device_longitude(self):
        return self._device_longitude

    @device_longitude.setter
    def device_longitude(self, value):
        self._device_longitude = value
    @property
    def device_online_time(self):
        return self._device_online_time

    @device_online_time.setter
    def device_online_time(self, value):
        self._device_online_time = value
    @property
    def device_os_version(self):
        return self._device_os_version

    @device_os_version.setter
    def device_os_version(self, value):
        self._device_os_version = value
    @property
    def device_province(self):
        return self._device_province

    @device_province.setter
    def device_province(self, value):
        self._device_province = value
    @property
    def device_sdk_version(self):
        return self._device_sdk_version

    @device_sdk_version.setter
    def device_sdk_version(self, value):
        self._device_sdk_version = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def device_sound(self):
        return self._device_sound

    @device_sound.setter
    def device_sound(self, value):
        self._device_sound = value
    @property
    def device_supplier_id(self):
        return self._device_supplier_id

    @device_supplier_id.setter
    def device_supplier_id(self, value):
        self._device_supplier_id = value
    @property
    def out_plan_end_time(self):
        return self._out_plan_end_time

    @out_plan_end_time.setter
    def out_plan_end_time(self, value):
        self._out_plan_end_time = value
    @property
    def out_plan_id(self):
        return self._out_plan_id

    @out_plan_id.setter
    def out_plan_id(self, value):
        self._out_plan_id = value
    @property
    def out_plan_start_time(self):
        return self._out_plan_start_time

    @out_plan_start_time.setter
    def out_plan_start_time(self, value):
        self._out_plan_start_time = value
    @property
    def scan_type(self):
        return self._scan_type

    @scan_type.setter
    def scan_type(self, value):
        self._scan_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def speech_content(self):
        return self._speech_content

    @speech_content.setter
    def speech_content(self, value):
        self._speech_content = value
    @property
    def speech_event(self):
        return self._speech_event

    @speech_event.setter
    def speech_event(self, value):
        self._speech_event = value
    @property
    def speech_id(self):
        return self._speech_id

    @speech_id.setter
    def speech_id(self, value):
        self._speech_id = value
    @property
    def speech_result(self):
        return self._speech_result

    @speech_result.setter
    def speech_result(self, value):
        self._speech_result = value
    @property
    def speech_result_msg(self):
        return self._speech_result_msg

    @speech_result_msg.setter
    def speech_result_msg(self, value):
        self._speech_result_msg = value
    @property
    def speech_scene(self):
        return self._speech_scene

    @speech_scene.setter
    def speech_scene(self, value):
        self._speech_scene = value
    @property
    def speech_time(self):
        return self._speech_time

    @speech_time.setter
    def speech_time(self, value):
        self._speech_time = value
    @property
    def trade_channel(self):
        return self._trade_channel

    @trade_channel.setter
    def trade_channel(self, value):
        self._trade_channel = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_plan_id:
            if hasattr(self.alipay_plan_id, 'to_alipay_dict'):
                params['alipay_plan_id'] = self.alipay_plan_id.to_alipay_dict()
            else:
                params['alipay_plan_id'] = self.alipay_plan_id
        if self.device_address:
            if hasattr(self.device_address, 'to_alipay_dict'):
                params['device_address'] = self.device_address.to_alipay_dict()
            else:
                params['device_address'] = self.device_address
        if self.device_city:
            if hasattr(self.device_city, 'to_alipay_dict'):
                params['device_city'] = self.device_city.to_alipay_dict()
            else:
                params['device_city'] = self.device_city
        if self.device_district:
            if hasattr(self.device_district, 'to_alipay_dict'):
                params['device_district'] = self.device_district.to_alipay_dict()
            else:
                params['device_district'] = self.device_district
        if self.device_ip:
            if hasattr(self.device_ip, 'to_alipay_dict'):
                params['device_ip'] = self.device_ip.to_alipay_dict()
            else:
                params['device_ip'] = self.device_ip
        if self.device_latitude:
            if hasattr(self.device_latitude, 'to_alipay_dict'):
                params['device_latitude'] = self.device_latitude.to_alipay_dict()
            else:
                params['device_latitude'] = self.device_latitude
        if self.device_longitude:
            if hasattr(self.device_longitude, 'to_alipay_dict'):
                params['device_longitude'] = self.device_longitude.to_alipay_dict()
            else:
                params['device_longitude'] = self.device_longitude
        if self.device_online_time:
            if hasattr(self.device_online_time, 'to_alipay_dict'):
                params['device_online_time'] = self.device_online_time.to_alipay_dict()
            else:
                params['device_online_time'] = self.device_online_time
        if self.device_os_version:
            if hasattr(self.device_os_version, 'to_alipay_dict'):
                params['device_os_version'] = self.device_os_version.to_alipay_dict()
            else:
                params['device_os_version'] = self.device_os_version
        if self.device_province:
            if hasattr(self.device_province, 'to_alipay_dict'):
                params['device_province'] = self.device_province.to_alipay_dict()
            else:
                params['device_province'] = self.device_province
        if self.device_sdk_version:
            if hasattr(self.device_sdk_version, 'to_alipay_dict'):
                params['device_sdk_version'] = self.device_sdk_version.to_alipay_dict()
            else:
                params['device_sdk_version'] = self.device_sdk_version
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.device_sound:
            if hasattr(self.device_sound, 'to_alipay_dict'):
                params['device_sound'] = self.device_sound.to_alipay_dict()
            else:
                params['device_sound'] = self.device_sound
        if self.device_supplier_id:
            if hasattr(self.device_supplier_id, 'to_alipay_dict'):
                params['device_supplier_id'] = self.device_supplier_id.to_alipay_dict()
            else:
                params['device_supplier_id'] = self.device_supplier_id
        if self.out_plan_end_time:
            if hasattr(self.out_plan_end_time, 'to_alipay_dict'):
                params['out_plan_end_time'] = self.out_plan_end_time.to_alipay_dict()
            else:
                params['out_plan_end_time'] = self.out_plan_end_time
        if self.out_plan_id:
            if hasattr(self.out_plan_id, 'to_alipay_dict'):
                params['out_plan_id'] = self.out_plan_id.to_alipay_dict()
            else:
                params['out_plan_id'] = self.out_plan_id
        if self.out_plan_start_time:
            if hasattr(self.out_plan_start_time, 'to_alipay_dict'):
                params['out_plan_start_time'] = self.out_plan_start_time.to_alipay_dict()
            else:
                params['out_plan_start_time'] = self.out_plan_start_time
        if self.scan_type:
            if hasattr(self.scan_type, 'to_alipay_dict'):
                params['scan_type'] = self.scan_type.to_alipay_dict()
            else:
                params['scan_type'] = self.scan_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.speech_content:
            if hasattr(self.speech_content, 'to_alipay_dict'):
                params['speech_content'] = self.speech_content.to_alipay_dict()
            else:
                params['speech_content'] = self.speech_content
        if self.speech_event:
            if hasattr(self.speech_event, 'to_alipay_dict'):
                params['speech_event'] = self.speech_event.to_alipay_dict()
            else:
                params['speech_event'] = self.speech_event
        if self.speech_id:
            if hasattr(self.speech_id, 'to_alipay_dict'):
                params['speech_id'] = self.speech_id.to_alipay_dict()
            else:
                params['speech_id'] = self.speech_id
        if self.speech_result:
            if hasattr(self.speech_result, 'to_alipay_dict'):
                params['speech_result'] = self.speech_result.to_alipay_dict()
            else:
                params['speech_result'] = self.speech_result
        if self.speech_result_msg:
            if hasattr(self.speech_result_msg, 'to_alipay_dict'):
                params['speech_result_msg'] = self.speech_result_msg.to_alipay_dict()
            else:
                params['speech_result_msg'] = self.speech_result_msg
        if self.speech_scene:
            if hasattr(self.speech_scene, 'to_alipay_dict'):
                params['speech_scene'] = self.speech_scene.to_alipay_dict()
            else:
                params['speech_scene'] = self.speech_scene
        if self.speech_time:
            if hasattr(self.speech_time, 'to_alipay_dict'):
                params['speech_time'] = self.speech_time.to_alipay_dict()
            else:
                params['speech_time'] = self.speech_time
        if self.trade_channel:
            if hasattr(self.trade_channel, 'to_alipay_dict'):
                params['trade_channel'] = self.trade_channel.to_alipay_dict()
            else:
                params['trade_channel'] = self.trade_channel
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpeechRecordDetail()
        if 'alipay_plan_id' in d:
            o.alipay_plan_id = d['alipay_plan_id']
        if 'device_address' in d:
            o.device_address = d['device_address']
        if 'device_city' in d:
            o.device_city = d['device_city']
        if 'device_district' in d:
            o.device_district = d['device_district']
        if 'device_ip' in d:
            o.device_ip = d['device_ip']
        if 'device_latitude' in d:
            o.device_latitude = d['device_latitude']
        if 'device_longitude' in d:
            o.device_longitude = d['device_longitude']
        if 'device_online_time' in d:
            o.device_online_time = d['device_online_time']
        if 'device_os_version' in d:
            o.device_os_version = d['device_os_version']
        if 'device_province' in d:
            o.device_province = d['device_province']
        if 'device_sdk_version' in d:
            o.device_sdk_version = d['device_sdk_version']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'device_sound' in d:
            o.device_sound = d['device_sound']
        if 'device_supplier_id' in d:
            o.device_supplier_id = d['device_supplier_id']
        if 'out_plan_end_time' in d:
            o.out_plan_end_time = d['out_plan_end_time']
        if 'out_plan_id' in d:
            o.out_plan_id = d['out_plan_id']
        if 'out_plan_start_time' in d:
            o.out_plan_start_time = d['out_plan_start_time']
        if 'scan_type' in d:
            o.scan_type = d['scan_type']
        if 'smid' in d:
            o.smid = d['smid']
        if 'speech_content' in d:
            o.speech_content = d['speech_content']
        if 'speech_event' in d:
            o.speech_event = d['speech_event']
        if 'speech_id' in d:
            o.speech_id = d['speech_id']
        if 'speech_result' in d:
            o.speech_result = d['speech_result']
        if 'speech_result_msg' in d:
            o.speech_result_msg = d['speech_result_msg']
        if 'speech_scene' in d:
            o.speech_scene = d['speech_scene']
        if 'speech_time' in d:
            o.speech_time = d['speech_time']
        if 'trade_channel' in d:
            o.trade_channel = d['trade_channel']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


