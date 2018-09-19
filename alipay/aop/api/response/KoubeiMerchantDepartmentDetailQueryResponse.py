#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SimpleShopModel import SimpleShopModel


class KoubeiMerchantDepartmentDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantDepartmentDetailQueryResponse, self).__init__()
        self._dept_id = None
        self._dept_name = None
        self._label_code = None
        self._parent_dept_id = None
        self._shops = None
        self._type = None

    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value
    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def label_code(self):
        return self._label_code

    @label_code.setter
    def label_code(self, value):
        self._label_code = value
    @property
    def parent_dept_id(self):
        return self._parent_dept_id

    @parent_dept_id.setter
    def parent_dept_id(self, value):
        self._parent_dept_id = value
    @property
    def shops(self):
        return self._shops

    @shops.setter
    def shops(self, value):
        if isinstance(value, list):
            self._shops = list()
            for i in value:
                if isinstance(i, SimpleShopModel):
                    self._shops.append(i)
                else:
                    self._shops.append(SimpleShopModel.from_alipay_dict(i))
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantDepartmentDetailQueryResponse, self).parse_response_content(response_content)
        if 'dept_id' in response:
            self.dept_id = response['dept_id']
        if 'dept_name' in response:
            self.dept_name = response['dept_name']
        if 'label_code' in response:
            self.label_code = response['label_code']
        if 'parent_dept_id' in response:
            self.parent_dept_id = response['parent_dept_id']
        if 'shops' in response:
            self.shops = response['shops']
        if 'type' in response:
            self.type = response['type']
