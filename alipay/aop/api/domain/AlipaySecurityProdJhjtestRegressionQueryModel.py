#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DomainNestOther import DomainNestOther
from alipay.aop.api.domain.PubNestPub import PubNestPub
from alipay.aop.api.domain.RegressionInDomian import RegressionInDomian
from alipay.aop.api.domain.RegressionPublic import RegressionPublic
from alipay.aop.api.domain.RegressionPublic import RegressionPublic


class AlipaySecurityProdJhjtestRegressionQueryModel(object):

    def __init__(self):
        self._a_test_a = None
        self._boolean_a = None
        self._date_a = None
        self._domain_nest = None
        self._nest_pubic = None
        self._number_a = None
        self._only_domin = None
        self._only_pub = None
        self._only_public = None
        self._path_para = None
        self._price_a = None
        self._query_para = None
        self._string = None
        self._string_open_id = None

    @property
    def a_test_a(self):
        return self._a_test_a

    @a_test_a.setter
    def a_test_a(self, value):
        self._a_test_a = value
    @property
    def boolean_a(self):
        return self._boolean_a

    @boolean_a.setter
    def boolean_a(self, value):
        self._boolean_a = value
    @property
    def date_a(self):
        return self._date_a

    @date_a.setter
    def date_a(self, value):
        self._date_a = value
    @property
    def domain_nest(self):
        return self._domain_nest

    @domain_nest.setter
    def domain_nest(self, value):
        if isinstance(value, DomainNestOther):
            self._domain_nest = value
        else:
            self._domain_nest = DomainNestOther.from_alipay_dict(value)
    @property
    def nest_pubic(self):
        return self._nest_pubic

    @nest_pubic.setter
    def nest_pubic(self, value):
        if isinstance(value, PubNestPub):
            self._nest_pubic = value
        else:
            self._nest_pubic = PubNestPub.from_alipay_dict(value)
    @property
    def number_a(self):
        return self._number_a

    @number_a.setter
    def number_a(self, value):
        self._number_a = value
    @property
    def only_domin(self):
        return self._only_domin

    @only_domin.setter
    def only_domin(self, value):
        if isinstance(value, RegressionInDomian):
            self._only_domin = value
        else:
            self._only_domin = RegressionInDomian.from_alipay_dict(value)
    @property
    def only_pub(self):
        return self._only_pub

    @only_pub.setter
    def only_pub(self, value):
        if isinstance(value, RegressionPublic):
            self._only_pub = value
        else:
            self._only_pub = RegressionPublic.from_alipay_dict(value)
    @property
    def only_public(self):
        return self._only_public

    @only_public.setter
    def only_public(self, value):
        if isinstance(value, RegressionPublic):
            self._only_public = value
        else:
            self._only_public = RegressionPublic.from_alipay_dict(value)
    @property
    def path_para(self):
        return self._path_para

    @path_para.setter
    def path_para(self, value):
        self._path_para = value
    @property
    def price_a(self):
        return self._price_a

    @price_a.setter
    def price_a(self, value):
        self._price_a = value
    @property
    def query_para(self):
        return self._query_para

    @query_para.setter
    def query_para(self, value):
        self._query_para = value
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value
    @property
    def string_open_id(self):
        return self._string_open_id

    @string_open_id.setter
    def string_open_id(self, value):
        self._string_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.a_test_a:
            if hasattr(self.a_test_a, 'to_alipay_dict'):
                params['a_test_a'] = self.a_test_a.to_alipay_dict()
            else:
                params['a_test_a'] = self.a_test_a
        if self.boolean_a:
            if hasattr(self.boolean_a, 'to_alipay_dict'):
                params['boolean_a'] = self.boolean_a.to_alipay_dict()
            else:
                params['boolean_a'] = self.boolean_a
        if self.date_a:
            if hasattr(self.date_a, 'to_alipay_dict'):
                params['date_a'] = self.date_a.to_alipay_dict()
            else:
                params['date_a'] = self.date_a
        if self.domain_nest:
            if hasattr(self.domain_nest, 'to_alipay_dict'):
                params['domain_nest'] = self.domain_nest.to_alipay_dict()
            else:
                params['domain_nest'] = self.domain_nest
        if self.nest_pubic:
            if hasattr(self.nest_pubic, 'to_alipay_dict'):
                params['nest_pubic'] = self.nest_pubic.to_alipay_dict()
            else:
                params['nest_pubic'] = self.nest_pubic
        if self.number_a:
            if hasattr(self.number_a, 'to_alipay_dict'):
                params['number_a'] = self.number_a.to_alipay_dict()
            else:
                params['number_a'] = self.number_a
        if self.only_domin:
            if hasattr(self.only_domin, 'to_alipay_dict'):
                params['only_domin'] = self.only_domin.to_alipay_dict()
            else:
                params['only_domin'] = self.only_domin
        if self.only_pub:
            if hasattr(self.only_pub, 'to_alipay_dict'):
                params['only_pub'] = self.only_pub.to_alipay_dict()
            else:
                params['only_pub'] = self.only_pub
        if self.only_public:
            if hasattr(self.only_public, 'to_alipay_dict'):
                params['only_public'] = self.only_public.to_alipay_dict()
            else:
                params['only_public'] = self.only_public
        if self.path_para:
            if hasattr(self.path_para, 'to_alipay_dict'):
                params['path_para'] = self.path_para.to_alipay_dict()
            else:
                params['path_para'] = self.path_para
        if self.price_a:
            if hasattr(self.price_a, 'to_alipay_dict'):
                params['price_a'] = self.price_a.to_alipay_dict()
            else:
                params['price_a'] = self.price_a
        if self.query_para:
            if hasattr(self.query_para, 'to_alipay_dict'):
                params['query_para'] = self.query_para.to_alipay_dict()
            else:
                params['query_para'] = self.query_para
        if self.string:
            if hasattr(self.string, 'to_alipay_dict'):
                params['string'] = self.string.to_alipay_dict()
            else:
                params['string'] = self.string
        if self.string_open_id:
            if hasattr(self.string_open_id, 'to_alipay_dict'):
                params['string_open_id'] = self.string_open_id.to_alipay_dict()
            else:
                params['string_open_id'] = self.string_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdJhjtestRegressionQueryModel()
        if 'a_test_a' in d:
            o.a_test_a = d['a_test_a']
        if 'boolean_a' in d:
            o.boolean_a = d['boolean_a']
        if 'date_a' in d:
            o.date_a = d['date_a']
        if 'domain_nest' in d:
            o.domain_nest = d['domain_nest']
        if 'nest_pubic' in d:
            o.nest_pubic = d['nest_pubic']
        if 'number_a' in d:
            o.number_a = d['number_a']
        if 'only_domin' in d:
            o.only_domin = d['only_domin']
        if 'only_pub' in d:
            o.only_pub = d['only_pub']
        if 'only_public' in d:
            o.only_public = d['only_public']
        if 'path_para' in d:
            o.path_para = d['path_para']
        if 'price_a' in d:
            o.price_a = d['price_a']
        if 'query_para' in d:
            o.query_para = d['query_para']
        if 'string' in d:
            o.string = d['string']
        if 'string_open_id' in d:
            o.string_open_id = d['string_open_id']
        return o


