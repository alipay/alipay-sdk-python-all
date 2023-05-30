#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportParkingExitinfoSyncModel(object):

    def __init__(self):
        self._is_encrypt_plate_no = None
        self._open_appid = None
        self._open_id = None
        self._out_serial_no = None
        self._out_time = None
        self._plate_color = None
        self._plate_no = None
        self._service_url = None

    @property
    def is_encrypt_plate_no(self):
        return self._is_encrypt_plate_no

    @is_encrypt_plate_no.setter
    def is_encrypt_plate_no(self, value):
        self._is_encrypt_plate_no = value
    @property
    def open_appid(self):
        return self._open_appid

    @open_appid.setter
    def open_appid(self, value):
        self._open_appid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def out_time(self):
        return self._out_time

    @out_time.setter
    def out_time(self, value):
        self._out_time = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_encrypt_plate_no:
            if hasattr(self.is_encrypt_plate_no, 'to_alipay_dict'):
                params['is_encrypt_plate_no'] = self.is_encrypt_plate_no.to_alipay_dict()
            else:
                params['is_encrypt_plate_no'] = self.is_encrypt_plate_no
        if self.open_appid:
            if hasattr(self.open_appid, 'to_alipay_dict'):
                params['open_appid'] = self.open_appid.to_alipay_dict()
            else:
                params['open_appid'] = self.open_appid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.out_time:
            if hasattr(self.out_time, 'to_alipay_dict'):
                params['out_time'] = self.out_time.to_alipay_dict()
            else:
                params['out_time'] = self.out_time
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportParkingExitinfoSyncModel()
        if 'is_encrypt_plate_no' in d:
            o.is_encrypt_plate_no = d['is_encrypt_plate_no']
        if 'open_appid' in d:
            o.open_appid = d['open_appid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'out_time' in d:
            o.out_time = d['out_time']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


