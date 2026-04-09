#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleAuctionBidInfoVO import RecycleAuctionBidInfoVO
from alipay.aop.api.domain.RecycleAuctionBuyerInfoVO import RecycleAuctionBuyerInfoVO
from alipay.aop.api.domain.RecycleAuctionDeliveryInfoVO import RecycleAuctionDeliveryInfoVO
from alipay.aop.api.domain.RecycleAuctionMerchantInfoVO import RecycleAuctionMerchantInfoVO


class RecycleAuctionInfoVO(object):

    def __init__(self):
        self._auction_bid_info_list = None
        self._auction_buyer_info = None
        self._auction_delivery_info = None
        self._auction_merchant_info = None
        self._auction_price = None
        self._auction_status = None
        self._delivery_amount = None
        self._fee_amount = None
        self._user_amount = None

    @property
    def auction_bid_info_list(self):
        return self._auction_bid_info_list

    @auction_bid_info_list.setter
    def auction_bid_info_list(self, value):
        if isinstance(value, RecycleAuctionBidInfoVO):
            self._auction_bid_info_list = value
        else:
            self._auction_bid_info_list = RecycleAuctionBidInfoVO.from_alipay_dict(value)
    @property
    def auction_buyer_info(self):
        return self._auction_buyer_info

    @auction_buyer_info.setter
    def auction_buyer_info(self, value):
        if isinstance(value, RecycleAuctionBuyerInfoVO):
            self._auction_buyer_info = value
        else:
            self._auction_buyer_info = RecycleAuctionBuyerInfoVO.from_alipay_dict(value)
    @property
    def auction_delivery_info(self):
        return self._auction_delivery_info

    @auction_delivery_info.setter
    def auction_delivery_info(self, value):
        if isinstance(value, RecycleAuctionDeliveryInfoVO):
            self._auction_delivery_info = value
        else:
            self._auction_delivery_info = RecycleAuctionDeliveryInfoVO.from_alipay_dict(value)
    @property
    def auction_merchant_info(self):
        return self._auction_merchant_info

    @auction_merchant_info.setter
    def auction_merchant_info(self, value):
        if isinstance(value, RecycleAuctionMerchantInfoVO):
            self._auction_merchant_info = value
        else:
            self._auction_merchant_info = RecycleAuctionMerchantInfoVO.from_alipay_dict(value)
    @property
    def auction_price(self):
        return self._auction_price

    @auction_price.setter
    def auction_price(self, value):
        self._auction_price = value
    @property
    def auction_status(self):
        return self._auction_status

    @auction_status.setter
    def auction_status(self, value):
        self._auction_status = value
    @property
    def delivery_amount(self):
        return self._delivery_amount

    @delivery_amount.setter
    def delivery_amount(self, value):
        self._delivery_amount = value
    @property
    def fee_amount(self):
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, value):
        self._fee_amount = value
    @property
    def user_amount(self):
        return self._user_amount

    @user_amount.setter
    def user_amount(self, value):
        self._user_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.auction_bid_info_list:
            if hasattr(self.auction_bid_info_list, 'to_alipay_dict'):
                params['auction_bid_info_list'] = self.auction_bid_info_list.to_alipay_dict()
            else:
                params['auction_bid_info_list'] = self.auction_bid_info_list
        if self.auction_buyer_info:
            if hasattr(self.auction_buyer_info, 'to_alipay_dict'):
                params['auction_buyer_info'] = self.auction_buyer_info.to_alipay_dict()
            else:
                params['auction_buyer_info'] = self.auction_buyer_info
        if self.auction_delivery_info:
            if hasattr(self.auction_delivery_info, 'to_alipay_dict'):
                params['auction_delivery_info'] = self.auction_delivery_info.to_alipay_dict()
            else:
                params['auction_delivery_info'] = self.auction_delivery_info
        if self.auction_merchant_info:
            if hasattr(self.auction_merchant_info, 'to_alipay_dict'):
                params['auction_merchant_info'] = self.auction_merchant_info.to_alipay_dict()
            else:
                params['auction_merchant_info'] = self.auction_merchant_info
        if self.auction_price:
            if hasattr(self.auction_price, 'to_alipay_dict'):
                params['auction_price'] = self.auction_price.to_alipay_dict()
            else:
                params['auction_price'] = self.auction_price
        if self.auction_status:
            if hasattr(self.auction_status, 'to_alipay_dict'):
                params['auction_status'] = self.auction_status.to_alipay_dict()
            else:
                params['auction_status'] = self.auction_status
        if self.delivery_amount:
            if hasattr(self.delivery_amount, 'to_alipay_dict'):
                params['delivery_amount'] = self.delivery_amount.to_alipay_dict()
            else:
                params['delivery_amount'] = self.delivery_amount
        if self.fee_amount:
            if hasattr(self.fee_amount, 'to_alipay_dict'):
                params['fee_amount'] = self.fee_amount.to_alipay_dict()
            else:
                params['fee_amount'] = self.fee_amount
        if self.user_amount:
            if hasattr(self.user_amount, 'to_alipay_dict'):
                params['user_amount'] = self.user_amount.to_alipay_dict()
            else:
                params['user_amount'] = self.user_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleAuctionInfoVO()
        if 'auction_bid_info_list' in d:
            o.auction_bid_info_list = d['auction_bid_info_list']
        if 'auction_buyer_info' in d:
            o.auction_buyer_info = d['auction_buyer_info']
        if 'auction_delivery_info' in d:
            o.auction_delivery_info = d['auction_delivery_info']
        if 'auction_merchant_info' in d:
            o.auction_merchant_info = d['auction_merchant_info']
        if 'auction_price' in d:
            o.auction_price = d['auction_price']
        if 'auction_status' in d:
            o.auction_status = d['auction_status']
        if 'delivery_amount' in d:
            o.delivery_amount = d['delivery_amount']
        if 'fee_amount' in d:
            o.fee_amount = d['fee_amount']
        if 'user_amount' in d:
            o.user_amount = d['user_amount']
        return o


