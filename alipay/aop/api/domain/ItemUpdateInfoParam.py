#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SkuUpdateInfoParam import SkuUpdateInfoParam


class ItemUpdateInfoParam(object):

    def __init__(self):
        self._insurance = None
        self._insurance_code = None
        self._item_code = None
        self._sku_list = None
        self._status = None
        self._tag_code = None

    @property
    def insurance(self):
        return self._insurance

    @insurance.setter
    def insurance(self, value):
        self._insurance = value
    @property
    def insurance_code(self):
        return self._insurance_code

    @insurance_code.setter
    def insurance_code(self, value):
        self._insurance_code = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, SkuUpdateInfoParam):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(SkuUpdateInfoParam.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.insurance:
            if hasattr(self.insurance, 'to_alipay_dict'):
                params['insurance'] = self.insurance.to_alipay_dict()
            else:
                params['insurance'] = self.insurance
        if self.insurance_code:
            if hasattr(self.insurance_code, 'to_alipay_dict'):
                params['insurance_code'] = self.insurance_code.to_alipay_dict()
            else:
                params['insurance_code'] = self.insurance_code
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemUpdateInfoParam()
        if 'insurance' in d:
            o.insurance = d['insurance']
        if 'insurance_code' in d:
            o.insurance_code = d['insurance_code']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'status' in d:
            o.status = d['status']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        return o


