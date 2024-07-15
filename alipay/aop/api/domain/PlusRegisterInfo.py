#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlusRegisterInfo(object):

    def __init__(self):
        self._write_off_address = None
        self._write_off_code = None
        self._write_off_doctor = None
        self._write_off_section = None
        self._write_off_status = None
        self._write_off_time = None

    @property
    def write_off_address(self):
        return self._write_off_address

    @write_off_address.setter
    def write_off_address(self, value):
        self._write_off_address = value
    @property
    def write_off_code(self):
        return self._write_off_code

    @write_off_code.setter
    def write_off_code(self, value):
        self._write_off_code = value
    @property
    def write_off_doctor(self):
        return self._write_off_doctor

    @write_off_doctor.setter
    def write_off_doctor(self, value):
        self._write_off_doctor = value
    @property
    def write_off_section(self):
        return self._write_off_section

    @write_off_section.setter
    def write_off_section(self, value):
        self._write_off_section = value
    @property
    def write_off_status(self):
        return self._write_off_status

    @write_off_status.setter
    def write_off_status(self, value):
        self._write_off_status = value
    @property
    def write_off_time(self):
        return self._write_off_time

    @write_off_time.setter
    def write_off_time(self, value):
        self._write_off_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.write_off_address:
            if hasattr(self.write_off_address, 'to_alipay_dict'):
                params['write_off_address'] = self.write_off_address.to_alipay_dict()
            else:
                params['write_off_address'] = self.write_off_address
        if self.write_off_code:
            if hasattr(self.write_off_code, 'to_alipay_dict'):
                params['write_off_code'] = self.write_off_code.to_alipay_dict()
            else:
                params['write_off_code'] = self.write_off_code
        if self.write_off_doctor:
            if hasattr(self.write_off_doctor, 'to_alipay_dict'):
                params['write_off_doctor'] = self.write_off_doctor.to_alipay_dict()
            else:
                params['write_off_doctor'] = self.write_off_doctor
        if self.write_off_section:
            if hasattr(self.write_off_section, 'to_alipay_dict'):
                params['write_off_section'] = self.write_off_section.to_alipay_dict()
            else:
                params['write_off_section'] = self.write_off_section
        if self.write_off_status:
            if hasattr(self.write_off_status, 'to_alipay_dict'):
                params['write_off_status'] = self.write_off_status.to_alipay_dict()
            else:
                params['write_off_status'] = self.write_off_status
        if self.write_off_time:
            if hasattr(self.write_off_time, 'to_alipay_dict'):
                params['write_off_time'] = self.write_off_time.to_alipay_dict()
            else:
                params['write_off_time'] = self.write_off_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlusRegisterInfo()
        if 'write_off_address' in d:
            o.write_off_address = d['write_off_address']
        if 'write_off_code' in d:
            o.write_off_code = d['write_off_code']
        if 'write_off_doctor' in d:
            o.write_off_doctor = d['write_off_doctor']
        if 'write_off_section' in d:
            o.write_off_section = d['write_off_section']
        if 'write_off_status' in d:
            o.write_off_status = d['write_off_status']
        if 'write_off_time' in d:
            o.write_off_time = d['write_off_time']
        return o


