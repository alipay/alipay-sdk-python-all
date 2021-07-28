#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmpeDeviceModelInfo import AmpeDeviceModelInfo


class AmpeProductInfo(object):

    def __init__(self):
        self._category_desc = None
        self._category_id = None
        self._device_model_list = None
        self._device_type = None
        self._device_type_desc = None
        self._gmt_create = None
        self._gmt_modified = None
        self._invoke_app_id = None
        self._product_id = None
        self._product_name = None
        self._product_pic = None
        self._reject_memo = None
        self._ship_quantity = None
        self._status = None
        self._status_desc = None

    @property
    def category_desc(self):
        return self._category_desc

    @category_desc.setter
    def category_desc(self, value):
        self._category_desc = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def device_model_list(self):
        return self._device_model_list

    @device_model_list.setter
    def device_model_list(self, value):
        if isinstance(value, list):
            self._device_model_list = list()
            for i in value:
                if isinstance(i, AmpeDeviceModelInfo):
                    self._device_model_list.append(i)
                else:
                    self._device_model_list.append(AmpeDeviceModelInfo.from_alipay_dict(i))
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def device_type_desc(self):
        return self._device_type_desc

    @device_type_desc.setter
    def device_type_desc(self, value):
        self._device_type_desc = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def invoke_app_id(self):
        return self._invoke_app_id

    @invoke_app_id.setter
    def invoke_app_id(self, value):
        self._invoke_app_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_pic(self):
        return self._product_pic

    @product_pic.setter
    def product_pic(self, value):
        self._product_pic = value
    @property
    def reject_memo(self):
        return self._reject_memo

    @reject_memo.setter
    def reject_memo(self, value):
        self._reject_memo = value
    @property
    def ship_quantity(self):
        return self._ship_quantity

    @ship_quantity.setter
    def ship_quantity(self, value):
        self._ship_quantity = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_desc:
            if hasattr(self.category_desc, 'to_alipay_dict'):
                params['category_desc'] = self.category_desc.to_alipay_dict()
            else:
                params['category_desc'] = self.category_desc
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.device_model_list:
            if isinstance(self.device_model_list, list):
                for i in range(0, len(self.device_model_list)):
                    element = self.device_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_model_list[i] = element.to_alipay_dict()
            if hasattr(self.device_model_list, 'to_alipay_dict'):
                params['device_model_list'] = self.device_model_list.to_alipay_dict()
            else:
                params['device_model_list'] = self.device_model_list
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.device_type_desc:
            if hasattr(self.device_type_desc, 'to_alipay_dict'):
                params['device_type_desc'] = self.device_type_desc.to_alipay_dict()
            else:
                params['device_type_desc'] = self.device_type_desc
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.invoke_app_id:
            if hasattr(self.invoke_app_id, 'to_alipay_dict'):
                params['invoke_app_id'] = self.invoke_app_id.to_alipay_dict()
            else:
                params['invoke_app_id'] = self.invoke_app_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_pic:
            if hasattr(self.product_pic, 'to_alipay_dict'):
                params['product_pic'] = self.product_pic.to_alipay_dict()
            else:
                params['product_pic'] = self.product_pic
        if self.reject_memo:
            if hasattr(self.reject_memo, 'to_alipay_dict'):
                params['reject_memo'] = self.reject_memo.to_alipay_dict()
            else:
                params['reject_memo'] = self.reject_memo
        if self.ship_quantity:
            if hasattr(self.ship_quantity, 'to_alipay_dict'):
                params['ship_quantity'] = self.ship_quantity.to_alipay_dict()
            else:
                params['ship_quantity'] = self.ship_quantity
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmpeProductInfo()
        if 'category_desc' in d:
            o.category_desc = d['category_desc']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'device_model_list' in d:
            o.device_model_list = d['device_model_list']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'device_type_desc' in d:
            o.device_type_desc = d['device_type_desc']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'invoke_app_id' in d:
            o.invoke_app_id = d['invoke_app_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_pic' in d:
            o.product_pic = d['product_pic']
        if 'reject_memo' in d:
            o.reject_memo = d['reject_memo']
        if 'ship_quantity' in d:
            o.ship_quantity = d['ship_quantity']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        return o


