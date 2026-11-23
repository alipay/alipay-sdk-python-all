#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RegisterSymptomTreeVO import RegisterSymptomTreeVO


class AlipayCommerceMedicalRegisterSymptomQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterSymptomQueryResponse, self).__init__()
        self._query = None
        self._res_prop = None
        self._symp_tree = None

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def res_prop(self):
        return self._res_prop

    @res_prop.setter
    def res_prop(self, value):
        self._res_prop = value
    @property
    def symp_tree(self):
        return self._symp_tree

    @symp_tree.setter
    def symp_tree(self, value):
        if isinstance(value, RegisterSymptomTreeVO):
            self._symp_tree = value
        else:
            self._symp_tree = RegisterSymptomTreeVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterSymptomQueryResponse, self).parse_response_content(response_content)
        if 'query' in response:
            self.query = response['query']
        if 'res_prop' in response:
            self.res_prop = response['res_prop']
        if 'symp_tree' in response:
            self.symp_tree = response['symp_tree']
