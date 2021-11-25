#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductAgentStatusInfo import ProductAgentStatusInfo
from alipay.aop.api.domain.SignRestrictInfo import SignRestrictInfo


class AlipayOpenAgentOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentOrderQueryResponse, self).__init__()
        self._agent_app_id = None
        self._confirm_url = None
        self._merchant_pid = None
        self._order_no = None
        self._order_status = None
        self._product_agent_status_infos = None
        self._reject_reason = None
        self._restrict_infos = None

    @property
    def agent_app_id(self):
        return self._agent_app_id

    @agent_app_id.setter
    def agent_app_id(self, value):
        self._agent_app_id = value
    @property
    def confirm_url(self):
        return self._confirm_url

    @confirm_url.setter
    def confirm_url(self, value):
        self._confirm_url = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
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
    def product_agent_status_infos(self):
        return self._product_agent_status_infos

    @product_agent_status_infos.setter
    def product_agent_status_infos(self, value):
        if isinstance(value, list):
            self._product_agent_status_infos = list()
            for i in value:
                if isinstance(i, ProductAgentStatusInfo):
                    self._product_agent_status_infos.append(i)
                else:
                    self._product_agent_status_infos.append(ProductAgentStatusInfo.from_alipay_dict(i))
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def restrict_infos(self):
        return self._restrict_infos

    @restrict_infos.setter
    def restrict_infos(self, value):
        if isinstance(value, list):
            self._restrict_infos = list()
            for i in value:
                if isinstance(i, SignRestrictInfo):
                    self._restrict_infos.append(i)
                else:
                    self._restrict_infos.append(SignRestrictInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentOrderQueryResponse, self).parse_response_content(response_content)
        if 'agent_app_id' in response:
            self.agent_app_id = response['agent_app_id']
        if 'confirm_url' in response:
            self.confirm_url = response['confirm_url']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'product_agent_status_infos' in response:
            self.product_agent_status_infos = response['product_agent_status_infos']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'restrict_infos' in response:
            self.restrict_infos = response['restrict_infos']
