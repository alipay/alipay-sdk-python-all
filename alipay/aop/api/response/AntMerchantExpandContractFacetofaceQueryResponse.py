#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandContractFacetofaceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandContractFacetofaceQueryResponse, self).__init__()
        self._gmt_create = None
        self._order_detail = None
        self._order_no = None
        self._order_status = None
        self._out_biz_no = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def order_detail(self):
        return self._order_detail

    @order_detail.setter
    def order_detail(self, value):
        self._order_detail = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandContractFacetofaceQueryResponse, self).parse_response_content(response_content)
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'order_detail' in response:
            self.order_detail = response['order_detail']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
