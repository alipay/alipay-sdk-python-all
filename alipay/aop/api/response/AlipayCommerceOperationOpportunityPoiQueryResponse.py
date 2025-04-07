#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationOpportunityPoiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationOpportunityPoiQueryResponse, self).__init__()
        self._opportunity_id = None
        self._opportunity_status = None
        self._opportunity_status_info = None
        self._out_biz_no = None

    @property
    def opportunity_id(self):
        return self._opportunity_id

    @opportunity_id.setter
    def opportunity_id(self, value):
        self._opportunity_id = value
    @property
    def opportunity_status(self):
        return self._opportunity_status

    @opportunity_status.setter
    def opportunity_status(self, value):
        self._opportunity_status = value
    @property
    def opportunity_status_info(self):
        return self._opportunity_status_info

    @opportunity_status_info.setter
    def opportunity_status_info(self, value):
        self._opportunity_status_info = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationOpportunityPoiQueryResponse, self).parse_response_content(response_content)
        if 'opportunity_id' in response:
            self.opportunity_id = response['opportunity_id']
        if 'opportunity_status' in response:
            self.opportunity_status = response['opportunity_status']
        if 'opportunity_status_info' in response:
            self.opportunity_status_info = response['opportunity_status_info']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
