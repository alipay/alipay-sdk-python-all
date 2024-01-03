#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PubNestPub import PubNestPub
from alipay.aop.api.domain.DomainNestOther import DomainNestOther
from alipay.aop.api.domain.RegressionPublic import RegressionPublic
from alipay.aop.api.domain.RegressionInDomian import RegressionInDomian


class AlipaySecurityProdJhjtestRegressionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdJhjtestRegressionQueryResponse, self).__init__()
        self._comp_c = None
        self._comp_d = None
        self._out_a = None
        self._out_comp_b = None
        self._out_open_id = None
        self._out_para = None

    @property
    def comp_c(self):
        return self._comp_c

    @comp_c.setter
    def comp_c(self, value):
        if isinstance(value, PubNestPub):
            self._comp_c = value
        else:
            self._comp_c = PubNestPub.from_alipay_dict(value)
    @property
    def comp_d(self):
        return self._comp_d

    @comp_d.setter
    def comp_d(self, value):
        if isinstance(value, DomainNestOther):
            self._comp_d = value
        else:
            self._comp_d = DomainNestOther.from_alipay_dict(value)
    @property
    def out_a(self):
        return self._out_a

    @out_a.setter
    def out_a(self, value):
        if isinstance(value, RegressionPublic):
            self._out_a = value
        else:
            self._out_a = RegressionPublic.from_alipay_dict(value)
    @property
    def out_comp_b(self):
        return self._out_comp_b

    @out_comp_b.setter
    def out_comp_b(self, value):
        if isinstance(value, RegressionInDomian):
            self._out_comp_b = value
        else:
            self._out_comp_b = RegressionInDomian.from_alipay_dict(value)
    @property
    def out_open_id(self):
        return self._out_open_id

    @out_open_id.setter
    def out_open_id(self, value):
        self._out_open_id = value
    @property
    def out_para(self):
        return self._out_para

    @out_para.setter
    def out_para(self, value):
        self._out_para = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdJhjtestRegressionQueryResponse, self).parse_response_content(response_content)
        if 'comp_c' in response:
            self.comp_c = response['comp_c']
        if 'comp_d' in response:
            self.comp_d = response['comp_d']
        if 'out_a' in response:
            self.out_a = response['out_a']
        if 'out_comp_b' in response:
            self.out_comp_b = response['out_comp_b']
        if 'out_open_id' in response:
            self.out_open_id = response['out_open_id']
        if 'out_para' in response:
            self.out_para = response['out_para']
