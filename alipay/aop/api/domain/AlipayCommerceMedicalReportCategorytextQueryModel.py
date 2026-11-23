#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalReportCategorytextQueryModel(object):

    def __init__(self):
        self._biz_category = None
        self._biz_scene_code = None
        self._biz_subcategory = None
        self._config_id = None
        self._org_id = None

    @property
    def biz_category(self):
        return self._biz_category

    @biz_category.setter
    def biz_category(self, value):
        self._biz_category = value
    @property
    def biz_scene_code(self):
        return self._biz_scene_code

    @biz_scene_code.setter
    def biz_scene_code(self, value):
        self._biz_scene_code = value
    @property
    def biz_subcategory(self):
        return self._biz_subcategory

    @biz_subcategory.setter
    def biz_subcategory(self, value):
        self._biz_subcategory = value
    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_category:
            if hasattr(self.biz_category, 'to_alipay_dict'):
                params['biz_category'] = self.biz_category.to_alipay_dict()
            else:
                params['biz_category'] = self.biz_category
        if self.biz_scene_code:
            if hasattr(self.biz_scene_code, 'to_alipay_dict'):
                params['biz_scene_code'] = self.biz_scene_code.to_alipay_dict()
            else:
                params['biz_scene_code'] = self.biz_scene_code
        if self.biz_subcategory:
            if hasattr(self.biz_subcategory, 'to_alipay_dict'):
                params['biz_subcategory'] = self.biz_subcategory.to_alipay_dict()
            else:
                params['biz_subcategory'] = self.biz_subcategory
        if self.config_id:
            if hasattr(self.config_id, 'to_alipay_dict'):
                params['config_id'] = self.config_id.to_alipay_dict()
            else:
                params['config_id'] = self.config_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalReportCategorytextQueryModel()
        if 'biz_category' in d:
            o.biz_category = d['biz_category']
        if 'biz_scene_code' in d:
            o.biz_scene_code = d['biz_scene_code']
        if 'biz_subcategory' in d:
            o.biz_subcategory = d['biz_subcategory']
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        return o


