#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommercializationCertificateInfo import CommercializationCertificateInfo


class AlipayEcoMycarCommercializationCertificateAppendModel(object):

    def __init__(self):
        self._certificate_info = None
        self._open_id = None
        self._operate_serial_number = None
        self._operate_time = None
        self._user_id = None

    @property
    def certificate_info(self):
        return self._certificate_info

    @certificate_info.setter
    def certificate_info(self, value):
        if isinstance(value, CommercializationCertificateInfo):
            self._certificate_info = value
        else:
            self._certificate_info = CommercializationCertificateInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operate_serial_number(self):
        return self._operate_serial_number

    @operate_serial_number.setter
    def operate_serial_number(self, value):
        self._operate_serial_number = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_info:
            if hasattr(self.certificate_info, 'to_alipay_dict'):
                params['certificate_info'] = self.certificate_info.to_alipay_dict()
            else:
                params['certificate_info'] = self.certificate_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operate_serial_number:
            if hasattr(self.operate_serial_number, 'to_alipay_dict'):
                params['operate_serial_number'] = self.operate_serial_number.to_alipay_dict()
            else:
                params['operate_serial_number'] = self.operate_serial_number
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarCommercializationCertificateAppendModel()
        if 'certificate_info' in d:
            o.certificate_info = d['certificate_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operate_serial_number' in d:
            o.operate_serial_number = d['operate_serial_number']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


