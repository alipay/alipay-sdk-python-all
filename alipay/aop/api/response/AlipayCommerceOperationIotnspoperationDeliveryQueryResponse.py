#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NDeliveryBaseInfo import NDeliveryBaseInfo
from alipay.aop.api.domain.NDeliveryPalyConfig import NDeliveryPalyConfig
from alipay.aop.api.domain.NDeliveryTargetRule import NDeliveryTargetRule


class AlipayCommerceOperationIotnspoperationDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationIotnspoperationDeliveryQueryResponse, self).__init__()
        self._n_delivery_base_info = None
        self._n_delivery_create_msg = None
        self._n_delivery_id = None
        self._n_delivery_paly_config = None
        self._n_delivery_reject_msg = None
        self._n_delivery_status = None
        self._n_delivery_target_rule = None

    @property
    def n_delivery_base_info(self):
        return self._n_delivery_base_info

    @n_delivery_base_info.setter
    def n_delivery_base_info(self, value):
        if isinstance(value, NDeliveryBaseInfo):
            self._n_delivery_base_info = value
        else:
            self._n_delivery_base_info = NDeliveryBaseInfo.from_alipay_dict(value)
    @property
    def n_delivery_create_msg(self):
        return self._n_delivery_create_msg

    @n_delivery_create_msg.setter
    def n_delivery_create_msg(self, value):
        self._n_delivery_create_msg = value
    @property
    def n_delivery_id(self):
        return self._n_delivery_id

    @n_delivery_id.setter
    def n_delivery_id(self, value):
        self._n_delivery_id = value
    @property
    def n_delivery_paly_config(self):
        return self._n_delivery_paly_config

    @n_delivery_paly_config.setter
    def n_delivery_paly_config(self, value):
        if isinstance(value, NDeliveryPalyConfig):
            self._n_delivery_paly_config = value
        else:
            self._n_delivery_paly_config = NDeliveryPalyConfig.from_alipay_dict(value)
    @property
    def n_delivery_reject_msg(self):
        return self._n_delivery_reject_msg

    @n_delivery_reject_msg.setter
    def n_delivery_reject_msg(self, value):
        self._n_delivery_reject_msg = value
    @property
    def n_delivery_status(self):
        return self._n_delivery_status

    @n_delivery_status.setter
    def n_delivery_status(self, value):
        self._n_delivery_status = value
    @property
    def n_delivery_target_rule(self):
        return self._n_delivery_target_rule

    @n_delivery_target_rule.setter
    def n_delivery_target_rule(self, value):
        if isinstance(value, NDeliveryTargetRule):
            self._n_delivery_target_rule = value
        else:
            self._n_delivery_target_rule = NDeliveryTargetRule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationIotnspoperationDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'n_delivery_base_info' in response:
            self.n_delivery_base_info = response['n_delivery_base_info']
        if 'n_delivery_create_msg' in response:
            self.n_delivery_create_msg = response['n_delivery_create_msg']
        if 'n_delivery_id' in response:
            self.n_delivery_id = response['n_delivery_id']
        if 'n_delivery_paly_config' in response:
            self.n_delivery_paly_config = response['n_delivery_paly_config']
        if 'n_delivery_reject_msg' in response:
            self.n_delivery_reject_msg = response['n_delivery_reject_msg']
        if 'n_delivery_status' in response:
            self.n_delivery_status = response['n_delivery_status']
        if 'n_delivery_target_rule' in response:
            self.n_delivery_target_rule = response['n_delivery_target_rule']
