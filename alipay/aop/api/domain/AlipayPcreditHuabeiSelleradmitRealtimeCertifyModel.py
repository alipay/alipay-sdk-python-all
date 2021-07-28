#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiSelleradmitRealtimeCertifyModel(object):

    def __init__(self):
        self._alipay_id = None
        self._from_app = None
        self._industry = None
        self._main_category = None
        self._platform = None
        self._seller_admit_scene = None
        self._seller_id = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def from_app(self):
        return self._from_app

    @from_app.setter
    def from_app(self, value):
        self._from_app = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def main_category(self):
        return self._main_category

    @main_category.setter
    def main_category(self, value):
        self._main_category = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def seller_admit_scene(self):
        return self._seller_admit_scene

    @seller_admit_scene.setter
    def seller_admit_scene(self, value):
        self._seller_admit_scene = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.from_app:
            if hasattr(self.from_app, 'to_alipay_dict'):
                params['from_app'] = self.from_app.to_alipay_dict()
            else:
                params['from_app'] = self.from_app
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.main_category:
            if hasattr(self.main_category, 'to_alipay_dict'):
                params['main_category'] = self.main_category.to_alipay_dict()
            else:
                params['main_category'] = self.main_category
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.seller_admit_scene:
            if hasattr(self.seller_admit_scene, 'to_alipay_dict'):
                params['seller_admit_scene'] = self.seller_admit_scene.to_alipay_dict()
            else:
                params['seller_admit_scene'] = self.seller_admit_scene
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiSelleradmitRealtimeCertifyModel()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'from_app' in d:
            o.from_app = d['from_app']
        if 'industry' in d:
            o.industry = d['industry']
        if 'main_category' in d:
            o.main_category = d['main_category']
        if 'platform' in d:
            o.platform = d['platform']
        if 'seller_admit_scene' in d:
            o.seller_admit_scene = d['seller_admit_scene']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        return o


