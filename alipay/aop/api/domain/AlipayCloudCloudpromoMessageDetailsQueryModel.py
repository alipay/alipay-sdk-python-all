#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMessageDetailsQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._page_no = None
        self._page_size = None
        self._phone_number = None
        self._send_date = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if isinstance(value, list):
            self._phone_number = list()
            for i in value:
                self._phone_number.append(i)
    @property
    def send_date(self):
        return self._send_date

    @send_date.setter
    def send_date(self, value):
        self._send_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.phone_number:
            if isinstance(self.phone_number, list):
                for i in range(0, len(self.phone_number)):
                    element = self.phone_number[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone_number[i] = element.to_alipay_dict()
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.send_date:
            if hasattr(self.send_date, 'to_alipay_dict'):
                params['send_date'] = self.send_date.to_alipay_dict()
            else:
                params['send_date'] = self.send_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMessageDetailsQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'send_date' in d:
            o.send_date = d['send_date']
        return o


