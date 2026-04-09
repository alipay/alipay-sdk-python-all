#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Mail(object):

    def __init__(self):
        self._courier_name = None
        self._courier_phone_num = None
        self._cp_code = None
        self._delivery_time = None
        self._mail_no = None

    @property
    def courier_name(self):
        return self._courier_name

    @courier_name.setter
    def courier_name(self, value):
        self._courier_name = value
    @property
    def courier_phone_num(self):
        return self._courier_phone_num

    @courier_phone_num.setter
    def courier_phone_num(self, value):
        self._courier_phone_num = value
    @property
    def cp_code(self):
        return self._cp_code

    @cp_code.setter
    def cp_code(self, value):
        self._cp_code = value
    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        self._delivery_time = value
    @property
    def mail_no(self):
        return self._mail_no

    @mail_no.setter
    def mail_no(self, value):
        self._mail_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.courier_name:
            if hasattr(self.courier_name, 'to_alipay_dict'):
                params['courier_name'] = self.courier_name.to_alipay_dict()
            else:
                params['courier_name'] = self.courier_name
        if self.courier_phone_num:
            if hasattr(self.courier_phone_num, 'to_alipay_dict'):
                params['courier_phone_num'] = self.courier_phone_num.to_alipay_dict()
            else:
                params['courier_phone_num'] = self.courier_phone_num
        if self.cp_code:
            if hasattr(self.cp_code, 'to_alipay_dict'):
                params['cp_code'] = self.cp_code.to_alipay_dict()
            else:
                params['cp_code'] = self.cp_code
        if self.delivery_time:
            if hasattr(self.delivery_time, 'to_alipay_dict'):
                params['delivery_time'] = self.delivery_time.to_alipay_dict()
            else:
                params['delivery_time'] = self.delivery_time
        if self.mail_no:
            if hasattr(self.mail_no, 'to_alipay_dict'):
                params['mail_no'] = self.mail_no.to_alipay_dict()
            else:
                params['mail_no'] = self.mail_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Mail()
        if 'courier_name' in d:
            o.courier_name = d['courier_name']
        if 'courier_phone_num' in d:
            o.courier_phone_num = d['courier_phone_num']
        if 'cp_code' in d:
            o.cp_code = d['cp_code']
        if 'delivery_time' in d:
            o.delivery_time = d['delivery_time']
        if 'mail_no' in d:
            o.mail_no = d['mail_no']
        return o


