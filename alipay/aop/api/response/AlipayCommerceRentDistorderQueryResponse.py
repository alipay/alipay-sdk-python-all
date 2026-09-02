#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DistributionMerchantAddressDTO import DistributionMerchantAddressDTO
from alipay.aop.api.domain.DistItemDTO import DistItemDTO
from alipay.aop.api.domain.DistLogisticsInfoDTO import DistLogisticsInfoDTO
from alipay.aop.api.domain.DistRentPlanInfoDTO import DistRentPlanInfoDTO
from alipay.aop.api.domain.DistributionMerchantAddressDTO import DistributionMerchantAddressDTO


class AlipayCommerceRentDistorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentDistorderQueryResponse, self).__init__()
        self._act_tag = None
        self._biz_order_id = None
        self._buyer_address = None
        self._buyer_nick = None
        self._channel_buyer_id = None
        self._channel_order_id = None
        self._close_reason = None
        self._create_time = None
        self._credit_deposit_amount = None
        self._credit_deposit_status = None
        self._distribution_channel = None
        self._end_time = None
        self._freight = None
        self._fund_deposit_amount = None
        self._items = None
        self._logistics_info = None
        self._pay_time = None
        self._rent_plan_info = None
        self._return_address = None
        self._ship_time = None
        self._status = None

    @property
    def act_tag(self):
        return self._act_tag

    @act_tag.setter
    def act_tag(self, value):
        self._act_tag = value
    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def buyer_address(self):
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, value):
        if isinstance(value, DistributionMerchantAddressDTO):
            self._buyer_address = value
        else:
            self._buyer_address = DistributionMerchantAddressDTO.from_alipay_dict(value)
    @property
    def buyer_nick(self):
        return self._buyer_nick

    @buyer_nick.setter
    def buyer_nick(self, value):
        self._buyer_nick = value
    @property
    def channel_buyer_id(self):
        return self._channel_buyer_id

    @channel_buyer_id.setter
    def channel_buyer_id(self, value):
        self._channel_buyer_id = value
    @property
    def channel_order_id(self):
        return self._channel_order_id

    @channel_order_id.setter
    def channel_order_id(self, value):
        self._channel_order_id = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def credit_deposit_amount(self):
        return self._credit_deposit_amount

    @credit_deposit_amount.setter
    def credit_deposit_amount(self, value):
        self._credit_deposit_amount = value
    @property
    def credit_deposit_status(self):
        return self._credit_deposit_status

    @credit_deposit_status.setter
    def credit_deposit_status(self, value):
        self._credit_deposit_status = value
    @property
    def distribution_channel(self):
        return self._distribution_channel

    @distribution_channel.setter
    def distribution_channel(self, value):
        self._distribution_channel = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def freight(self):
        return self._freight

    @freight.setter
    def freight(self, value):
        self._freight = value
    @property
    def fund_deposit_amount(self):
        return self._fund_deposit_amount

    @fund_deposit_amount.setter
    def fund_deposit_amount(self, value):
        self._fund_deposit_amount = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, DistItemDTO):
                    self._items.append(i)
                else:
                    self._items.append(DistItemDTO.from_alipay_dict(i))
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        if isinstance(value, DistLogisticsInfoDTO):
            self._logistics_info = value
        else:
            self._logistics_info = DistLogisticsInfoDTO.from_alipay_dict(value)
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def rent_plan_info(self):
        return self._rent_plan_info

    @rent_plan_info.setter
    def rent_plan_info(self, value):
        if isinstance(value, DistRentPlanInfoDTO):
            self._rent_plan_info = value
        else:
            self._rent_plan_info = DistRentPlanInfoDTO.from_alipay_dict(value)
    @property
    def return_address(self):
        return self._return_address

    @return_address.setter
    def return_address(self, value):
        if isinstance(value, DistributionMerchantAddressDTO):
            self._return_address = value
        else:
            self._return_address = DistributionMerchantAddressDTO.from_alipay_dict(value)
    @property
    def ship_time(self):
        return self._ship_time

    @ship_time.setter
    def ship_time(self, value):
        self._ship_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentDistorderQueryResponse, self).parse_response_content(response_content)
        if 'act_tag' in response:
            self.act_tag = response['act_tag']
        if 'biz_order_id' in response:
            self.biz_order_id = response['biz_order_id']
        if 'buyer_address' in response:
            self.buyer_address = response['buyer_address']
        if 'buyer_nick' in response:
            self.buyer_nick = response['buyer_nick']
        if 'channel_buyer_id' in response:
            self.channel_buyer_id = response['channel_buyer_id']
        if 'channel_order_id' in response:
            self.channel_order_id = response['channel_order_id']
        if 'close_reason' in response:
            self.close_reason = response['close_reason']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'credit_deposit_amount' in response:
            self.credit_deposit_amount = response['credit_deposit_amount']
        if 'credit_deposit_status' in response:
            self.credit_deposit_status = response['credit_deposit_status']
        if 'distribution_channel' in response:
            self.distribution_channel = response['distribution_channel']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'freight' in response:
            self.freight = response['freight']
        if 'fund_deposit_amount' in response:
            self.fund_deposit_amount = response['fund_deposit_amount']
        if 'items' in response:
            self.items = response['items']
        if 'logistics_info' in response:
            self.logistics_info = response['logistics_info']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'rent_plan_info' in response:
            self.rent_plan_info = response['rent_plan_info']
        if 'return_address' in response:
            self.return_address = response['return_address']
        if 'ship_time' in response:
            self.ship_time = response['ship_time']
        if 'status' in response:
            self.status = response['status']
