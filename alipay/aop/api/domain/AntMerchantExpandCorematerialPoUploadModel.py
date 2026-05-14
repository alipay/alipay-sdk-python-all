#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CoreMaterialPoData import CoreMaterialPoData


class AntMerchantExpandCorematerialPoUploadModel(object):

    def __init__(self):
        self._po_data_list = None
        self._supplier_id = None
        self._supplier_name = None
        self._upload_type = None

    @property
    def po_data_list(self):
        return self._po_data_list

    @po_data_list.setter
    def po_data_list(self, value):
        if isinstance(value, list):
            self._po_data_list = list()
            for i in value:
                if isinstance(i, CoreMaterialPoData):
                    self._po_data_list.append(i)
                else:
                    self._po_data_list.append(CoreMaterialPoData.from_alipay_dict(i))
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value):
        self._supplier_name = value
    @property
    def upload_type(self):
        return self._upload_type

    @upload_type.setter
    def upload_type(self, value):
        self._upload_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.po_data_list:
            if isinstance(self.po_data_list, list):
                for i in range(0, len(self.po_data_list)):
                    element = self.po_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.po_data_list[i] = element.to_alipay_dict()
            if hasattr(self.po_data_list, 'to_alipay_dict'):
                params['po_data_list'] = self.po_data_list.to_alipay_dict()
            else:
                params['po_data_list'] = self.po_data_list
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_name:
            if hasattr(self.supplier_name, 'to_alipay_dict'):
                params['supplier_name'] = self.supplier_name.to_alipay_dict()
            else:
                params['supplier_name'] = self.supplier_name
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
        o = AntMerchantExpandCorematerialPoUploadModel()
        if 'po_data_list' in d:
            o.po_data_list = d['po_data_list']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_name' in d:
            o.supplier_name = d['supplier_name']
        if 'upload_type' in d:
            o.upload_type = d['upload_type']
        return o


