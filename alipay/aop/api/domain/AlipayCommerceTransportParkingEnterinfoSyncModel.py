#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportParkingEnterinfoSyncModel(object):

    def __init__(self):
        self._agreement_query = None
        self._free_enter_minutes = None
        self._in_time = None
        self._is_encrypt_plate_no = None
        self._need_charge = None
        self._open_appid = None
        self._open_id = None
        self._out_serial_no = None
        self._parking_id = None
        self._plate_color = None
        self._plate_no = None
        self._service_url = None

    @property
    def agreement_query(self):
        return self._agreement_query

    @agreement_query.setter
    def agreement_query(self, value):
        self._agreement_query = value
    @property
    def free_enter_minutes(self):
        return self._free_enter_minutes

    @free_enter_minutes.setter
    def free_enter_minutes(self, value):
        self._free_enter_minutes = value
    @property
    def in_time(self):
        return self._in_time

    @in_time.setter
    def in_time(self, value):
        self._in_time = value
    @property
    def is_encrypt_plate_no(self):
        return self._is_encrypt_plate_no

    @is_encrypt_plate_no.setter
    def is_encrypt_plate_no(self, value):
        self._is_encrypt_plate_no = value
    @property
    def need_charge(self):
        return self._need_charge

    @need_charge.setter
    def need_charge(self, value):
        self._need_charge = value
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
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
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
        if self.agreement_query:
            if hasattr(self.agreement_query, 'to_alipay_dict'):
                params['agreement_query'] = self.agreement_query.to_alipay_dict()
            else:
                params['agreement_query'] = self.agreement_query
        if self.free_enter_minutes:
            if hasattr(self.free_enter_minutes, 'to_alipay_dict'):
                params['free_enter_minutes'] = self.free_enter_minutes.to_alipay_dict()
            else:
                params['free_enter_minutes'] = self.free_enter_minutes
        if self.in_time:
            if hasattr(self.in_time, 'to_alipay_dict'):
                params['in_time'] = self.in_time.to_alipay_dict()
            else:
                params['in_time'] = self.in_time
        if self.is_encrypt_plate_no:
            if hasattr(self.is_encrypt_plate_no, 'to_alipay_dict'):
                params['is_encrypt_plate_no'] = self.is_encrypt_plate_no.to_alipay_dict()
            else:
                params['is_encrypt_plate_no'] = self.is_encrypt_plate_no
        if self.need_charge:
            if hasattr(self.need_charge, 'to_alipay_dict'):
                params['need_charge'] = self.need_charge.to_alipay_dict()
            else:
                params['need_charge'] = self.need_charge
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
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
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
        o = AlipayCommerceTransportParkingEnterinfoSyncModel()
        if 'agreement_query' in d:
            o.agreement_query = d['agreement_query']
        if 'free_enter_minutes' in d:
            o.free_enter_minutes = d['free_enter_minutes']
        if 'in_time' in d:
            o.in_time = d['in_time']
        if 'is_encrypt_plate_no' in d:
            o.is_encrypt_plate_no = d['is_encrypt_plate_no']
        if 'need_charge' in d:
            o.need_charge = d['need_charge']
        if 'open_appid' in d:
            o.open_appid = d['open_appid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


