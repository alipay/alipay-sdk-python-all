#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FlowSigner import FlowSigner


class AlipayEcoSignFlowQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoSignFlowQueryResponse, self).__init__()
        self._business_scene = None
        self._contract_validity = None
        self._flow_desc = None
        self._flow_end_time = None
        self._flow_id = None
        self._flow_start_time = None
        self._flow_status = None
        self._notice_developer_url = None
        self._sign_validity = None
        self._signers = None

    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def contract_validity(self):
        return self._contract_validity

    @contract_validity.setter
    def contract_validity(self, value):
        self._contract_validity = value
    @property
    def flow_desc(self):
        return self._flow_desc

    @flow_desc.setter
    def flow_desc(self, value):
        self._flow_desc = value
    @property
    def flow_end_time(self):
        return self._flow_end_time

    @flow_end_time.setter
    def flow_end_time(self, value):
        self._flow_end_time = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def flow_start_time(self):
        return self._flow_start_time

    @flow_start_time.setter
    def flow_start_time(self, value):
        self._flow_start_time = value
    @property
    def flow_status(self):
        return self._flow_status

    @flow_status.setter
    def flow_status(self, value):
        self._flow_status = value
    @property
    def notice_developer_url(self):
        return self._notice_developer_url

    @notice_developer_url.setter
    def notice_developer_url(self, value):
        self._notice_developer_url = value
    @property
    def sign_validity(self):
        return self._sign_validity

    @sign_validity.setter
    def sign_validity(self, value):
        self._sign_validity = value
    @property
    def signers(self):
        return self._signers

    @signers.setter
    def signers(self, value):
        if isinstance(value, list):
            self._signers = list()
            for i in value:
                if isinstance(i, FlowSigner):
                    self._signers.append(i)
                else:
                    self._signers.append(FlowSigner.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoSignFlowQueryResponse, self).parse_response_content(response_content)
        if 'business_scene' in response:
            self.business_scene = response['business_scene']
        if 'contract_validity' in response:
            self.contract_validity = response['contract_validity']
        if 'flow_desc' in response:
            self.flow_desc = response['flow_desc']
        if 'flow_end_time' in response:
            self.flow_end_time = response['flow_end_time']
        if 'flow_id' in response:
            self.flow_id = response['flow_id']
        if 'flow_start_time' in response:
            self.flow_start_time = response['flow_start_time']
        if 'flow_status' in response:
            self.flow_status = response['flow_status']
        if 'notice_developer_url' in response:
            self.notice_developer_url = response['notice_developer_url']
        if 'sign_validity' in response:
            self.sign_validity = response['sign_validity']
        if 'signers' in response:
            self.signers = response['signers']
