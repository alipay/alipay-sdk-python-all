#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantContent import MerchantContent


class AlipayPayDeviceNlinkMerchantSubmitModel(object):

    def __init__(self):
        self._biz_code = None
        self._merchant_content = None
        self._sn = None
        self._sub_biz_code = None
        self._supplier_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def merchant_content(self):
        return self._merchant_content

    @merchant_content.setter
    def merchant_content(self, value):
        if isinstance(value, MerchantContent):
            self._merchant_content = value
        else:
            self._merchant_content = MerchantContent.from_alipay_dict(value)
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def sub_biz_code(self):
        return self._sub_biz_code

    @sub_biz_code.setter
    def sub_biz_code(self, value):
        self._sub_biz_code = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.merchant_content:
            if hasattr(self.merchant_content, 'to_alipay_dict'):
                params['merchant_content'] = self.merchant_content.to_alipay_dict()
            else:
                params['merchant_content'] = self.merchant_content
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.sub_biz_code:
            if hasattr(self.sub_biz_code, 'to_alipay_dict'):
                params['sub_biz_code'] = self.sub_biz_code.to_alipay_dict()
            else:
                params['sub_biz_code'] = self.sub_biz_code
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayDeviceNlinkMerchantSubmitModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'merchant_content' in d:
            o.merchant_content = d['merchant_content']
        if 'sn' in d:
            o.sn = d['sn']
        if 'sub_biz_code' in d:
            o.sub_biz_code = d['sub_biz_code']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


