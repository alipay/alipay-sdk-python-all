#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FqQrCodeExtendParams import FqQrCodeExtendParams


class AlipayPcreditHuabeiIsvOpeninfoModifyModel(object):

    def __init__(self):
        self._ext_info = None
        self._isv_marketing_copy = None
        self._merchant_name = None
        self._out_request_no = None
        self._smid = None
        self._store_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, FqQrCodeExtendParams):
            self._ext_info = value
        else:
            self._ext_info = FqQrCodeExtendParams.from_alipay_dict(value)
    @property
    def isv_marketing_copy(self):
        return self._isv_marketing_copy

    @isv_marketing_copy.setter
    def isv_marketing_copy(self, value):
        self._isv_marketing_copy = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.isv_marketing_copy:
            if hasattr(self.isv_marketing_copy, 'to_alipay_dict'):
                params['isv_marketing_copy'] = self.isv_marketing_copy.to_alipay_dict()
            else:
                params['isv_marketing_copy'] = self.isv_marketing_copy
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
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
        o = AlipayPcreditHuabeiIsvOpeninfoModifyModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'isv_marketing_copy' in d:
            o.isv_marketing_copy = d['isv_marketing_copy']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'smid' in d:
            o.smid = d['smid']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


