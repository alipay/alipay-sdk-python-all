#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductBaseVO import ProductBaseVO
from alipay.aop.api.domain.ProdIPRelationVO import ProdIPRelationVO
from alipay.aop.api.domain.ProdLORelationVO import ProdLORelationVO
from alipay.aop.api.domain.ProdMarkRelationVO import ProdMarkRelationVO
from alipay.aop.api.domain.ProdRelationVO import ProdRelationVO


class AntProdpaasProductCommonQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntProdpaasProductCommonQueryResponse, self).__init__()
        self._prod_base = None
        self._prod_condition = None
        self._prod_ip_list = None
        self._prod_lo_list = None
        self._prod_mark_list = None
        self._prod_rel_list = None

    @property
    def prod_base(self):
        return self._prod_base

    @prod_base.setter
    def prod_base(self, value):
        if isinstance(value, ProductBaseVO):
            self._prod_base = value
        else:
            self._prod_base = ProductBaseVO.from_alipay_dict(value)
    @property
    def prod_condition(self):
        return self._prod_condition

    @prod_condition.setter
    def prod_condition(self, value):
        self._prod_condition = value
    @property
    def prod_ip_list(self):
        return self._prod_ip_list

    @prod_ip_list.setter
    def prod_ip_list(self, value):
        if isinstance(value, list):
            self._prod_ip_list = list()
            for i in value:
                if isinstance(i, ProdIPRelationVO):
                    self._prod_ip_list.append(i)
                else:
                    self._prod_ip_list.append(ProdIPRelationVO.from_alipay_dict(i))
    @property
    def prod_lo_list(self):
        return self._prod_lo_list

    @prod_lo_list.setter
    def prod_lo_list(self, value):
        if isinstance(value, list):
            self._prod_lo_list = list()
            for i in value:
                if isinstance(i, ProdLORelationVO):
                    self._prod_lo_list.append(i)
                else:
                    self._prod_lo_list.append(ProdLORelationVO.from_alipay_dict(i))
    @property
    def prod_mark_list(self):
        return self._prod_mark_list

    @prod_mark_list.setter
    def prod_mark_list(self, value):
        if isinstance(value, list):
            self._prod_mark_list = list()
            for i in value:
                if isinstance(i, ProdMarkRelationVO):
                    self._prod_mark_list.append(i)
                else:
                    self._prod_mark_list.append(ProdMarkRelationVO.from_alipay_dict(i))
    @property
    def prod_rel_list(self):
        return self._prod_rel_list

    @prod_rel_list.setter
    def prod_rel_list(self, value):
        if isinstance(value, list):
            self._prod_rel_list = list()
            for i in value:
                if isinstance(i, ProdRelationVO):
                    self._prod_rel_list.append(i)
                else:
                    self._prod_rel_list.append(ProdRelationVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntProdpaasProductCommonQueryResponse, self).parse_response_content(response_content)
        if 'prod_base' in response:
            self.prod_base = response['prod_base']
        if 'prod_condition' in response:
            self.prod_condition = response['prod_condition']
        if 'prod_ip_list' in response:
            self.prod_ip_list = response['prod_ip_list']
        if 'prod_lo_list' in response:
            self.prod_lo_list = response['prod_lo_list']
        if 'prod_mark_list' in response:
            self.prod_mark_list = response['prod_mark_list']
        if 'prod_rel_list' in response:
            self.prod_rel_list = response['prod_rel_list']
