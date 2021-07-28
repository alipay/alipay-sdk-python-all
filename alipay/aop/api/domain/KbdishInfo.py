#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishPracticeInfo import KbdishPracticeInfo
from alipay.aop.api.domain.KbdishSkuInfo import KbdishSkuInfo
from alipay.aop.api.domain.KbdishMaterialBindingInfo import KbdishMaterialBindingInfo
from alipay.aop.api.domain.KbdishPropertyInfo import KbdishPropertyInfo


class KbdishInfo(object):

    def __init__(self):
        self._catetory_big_id = None
        self._catetory_small_id = None
        self._create_user = None
        self._cur_price_flag = None
        self._default_in_carts = None
        self._default_in_carts_detail = None
        self._dish_cuisine = None
        self._dish_detail_img_list = None
        self._dish_id = None
        self._dish_img = None
        self._dish_name = None
        self._dish_practice_list = None
        self._dish_sku_list = None
        self._dish_version = None
        self._en_remember_code = None
        self._ext_content = None
        self._goods_id = None
        self._material_binding_info_list = None
        self._merchant_id = None
        self._min_serving = None
        self._mini_add_num = None
        self._nb_remember_code = None
        self._not_count_threshold = None
        self._out_dish_id = None
        self._property_info_list = None
        self._remarks = None
        self._shop_id = None
        self._status = None
        self._tags = None
        self._type_big = None
        self._type_small = None
        self._unit_id = None
        self._update_user = None

    @property
    def catetory_big_id(self):
        return self._catetory_big_id

    @catetory_big_id.setter
    def catetory_big_id(self, value):
        self._catetory_big_id = value
    @property
    def catetory_small_id(self):
        return self._catetory_small_id

    @catetory_small_id.setter
    def catetory_small_id(self, value):
        self._catetory_small_id = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def cur_price_flag(self):
        return self._cur_price_flag

    @cur_price_flag.setter
    def cur_price_flag(self, value):
        self._cur_price_flag = value
    @property
    def default_in_carts(self):
        return self._default_in_carts

    @default_in_carts.setter
    def default_in_carts(self, value):
        self._default_in_carts = value
    @property
    def default_in_carts_detail(self):
        return self._default_in_carts_detail

    @default_in_carts_detail.setter
    def default_in_carts_detail(self, value):
        self._default_in_carts_detail = value
    @property
    def dish_cuisine(self):
        return self._dish_cuisine

    @dish_cuisine.setter
    def dish_cuisine(self, value):
        self._dish_cuisine = value
    @property
    def dish_detail_img_list(self):
        return self._dish_detail_img_list

    @dish_detail_img_list.setter
    def dish_detail_img_list(self, value):
        if isinstance(value, list):
            self._dish_detail_img_list = list()
            for i in value:
                self._dish_detail_img_list.append(i)
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_img(self):
        return self._dish_img

    @dish_img.setter
    def dish_img(self, value):
        self._dish_img = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dish_practice_list(self):
        return self._dish_practice_list

    @dish_practice_list.setter
    def dish_practice_list(self, value):
        if isinstance(value, list):
            self._dish_practice_list = list()
            for i in value:
                if isinstance(i, KbdishPracticeInfo):
                    self._dish_practice_list.append(i)
                else:
                    self._dish_practice_list.append(KbdishPracticeInfo.from_alipay_dict(i))
    @property
    def dish_sku_list(self):
        return self._dish_sku_list

    @dish_sku_list.setter
    def dish_sku_list(self, value):
        if isinstance(value, list):
            self._dish_sku_list = list()
            for i in value:
                if isinstance(i, KbdishSkuInfo):
                    self._dish_sku_list.append(i)
                else:
                    self._dish_sku_list.append(KbdishSkuInfo.from_alipay_dict(i))
    @property
    def dish_version(self):
        return self._dish_version

    @dish_version.setter
    def dish_version(self, value):
        self._dish_version = value
    @property
    def en_remember_code(self):
        return self._en_remember_code

    @en_remember_code.setter
    def en_remember_code(self, value):
        self._en_remember_code = value
    @property
    def ext_content(self):
        return self._ext_content

    @ext_content.setter
    def ext_content(self, value):
        self._ext_content = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def material_binding_info_list(self):
        return self._material_binding_info_list

    @material_binding_info_list.setter
    def material_binding_info_list(self, value):
        if isinstance(value, list):
            self._material_binding_info_list = list()
            for i in value:
                if isinstance(i, KbdishMaterialBindingInfo):
                    self._material_binding_info_list.append(i)
                else:
                    self._material_binding_info_list.append(KbdishMaterialBindingInfo.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def min_serving(self):
        return self._min_serving

    @min_serving.setter
    def min_serving(self, value):
        self._min_serving = value
    @property
    def mini_add_num(self):
        return self._mini_add_num

    @mini_add_num.setter
    def mini_add_num(self, value):
        self._mini_add_num = value
    @property
    def nb_remember_code(self):
        return self._nb_remember_code

    @nb_remember_code.setter
    def nb_remember_code(self, value):
        self._nb_remember_code = value
    @property
    def not_count_threshold(self):
        return self._not_count_threshold

    @not_count_threshold.setter
    def not_count_threshold(self, value):
        self._not_count_threshold = value
    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def property_info_list(self):
        return self._property_info_list

    @property_info_list.setter
    def property_info_list(self, value):
        if isinstance(value, list):
            self._property_info_list = list()
            for i in value:
                if isinstance(i, KbdishPropertyInfo):
                    self._property_info_list.append(i)
                else:
                    self._property_info_list.append(KbdishPropertyInfo.from_alipay_dict(i))
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def type_big(self):
        return self._type_big

    @type_big.setter
    def type_big(self, value):
        self._type_big = value
    @property
    def type_small(self):
        return self._type_small

    @type_small.setter
    def type_small(self, value):
        self._type_small = value
    @property
    def unit_id(self):
        return self._unit_id

    @unit_id.setter
    def unit_id(self, value):
        self._unit_id = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_big_id:
            if hasattr(self.catetory_big_id, 'to_alipay_dict'):
                params['catetory_big_id'] = self.catetory_big_id.to_alipay_dict()
            else:
                params['catetory_big_id'] = self.catetory_big_id
        if self.catetory_small_id:
            if hasattr(self.catetory_small_id, 'to_alipay_dict'):
                params['catetory_small_id'] = self.catetory_small_id.to_alipay_dict()
            else:
                params['catetory_small_id'] = self.catetory_small_id
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.cur_price_flag:
            if hasattr(self.cur_price_flag, 'to_alipay_dict'):
                params['cur_price_flag'] = self.cur_price_flag.to_alipay_dict()
            else:
                params['cur_price_flag'] = self.cur_price_flag
        if self.default_in_carts:
            if hasattr(self.default_in_carts, 'to_alipay_dict'):
                params['default_in_carts'] = self.default_in_carts.to_alipay_dict()
            else:
                params['default_in_carts'] = self.default_in_carts
        if self.default_in_carts_detail:
            if hasattr(self.default_in_carts_detail, 'to_alipay_dict'):
                params['default_in_carts_detail'] = self.default_in_carts_detail.to_alipay_dict()
            else:
                params['default_in_carts_detail'] = self.default_in_carts_detail
        if self.dish_cuisine:
            if hasattr(self.dish_cuisine, 'to_alipay_dict'):
                params['dish_cuisine'] = self.dish_cuisine.to_alipay_dict()
            else:
                params['dish_cuisine'] = self.dish_cuisine
        if self.dish_detail_img_list:
            if isinstance(self.dish_detail_img_list, list):
                for i in range(0, len(self.dish_detail_img_list)):
                    element = self.dish_detail_img_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_detail_img_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_detail_img_list, 'to_alipay_dict'):
                params['dish_detail_img_list'] = self.dish_detail_img_list.to_alipay_dict()
            else:
                params['dish_detail_img_list'] = self.dish_detail_img_list
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_img:
            if hasattr(self.dish_img, 'to_alipay_dict'):
                params['dish_img'] = self.dish_img.to_alipay_dict()
            else:
                params['dish_img'] = self.dish_img
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dish_practice_list:
            if isinstance(self.dish_practice_list, list):
                for i in range(0, len(self.dish_practice_list)):
                    element = self.dish_practice_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_practice_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_practice_list, 'to_alipay_dict'):
                params['dish_practice_list'] = self.dish_practice_list.to_alipay_dict()
            else:
                params['dish_practice_list'] = self.dish_practice_list
        if self.dish_sku_list:
            if isinstance(self.dish_sku_list, list):
                for i in range(0, len(self.dish_sku_list)):
                    element = self.dish_sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_sku_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_sku_list, 'to_alipay_dict'):
                params['dish_sku_list'] = self.dish_sku_list.to_alipay_dict()
            else:
                params['dish_sku_list'] = self.dish_sku_list
        if self.dish_version:
            if hasattr(self.dish_version, 'to_alipay_dict'):
                params['dish_version'] = self.dish_version.to_alipay_dict()
            else:
                params['dish_version'] = self.dish_version
        if self.en_remember_code:
            if hasattr(self.en_remember_code, 'to_alipay_dict'):
                params['en_remember_code'] = self.en_remember_code.to_alipay_dict()
            else:
                params['en_remember_code'] = self.en_remember_code
        if self.ext_content:
            if hasattr(self.ext_content, 'to_alipay_dict'):
                params['ext_content'] = self.ext_content.to_alipay_dict()
            else:
                params['ext_content'] = self.ext_content
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.material_binding_info_list:
            if isinstance(self.material_binding_info_list, list):
                for i in range(0, len(self.material_binding_info_list)):
                    element = self.material_binding_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_binding_info_list[i] = element.to_alipay_dict()
            if hasattr(self.material_binding_info_list, 'to_alipay_dict'):
                params['material_binding_info_list'] = self.material_binding_info_list.to_alipay_dict()
            else:
                params['material_binding_info_list'] = self.material_binding_info_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.min_serving:
            if hasattr(self.min_serving, 'to_alipay_dict'):
                params['min_serving'] = self.min_serving.to_alipay_dict()
            else:
                params['min_serving'] = self.min_serving
        if self.mini_add_num:
            if hasattr(self.mini_add_num, 'to_alipay_dict'):
                params['mini_add_num'] = self.mini_add_num.to_alipay_dict()
            else:
                params['mini_add_num'] = self.mini_add_num
        if self.nb_remember_code:
            if hasattr(self.nb_remember_code, 'to_alipay_dict'):
                params['nb_remember_code'] = self.nb_remember_code.to_alipay_dict()
            else:
                params['nb_remember_code'] = self.nb_remember_code
        if self.not_count_threshold:
            if hasattr(self.not_count_threshold, 'to_alipay_dict'):
                params['not_count_threshold'] = self.not_count_threshold.to_alipay_dict()
            else:
                params['not_count_threshold'] = self.not_count_threshold
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.property_info_list:
            if isinstance(self.property_info_list, list):
                for i in range(0, len(self.property_info_list)):
                    element = self.property_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_info_list[i] = element.to_alipay_dict()
            if hasattr(self.property_info_list, 'to_alipay_dict'):
                params['property_info_list'] = self.property_info_list.to_alipay_dict()
            else:
                params['property_info_list'] = self.property_info_list
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.type_big:
            if hasattr(self.type_big, 'to_alipay_dict'):
                params['type_big'] = self.type_big.to_alipay_dict()
            else:
                params['type_big'] = self.type_big
        if self.type_small:
            if hasattr(self.type_small, 'to_alipay_dict'):
                params['type_small'] = self.type_small.to_alipay_dict()
            else:
                params['type_small'] = self.type_small
        if self.unit_id:
            if hasattr(self.unit_id, 'to_alipay_dict'):
                params['unit_id'] = self.unit_id.to_alipay_dict()
            else:
                params['unit_id'] = self.unit_id
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishInfo()
        if 'catetory_big_id' in d:
            o.catetory_big_id = d['catetory_big_id']
        if 'catetory_small_id' in d:
            o.catetory_small_id = d['catetory_small_id']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'cur_price_flag' in d:
            o.cur_price_flag = d['cur_price_flag']
        if 'default_in_carts' in d:
            o.default_in_carts = d['default_in_carts']
        if 'default_in_carts_detail' in d:
            o.default_in_carts_detail = d['default_in_carts_detail']
        if 'dish_cuisine' in d:
            o.dish_cuisine = d['dish_cuisine']
        if 'dish_detail_img_list' in d:
            o.dish_detail_img_list = d['dish_detail_img_list']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_img' in d:
            o.dish_img = d['dish_img']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_practice_list' in d:
            o.dish_practice_list = d['dish_practice_list']
        if 'dish_sku_list' in d:
            o.dish_sku_list = d['dish_sku_list']
        if 'dish_version' in d:
            o.dish_version = d['dish_version']
        if 'en_remember_code' in d:
            o.en_remember_code = d['en_remember_code']
        if 'ext_content' in d:
            o.ext_content = d['ext_content']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'material_binding_info_list' in d:
            o.material_binding_info_list = d['material_binding_info_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'min_serving' in d:
            o.min_serving = d['min_serving']
        if 'mini_add_num' in d:
            o.mini_add_num = d['mini_add_num']
        if 'nb_remember_code' in d:
            o.nb_remember_code = d['nb_remember_code']
        if 'not_count_threshold' in d:
            o.not_count_threshold = d['not_count_threshold']
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'property_info_list' in d:
            o.property_info_list = d['property_info_list']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'tags' in d:
            o.tags = d['tags']
        if 'type_big' in d:
            o.type_big = d['type_big']
        if 'type_small' in d:
            o.type_small = d['type_small']
        if 'unit_id' in d:
            o.unit_id = d['unit_id']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


