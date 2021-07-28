#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransInvoiceSyncdataModifyModel(object):

    def __init__(self):
        self._amount = None
        self._area = None
        self._file_type = None
        self._invoice_code = None
        self._invoice_name = None
        self._invoice_number = None
        self._invoice_type = None
        self._is_block = None
        self._is_old_data_sync = None
        self._open_biz_no = None
        self._party_code = None
        self._party_name = None
        self._payer_id = None
        self._payer_id_type = None
        self._payer_id_value = None
        self._payer_name = None
        self._status = None
        self._time = None
        self._type = None
        self._url = None
        self._user_id = None
        self._verify = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_name(self):
        return self._invoice_name

    @invoice_name.setter
    def invoice_name(self, value):
        self._invoice_name = value
    @property
    def invoice_number(self):
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self._invoice_number = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def is_block(self):
        return self._is_block

    @is_block.setter
    def is_block(self, value):
        self._is_block = value
    @property
    def is_old_data_sync(self):
        return self._is_old_data_sync

    @is_old_data_sync.setter
    def is_old_data_sync(self, value):
        self._is_old_data_sync = value
    @property
    def open_biz_no(self):
        return self._open_biz_no

    @open_biz_no.setter
    def open_biz_no(self, value):
        self._open_biz_no = value
    @property
    def party_code(self):
        return self._party_code

    @party_code.setter
    def party_code(self, value):
        self._party_code = value
    @property
    def party_name(self):
        return self._party_name

    @party_name.setter
    def party_name(self, value):
        self._party_name = value
    @property
    def payer_id(self):
        return self._payer_id

    @payer_id.setter
    def payer_id(self, value):
        self._payer_id = value
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
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def verify(self):
        return self._verify

    @verify.setter
    def verify(self, value):
        self._verify = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_name:
            if hasattr(self.invoice_name, 'to_alipay_dict'):
                params['invoice_name'] = self.invoice_name.to_alipay_dict()
            else:
                params['invoice_name'] = self.invoice_name
        if self.invoice_number:
            if hasattr(self.invoice_number, 'to_alipay_dict'):
                params['invoice_number'] = self.invoice_number.to_alipay_dict()
            else:
                params['invoice_number'] = self.invoice_number
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.is_block:
            if hasattr(self.is_block, 'to_alipay_dict'):
                params['is_block'] = self.is_block.to_alipay_dict()
            else:
                params['is_block'] = self.is_block
        if self.is_old_data_sync:
            if hasattr(self.is_old_data_sync, 'to_alipay_dict'):
                params['is_old_data_sync'] = self.is_old_data_sync.to_alipay_dict()
            else:
                params['is_old_data_sync'] = self.is_old_data_sync
        if self.open_biz_no:
            if hasattr(self.open_biz_no, 'to_alipay_dict'):
                params['open_biz_no'] = self.open_biz_no.to_alipay_dict()
            else:
                params['open_biz_no'] = self.open_biz_no
        if self.party_code:
            if hasattr(self.party_code, 'to_alipay_dict'):
                params['party_code'] = self.party_code.to_alipay_dict()
            else:
                params['party_code'] = self.party_code
        if self.party_name:
            if hasattr(self.party_name, 'to_alipay_dict'):
                params['party_name'] = self.party_name.to_alipay_dict()
            else:
                params['party_name'] = self.party_name
        if self.payer_id:
            if hasattr(self.payer_id, 'to_alipay_dict'):
                params['payer_id'] = self.payer_id.to_alipay_dict()
            else:
                params['payer_id'] = self.payer_id
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
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.verify:
            if hasattr(self.verify, 'to_alipay_dict'):
                params['verify'] = self.verify.to_alipay_dict()
            else:
                params['verify'] = self.verify
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransInvoiceSyncdataModifyModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'area' in d:
            o.area = d['area']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_name' in d:
            o.invoice_name = d['invoice_name']
        if 'invoice_number' in d:
            o.invoice_number = d['invoice_number']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'is_block' in d:
            o.is_block = d['is_block']
        if 'is_old_data_sync' in d:
            o.is_old_data_sync = d['is_old_data_sync']
        if 'open_biz_no' in d:
            o.open_biz_no = d['open_biz_no']
        if 'party_code' in d:
            o.party_code = d['party_code']
        if 'party_name' in d:
            o.party_name = d['party_name']
        if 'payer_id' in d:
            o.payer_id = d['payer_id']
        if 'payer_id_type' in d:
            o.payer_id_type = d['payer_id_type']
        if 'payer_id_value' in d:
            o.payer_id_value = d['payer_id_value']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'status' in d:
            o.status = d['status']
        if 'time' in d:
            o.time = d['time']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'verify' in d:
            o.verify = d['verify']
        return o


