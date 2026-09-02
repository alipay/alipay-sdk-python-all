#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FoodItem import FoodItem


class DietRecordItem(object):

    def __init__(self):
        self._ai_calorie = None
        self._ai_summary = None
        self._carbohydrate = None
        self._fat = None
        self._food_image_urls = None
        self._food_items = None
        self._meal_type = None
        self._meal_type_name = None
        self._protein = None
        self._record_date = None
        self._record_id = None
        self._record_time = None
        self._text_desc = None

    @property
    def ai_calorie(self):
        return self._ai_calorie

    @ai_calorie.setter
    def ai_calorie(self, value):
        self._ai_calorie = value
    @property
    def ai_summary(self):
        return self._ai_summary

    @ai_summary.setter
    def ai_summary(self, value):
        self._ai_summary = value
    @property
    def carbohydrate(self):
        return self._carbohydrate

    @carbohydrate.setter
    def carbohydrate(self, value):
        self._carbohydrate = value
    @property
    def fat(self):
        return self._fat

    @fat.setter
    def fat(self, value):
        self._fat = value
    @property
    def food_image_urls(self):
        return self._food_image_urls

    @food_image_urls.setter
    def food_image_urls(self, value):
        if isinstance(value, list):
            self._food_image_urls = list()
            for i in value:
                self._food_image_urls.append(i)
    @property
    def food_items(self):
        return self._food_items

    @food_items.setter
    def food_items(self, value):
        if isinstance(value, list):
            self._food_items = list()
            for i in value:
                if isinstance(i, FoodItem):
                    self._food_items.append(i)
                else:
                    self._food_items.append(FoodItem.from_alipay_dict(i))
    @property
    def meal_type(self):
        return self._meal_type

    @meal_type.setter
    def meal_type(self, value):
        self._meal_type = value
    @property
    def meal_type_name(self):
        return self._meal_type_name

    @meal_type_name.setter
    def meal_type_name(self, value):
        self._meal_type_name = value
    @property
    def protein(self):
        return self._protein

    @protein.setter
    def protein(self, value):
        self._protein = value
    @property
    def record_date(self):
        return self._record_date

    @record_date.setter
    def record_date(self, value):
        self._record_date = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def record_time(self):
        return self._record_time

    @record_time.setter
    def record_time(self, value):
        self._record_time = value
    @property
    def text_desc(self):
        return self._text_desc

    @text_desc.setter
    def text_desc(self, value):
        self._text_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_calorie:
            if hasattr(self.ai_calorie, 'to_alipay_dict'):
                params['ai_calorie'] = self.ai_calorie.to_alipay_dict()
            else:
                params['ai_calorie'] = self.ai_calorie
        if self.ai_summary:
            if hasattr(self.ai_summary, 'to_alipay_dict'):
                params['ai_summary'] = self.ai_summary.to_alipay_dict()
            else:
                params['ai_summary'] = self.ai_summary
        if self.carbohydrate:
            if hasattr(self.carbohydrate, 'to_alipay_dict'):
                params['carbohydrate'] = self.carbohydrate.to_alipay_dict()
            else:
                params['carbohydrate'] = self.carbohydrate
        if self.fat:
            if hasattr(self.fat, 'to_alipay_dict'):
                params['fat'] = self.fat.to_alipay_dict()
            else:
                params['fat'] = self.fat
        if self.food_image_urls:
            if isinstance(self.food_image_urls, list):
                for i in range(0, len(self.food_image_urls)):
                    element = self.food_image_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.food_image_urls[i] = element.to_alipay_dict()
            if hasattr(self.food_image_urls, 'to_alipay_dict'):
                params['food_image_urls'] = self.food_image_urls.to_alipay_dict()
            else:
                params['food_image_urls'] = self.food_image_urls
        if self.food_items:
            if isinstance(self.food_items, list):
                for i in range(0, len(self.food_items)):
                    element = self.food_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.food_items[i] = element.to_alipay_dict()
            if hasattr(self.food_items, 'to_alipay_dict'):
                params['food_items'] = self.food_items.to_alipay_dict()
            else:
                params['food_items'] = self.food_items
        if self.meal_type:
            if hasattr(self.meal_type, 'to_alipay_dict'):
                params['meal_type'] = self.meal_type.to_alipay_dict()
            else:
                params['meal_type'] = self.meal_type
        if self.meal_type_name:
            if hasattr(self.meal_type_name, 'to_alipay_dict'):
                params['meal_type_name'] = self.meal_type_name.to_alipay_dict()
            else:
                params['meal_type_name'] = self.meal_type_name
        if self.protein:
            if hasattr(self.protein, 'to_alipay_dict'):
                params['protein'] = self.protein.to_alipay_dict()
            else:
                params['protein'] = self.protein
        if self.record_date:
            if hasattr(self.record_date, 'to_alipay_dict'):
                params['record_date'] = self.record_date.to_alipay_dict()
            else:
                params['record_date'] = self.record_date
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.record_time:
            if hasattr(self.record_time, 'to_alipay_dict'):
                params['record_time'] = self.record_time.to_alipay_dict()
            else:
                params['record_time'] = self.record_time
        if self.text_desc:
            if hasattr(self.text_desc, 'to_alipay_dict'):
                params['text_desc'] = self.text_desc.to_alipay_dict()
            else:
                params['text_desc'] = self.text_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DietRecordItem()
        if 'ai_calorie' in d:
            o.ai_calorie = d['ai_calorie']
        if 'ai_summary' in d:
            o.ai_summary = d['ai_summary']
        if 'carbohydrate' in d:
            o.carbohydrate = d['carbohydrate']
        if 'fat' in d:
            o.fat = d['fat']
        if 'food_image_urls' in d:
            o.food_image_urls = d['food_image_urls']
        if 'food_items' in d:
            o.food_items = d['food_items']
        if 'meal_type' in d:
            o.meal_type = d['meal_type']
        if 'meal_type_name' in d:
            o.meal_type_name = d['meal_type_name']
        if 'protein' in d:
            o.protein = d['protein']
        if 'record_date' in d:
            o.record_date = d['record_date']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'record_time' in d:
            o.record_time = d['record_time']
        if 'text_desc' in d:
            o.text_desc = d['text_desc']
        return o


