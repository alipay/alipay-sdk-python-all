#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceFsupvTaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceFsupvTaskCreateResponse, self).__init__()
        self._accepted_no = None
        self._authorization_link = None
        self._fund_supv_task_id = None
        self._link_expiry = None

    @property
    def accepted_no(self):
        return self._accepted_no

    @accepted_no.setter
    def accepted_no(self, value):
        self._accepted_no = value
    @property
    def authorization_link(self):
        return self._authorization_link

    @authorization_link.setter
    def authorization_link(self, value):
        self._authorization_link = value
    @property
    def fund_supv_task_id(self):
        return self._fund_supv_task_id

    @fund_supv_task_id.setter
    def fund_supv_task_id(self, value):
        self._fund_supv_task_id = value
    @property
    def link_expiry(self):
        return self._link_expiry

    @link_expiry.setter
    def link_expiry(self, value):
        self._link_expiry = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceFsupvTaskCreateResponse, self).parse_response_content(response_content)
        if 'accepted_no' in response:
            self.accepted_no = response['accepted_no']
        if 'authorization_link' in response:
            self.authorization_link = response['authorization_link']
        if 'fund_supv_task_id' in response:
            self.fund_supv_task_id = response['fund_supv_task_id']
        if 'link_expiry' in response:
            self.link_expiry = response['link_expiry']
