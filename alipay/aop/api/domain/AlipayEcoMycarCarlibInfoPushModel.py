#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarCarlibInfoPushModel(object):

    def __init__(self):
        self._brand = None
        self._cc = None
        self._company = None
        self._engine = None
        self._marker = None
        self._prod_year = None
        self._serie = None
        self._style = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, value):
        self._cc = value
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value
    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value
    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value
    @property
    def prod_year(self):
        return self._prod_year

    @prod_year.setter
    def prod_year(self, value):
        self._prod_year = value
    @property
    def serie(self):
        return self._serie

    @serie.setter
    def serie(self, value):
        self._serie = value
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.cc:
            if hasattr(self.cc, 'to_alipay_dict'):
                params['cc'] = self.cc.to_alipay_dict()
            else:
                params['cc'] = self.cc
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = self.company.to_alipay_dict()
            else:
                params['company'] = self.company
        if self.engine:
            if hasattr(self.engine, 'to_alipay_dict'):
                params['engine'] = self.engine.to_alipay_dict()
            else:
                params['engine'] = self.engine
        if self.marker:
            if hasattr(self.marker, 'to_alipay_dict'):
                params['marker'] = self.marker.to_alipay_dict()
            else:
                params['marker'] = self.marker
        if self.prod_year:
            if hasattr(self.prod_year, 'to_alipay_dict'):
                params['prod_year'] = self.prod_year.to_alipay_dict()
            else:
                params['prod_year'] = self.prod_year
        if self.serie:
            if hasattr(self.serie, 'to_alipay_dict'):
                params['serie'] = self.serie.to_alipay_dict()
            else:
                params['serie'] = self.serie
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
        o = AlipayEcoMycarCarlibInfoPushModel()
        if 'brand' in d:
            o.brand = d['brand']
        if 'cc' in d:
            o.cc = d['cc']
        if 'company' in d:
            o.company = d['company']
        if 'engine' in d:
            o.engine = d['engine']
        if 'marker' in d:
            o.marker = d['marker']
        if 'prod_year' in d:
            o.prod_year = d['prod_year']
        if 'serie' in d:
            o.serie = d['serie']
        if 'style' in d:
            o.style = d['style']
        return o


