#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedicineItemCreateModel(object):

    def __init__(self):
        self._alipay_store_id = None
        self._delivery_id = None
        self._insurance_flag = None
        self._main_image = None
        self._name = None
        self._original_price = None
        self._other_images = None
        self._out_item_id = None
        self._path = None
        self._sale_price = None
        self._sale_status = None
        self._stock_num = None
        self._upc = None

    @property
    def alipay_store_id(self):
        return self._alipay_store_id

    @alipay_store_id.setter
    def alipay_store_id(self, value):
        self._alipay_store_id = value
    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def insurance_flag(self):
        return self._insurance_flag

    @insurance_flag.setter
    def insurance_flag(self, value):
        self._insurance_flag = value
    @property
    def main_image(self):
        return self._main_image

    @main_image.setter
    def main_image(self, value):
        self._main_image = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def other_images(self):
        return self._other_images

    @other_images.setter
    def other_images(self, value):
        if isinstance(value, list):
            self._other_images = list()
            for i in value:
                self._other_images.append(i)
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def upc(self):
        return self._upc

    @upc.setter
    def upc(self, value):
        self._upc = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_store_id:
            if hasattr(self.alipay_store_id, 'to_alipay_dict'):
                params['alipay_store_id'] = self.alipay_store_id.to_alipay_dict()
            else:
                params['alipay_store_id'] = self.alipay_store_id
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
        if self.insurance_flag:
            if hasattr(self.insurance_flag, 'to_alipay_dict'):
                params['insurance_flag'] = self.insurance_flag.to_alipay_dict()
            else:
                params['insurance_flag'] = self.insurance_flag
        if self.main_image:
            if hasattr(self.main_image, 'to_alipay_dict'):
                params['main_image'] = self.main_image.to_alipay_dict()
            else:
                params['main_image'] = self.main_image
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.other_images:
            if isinstance(self.other_images, list):
                for i in range(0, len(self.other_images)):
                    element = self.other_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_images[i] = element.to_alipay_dict()
            if hasattr(self.other_images, 'to_alipay_dict'):
                params['other_images'] = self.other_images.to_alipay_dict()
            else:
                params['other_images'] = self.other_images
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.upc:
            if hasattr(self.upc, 'to_alipay_dict'):
                params['upc'] = self.upc.to_alipay_dict()
            else:
                params['upc'] = self.upc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedicineItemCreateModel()
        if 'alipay_store_id' in d:
            o.alipay_store_id = d['alipay_store_id']
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'insurance_flag' in d:
            o.insurance_flag = d['insurance_flag']
        if 'main_image' in d:
            o.main_image = d['main_image']
        if 'name' in d:
            o.name = d['name']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'other_images' in d:
            o.other_images = d['other_images']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'path' in d:
            o.path = d['path']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'upc' in d:
            o.upc = d['upc']
        return o


