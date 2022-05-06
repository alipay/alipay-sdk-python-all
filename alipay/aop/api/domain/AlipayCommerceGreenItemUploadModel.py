#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BelongGreenMerchantInfo import BelongGreenMerchantInfo


class AlipayCommerceGreenItemUploadModel(object):

    def __init__(self):
        self._belong_merchant_info = None
        self._data_operation = None
        self._goods_id = None
        self._goods_name = None
        self._qr_code_list = None
        self._upload_time = None

    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, BelongGreenMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = BelongGreenMerchantInfo.from_alipay_dict(value)
    @property
    def data_operation(self):
        return self._data_operation

    @data_operation.setter
    def data_operation(self, value):
        self._data_operation = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def qr_code_list(self):
        return self._qr_code_list

    @qr_code_list.setter
    def qr_code_list(self, value):
        if isinstance(value, list):
            self._qr_code_list = list()
            for i in value:
                self._qr_code_list.append(i)
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
        if self.data_operation:
            if hasattr(self.data_operation, 'to_alipay_dict'):
                params['data_operation'] = self.data_operation.to_alipay_dict()
            else:
                params['data_operation'] = self.data_operation
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.qr_code_list:
            if isinstance(self.qr_code_list, list):
                for i in range(0, len(self.qr_code_list)):
                    element = self.qr_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qr_code_list[i] = element.to_alipay_dict()
            if hasattr(self.qr_code_list, 'to_alipay_dict'):
                params['qr_code_list'] = self.qr_code_list.to_alipay_dict()
            else:
                params['qr_code_list'] = self.qr_code_list
        if self.upload_time:
            if hasattr(self.upload_time, 'to_alipay_dict'):
                params['upload_time'] = self.upload_time.to_alipay_dict()
            else:
                params['upload_time'] = self.upload_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceGreenItemUploadModel()
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'data_operation' in d:
            o.data_operation = d['data_operation']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'qr_code_list' in d:
            o.qr_code_list = d['qr_code_list']
        if 'upload_time' in d:
            o.upload_time = d['upload_time']
        return o


