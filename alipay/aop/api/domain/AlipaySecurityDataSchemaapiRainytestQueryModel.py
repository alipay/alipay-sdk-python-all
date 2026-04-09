#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserInfoDemo import UserInfoDemo


class AlipaySecurityDataSchemaapiRainytestQueryModel(object):

    def __init__(self):
        self._demo_body = None
        self._demo_path = None
        self._demo_query = None
        self._test = None

    @property
    def demo_body(self):
        return self._demo_body

    @demo_body.setter
    def demo_body(self, value):
        self._demo_body = value
    @property
    def demo_path(self):
        return self._demo_path

    @demo_path.setter
    def demo_path(self, value):
        self._demo_path = value
    @property
    def demo_query(self):
        return self._demo_query

    @demo_query.setter
    def demo_query(self, value):
        if isinstance(value, list):
            self._demo_query = list()
            for i in value:
                self._demo_query.append(i)
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, UserInfoDemo):
            self._test = value
        else:
            self._test = UserInfoDemo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo_body:
            if hasattr(self.demo_body, 'to_alipay_dict'):
                params['demo_body'] = self.demo_body.to_alipay_dict()
            else:
                params['demo_body'] = self.demo_body
        if self.demo_path:
            if hasattr(self.demo_path, 'to_alipay_dict'):
                params['demo_path'] = self.demo_path.to_alipay_dict()
            else:
                params['demo_path'] = self.demo_path
        if self.demo_query:
            if isinstance(self.demo_query, list):
                for i in range(0, len(self.demo_query)):
                    element = self.demo_query[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.demo_query[i] = element.to_alipay_dict()
            if hasattr(self.demo_query, 'to_alipay_dict'):
                params['demo_query'] = self.demo_query.to_alipay_dict()
            else:
                params['demo_query'] = self.demo_query
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataSchemaapiRainytestQueryModel()
        if 'demo_body' in d:
            o.demo_body = d['demo_body']
        if 'demo_path' in d:
            o.demo_path = d['demo_path']
        if 'demo_query' in d:
            o.demo_query = d['demo_query']
        if 'test' in d:
            o.test = d['test']
        return o


