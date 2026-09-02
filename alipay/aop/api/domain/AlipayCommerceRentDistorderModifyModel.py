#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DistributionProcessBuyerAddressModifyApplyDTO import DistributionProcessBuyerAddressModifyApplyDTO
from alipay.aop.api.domain.DistributionOrderPriceAndPeriodDTO import DistributionOrderPriceAndPeriodDTO
from alipay.aop.api.domain.DistributionOrderReturnAddressDTO import DistributionOrderReturnAddressDTO


class AlipayCommerceRentDistorderModifyModel(object):

    def __init__(self):
        self._biz_order_id = None
        self._buyer_address_modify_apply_info = None
        self._channel_buyer_id = None
        self._channel_order_id = None
        self._distribution_channel = None
        self._modify_type = None
        self._price_and_period_info = None
        self._return_address_info = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def buyer_address_modify_apply_info(self):
        return self._buyer_address_modify_apply_info

    @buyer_address_modify_apply_info.setter
    def buyer_address_modify_apply_info(self, value):
        if isinstance(value, DistributionProcessBuyerAddressModifyApplyDTO):
            self._buyer_address_modify_apply_info = value
        else:
            self._buyer_address_modify_apply_info = DistributionProcessBuyerAddressModifyApplyDTO.from_alipay_dict(value)
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
    def distribution_channel(self):
        return self._distribution_channel

    @distribution_channel.setter
    def distribution_channel(self, value):
        self._distribution_channel = value
    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value
    @property
    def price_and_period_info(self):
        return self._price_and_period_info

    @price_and_period_info.setter
    def price_and_period_info(self, value):
        if isinstance(value, DistributionOrderPriceAndPeriodDTO):
            self._price_and_period_info = value
        else:
            self._price_and_period_info = DistributionOrderPriceAndPeriodDTO.from_alipay_dict(value)
    @property
    def return_address_info(self):
        return self._return_address_info

    @return_address_info.setter
    def return_address_info(self, value):
        if isinstance(value, DistributionOrderReturnAddressDTO):
            self._return_address_info = value
        else:
            self._return_address_info = DistributionOrderReturnAddressDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.buyer_address_modify_apply_info:
            if hasattr(self.buyer_address_modify_apply_info, 'to_alipay_dict'):
                params['buyer_address_modify_apply_info'] = self.buyer_address_modify_apply_info.to_alipay_dict()
            else:
                params['buyer_address_modify_apply_info'] = self.buyer_address_modify_apply_info
        if self.channel_buyer_id:
            if hasattr(self.channel_buyer_id, 'to_alipay_dict'):
                params['channel_buyer_id'] = self.channel_buyer_id.to_alipay_dict()
            else:
                params['channel_buyer_id'] = self.channel_buyer_id
        if self.channel_order_id:
            if hasattr(self.channel_order_id, 'to_alipay_dict'):
                params['channel_order_id'] = self.channel_order_id.to_alipay_dict()
            else:
                params['channel_order_id'] = self.channel_order_id
        if self.distribution_channel:
            if hasattr(self.distribution_channel, 'to_alipay_dict'):
                params['distribution_channel'] = self.distribution_channel.to_alipay_dict()
            else:
                params['distribution_channel'] = self.distribution_channel
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
        if self.price_and_period_info:
            if hasattr(self.price_and_period_info, 'to_alipay_dict'):
                params['price_and_period_info'] = self.price_and_period_info.to_alipay_dict()
            else:
                params['price_and_period_info'] = self.price_and_period_info
        if self.return_address_info:
            if hasattr(self.return_address_info, 'to_alipay_dict'):
                params['return_address_info'] = self.return_address_info.to_alipay_dict()
            else:
                params['return_address_info'] = self.return_address_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentDistorderModifyModel()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'buyer_address_modify_apply_info' in d:
            o.buyer_address_modify_apply_info = d['buyer_address_modify_apply_info']
        if 'channel_buyer_id' in d:
            o.channel_buyer_id = d['channel_buyer_id']
        if 'channel_order_id' in d:
            o.channel_order_id = d['channel_order_id']
        if 'distribution_channel' in d:
            o.distribution_channel = d['distribution_channel']
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        if 'price_and_period_info' in d:
            o.price_and_period_info = d['price_and_period_info']
        if 'return_address_info' in d:
            o.return_address_info = d['return_address_info']
        return o


