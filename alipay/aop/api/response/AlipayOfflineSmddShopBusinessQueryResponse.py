#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessTimeBean import BusinessTimeBean


class AlipayOfflineSmddShopBusinessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddShopBusinessQueryResponse, self).__init__()
        self._business_status = None
        self._business_time_desc = None
        self._business_time_list = None
        self._business_time_rest = None

    @property
    def business_status(self):
        return self._business_status

    @business_status.setter
    def business_status(self, value):
        self._business_status = value
    @property
    def business_time_desc(self):
        return self._business_time_desc

    @business_time_desc.setter
    def business_time_desc(self, value):
        self._business_time_desc = value
    @property
    def business_time_list(self):
        return self._business_time_list

    @business_time_list.setter
    def business_time_list(self, value):
        if isinstance(value, list):
            self._business_time_list = list()
            for i in value:
                if isinstance(i, BusinessTimeBean):
                    self._business_time_list.append(i)
                else:
                    self._business_time_list.append(BusinessTimeBean.from_alipay_dict(i))
    @property
    def business_time_rest(self):
        return self._business_time_rest

    @business_time_rest.setter
    def business_time_rest(self, value):
        self._business_time_rest = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddShopBusinessQueryResponse, self).parse_response_content(response_content)
        if 'business_status' in response:
            self.business_status = response['business_status']
        if 'business_time_desc' in response:
            self.business_time_desc = response['business_time_desc']
        if 'business_time_list' in response:
            self.business_time_list = response['business_time_list']
        if 'business_time_rest' in response:
            self.business_time_rest = response['business_time_rest']
