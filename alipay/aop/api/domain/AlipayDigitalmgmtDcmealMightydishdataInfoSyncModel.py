#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtDcmealMightydishdataInfoSyncModel(object):

    def __init__(self):
        self._allergy_risk = None
        self._campus_id = None
        self._campus_name = None
        self._category_id = None
        self._create_date = None
        self._dietary = None
        self._dish_img = None
        self._food_id = None
        self._food_name = None
        self._food_no = None
        self._labs_healthcard = None
        self._nutrition = None
        self._price = None
        self._restaurant_id = None
        self._restaurant_name = None
        self._special_population = None
        self._state = None
        self._unit = None
        self._update_date = None
        self._weight = None
        self._weight_type = None

    @property
    def allergy_risk(self):
        return self._allergy_risk

    @allergy_risk.setter
    def allergy_risk(self, value):
        self._allergy_risk = value
    @property
    def campus_id(self):
        return self._campus_id

    @campus_id.setter
    def campus_id(self, value):
        self._campus_id = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def dietary(self):
        return self._dietary

    @dietary.setter
    def dietary(self, value):
        self._dietary = value
    @property
    def dish_img(self):
        return self._dish_img

    @dish_img.setter
    def dish_img(self, value):
        self._dish_img = value
    @property
    def food_id(self):
        return self._food_id

    @food_id.setter
    def food_id(self, value):
        self._food_id = value
    @property
    def food_name(self):
        return self._food_name

    @food_name.setter
    def food_name(self, value):
        self._food_name = value
    @property
    def food_no(self):
        return self._food_no

    @food_no.setter
    def food_no(self, value):
        self._food_no = value
    @property
    def labs_healthcard(self):
        return self._labs_healthcard

    @labs_healthcard.setter
    def labs_healthcard(self, value):
        self._labs_healthcard = value
    @property
    def nutrition(self):
        return self._nutrition

    @nutrition.setter
    def nutrition(self, value):
        self._nutrition = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def restaurant_id(self):
        return self._restaurant_id

    @restaurant_id.setter
    def restaurant_id(self, value):
        self._restaurant_id = value
    @property
    def restaurant_name(self):
        return self._restaurant_name

    @restaurant_name.setter
    def restaurant_name(self, value):
        self._restaurant_name = value
    @property
    def special_population(self):
        return self._special_population

    @special_population.setter
    def special_population(self, value):
        self._special_population = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def update_date(self):
        return self._update_date

    @update_date.setter
    def update_date(self, value):
        self._update_date = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
    @property
    def weight_type(self):
        return self._weight_type

    @weight_type.setter
    def weight_type(self, value):
        self._weight_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.allergy_risk:
            if hasattr(self.allergy_risk, 'to_alipay_dict'):
                params['allergy_risk'] = self.allergy_risk.to_alipay_dict()
            else:
                params['allergy_risk'] = self.allergy_risk
        if self.campus_id:
            if hasattr(self.campus_id, 'to_alipay_dict'):
                params['campus_id'] = self.campus_id.to_alipay_dict()
            else:
                params['campus_id'] = self.campus_id
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.dietary:
            if hasattr(self.dietary, 'to_alipay_dict'):
                params['dietary'] = self.dietary.to_alipay_dict()
            else:
                params['dietary'] = self.dietary
        if self.dish_img:
            if hasattr(self.dish_img, 'to_alipay_dict'):
                params['dish_img'] = self.dish_img.to_alipay_dict()
            else:
                params['dish_img'] = self.dish_img
        if self.food_id:
            if hasattr(self.food_id, 'to_alipay_dict'):
                params['food_id'] = self.food_id.to_alipay_dict()
            else:
                params['food_id'] = self.food_id
        if self.food_name:
            if hasattr(self.food_name, 'to_alipay_dict'):
                params['food_name'] = self.food_name.to_alipay_dict()
            else:
                params['food_name'] = self.food_name
        if self.food_no:
            if hasattr(self.food_no, 'to_alipay_dict'):
                params['food_no'] = self.food_no.to_alipay_dict()
            else:
                params['food_no'] = self.food_no
        if self.labs_healthcard:
            if hasattr(self.labs_healthcard, 'to_alipay_dict'):
                params['labs_healthcard'] = self.labs_healthcard.to_alipay_dict()
            else:
                params['labs_healthcard'] = self.labs_healthcard
        if self.nutrition:
            if hasattr(self.nutrition, 'to_alipay_dict'):
                params['nutrition'] = self.nutrition.to_alipay_dict()
            else:
                params['nutrition'] = self.nutrition
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.restaurant_id:
            if hasattr(self.restaurant_id, 'to_alipay_dict'):
                params['restaurant_id'] = self.restaurant_id.to_alipay_dict()
            else:
                params['restaurant_id'] = self.restaurant_id
        if self.restaurant_name:
            if hasattr(self.restaurant_name, 'to_alipay_dict'):
                params['restaurant_name'] = self.restaurant_name.to_alipay_dict()
            else:
                params['restaurant_name'] = self.restaurant_name
        if self.special_population:
            if hasattr(self.special_population, 'to_alipay_dict'):
                params['special_population'] = self.special_population.to_alipay_dict()
            else:
                params['special_population'] = self.special_population
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.update_date:
            if hasattr(self.update_date, 'to_alipay_dict'):
                params['update_date'] = self.update_date.to_alipay_dict()
            else:
                params['update_date'] = self.update_date
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        if self.weight_type:
            if hasattr(self.weight_type, 'to_alipay_dict'):
                params['weight_type'] = self.weight_type.to_alipay_dict()
            else:
                params['weight_type'] = self.weight_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtDcmealMightydishdataInfoSyncModel()
        if 'allergy_risk' in d:
            o.allergy_risk = d['allergy_risk']
        if 'campus_id' in d:
            o.campus_id = d['campus_id']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'dietary' in d:
            o.dietary = d['dietary']
        if 'dish_img' in d:
            o.dish_img = d['dish_img']
        if 'food_id' in d:
            o.food_id = d['food_id']
        if 'food_name' in d:
            o.food_name = d['food_name']
        if 'food_no' in d:
            o.food_no = d['food_no']
        if 'labs_healthcard' in d:
            o.labs_healthcard = d['labs_healthcard']
        if 'nutrition' in d:
            o.nutrition = d['nutrition']
        if 'price' in d:
            o.price = d['price']
        if 'restaurant_id' in d:
            o.restaurant_id = d['restaurant_id']
        if 'restaurant_name' in d:
            o.restaurant_name = d['restaurant_name']
        if 'special_population' in d:
            o.special_population = d['special_population']
        if 'state' in d:
            o.state = d['state']
        if 'unit' in d:
            o.unit = d['unit']
        if 'update_date' in d:
            o.update_date = d['update_date']
        if 'weight' in d:
            o.weight = d['weight']
        if 'weight_type' in d:
            o.weight_type = d['weight_type']
        return o


