#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ErrorDeliveryConfig import ErrorDeliveryConfig
from alipay.aop.api.domain.SuccessDeliveryConfig import SuccessDeliveryConfig


class AlipayMarketingActivityDeliveryStopResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityDeliveryStopResponse, self).__init__()
        self._delivery_id = None
        self._error_delivery_config_list = None
        self._success_delivery_config_list = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def error_delivery_config_list(self):
        return self._error_delivery_config_list

    @error_delivery_config_list.setter
    def error_delivery_config_list(self, value):
        if isinstance(value, list):
            self._error_delivery_config_list = list()
            for i in value:
                if isinstance(i, ErrorDeliveryConfig):
                    self._error_delivery_config_list.append(i)
                else:
                    self._error_delivery_config_list.append(ErrorDeliveryConfig.from_alipay_dict(i))
    @property
    def success_delivery_config_list(self):
        return self._success_delivery_config_list

    @success_delivery_config_list.setter
    def success_delivery_config_list(self, value):
        if isinstance(value, list):
            self._success_delivery_config_list = list()
            for i in value:
                if isinstance(i, SuccessDeliveryConfig):
                    self._success_delivery_config_list.append(i)
                else:
                    self._success_delivery_config_list.append(SuccessDeliveryConfig.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityDeliveryStopResponse, self).parse_response_content(response_content)
        if 'delivery_id' in response:
            self.delivery_id = response['delivery_id']
        if 'error_delivery_config_list' in response:
            self.error_delivery_config_list = response['error_delivery_config_list']
        if 'success_delivery_config_list' in response:
            self.success_delivery_config_list = response['success_delivery_config_list']
