#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankQrcodedataQueryModel(object):

    def __init__(self):
        self._data_date = None
        self._qrcode_id = None
        self._qrcode_out_id = None

    @property
    def data_date(self):
        return self._data_date

    @data_date.setter
    def data_date(self, value):
        self._data_date = value
    @property
    def qrcode_id(self):
        return self._qrcode_id

    @qrcode_id.setter
    def qrcode_id(self, value):
        self._qrcode_id = value
    @property
    def qrcode_out_id(self):
        return self._qrcode_out_id

    @qrcode_out_id.setter
    def qrcode_out_id(self, value):
        self._qrcode_out_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_date:
            if hasattr(self.data_date, 'to_alipay_dict'):
                params['data_date'] = self.data_date.to_alipay_dict()
            else:
                params['data_date'] = self.data_date
        if self.qrcode_id:
            if hasattr(self.qrcode_id, 'to_alipay_dict'):
                params['qrcode_id'] = self.qrcode_id.to_alipay_dict()
            else:
                params['qrcode_id'] = self.qrcode_id
        if self.qrcode_out_id:
            if hasattr(self.qrcode_out_id, 'to_alipay_dict'):
                params['qrcode_out_id'] = self.qrcode_out_id.to_alipay_dict()
            else:
                params['qrcode_out_id'] = self.qrcode_out_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDtbankQrcodedataQueryModel()
        if 'data_date' in d:
            o.data_date = d['data_date']
        if 'qrcode_id' in d:
            o.qrcode_id = d['qrcode_id']
        if 'qrcode_out_id' in d:
            o.qrcode_out_id = d['qrcode_out_id']
        return o


