#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmsSendDetail(object):

    def __init__(self):
        self._content = None
        self._out_biz_no = None
        self._phone_number = None
        self._send_date = None
        self._sms_code = None
        self._sms_desc = None
        self._template_code = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
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
    def send_date(self):
        return self._send_date

    @send_date.setter
    def send_date(self, value):
        self._send_date = value
    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value
    @property
    def sms_desc(self):
        return self._sms_desc

    @sms_desc.setter
    def sms_desc(self, value):
        self._sms_desc = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
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
        if self.send_date:
            if hasattr(self.send_date, 'to_alipay_dict'):
                params['send_date'] = self.send_date.to_alipay_dict()
            else:
                params['send_date'] = self.send_date
        if self.sms_code:
            if hasattr(self.sms_code, 'to_alipay_dict'):
                params['sms_code'] = self.sms_code.to_alipay_dict()
            else:
                params['sms_code'] = self.sms_code
        if self.sms_desc:
            if hasattr(self.sms_desc, 'to_alipay_dict'):
                params['sms_desc'] = self.sms_desc.to_alipay_dict()
            else:
                params['sms_desc'] = self.sms_desc
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SmsSendDetail()
        if 'content' in d:
            o.content = d['content']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'send_date' in d:
            o.send_date = d['send_date']
        if 'sms_code' in d:
            o.sms_code = d['sms_code']
        if 'sms_desc' in d:
            o.sms_desc = d['sms_desc']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


