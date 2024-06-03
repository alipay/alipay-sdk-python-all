#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsightBrandItem import InsightBrandItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem
from alipay.aop.api.domain.InsightDistItem import InsightDistItem


class AnttechMorseDataserviceInsightreportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseDataserviceInsightreportQueryResponse, self).__init__()
        self._biz_no = None
        self._brands = None
        self._home_base_age_dist = None
        self._home_base_occupation_dist = None
        self._home_base_sex_dist = None
        self._home_payment_consumption_level_dist = None
        self._permanent_base_age_dist = None
        self._permanent_base_occupation_dist = None
        self._permanent_base_sex_dist = None
        self._permanent_media_apptype_dist = None
        self._permanent_payment_consumption_level_dist = None
        self._permanent_payment_food_poitype_dist = None
        self._uv_home = None
        self._uv_permanent = None
        self._uv_weekday_day = None
        self._uv_weekend_day = None
        self._uv_work = None
        self._work_base_age_dist = None
        self._work_base_occupation_dist = None
        self._work_base_sex_dist = None
        self._work_payment_consumption_level_dist = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def brands(self):
        return self._brands

    @brands.setter
    def brands(self, value):
        if isinstance(value, list):
            self._brands = list()
            for i in value:
                if isinstance(i, InsightBrandItem):
                    self._brands.append(i)
                else:
                    self._brands.append(InsightBrandItem.from_alipay_dict(i))
    @property
    def home_base_age_dist(self):
        return self._home_base_age_dist

    @home_base_age_dist.setter
    def home_base_age_dist(self, value):
        if isinstance(value, list):
            self._home_base_age_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._home_base_age_dist.append(i)
                else:
                    self._home_base_age_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def home_base_occupation_dist(self):
        return self._home_base_occupation_dist

    @home_base_occupation_dist.setter
    def home_base_occupation_dist(self, value):
        if isinstance(value, list):
            self._home_base_occupation_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._home_base_occupation_dist.append(i)
                else:
                    self._home_base_occupation_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def home_base_sex_dist(self):
        return self._home_base_sex_dist

    @home_base_sex_dist.setter
    def home_base_sex_dist(self, value):
        if isinstance(value, list):
            self._home_base_sex_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._home_base_sex_dist.append(i)
                else:
                    self._home_base_sex_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def home_payment_consumption_level_dist(self):
        return self._home_payment_consumption_level_dist

    @home_payment_consumption_level_dist.setter
    def home_payment_consumption_level_dist(self, value):
        if isinstance(value, list):
            self._home_payment_consumption_level_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._home_payment_consumption_level_dist.append(i)
                else:
                    self._home_payment_consumption_level_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def permanent_base_age_dist(self):
        return self._permanent_base_age_dist

    @permanent_base_age_dist.setter
    def permanent_base_age_dist(self, value):
        if isinstance(value, list):
            self._permanent_base_age_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._permanent_base_age_dist.append(i)
                else:
                    self._permanent_base_age_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def permanent_base_occupation_dist(self):
        return self._permanent_base_occupation_dist

    @permanent_base_occupation_dist.setter
    def permanent_base_occupation_dist(self, value):
        if isinstance(value, list):
            self._permanent_base_occupation_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._permanent_base_occupation_dist.append(i)
                else:
                    self._permanent_base_occupation_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def permanent_base_sex_dist(self):
        return self._permanent_base_sex_dist

    @permanent_base_sex_dist.setter
    def permanent_base_sex_dist(self, value):
        if isinstance(value, list):
            self._permanent_base_sex_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._permanent_base_sex_dist.append(i)
                else:
                    self._permanent_base_sex_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def permanent_media_apptype_dist(self):
        return self._permanent_media_apptype_dist

    @permanent_media_apptype_dist.setter
    def permanent_media_apptype_dist(self, value):
        if isinstance(value, list):
            self._permanent_media_apptype_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._permanent_media_apptype_dist.append(i)
                else:
                    self._permanent_media_apptype_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def permanent_payment_consumption_level_dist(self):
        return self._permanent_payment_consumption_level_dist

    @permanent_payment_consumption_level_dist.setter
    def permanent_payment_consumption_level_dist(self, value):
        if isinstance(value, list):
            self._permanent_payment_consumption_level_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._permanent_payment_consumption_level_dist.append(i)
                else:
                    self._permanent_payment_consumption_level_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def permanent_payment_food_poitype_dist(self):
        return self._permanent_payment_food_poitype_dist

    @permanent_payment_food_poitype_dist.setter
    def permanent_payment_food_poitype_dist(self, value):
        if isinstance(value, list):
            self._permanent_payment_food_poitype_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._permanent_payment_food_poitype_dist.append(i)
                else:
                    self._permanent_payment_food_poitype_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def uv_home(self):
        return self._uv_home

    @uv_home.setter
    def uv_home(self, value):
        self._uv_home = value
    @property
    def uv_permanent(self):
        return self._uv_permanent

    @uv_permanent.setter
    def uv_permanent(self, value):
        self._uv_permanent = value
    @property
    def uv_weekday_day(self):
        return self._uv_weekday_day

    @uv_weekday_day.setter
    def uv_weekday_day(self, value):
        self._uv_weekday_day = value
    @property
    def uv_weekend_day(self):
        return self._uv_weekend_day

    @uv_weekend_day.setter
    def uv_weekend_day(self, value):
        self._uv_weekend_day = value
    @property
    def uv_work(self):
        return self._uv_work

    @uv_work.setter
    def uv_work(self, value):
        self._uv_work = value
    @property
    def work_base_age_dist(self):
        return self._work_base_age_dist

    @work_base_age_dist.setter
    def work_base_age_dist(self, value):
        if isinstance(value, list):
            self._work_base_age_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._work_base_age_dist.append(i)
                else:
                    self._work_base_age_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def work_base_occupation_dist(self):
        return self._work_base_occupation_dist

    @work_base_occupation_dist.setter
    def work_base_occupation_dist(self, value):
        if isinstance(value, list):
            self._work_base_occupation_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._work_base_occupation_dist.append(i)
                else:
                    self._work_base_occupation_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def work_base_sex_dist(self):
        return self._work_base_sex_dist

    @work_base_sex_dist.setter
    def work_base_sex_dist(self, value):
        if isinstance(value, list):
            self._work_base_sex_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._work_base_sex_dist.append(i)
                else:
                    self._work_base_sex_dist.append(InsightDistItem.from_alipay_dict(i))
    @property
    def work_payment_consumption_level_dist(self):
        return self._work_payment_consumption_level_dist

    @work_payment_consumption_level_dist.setter
    def work_payment_consumption_level_dist(self, value):
        if isinstance(value, list):
            self._work_payment_consumption_level_dist = list()
            for i in value:
                if isinstance(i, InsightDistItem):
                    self._work_payment_consumption_level_dist.append(i)
                else:
                    self._work_payment_consumption_level_dist.append(InsightDistItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechMorseDataserviceInsightreportQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'brands' in response:
            self.brands = response['brands']
        if 'home_base_age_dist' in response:
            self.home_base_age_dist = response['home_base_age_dist']
        if 'home_base_occupation_dist' in response:
            self.home_base_occupation_dist = response['home_base_occupation_dist']
        if 'home_base_sex_dist' in response:
            self.home_base_sex_dist = response['home_base_sex_dist']
        if 'home_payment_consumption_level_dist' in response:
            self.home_payment_consumption_level_dist = response['home_payment_consumption_level_dist']
        if 'permanent_base_age_dist' in response:
            self.permanent_base_age_dist = response['permanent_base_age_dist']
        if 'permanent_base_occupation_dist' in response:
            self.permanent_base_occupation_dist = response['permanent_base_occupation_dist']
        if 'permanent_base_sex_dist' in response:
            self.permanent_base_sex_dist = response['permanent_base_sex_dist']
        if 'permanent_media_apptype_dist' in response:
            self.permanent_media_apptype_dist = response['permanent_media_apptype_dist']
        if 'permanent_payment_consumption_level_dist' in response:
            self.permanent_payment_consumption_level_dist = response['permanent_payment_consumption_level_dist']
        if 'permanent_payment_food_poitype_dist' in response:
            self.permanent_payment_food_poitype_dist = response['permanent_payment_food_poitype_dist']
        if 'uv_home' in response:
            self.uv_home = response['uv_home']
        if 'uv_permanent' in response:
            self.uv_permanent = response['uv_permanent']
        if 'uv_weekday_day' in response:
            self.uv_weekday_day = response['uv_weekday_day']
        if 'uv_weekend_day' in response:
            self.uv_weekend_day = response['uv_weekend_day']
        if 'uv_work' in response:
            self.uv_work = response['uv_work']
        if 'work_base_age_dist' in response:
            self.work_base_age_dist = response['work_base_age_dist']
        if 'work_base_occupation_dist' in response:
            self.work_base_occupation_dist = response['work_base_occupation_dist']
        if 'work_base_sex_dist' in response:
            self.work_base_sex_dist = response['work_base_sex_dist']
        if 'work_payment_consumption_level_dist' in response:
            self.work_payment_consumption_level_dist = response['work_payment_consumption_level_dist']
