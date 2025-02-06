#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DetailCommissionInfo import DetailCommissionInfo


class AlipayOpenSpCommissionDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpCommissionDetailQueryResponse, self).__init__()
        self._commission_list = None
        self._commission_mode = None
        self._commission_scene = None
        self._merchant_confirm_url = None
        self._merchant_id = None
        self._merchant_logon_id = None
        self._merchant_name = None
        self._modify_time = None

    @property
    def commission_list(self):
        return self._commission_list

    @commission_list.setter
    def commission_list(self, value):
        if isinstance(value, list):
            self._commission_list = list()
            for i in value:
                if isinstance(i, DetailCommissionInfo):
                    self._commission_list.append(i)
                else:
                    self._commission_list.append(DetailCommissionInfo.from_alipay_dict(i))
    @property
    def commission_mode(self):
        return self._commission_mode

    @commission_mode.setter
    def commission_mode(self, value):
        self._commission_mode = value
    @property
    def commission_scene(self):
        return self._commission_scene

    @commission_scene.setter
    def commission_scene(self, value):
        self._commission_scene = value
    @property
    def merchant_confirm_url(self):
        return self._merchant_confirm_url

    @merchant_confirm_url.setter
    def merchant_confirm_url(self, value):
        self._merchant_confirm_url = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_logon_id(self):
        return self._merchant_logon_id

    @merchant_logon_id.setter
    def merchant_logon_id(self, value):
        self._merchant_logon_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpCommissionDetailQueryResponse, self).parse_response_content(response_content)
        if 'commission_list' in response:
            self.commission_list = response['commission_list']
        if 'commission_mode' in response:
            self.commission_mode = response['commission_mode']
        if 'commission_scene' in response:
            self.commission_scene = response['commission_scene']
        if 'merchant_confirm_url' in response:
            self.merchant_confirm_url = response['merchant_confirm_url']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'merchant_logon_id' in response:
            self.merchant_logon_id = response['merchant_logon_id']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'modify_time' in response:
            self.modify_time = response['modify_time']
