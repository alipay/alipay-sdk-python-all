#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarCarmodelModifyModel(object):

    def __init__(self):
        self._background_url = None
        self._brand_id = None
        self._brand_logo = None
        self._brand_name = None
        self._cc = None
        self._company_id = None
        self._company_name = None
        self._engine = None
        self._model_id = None
        self._model_name = None
        self._modify_type = None
        self._prod_year = None
        self._serie_group = None
        self._serie_id = None
        self._serie_name = None
        self._serie_photo = None
        self._style = None

    @property
    def background_url(self):
        return self._background_url

    @background_url.setter
    def background_url(self, value):
        self._background_url = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, value):
        self._cc = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value
    @property
    def prod_year(self):
        return self._prod_year

    @prod_year.setter
    def prod_year(self, value):
        self._prod_year = value
    @property
    def serie_group(self):
        return self._serie_group

    @serie_group.setter
    def serie_group(self, value):
        self._serie_group = value
    @property
    def serie_id(self):
        return self._serie_id

    @serie_id.setter
    def serie_id(self, value):
        self._serie_id = value
    @property
    def serie_name(self):
        return self._serie_name

    @serie_name.setter
    def serie_name(self, value):
        self._serie_name = value
    @property
    def serie_photo(self):
        return self._serie_photo

    @serie_photo.setter
    def serie_photo(self, value):
        self._serie_photo = value
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_url:
            if hasattr(self.background_url, 'to_alipay_dict'):
                params['background_url'] = self.background_url.to_alipay_dict()
            else:
                params['background_url'] = self.background_url
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.cc:
            if hasattr(self.cc, 'to_alipay_dict'):
                params['cc'] = self.cc.to_alipay_dict()
            else:
                params['cc'] = self.cc
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.engine:
            if hasattr(self.engine, 'to_alipay_dict'):
                params['engine'] = self.engine.to_alipay_dict()
            else:
                params['engine'] = self.engine
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
        if self.prod_year:
            if hasattr(self.prod_year, 'to_alipay_dict'):
                params['prod_year'] = self.prod_year.to_alipay_dict()
            else:
                params['prod_year'] = self.prod_year
        if self.serie_group:
            if hasattr(self.serie_group, 'to_alipay_dict'):
                params['serie_group'] = self.serie_group.to_alipay_dict()
            else:
                params['serie_group'] = self.serie_group
        if self.serie_id:
            if hasattr(self.serie_id, 'to_alipay_dict'):
                params['serie_id'] = self.serie_id.to_alipay_dict()
            else:
                params['serie_id'] = self.serie_id
        if self.serie_name:
            if hasattr(self.serie_name, 'to_alipay_dict'):
                params['serie_name'] = self.serie_name.to_alipay_dict()
            else:
                params['serie_name'] = self.serie_name
        if self.serie_photo:
            if hasattr(self.serie_photo, 'to_alipay_dict'):
                params['serie_photo'] = self.serie_photo.to_alipay_dict()
            else:
                params['serie_photo'] = self.serie_photo
        if self.style:
            if hasattr(self.style, 'to_alipay_dict'):
                params['style'] = self.style.to_alipay_dict()
            else:
                params['style'] = self.style
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarCarmodelModifyModel()
        if 'background_url' in d:
            o.background_url = d['background_url']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'cc' in d:
            o.cc = d['cc']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'engine' in d:
            o.engine = d['engine']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'model_name' in d:
            o.model_name = d['model_name']
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        if 'prod_year' in d:
            o.prod_year = d['prod_year']
        if 'serie_group' in d:
            o.serie_group = d['serie_group']
        if 'serie_id' in d:
            o.serie_id = d['serie_id']
        if 'serie_name' in d:
            o.serie_name = d['serie_name']
        if 'serie_photo' in d:
            o.serie_photo = d['serie_photo']
        if 'style' in d:
            o.style = d['style']
        return o


