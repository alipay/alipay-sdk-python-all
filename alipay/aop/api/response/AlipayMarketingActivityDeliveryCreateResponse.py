#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ErrorDeliveryConfig import ErrorDeliveryConfig
from alipay.aop.api.domain.SuccessDeliveryConfig import SuccessDeliveryConfig


class AlipayMarketingActivityDeliveryCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityDeliveryCreateResponse, self).__init__()
        self._delivery_guide_preview_url = None
        self._delivery_id = None
        self._error_delivery_config_list = None
        self._out_biz_no = None
        self._success_delivery_config_list = None

    @property
    def delivery_guide_preview_url(self):
        return self._delivery_guide_preview_url

    @delivery_guide_preview_url.setter
    def delivery_guide_preview_url(self, value):
        self._delivery_guide_preview_url = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
        response = super(AlipayMarketingActivityDeliveryCreateResponse, self).parse_response_content(response_content)
        if 'delivery_guide_preview_url' in response:
            self.delivery_guide_preview_url = response['delivery_guide_preview_url']
        if 'delivery_id' in response:
            self.delivery_id = response['delivery_id']
        if 'error_delivery_config_list' in response:
            self.error_delivery_config_list = response['error_delivery_config_list']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'success_delivery_config_list' in response:
            self.success_delivery_config_list = response['success_delivery_config_list']
