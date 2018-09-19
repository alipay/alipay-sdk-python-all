#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountInfos import DiscountInfos
from alipay.aop.api.domain.SelectedMealInfo import SelectedMealInfo


class DishList(object):

    def __init__(self):
        self._amount = None
        self._batch_no = None
        self._discount_amount = None
        self._discount_infos = None
        self._dish_id = None
        self._dish_name = None
        self._dish_type = None
        self._ext_infos = None
        self._num = None
        self._out_detail_id = None
        self._out_dish_id = None
        self._out_dish_infos = None
        self._out_sku_id = None
        self._price = None
        self._selected_meal_info = None
        self._sku_id = None
        self._status = None
        self._temporary_dish = None
        self._unit = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_infos(self):
        return self._discount_infos

    @discount_infos.setter
    def discount_infos(self, value):
        if isinstance(value, list):
            self._discount_infos = list()
            for i in value:
                if isinstance(i, DiscountInfos):
                    self._discount_infos.append(i)
                else:
                    self._discount_infos.append(DiscountInfos.from_alipay_dict(i))
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dish_type(self):
        return self._dish_type

    @dish_type.setter
    def dish_type(self, value):
        self._dish_type = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def out_detail_id(self):
        return self._out_detail_id

    @out_detail_id.setter
    def out_detail_id(self, value):
        self._out_detail_id = value
    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def out_dish_infos(self):
        return self._out_dish_infos

    @out_dish_infos.setter
    def out_dish_infos(self, value):
        self._out_dish_infos = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def selected_meal_info(self):
        return self._selected_meal_info

    @selected_meal_info.setter
    def selected_meal_info(self, value):
        if isinstance(value, list):
            self._selected_meal_info = list()
            for i in value:
                if isinstance(i, SelectedMealInfo):
                    self._selected_meal_info.append(i)
                else:
                    self._selected_meal_info.append(SelectedMealInfo.from_alipay_dict(i))
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def temporary_dish(self):
        return self._temporary_dish

    @temporary_dish.setter
    def temporary_dish(self, value):
        self._temporary_dish = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_infos:
            if isinstance(self.discount_infos, list):
                for i in range(0, len(self.discount_infos)):
                    element = self.discount_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_infos[i] = element.to_alipay_dict()
            if hasattr(self.discount_infos, 'to_alipay_dict'):
                params['discount_infos'] = self.discount_infos.to_alipay_dict()
            else:
                params['discount_infos'] = self.discount_infos
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dish_type:
            if hasattr(self.dish_type, 'to_alipay_dict'):
                params['dish_type'] = self.dish_type.to_alipay_dict()
            else:
                params['dish_type'] = self.dish_type
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.out_detail_id:
            if hasattr(self.out_detail_id, 'to_alipay_dict'):
                params['out_detail_id'] = self.out_detail_id.to_alipay_dict()
            else:
                params['out_detail_id'] = self.out_detail_id
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.out_dish_infos:
            if hasattr(self.out_dish_infos, 'to_alipay_dict'):
                params['out_dish_infos'] = self.out_dish_infos.to_alipay_dict()
            else:
                params['out_dish_infos'] = self.out_dish_infos
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.selected_meal_info:
            if isinstance(self.selected_meal_info, list):
                for i in range(0, len(self.selected_meal_info)):
                    element = self.selected_meal_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.selected_meal_info[i] = element.to_alipay_dict()
            if hasattr(self.selected_meal_info, 'to_alipay_dict'):
                params['selected_meal_info'] = self.selected_meal_info.to_alipay_dict()
            else:
                params['selected_meal_info'] = self.selected_meal_info
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.temporary_dish:
            if hasattr(self.temporary_dish, 'to_alipay_dict'):
                params['temporary_dish'] = self.temporary_dish.to_alipay_dict()
            else:
                params['temporary_dish'] = self.temporary_dish
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DishList()
        if 'amount' in d:
            o.amount = d['amount']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_infos' in d:
            o.discount_infos = d['discount_infos']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_type' in d:
            o.dish_type = d['dish_type']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'num' in d:
            o.num = d['num']
        if 'out_detail_id' in d:
            o.out_detail_id = d['out_detail_id']
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'out_dish_infos' in d:
            o.out_dish_infos = d['out_dish_infos']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'price' in d:
            o.price = d['price']
        if 'selected_meal_info' in d:
            o.selected_meal_info = d['selected_meal_info']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'status' in d:
            o.status = d['status']
        if 'temporary_dish' in d:
            o.temporary_dish = d['temporary_dish']
        if 'unit' in d:
            o.unit = d['unit']
        return o


