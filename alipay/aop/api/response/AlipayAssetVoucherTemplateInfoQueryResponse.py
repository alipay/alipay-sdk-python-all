#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VcpFundInfo import VcpFundInfo


class AlipayAssetVoucherTemplateInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetVoucherTemplateInfoQueryResponse, self).__init__()
        self._asset_code = None
        self._fund_infos = None
        self._product_code = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._status = None
        self._template_id = None
        self._template_name = None

    @property
    def asset_code(self):
        return self._asset_code

    @asset_code.setter
    def asset_code(self, value):
        self._asset_code = value
    @property
    def fund_infos(self):
        return self._fund_infos

    @fund_infos.setter
    def fund_infos(self, value):
        if isinstance(value, list):
            self._fund_infos = list()
            for i in value:
                if isinstance(i, VcpFundInfo):
                    self._fund_infos.append(i)
                else:
                    self._fund_infos.append(VcpFundInfo.from_alipay_dict(i))
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetVoucherTemplateInfoQueryResponse, self).parse_response_content(response_content)
        if 'asset_code' in response:
            self.asset_code = response['asset_code']
        if 'fund_infos' in response:
            self.fund_infos = response['fund_infos']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'publish_end_time' in response:
            self.publish_end_time = response['publish_end_time']
        if 'publish_start_time' in response:
            self.publish_start_time = response['publish_start_time']
        if 'status' in response:
            self.status = response['status']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'template_name' in response:
            self.template_name = response['template_name']
