#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarCarmodelCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarCarmodelCreateResponse, self).__init__()
        self._brand_id = None
        self._company_id = None
        self._model_id = None
        self._serie_id = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def serie_id(self):
        return self._serie_id

    @serie_id.setter
    def serie_id(self, value):
        self._serie_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarCarmodelCreateResponse, self).parse_response_content(response_content)
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
        if 'company_id' in response:
            self.company_id = response['company_id']
        if 'model_id' in response:
            self.model_id = response['model_id']
        if 'serie_id' in response:
            self.serie_id = response['serie_id']
