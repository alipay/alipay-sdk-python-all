#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransInvoiceFromisvnotifyModifyModel(object):

    def __init__(self):
        self._area = None
        self._invoice_code = None
        self._invoice_number = None
        self._is_old_data_sync = None
        self._payer_id_type = None
        self._payer_id_value = None
        self._user_id = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_number(self):
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self._invoice_number = value
    @property
    def is_old_data_sync(self):
        return self._is_old_data_sync

    @is_old_data_sync.setter
    def is_old_data_sync(self, value):
        self._is_old_data_sync = value
    @property
    def payer_id_type(self):
        return self._payer_id_type

    @payer_id_type.setter
    def payer_id_type(self, value):
        self._payer_id_type = value
    @property
    def payer_id_value(self):
        return self._payer_id_value

    @payer_id_value.setter
    def payer_id_value(self, value):
        self._payer_id_value = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_number:
            if hasattr(self.invoice_number, 'to_alipay_dict'):
                params['invoice_number'] = self.invoice_number.to_alipay_dict()
            else:
                params['invoice_number'] = self.invoice_number
        if self.is_old_data_sync:
            if hasattr(self.is_old_data_sync, 'to_alipay_dict'):
                params['is_old_data_sync'] = self.is_old_data_sync.to_alipay_dict()
            else:
                params['is_old_data_sync'] = self.is_old_data_sync
        if self.payer_id_type:
            if hasattr(self.payer_id_type, 'to_alipay_dict'):
                params['payer_id_type'] = self.payer_id_type.to_alipay_dict()
            else:
                params['payer_id_type'] = self.payer_id_type
        if self.payer_id_value:
            if hasattr(self.payer_id_value, 'to_alipay_dict'):
                params['payer_id_value'] = self.payer_id_value.to_alipay_dict()
            else:
                params['payer_id_value'] = self.payer_id_value
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
        o = AlipayFundTransInvoiceFromisvnotifyModifyModel()
        if 'area' in d:
            o.area = d['area']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_number' in d:
            o.invoice_number = d['invoice_number']
        if 'is_old_data_sync' in d:
            o.is_old_data_sync = d['is_old_data_sync']
        if 'payer_id_type' in d:
            o.payer_id_type = d['payer_id_type']
        if 'payer_id_value' in d:
            o.payer_id_value = d['payer_id_value']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


