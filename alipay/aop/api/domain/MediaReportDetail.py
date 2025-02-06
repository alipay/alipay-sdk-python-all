#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MediaReportDetail(object):

    def __init__(self):
        self._ad_pos_id = None
        self._ad_pos_name = None
        self._ad_pos_type = None
        self._ad_pos_type_name = None
        self._app_name = None
        self._application_id = None
        self._click = None
        self._click_rate = None
        self._component_exposure = None
        self._cpm = None
        self._date = None
        self._es_income = None
        self._exposure = None
        self._space_code_list = None

    @property
    def ad_pos_id(self):
        return self._ad_pos_id

    @ad_pos_id.setter
    def ad_pos_id(self, value):
        self._ad_pos_id = value
    @property
    def ad_pos_name(self):
        return self._ad_pos_name

    @ad_pos_name.setter
    def ad_pos_name(self, value):
        self._ad_pos_name = value
    @property
    def ad_pos_type(self):
        return self._ad_pos_type

    @ad_pos_type.setter
    def ad_pos_type(self, value):
        self._ad_pos_type = value
    @property
    def ad_pos_type_name(self):
        return self._ad_pos_type_name

    @ad_pos_type_name.setter
    def ad_pos_type_name(self, value):
        self._ad_pos_type_name = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def click(self):
        return self._click

    @click.setter
    def click(self, value):
        self._click = value
    @property
    def click_rate(self):
        return self._click_rate

    @click_rate.setter
    def click_rate(self, value):
        self._click_rate = value
    @property
    def component_exposure(self):
        return self._component_exposure

    @component_exposure.setter
    def component_exposure(self, value):
        self._component_exposure = value
    @property
    def cpm(self):
        return self._cpm

    @cpm.setter
    def cpm(self, value):
        self._cpm = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def es_income(self):
        return self._es_income

    @es_income.setter
    def es_income(self, value):
        self._es_income = value
    @property
    def exposure(self):
        return self._exposure

    @exposure.setter
    def exposure(self, value):
        self._exposure = value
    @property
    def space_code_list(self):
        return self._space_code_list

    @space_code_list.setter
    def space_code_list(self, value):
        self._space_code_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_pos_id:
            if hasattr(self.ad_pos_id, 'to_alipay_dict'):
                params['ad_pos_id'] = self.ad_pos_id.to_alipay_dict()
            else:
                params['ad_pos_id'] = self.ad_pos_id
        if self.ad_pos_name:
            if hasattr(self.ad_pos_name, 'to_alipay_dict'):
                params['ad_pos_name'] = self.ad_pos_name.to_alipay_dict()
            else:
                params['ad_pos_name'] = self.ad_pos_name
        if self.ad_pos_type:
            if hasattr(self.ad_pos_type, 'to_alipay_dict'):
                params['ad_pos_type'] = self.ad_pos_type.to_alipay_dict()
            else:
                params['ad_pos_type'] = self.ad_pos_type
        if self.ad_pos_type_name:
            if hasattr(self.ad_pos_type_name, 'to_alipay_dict'):
                params['ad_pos_type_name'] = self.ad_pos_type_name.to_alipay_dict()
            else:
                params['ad_pos_type_name'] = self.ad_pos_type_name
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.click:
            if hasattr(self.click, 'to_alipay_dict'):
                params['click'] = self.click.to_alipay_dict()
            else:
                params['click'] = self.click
        if self.click_rate:
            if hasattr(self.click_rate, 'to_alipay_dict'):
                params['click_rate'] = self.click_rate.to_alipay_dict()
            else:
                params['click_rate'] = self.click_rate
        if self.component_exposure:
            if hasattr(self.component_exposure, 'to_alipay_dict'):
                params['component_exposure'] = self.component_exposure.to_alipay_dict()
            else:
                params['component_exposure'] = self.component_exposure
        if self.cpm:
            if hasattr(self.cpm, 'to_alipay_dict'):
                params['cpm'] = self.cpm.to_alipay_dict()
            else:
                params['cpm'] = self.cpm
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.es_income:
            if hasattr(self.es_income, 'to_alipay_dict'):
                params['es_income'] = self.es_income.to_alipay_dict()
            else:
                params['es_income'] = self.es_income
        if self.exposure:
            if hasattr(self.exposure, 'to_alipay_dict'):
                params['exposure'] = self.exposure.to_alipay_dict()
            else:
                params['exposure'] = self.exposure
        if self.space_code_list:
            if hasattr(self.space_code_list, 'to_alipay_dict'):
                params['space_code_list'] = self.space_code_list.to_alipay_dict()
            else:
                params['space_code_list'] = self.space_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MediaReportDetail()
        if 'ad_pos_id' in d:
            o.ad_pos_id = d['ad_pos_id']
        if 'ad_pos_name' in d:
            o.ad_pos_name = d['ad_pos_name']
        if 'ad_pos_type' in d:
            o.ad_pos_type = d['ad_pos_type']
        if 'ad_pos_type_name' in d:
            o.ad_pos_type_name = d['ad_pos_type_name']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'click' in d:
            o.click = d['click']
        if 'click_rate' in d:
            o.click_rate = d['click_rate']
        if 'component_exposure' in d:
            o.component_exposure = d['component_exposure']
        if 'cpm' in d:
            o.cpm = d['cpm']
        if 'date' in d:
            o.date = d['date']
        if 'es_income' in d:
            o.es_income = d['es_income']
        if 'exposure' in d:
            o.exposure = d['exposure']
        if 'space_code_list' in d:
            o.space_code_list = d['space_code_list']
        return o


