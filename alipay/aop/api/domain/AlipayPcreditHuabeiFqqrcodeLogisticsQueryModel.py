#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FqQrCodeExtendParams import FqQrCodeExtendParams


class AlipayPcreditHuabeiFqqrcodeLogisticsQueryModel(object):

    def __init__(self):
        self._fqqr_code_ext_info = None
        self._merchant_id = None
        self._out_request_no = None
        self._process_id = None
        self._source = None

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
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.process_id:
            if hasattr(self.process_id, 'to_alipay_dict'):
                params['process_id'] = self.process_id.to_alipay_dict()
            else:
                params['process_id'] = self.process_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiFqqrcodeLogisticsQueryModel()
        if 'fqqr_code_ext_info' in d:
            o.fqqr_code_ext_info = d['fqqr_code_ext_info']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'process_id' in d:
            o.process_id = d['process_id']
        if 'source' in d:
            o.source = d['source']
        return o


