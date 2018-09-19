#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishDictionaryQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._dictionary_id = None
        self._ext_info = None
        self._merchant_id = None
        self._status = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def dictionary_id(self):
        return self._dictionary_id

    @dictionary_id.setter
    def dictionary_id(self, value):
        self._dictionary_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.dictionary_id:
            if hasattr(self.dictionary_id, 'to_alipay_dict'):
                params['dictionary_id'] = self.dictionary_id.to_alipay_dict()
            else:
                params['dictionary_id'] = self.dictionary_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishDictionaryQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'dictionary_id' in d:
            o.dictionary_id = d['dictionary_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'status' in d:
            o.status = d['status']
        return o


