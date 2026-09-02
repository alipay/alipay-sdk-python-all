#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceApplyExpressInfo import DeviceApplyExpressInfo


class AlipayCommerceIotDapplyOrderlogisticsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyOrderlogisticsQueryResponse, self).__init__()
        self._asset_apply_order_id = None
        self._deliver_count = None
        self._express_list = None
        self._receiver_mobile = None
        self._receiver_name = None

    @property
    def asset_apply_order_id(self):
        return self._asset_apply_order_id

    @asset_apply_order_id.setter
    def asset_apply_order_id(self, value):
        self._asset_apply_order_id = value
    @property
    def deliver_count(self):
        return self._deliver_count

    @deliver_count.setter
    def deliver_count(self, value):
        self._deliver_count = value
    @property
    def express_list(self):
        return self._express_list

    @express_list.setter
    def express_list(self, value):
        if isinstance(value, list):
            self._express_list = list()
            for i in value:
                if isinstance(i, DeviceApplyExpressInfo):
                    self._express_list.append(i)
                else:
                    self._express_list.append(DeviceApplyExpressInfo.from_alipay_dict(i))
    @property
    def receiver_mobile(self):
        return self._receiver_mobile

    @receiver_mobile.setter
    def receiver_mobile(self, value):
        self._receiver_mobile = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyOrderlogisticsQueryResponse, self).parse_response_content(response_content)
        if 'asset_apply_order_id' in response:
            self.asset_apply_order_id = response['asset_apply_order_id']
        if 'deliver_count' in response:
            self.deliver_count = response['deliver_count']
        if 'express_list' in response:
            self.express_list = response['express_list']
        if 'receiver_mobile' in response:
            self.receiver_mobile = response['receiver_mobile']
        if 'receiver_name' in response:
            self.receiver_name = response['receiver_name']
