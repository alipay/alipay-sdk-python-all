#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarCarmodelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarCarmodelQueryResponse, self).__init__()
        self._background_url = None
        self._brand_id = None
        self._brand_name = None
        self._cc = None
        self._company_id = None
        self._company_name = None
        self._engine = None
        self._logo_url = None
        self._model_id = None
        self._model_name = None
        self._prod_year = None
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
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
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
    def prod_year(self):
        return self._prod_year

    @prod_year.setter
    def prod_year(self, value):
        self._prod_year = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarCarmodelQueryResponse, self).parse_response_content(response_content)
        if 'background_url' in response:
            self.background_url = response['background_url']
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
        if 'brand_name' in response:
            self.brand_name = response['brand_name']
        if 'cc' in response:
            self.cc = response['cc']
        if 'company_id' in response:
            self.company_id = response['company_id']
        if 'company_name' in response:
            self.company_name = response['company_name']
        if 'engine' in response:
            self.engine = response['engine']
        if 'logo_url' in response:
            self.logo_url = response['logo_url']
        if 'model_id' in response:
            self.model_id = response['model_id']
        if 'model_name' in response:
            self.model_name = response['model_name']
        if 'prod_year' in response:
            self.prod_year = response['prod_year']
        if 'serie_id' in response:
            self.serie_id = response['serie_id']
        if 'serie_name' in response:
            self.serie_name = response['serie_name']
        if 'serie_photo' in response:
            self.serie_photo = response['serie_photo']
        if 'style' in response:
            self.style = response['style']
