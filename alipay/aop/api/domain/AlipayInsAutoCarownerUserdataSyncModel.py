#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoCarownerUserdataSyncModel(object):

    def __init__(self):
        self._car_engine_no = None
        self._car_frame_no = None
        self._car_model = None
        self._car_no = None
        self._cert_no = None
        self._com_id = None
        self._first_register_date = None
        self._out_leads_id = None
        self._send_time = None

    @property
    def car_engine_no(self):
        return self._car_engine_no

    @car_engine_no.setter
    def car_engine_no(self, value):
        self._car_engine_no = value
    @property
    def car_frame_no(self):
        return self._car_frame_no

    @car_frame_no.setter
    def car_frame_no(self, value):
        self._car_frame_no = value
    @property
    def car_model(self):
        return self._car_model

    @car_model.setter
    def car_model(self, value):
        self._car_model = value
    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def com_id(self):
        return self._com_id

    @com_id.setter
    def com_id(self, value):
        self._com_id = value
    @property
    def first_register_date(self):
        return self._first_register_date

    @first_register_date.setter
    def first_register_date(self, value):
        self._first_register_date = value
    @property
    def out_leads_id(self):
        return self._out_leads_id

    @out_leads_id.setter
    def out_leads_id(self, value):
        self._out_leads_id = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_engine_no:
            if hasattr(self.car_engine_no, 'to_alipay_dict'):
                params['car_engine_no'] = self.car_engine_no.to_alipay_dict()
            else:
                params['car_engine_no'] = self.car_engine_no
        if self.car_frame_no:
            if hasattr(self.car_frame_no, 'to_alipay_dict'):
                params['car_frame_no'] = self.car_frame_no.to_alipay_dict()
            else:
                params['car_frame_no'] = self.car_frame_no
        if self.car_model:
            if hasattr(self.car_model, 'to_alipay_dict'):
                params['car_model'] = self.car_model.to_alipay_dict()
            else:
                params['car_model'] = self.car_model
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.com_id:
            if hasattr(self.com_id, 'to_alipay_dict'):
                params['com_id'] = self.com_id.to_alipay_dict()
            else:
                params['com_id'] = self.com_id
        if self.first_register_date:
            if hasattr(self.first_register_date, 'to_alipay_dict'):
                params['first_register_date'] = self.first_register_date.to_alipay_dict()
            else:
                params['first_register_date'] = self.first_register_date
        if self.out_leads_id:
            if hasattr(self.out_leads_id, 'to_alipay_dict'):
                params['out_leads_id'] = self.out_leads_id.to_alipay_dict()
            else:
                params['out_leads_id'] = self.out_leads_id
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoCarownerUserdataSyncModel()
        if 'car_engine_no' in d:
            o.car_engine_no = d['car_engine_no']
        if 'car_frame_no' in d:
            o.car_frame_no = d['car_frame_no']
        if 'car_model' in d:
            o.car_model = d['car_model']
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'com_id' in d:
            o.com_id = d['com_id']
        if 'first_register_date' in d:
            o.first_register_date = d['first_register_date']
        if 'out_leads_id' in d:
            o.out_leads_id = d['out_leads_id']
        if 'send_time' in d:
            o.send_time = d['send_time']
        return o


