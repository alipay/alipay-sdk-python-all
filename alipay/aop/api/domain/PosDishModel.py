#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosChooseDishGroupModel import PosChooseDishGroupModel
from alipay.aop.api.domain.PosSkuModel import PosSkuModel
from alipay.aop.api.domain.PosFixedDishGroupModel import PosFixedDishGroupModel
from alipay.aop.api.domain.PosDishMaterialModel import PosDishMaterialModel
from alipay.aop.api.domain.PosDishPracticeModel import PosDishPracticeModel
from alipay.aop.api.domain.PosStallModel import PosStallModel


class PosDishModel(object):

    def __init__(self):
        self._category_big_id = None
        self._choose_dish_group_list = None
        self._cook_id = None
        self._create_user = None
        self._dish_id = None
        self._dish_img = None
        self._dish_name = None
        self._dish_sku_list = None
        self._en_remember_code = None
        self._fixed_dish_group_list = None
        self._making_time = None
        self._material_list = None
        self._max_copies_per_time = None
        self._min_serving = None
        self._nb_remember_code = None
        self._practice_list = None
        self._remarks = None
        self._sell_price = None
        self._shop_id = None
        self._stall_list = None
        self._status = None
        self._sync_type = None
        self._tags = None
        self._type_big = None
        self._type_small = None
        self._unit_name = None
        self._update_user = None

    @property
    def category_big_id(self):
        return self._category_big_id

    @category_big_id.setter
    def category_big_id(self, value):
        self._category_big_id = value
    @property
    def choose_dish_group_list(self):
        return self._choose_dish_group_list

    @choose_dish_group_list.setter
    def choose_dish_group_list(self, value):
        if isinstance(value, list):
            self._choose_dish_group_list = list()
            for i in value:
                if isinstance(i, PosChooseDishGroupModel):
                    self._choose_dish_group_list.append(i)
                else:
                    self._choose_dish_group_list.append(PosChooseDishGroupModel.from_alipay_dict(i))
    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
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
    def dish_sku_list(self):
        return self._dish_sku_list

    @dish_sku_list.setter
    def dish_sku_list(self, value):
        if isinstance(value, list):
            self._dish_sku_list = list()
            for i in value:
                if isinstance(i, PosSkuModel):
                    self._dish_sku_list.append(i)
                else:
                    self._dish_sku_list.append(PosSkuModel.from_alipay_dict(i))
    @property
    def en_remember_code(self):
        return self._en_remember_code

    @en_remember_code.setter
    def en_remember_code(self, value):
        self._en_remember_code = value
    @property
    def fixed_dish_group_list(self):
        return self._fixed_dish_group_list

    @fixed_dish_group_list.setter
    def fixed_dish_group_list(self, value):
        if isinstance(value, list):
            self._fixed_dish_group_list = list()
            for i in value:
                if isinstance(i, PosFixedDishGroupModel):
                    self._fixed_dish_group_list.append(i)
                else:
                    self._fixed_dish_group_list.append(PosFixedDishGroupModel.from_alipay_dict(i))
    @property
    def making_time(self):
        return self._making_time

    @making_time.setter
    def making_time(self, value):
        self._making_time = value
    @property
    def material_list(self):
        return self._material_list

    @material_list.setter
    def material_list(self, value):
        if isinstance(value, list):
            self._material_list = list()
            for i in value:
                if isinstance(i, PosDishMaterialModel):
                    self._material_list.append(i)
                else:
                    self._material_list.append(PosDishMaterialModel.from_alipay_dict(i))
    @property
    def max_copies_per_time(self):
        return self._max_copies_per_time

    @max_copies_per_time.setter
    def max_copies_per_time(self, value):
        self._max_copies_per_time = value
    @property
    def min_serving(self):
        return self._min_serving

    @min_serving.setter
    def min_serving(self, value):
        self._min_serving = value
    @property
    def nb_remember_code(self):
        return self._nb_remember_code

    @nb_remember_code.setter
    def nb_remember_code(self, value):
        self._nb_remember_code = value
    @property
    def practice_list(self):
        return self._practice_list

    @practice_list.setter
    def practice_list(self, value):
        if isinstance(value, list):
            self._practice_list = list()
            for i in value:
                if isinstance(i, PosDishPracticeModel):
                    self._practice_list.append(i)
                else:
                    self._practice_list.append(PosDishPracticeModel.from_alipay_dict(i))
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def stall_list(self):
        return self._stall_list

    @stall_list.setter
    def stall_list(self, value):
        if isinstance(value, list):
            self._stall_list = list()
            for i in value:
                if isinstance(i, PosStallModel):
                    self._stall_list.append(i)
                else:
                    self._stall_list.append(PosStallModel.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value
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
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_big_id:
            if hasattr(self.category_big_id, 'to_alipay_dict'):
                params['category_big_id'] = self.category_big_id.to_alipay_dict()
            else:
                params['category_big_id'] = self.category_big_id
        if self.choose_dish_group_list:
            if isinstance(self.choose_dish_group_list, list):
                for i in range(0, len(self.choose_dish_group_list)):
                    element = self.choose_dish_group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.choose_dish_group_list[i] = element.to_alipay_dict()
            if hasattr(self.choose_dish_group_list, 'to_alipay_dict'):
                params['choose_dish_group_list'] = self.choose_dish_group_list.to_alipay_dict()
            else:
                params['choose_dish_group_list'] = self.choose_dish_group_list
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
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
        if self.en_remember_code:
            if hasattr(self.en_remember_code, 'to_alipay_dict'):
                params['en_remember_code'] = self.en_remember_code.to_alipay_dict()
            else:
                params['en_remember_code'] = self.en_remember_code
        if self.fixed_dish_group_list:
            if isinstance(self.fixed_dish_group_list, list):
                for i in range(0, len(self.fixed_dish_group_list)):
                    element = self.fixed_dish_group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fixed_dish_group_list[i] = element.to_alipay_dict()
            if hasattr(self.fixed_dish_group_list, 'to_alipay_dict'):
                params['fixed_dish_group_list'] = self.fixed_dish_group_list.to_alipay_dict()
            else:
                params['fixed_dish_group_list'] = self.fixed_dish_group_list
        if self.making_time:
            if hasattr(self.making_time, 'to_alipay_dict'):
                params['making_time'] = self.making_time.to_alipay_dict()
            else:
                params['making_time'] = self.making_time
        if self.material_list:
            if isinstance(self.material_list, list):
                for i in range(0, len(self.material_list)):
                    element = self.material_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_list[i] = element.to_alipay_dict()
            if hasattr(self.material_list, 'to_alipay_dict'):
                params['material_list'] = self.material_list.to_alipay_dict()
            else:
                params['material_list'] = self.material_list
        if self.max_copies_per_time:
            if hasattr(self.max_copies_per_time, 'to_alipay_dict'):
                params['max_copies_per_time'] = self.max_copies_per_time.to_alipay_dict()
            else:
                params['max_copies_per_time'] = self.max_copies_per_time
        if self.min_serving:
            if hasattr(self.min_serving, 'to_alipay_dict'):
                params['min_serving'] = self.min_serving.to_alipay_dict()
            else:
                params['min_serving'] = self.min_serving
        if self.nb_remember_code:
            if hasattr(self.nb_remember_code, 'to_alipay_dict'):
                params['nb_remember_code'] = self.nb_remember_code.to_alipay_dict()
            else:
                params['nb_remember_code'] = self.nb_remember_code
        if self.practice_list:
            if isinstance(self.practice_list, list):
                for i in range(0, len(self.practice_list)):
                    element = self.practice_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.practice_list[i] = element.to_alipay_dict()
            if hasattr(self.practice_list, 'to_alipay_dict'):
                params['practice_list'] = self.practice_list.to_alipay_dict()
            else:
                params['practice_list'] = self.practice_list
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.stall_list:
            if isinstance(self.stall_list, list):
                for i in range(0, len(self.stall_list)):
                    element = self.stall_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stall_list[i] = element.to_alipay_dict()
            if hasattr(self.stall_list, 'to_alipay_dict'):
                params['stall_list'] = self.stall_list.to_alipay_dict()
            else:
                params['stall_list'] = self.stall_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
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
        if self.unit_name:
            if hasattr(self.unit_name, 'to_alipay_dict'):
                params['unit_name'] = self.unit_name.to_alipay_dict()
            else:
                params['unit_name'] = self.unit_name
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
        o = PosDishModel()
        if 'category_big_id' in d:
            o.category_big_id = d['category_big_id']
        if 'choose_dish_group_list' in d:
            o.choose_dish_group_list = d['choose_dish_group_list']
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_img' in d:
            o.dish_img = d['dish_img']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_sku_list' in d:
            o.dish_sku_list = d['dish_sku_list']
        if 'en_remember_code' in d:
            o.en_remember_code = d['en_remember_code']
        if 'fixed_dish_group_list' in d:
            o.fixed_dish_group_list = d['fixed_dish_group_list']
        if 'making_time' in d:
            o.making_time = d['making_time']
        if 'material_list' in d:
            o.material_list = d['material_list']
        if 'max_copies_per_time' in d:
            o.max_copies_per_time = d['max_copies_per_time']
        if 'min_serving' in d:
            o.min_serving = d['min_serving']
        if 'nb_remember_code' in d:
            o.nb_remember_code = d['nb_remember_code']
        if 'practice_list' in d:
            o.practice_list = d['practice_list']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'stall_list' in d:
            o.stall_list = d['stall_list']
        if 'status' in d:
            o.status = d['status']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        if 'tags' in d:
            o.tags = d['tags']
        if 'type_big' in d:
            o.type_big = d['type_big']
        if 'type_small' in d:
            o.type_small = d['type_small']
        if 'unit_name' in d:
            o.unit_name = d['unit_name']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


