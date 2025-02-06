#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmepTaxViolationInfo(object):

    def __init__(self):
        self._ajxz = None
        self._event_time = None
        self._nsr_cert_no = None
        self._nsr_name = None
        self._pub_time = None
        self._registered_address = None
        self._xgflyjjswclcfqk = None
        self._zywfss = None
        self._zzjg_code = None

    @property
    def ajxz(self):
        return self._ajxz

    @ajxz.setter
    def ajxz(self, value):
        self._ajxz = value
    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def nsr_cert_no(self):
        return self._nsr_cert_no

    @nsr_cert_no.setter
    def nsr_cert_no(self, value):
        self._nsr_cert_no = value
    @property
    def nsr_name(self):
        return self._nsr_name

    @nsr_name.setter
    def nsr_name(self, value):
        self._nsr_name = value
    @property
    def pub_time(self):
        return self._pub_time

    @pub_time.setter
    def pub_time(self, value):
        self._pub_time = value
    @property
    def registered_address(self):
        return self._registered_address

    @registered_address.setter
    def registered_address(self, value):
        self._registered_address = value
    @property
    def xgflyjjswclcfqk(self):
        return self._xgflyjjswclcfqk

    @xgflyjjswclcfqk.setter
    def xgflyjjswclcfqk(self, value):
        self._xgflyjjswclcfqk = value
    @property
    def zywfss(self):
        return self._zywfss

    @zywfss.setter
    def zywfss(self, value):
        self._zywfss = value
    @property
    def zzjg_code(self):
        return self._zzjg_code

    @zzjg_code.setter
    def zzjg_code(self, value):
        self._zzjg_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ajxz:
            if hasattr(self.ajxz, 'to_alipay_dict'):
                params['ajxz'] = self.ajxz.to_alipay_dict()
            else:
                params['ajxz'] = self.ajxz
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.nsr_cert_no:
            if hasattr(self.nsr_cert_no, 'to_alipay_dict'):
                params['nsr_cert_no'] = self.nsr_cert_no.to_alipay_dict()
            else:
                params['nsr_cert_no'] = self.nsr_cert_no
        if self.nsr_name:
            if hasattr(self.nsr_name, 'to_alipay_dict'):
                params['nsr_name'] = self.nsr_name.to_alipay_dict()
            else:
                params['nsr_name'] = self.nsr_name
        if self.pub_time:
            if hasattr(self.pub_time, 'to_alipay_dict'):
                params['pub_time'] = self.pub_time.to_alipay_dict()
            else:
                params['pub_time'] = self.pub_time
        if self.registered_address:
            if hasattr(self.registered_address, 'to_alipay_dict'):
                params['registered_address'] = self.registered_address.to_alipay_dict()
            else:
                params['registered_address'] = self.registered_address
        if self.xgflyjjswclcfqk:
            if hasattr(self.xgflyjjswclcfqk, 'to_alipay_dict'):
                params['xgflyjjswclcfqk'] = self.xgflyjjswclcfqk.to_alipay_dict()
            else:
                params['xgflyjjswclcfqk'] = self.xgflyjjswclcfqk
        if self.zywfss:
            if hasattr(self.zywfss, 'to_alipay_dict'):
                params['zywfss'] = self.zywfss.to_alipay_dict()
            else:
                params['zywfss'] = self.zywfss
        if self.zzjg_code:
            if hasattr(self.zzjg_code, 'to_alipay_dict'):
                params['zzjg_code'] = self.zzjg_code.to_alipay_dict()
            else:
                params['zzjg_code'] = self.zzjg_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepTaxViolationInfo()
        if 'ajxz' in d:
            o.ajxz = d['ajxz']
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'nsr_cert_no' in d:
            o.nsr_cert_no = d['nsr_cert_no']
        if 'nsr_name' in d:
            o.nsr_name = d['nsr_name']
        if 'pub_time' in d:
            o.pub_time = d['pub_time']
        if 'registered_address' in d:
            o.registered_address = d['registered_address']
        if 'xgflyjjswclcfqk' in d:
            o.xgflyjjswclcfqk = d['xgflyjjswclcfqk']
        if 'zywfss' in d:
            o.zywfss = d['zywfss']
        if 'zzjg_code' in d:
            o.zzjg_code = d['zzjg_code']
        return o


