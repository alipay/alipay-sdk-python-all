#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FqQrCodeExtendParams import FqQrCodeExtendParams


class AlipayPcreditHuabeiFqqrcodeHbfqBindModel(object):

    def __init__(self):
        self._bind_type = None
        self._code_type = None
        self._fqqr_code_ext_info = None
        self._merchant_id = None
        self._out_request_no = None
        self._qr_code_token = None
        self._smid = None
        self._source = None
        self._store_id = None

    @property
    def bind_type(self):
        return self._bind_type

    @bind_type.setter
    def bind_type(self, value):
        self._bind_type = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def fqqr_code_ext_info(self):
        return self._fqqr_code_ext_info

    @fqqr_code_ext_info.setter
    def fqqr_code_ext_info(self, value):
        if isinstance(value, FqQrCodeExtendParams):
            self._fqqr_code_ext_info = value
        else:
            self._fqqr_code_ext_info = FqQrCodeExtendParams.from_alipay_dict(value)
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def qr_code_token(self):
        return self._qr_code_token

    @qr_code_token.setter
    def qr_code_token(self, value):
        self._qr_code_token = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_type:
            if hasattr(self.bind_type, 'to_alipay_dict'):
                params['bind_type'] = self.bind_type.to_alipay_dict()
            else:
                params['bind_type'] = self.bind_type
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.fqqr_code_ext_info:
            if hasattr(self.fqqr_code_ext_info, 'to_alipay_dict'):
                params['fqqr_code_ext_info'] = self.fqqr_code_ext_info.to_alipay_dict()
            else:
                params['fqqr_code_ext_info'] = self.fqqr_code_ext_info
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.qr_code_token:
            if hasattr(self.qr_code_token, 'to_alipay_dict'):
                params['qr_code_token'] = self.qr_code_token.to_alipay_dict()
            else:
                params['qr_code_token'] = self.qr_code_token
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiFqqrcodeHbfqBindModel()
        if 'bind_type' in d:
            o.bind_type = d['bind_type']
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'fqqr_code_ext_info' in d:
            o.fqqr_code_ext_info = d['fqqr_code_ext_info']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'qr_code_token' in d:
            o.qr_code_token = d['qr_code_token']
        if 'smid' in d:
            o.smid = d['smid']
        if 'source' in d:
            o.source = d['source']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


