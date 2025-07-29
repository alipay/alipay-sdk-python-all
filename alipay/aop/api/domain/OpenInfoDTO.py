#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenInfoDTO(object):

    def __init__(self):
        self._card_no = None
        self._expiration_date = None
        self._open_status = None
        self._open_time = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.expiration_date:
            if hasattr(self.expiration_date, 'to_alipay_dict'):
                params['expiration_date'] = self.expiration_date.to_alipay_dict()
            else:
                params['expiration_date'] = self.expiration_date
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenInfoDTO()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'expiration_date' in d:
            o.expiration_date = d['expiration_date']
        if 'open_status' in d:
            o.open_status = d['open_status']
        if 'open_time' in d:
            o.open_time = d['open_time']
        return o


