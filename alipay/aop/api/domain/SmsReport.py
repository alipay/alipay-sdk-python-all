#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmsReport(object):

    def __init__(self):
        self._biz_id = None
        self._err_code = None
        self._err_msg = None
        self._out_biz_no = None
        self._phone_number = None
        self._send_time = None
        self._sms_size = None
        self._success = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def err_code(self):
        return self._err_code

    @err_code.setter
    def err_code(self, value):
        self._err_code = value
    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def sms_size(self):
        return self._sms_size

    @sms_size.setter
    def sms_size(self, value):
        self._sms_size = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.err_code:
            if hasattr(self.err_code, 'to_alipay_dict'):
                params['err_code'] = self.err_code.to_alipay_dict()
            else:
                params['err_code'] = self.err_code
        if self.err_msg:
            if hasattr(self.err_msg, 'to_alipay_dict'):
                params['err_msg'] = self.err_msg.to_alipay_dict()
            else:
                params['err_msg'] = self.err_msg
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.sms_size:
            if hasattr(self.sms_size, 'to_alipay_dict'):
                params['sms_size'] = self.sms_size.to_alipay_dict()
            else:
                params['sms_size'] = self.sms_size
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SmsReport()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'err_code' in d:
            o.err_code = d['err_code']
        if 'err_msg' in d:
            o.err_msg = d['err_msg']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'sms_size' in d:
            o.sms_size = d['sms_size']
        if 'success' in d:
            o.success = d['success']
        return o


