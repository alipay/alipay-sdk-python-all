#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CVGoodsInfo(object):

    def __init__(self):
        self._algorithm_id = None
        self._big_category = None
        self._category = None
        self._depth = None
        self._gb_code = None
        self._goods_name = None
        self._height = None
        self._img_info = None
        self._main_algorithm_id = None
        self._package_type = None
        self._small_category = None
        self._standard_goods = None
        self._standard_saleable_goods = None
        self._weight_list = None
        self._width = None

    @property
    def algorithm_id(self):
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, value):
        self._algorithm_id = value
    @property
    def big_category(self):
        return self._big_category

    @big_category.setter
    def big_category(self, value):
        self._big_category = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value
    @property
    def gb_code(self):
        return self._gb_code

    @gb_code.setter
    def gb_code(self, value):
        self._gb_code = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def img_info(self):
        return self._img_info

    @img_info.setter
    def img_info(self, value):
        self._img_info = value
    @property
    def main_algorithm_id(self):
        return self._main_algorithm_id

    @main_algorithm_id.setter
    def main_algorithm_id(self, value):
        self._main_algorithm_id = value
    @property
    def package_type(self):
        return self._package_type

    @package_type.setter
    def package_type(self, value):
        self._package_type = value
    @property
    def small_category(self):
        return self._small_category

    @small_category.setter
    def small_category(self, value):
        self._small_category = value
    @property
    def standard_goods(self):
        return self._standard_goods

    @standard_goods.setter
    def standard_goods(self, value):
        self._standard_goods = value
    @property
    def standard_saleable_goods(self):
        return self._standard_saleable_goods

    @standard_saleable_goods.setter
    def standard_saleable_goods(self, value):
        self._standard_saleable_goods = value
    @property
    def weight_list(self):
        return self._weight_list

    @weight_list.setter
    def weight_list(self, value):
        self._weight_list = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_id:
            if hasattr(self.algorithm_id, 'to_alipay_dict'):
                params['algorithm_id'] = self.algorithm_id.to_alipay_dict()
            else:
                params['algorithm_id'] = self.algorithm_id
        if self.big_category:
            if hasattr(self.big_category, 'to_alipay_dict'):
                params['big_category'] = self.big_category.to_alipay_dict()
            else:
                params['big_category'] = self.big_category
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.depth:
            if hasattr(self.depth, 'to_alipay_dict'):
                params['depth'] = self.depth.to_alipay_dict()
            else:
                params['depth'] = self.depth
        if self.gb_code:
            if hasattr(self.gb_code, 'to_alipay_dict'):
                params['gb_code'] = self.gb_code.to_alipay_dict()
            else:
                params['gb_code'] = self.gb_code
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.img_info:
            if hasattr(self.img_info, 'to_alipay_dict'):
                params['img_info'] = self.img_info.to_alipay_dict()
            else:
                params['img_info'] = self.img_info
        if self.main_algorithm_id:
            if hasattr(self.main_algorithm_id, 'to_alipay_dict'):
                params['main_algorithm_id'] = self.main_algorithm_id.to_alipay_dict()
            else:
                params['main_algorithm_id'] = self.main_algorithm_id
        if self.package_type:
            if hasattr(self.package_type, 'to_alipay_dict'):
                params['package_type'] = self.package_type.to_alipay_dict()
            else:
                params['package_type'] = self.package_type
        if self.small_category:
            if hasattr(self.small_category, 'to_alipay_dict'):
                params['small_category'] = self.small_category.to_alipay_dict()
            else:
                params['small_category'] = self.small_category
        if self.standard_goods:
            if hasattr(self.standard_goods, 'to_alipay_dict'):
                params['standard_goods'] = self.standard_goods.to_alipay_dict()
            else:
                params['standard_goods'] = self.standard_goods
        if self.standard_saleable_goods:
            if hasattr(self.standard_saleable_goods, 'to_alipay_dict'):
                params['standard_saleable_goods'] = self.standard_saleable_goods.to_alipay_dict()
            else:
                params['standard_saleable_goods'] = self.standard_saleable_goods
        if self.weight_list:
            if hasattr(self.weight_list, 'to_alipay_dict'):
                params['weight_list'] = self.weight_list.to_alipay_dict()
            else:
                params['weight_list'] = self.weight_list
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CVGoodsInfo()
        if 'algorithm_id' in d:
            o.algorithm_id = d['algorithm_id']
        if 'big_category' in d:
            o.big_category = d['big_category']
        if 'category' in d:
            o.category = d['category']
        if 'depth' in d:
            o.depth = d['depth']
        if 'gb_code' in d:
            o.gb_code = d['gb_code']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'height' in d:
            o.height = d['height']
        if 'img_info' in d:
            o.img_info = d['img_info']
        if 'main_algorithm_id' in d:
            o.main_algorithm_id = d['main_algorithm_id']
        if 'package_type' in d:
            o.package_type = d['package_type']
        if 'small_category' in d:
            o.small_category = d['small_category']
        if 'standard_goods' in d:
            o.standard_goods = d['standard_goods']
        if 'standard_saleable_goods' in d:
            o.standard_saleable_goods = d['standard_saleable_goods']
        if 'weight_list' in d:
            o.weight_list = d['weight_list']
        if 'width' in d:
            o.width = d['width']
        return o


