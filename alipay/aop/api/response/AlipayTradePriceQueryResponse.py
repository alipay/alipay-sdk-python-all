#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NexusPayProduct import NexusPayProduct
from alipay.aop.api.domain.RecurringConfig import RecurringConfig


class AlipayTradePriceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePriceQueryResponse, self).__init__()
        self._active = None
        self._gmt_create = None
        self._id = None
        self._metadata = None
        self._product = None
        self._product_id = None
        self._recurring = None
        self._type = None
        self._unit_amount = None

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, NexusPayProduct):
            self._product = value
        else:
            self._product = NexusPayProduct.from_alipay_dict(value)
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def recurring(self):
        return self._recurring

    @recurring.setter
    def recurring(self, value):
        if isinstance(value, RecurringConfig):
            self._recurring = value
        else:
            self._recurring = RecurringConfig.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self._unit_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePriceQueryResponse, self).parse_response_content(response_content)
        if 'active' in response:
            self.active = response['active']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'id' in response:
            self.id = response['id']
        if 'metadata' in response:
            self.metadata = response['metadata']
        if 'product' in response:
            self.product = response['product']
        if 'product_id' in response:
            self.product_id = response['product_id']
        if 'recurring' in response:
            self.recurring = response['recurring']
        if 'type' in response:
            self.type = response['type']
        if 'unit_amount' in response:
            self.unit_amount = response['unit_amount']
