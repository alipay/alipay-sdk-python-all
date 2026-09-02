#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentZatSellerPublishModel(object):

    def __init__(self):
        self._biz_order_id = None
        self._operate_type = None
        self._sub_merchant_id = None
        self._sub_smid = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def sub_smid(self):
        return self._sub_smid

    @sub_smid.setter
    def sub_smid(self, value):
        self._sub_smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.sub_smid:
            if hasattr(self.sub_smid, 'to_alipay_dict'):
                params['sub_smid'] = self.sub_smid.to_alipay_dict()
            else:
                params['sub_smid'] = self.sub_smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentZatSellerPublishModel()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'sub_smid' in d:
            o.sub_smid = d['sub_smid']
        return o


