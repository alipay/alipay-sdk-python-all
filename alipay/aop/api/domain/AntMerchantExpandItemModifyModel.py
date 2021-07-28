#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemLabelModifyInfo import ItemLabelModifyInfo
from alipay.aop.api.domain.ItemSkuModifyInfo import ItemSkuModifyInfo


class AntMerchantExpandItemModifyModel(object):

    def __init__(self):
        self._detail_url = None
        self._ext_info = None
        self._external_item_id = None
        self._front_category_id = None
        self._item_id = None
        self._label_list = None
        self._main_pic = None
        self._name = None
        self._op_timestamp = None
        self._scene = None
        self._sku_list = None
        self._status = None

    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def external_item_id(self):
        return self._external_item_id

    @external_item_id.setter
    def external_item_id(self, value):
        self._external_item_id = value
    @property
    def front_category_id(self):
        return self._front_category_id

    @front_category_id.setter
    def front_category_id(self, value):
        self._front_category_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def label_list(self):
        return self._label_list

    @label_list.setter
    def label_list(self, value):
        if isinstance(value, list):
            self._label_list = list()
            for i in value:
                if isinstance(i, ItemLabelModifyInfo):
                    self._label_list.append(i)
                else:
                    self._label_list.append(ItemLabelModifyInfo.from_alipay_dict(i))
    @property
    def main_pic(self):
        return self._main_pic

    @main_pic.setter
    def main_pic(self, value):
        self._main_pic = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def op_timestamp(self):
        return self._op_timestamp

    @op_timestamp.setter
    def op_timestamp(self, value):
        self._op_timestamp = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, ItemSkuModifyInfo):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(ItemSkuModifyInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.external_item_id:
            if hasattr(self.external_item_id, 'to_alipay_dict'):
                params['external_item_id'] = self.external_item_id.to_alipay_dict()
            else:
                params['external_item_id'] = self.external_item_id
        if self.front_category_id:
            if hasattr(self.front_category_id, 'to_alipay_dict'):
                params['front_category_id'] = self.front_category_id.to_alipay_dict()
            else:
                params['front_category_id'] = self.front_category_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.label_list:
            if isinstance(self.label_list, list):
                for i in range(0, len(self.label_list)):
                    element = self.label_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_list[i] = element.to_alipay_dict()
            if hasattr(self.label_list, 'to_alipay_dict'):
                params['label_list'] = self.label_list.to_alipay_dict()
            else:
                params['label_list'] = self.label_list
        if self.main_pic:
            if hasattr(self.main_pic, 'to_alipay_dict'):
                params['main_pic'] = self.main_pic.to_alipay_dict()
            else:
                params['main_pic'] = self.main_pic
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.op_timestamp:
            if hasattr(self.op_timestamp, 'to_alipay_dict'):
                params['op_timestamp'] = self.op_timestamp.to_alipay_dict()
            else:
                params['op_timestamp'] = self.op_timestamp
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandItemModifyModel()
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'external_item_id' in d:
            o.external_item_id = d['external_item_id']
        if 'front_category_id' in d:
            o.front_category_id = d['front_category_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'label_list' in d:
            o.label_list = d['label_list']
        if 'main_pic' in d:
            o.main_pic = d['main_pic']
        if 'name' in d:
            o.name = d['name']
        if 'op_timestamp' in d:
            o.op_timestamp = d['op_timestamp']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'status' in d:
            o.status = d['status']
        return o


