#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationOpportunityLeadsCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationOpportunityLeadsCreateResponse, self).__init__()
        self._installation_code = None
        self._leads_id = None
        self._opportunity_id = None
        self._opportunity_status = None
        self._opportunity_status_info = None
        self._out_biz_no = None
        self._source = None

    @property
    def installation_code(self):
        return self._installation_code

    @installation_code.setter
    def installation_code(self, value):
        self._installation_code = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
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
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationOpportunityLeadsCreateResponse, self).parse_response_content(response_content)
        if 'installation_code' in response:
            self.installation_code = response['installation_code']
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
        if 'opportunity_id' in response:
            self.opportunity_id = response['opportunity_id']
        if 'opportunity_status' in response:
            self.opportunity_status = response['opportunity_status']
        if 'opportunity_status_info' in response:
            self.opportunity_status_info = response['opportunity_status_info']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'source' in response:
            self.source = response['source']
