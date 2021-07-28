#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiDriverSendModel(object):

    def __init__(self):
        self._alipay_account = None
        self._car_no = None
        self._driver_cert_no = None
        self._driver_job_no = None
        self._driver_name = None
        self._driver_phone = None
        self._ext_info = None
        self._source = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def driver_cert_no(self):
        return self._driver_cert_no

    @driver_cert_no.setter
    def driver_cert_no(self, value):
        self._driver_cert_no = value
    @property
    def driver_job_no(self):
        return self._driver_job_no

    @driver_job_no.setter
    def driver_job_no(self, value):
        self._driver_job_no = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driver_phone(self):
        return self._driver_phone

    @driver_phone.setter
    def driver_phone(self, value):
        self._driver_phone = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.driver_cert_no:
            if hasattr(self.driver_cert_no, 'to_alipay_dict'):
                params['driver_cert_no'] = self.driver_cert_no.to_alipay_dict()
            else:
                params['driver_cert_no'] = self.driver_cert_no
        if self.driver_job_no:
            if hasattr(self.driver_job_no, 'to_alipay_dict'):
                params['driver_job_no'] = self.driver_job_no.to_alipay_dict()
            else:
                params['driver_job_no'] = self.driver_job_no
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.driver_phone:
            if hasattr(self.driver_phone, 'to_alipay_dict'):
                params['driver_phone'] = self.driver_phone.to_alipay_dict()
            else:
                params['driver_phone'] = self.driver_phone
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiDriverSendModel()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'driver_cert_no' in d:
            o.driver_cert_no = d['driver_cert_no']
        if 'driver_job_no' in d:
            o.driver_job_no = d['driver_job_no']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'driver_phone' in d:
            o.driver_phone = d['driver_phone']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'source' in d:
            o.source = d['source']
        return o


