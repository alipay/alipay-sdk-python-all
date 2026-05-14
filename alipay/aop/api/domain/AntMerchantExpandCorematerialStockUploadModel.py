#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CoreMaterialStockData import CoreMaterialStockData
from alipay.aop.api.domain.CoreMaterialStockDetail import CoreMaterialStockDetail


class AntMerchantExpandCorematerialStockUploadModel(object):

    def __init__(self):
        self._stock_data_list = None
        self._stock_detail_list = None
        self._upload_batch_no = None
        self._upload_type = None

    @property
    def stock_data_list(self):
        return self._stock_data_list

    @stock_data_list.setter
    def stock_data_list(self, value):
        if isinstance(value, list):
            self._stock_data_list = list()
            for i in value:
                if isinstance(i, CoreMaterialStockData):
                    self._stock_data_list.append(i)
                else:
                    self._stock_data_list.append(CoreMaterialStockData.from_alipay_dict(i))
    @property
    def stock_detail_list(self):
        return self._stock_detail_list

    @stock_detail_list.setter
    def stock_detail_list(self, value):
        if isinstance(value, list):
            self._stock_detail_list = list()
            for i in value:
                if isinstance(i, CoreMaterialStockDetail):
                    self._stock_detail_list.append(i)
                else:
                    self._stock_detail_list.append(CoreMaterialStockDetail.from_alipay_dict(i))
    @property
    def upload_batch_no(self):
        return self._upload_batch_no

    @upload_batch_no.setter
    def upload_batch_no(self, value):
        self._upload_batch_no = value
    @property
    def upload_type(self):
        return self._upload_type

    @upload_type.setter
    def upload_type(self, value):
        self._upload_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.stock_data_list:
            if isinstance(self.stock_data_list, list):
                for i in range(0, len(self.stock_data_list)):
                    element = self.stock_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stock_data_list[i] = element.to_alipay_dict()
            if hasattr(self.stock_data_list, 'to_alipay_dict'):
                params['stock_data_list'] = self.stock_data_list.to_alipay_dict()
            else:
                params['stock_data_list'] = self.stock_data_list
        if self.stock_detail_list:
            if isinstance(self.stock_detail_list, list):
                for i in range(0, len(self.stock_detail_list)):
                    element = self.stock_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stock_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.stock_detail_list, 'to_alipay_dict'):
                params['stock_detail_list'] = self.stock_detail_list.to_alipay_dict()
            else:
                params['stock_detail_list'] = self.stock_detail_list
        if self.upload_batch_no:
            if hasattr(self.upload_batch_no, 'to_alipay_dict'):
                params['upload_batch_no'] = self.upload_batch_no.to_alipay_dict()
            else:
                params['upload_batch_no'] = self.upload_batch_no
        if self.upload_type:
            if hasattr(self.upload_type, 'to_alipay_dict'):
                params['upload_type'] = self.upload_type.to_alipay_dict()
            else:
                params['upload_type'] = self.upload_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandCorematerialStockUploadModel()
        if 'stock_data_list' in d:
            o.stock_data_list = d['stock_data_list']
        if 'stock_detail_list' in d:
            o.stock_detail_list = d['stock_detail_list']
        if 'upload_batch_no' in d:
            o.upload_batch_no = d['upload_batch_no']
        if 'upload_type' in d:
            o.upload_type = d['upload_type']
        return o


