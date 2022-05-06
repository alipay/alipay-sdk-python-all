#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryBaseInfo import DeliveryBaseInfo
from alipay.aop.api.domain.PromoDeliveryInfo import PromoDeliveryInfo
from alipay.aop.api.domain.DeliveryPlayConfig import DeliveryPlayConfig
from alipay.aop.api.domain.DeliveryTargetRule import DeliveryTargetRule


class AlipayMarketingActivityDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityDeliveryQueryResponse, self).__init__()
        self._delivery_base_info = None
        self._delivery_booth_code = None
        self._delivery_error_msg = None
        self._delivery_id = None
        self._delivery_info_list = None
        self._delivery_play_config = None
        self._delivery_status = None
        self._delivery_target_rule = None

    @property
    def delivery_base_info(self):
        return self._delivery_base_info

    @delivery_base_info.setter
    def delivery_base_info(self, value):
        if isinstance(value, DeliveryBaseInfo):
            self._delivery_base_info = value
        else:
            self._delivery_base_info = DeliveryBaseInfo.from_alipay_dict(value)
    @property
    def delivery_booth_code(self):
        return self._delivery_booth_code

    @delivery_booth_code.setter
    def delivery_booth_code(self, value):
        self._delivery_booth_code = value
    @property
    def delivery_error_msg(self):
        return self._delivery_error_msg

    @delivery_error_msg.setter
    def delivery_error_msg(self, value):
        self._delivery_error_msg = value
    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def delivery_info_list(self):
        return self._delivery_info_list

    @delivery_info_list.setter
    def delivery_info_list(self, value):
        if isinstance(value, list):
            self._delivery_info_list = list()
            for i in value:
                if isinstance(i, PromoDeliveryInfo):
                    self._delivery_info_list.append(i)
                else:
                    self._delivery_info_list.append(PromoDeliveryInfo.from_alipay_dict(i))
    @property
    def delivery_play_config(self):
        return self._delivery_play_config

    @delivery_play_config.setter
    def delivery_play_config(self, value):
        if isinstance(value, DeliveryPlayConfig):
            self._delivery_play_config = value
        else:
            self._delivery_play_config = DeliveryPlayConfig.from_alipay_dict(value)
    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def delivery_target_rule(self):
        return self._delivery_target_rule

    @delivery_target_rule.setter
    def delivery_target_rule(self, value):
        if isinstance(value, DeliveryTargetRule):
            self._delivery_target_rule = value
        else:
            self._delivery_target_rule = DeliveryTargetRule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'delivery_base_info' in response:
            self.delivery_base_info = response['delivery_base_info']
        if 'delivery_booth_code' in response:
            self.delivery_booth_code = response['delivery_booth_code']
        if 'delivery_error_msg' in response:
            self.delivery_error_msg = response['delivery_error_msg']
        if 'delivery_id' in response:
            self.delivery_id = response['delivery_id']
        if 'delivery_info_list' in response:
            self.delivery_info_list = response['delivery_info_list']
        if 'delivery_play_config' in response:
            self.delivery_play_config = response['delivery_play_config']
        if 'delivery_status' in response:
            self.delivery_status = response['delivery_status']
        if 'delivery_target_rule' in response:
            self.delivery_target_rule = response['delivery_target_rule']
