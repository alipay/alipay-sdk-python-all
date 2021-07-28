#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NetFlowOfferInfo import NetFlowOfferInfo


class NetFlowDeviceOfferInfoResponse(object):

    def __init__(self):
        self._card_status = None
        self._expire_time = None
        self._net_flow_offer_info_list = None
        self._offer_amount = None
        self._offer_url = None

    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def net_flow_offer_info_list(self):
        return self._net_flow_offer_info_list

    @net_flow_offer_info_list.setter
    def net_flow_offer_info_list(self, value):
        if isinstance(value, NetFlowOfferInfo):
            self._net_flow_offer_info_list = value
        else:
            self._net_flow_offer_info_list = NetFlowOfferInfo.from_alipay_dict(value)
    @property
    def offer_amount(self):
        return self._offer_amount

    @offer_amount.setter
    def offer_amount(self, value):
        self._offer_amount = value
    @property
    def offer_url(self):
        return self._offer_url

    @offer_url.setter
    def offer_url(self, value):
        self._offer_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.net_flow_offer_info_list:
            if hasattr(self.net_flow_offer_info_list, 'to_alipay_dict'):
                params['net_flow_offer_info_list'] = self.net_flow_offer_info_list.to_alipay_dict()
            else:
                params['net_flow_offer_info_list'] = self.net_flow_offer_info_list
        if self.offer_amount:
            if hasattr(self.offer_amount, 'to_alipay_dict'):
                params['offer_amount'] = self.offer_amount.to_alipay_dict()
            else:
                params['offer_amount'] = self.offer_amount
        if self.offer_url:
            if hasattr(self.offer_url, 'to_alipay_dict'):
                params['offer_url'] = self.offer_url.to_alipay_dict()
            else:
                params['offer_url'] = self.offer_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NetFlowDeviceOfferInfoResponse()
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'net_flow_offer_info_list' in d:
            o.net_flow_offer_info_list = d['net_flow_offer_info_list']
        if 'offer_amount' in d:
            o.offer_amount = d['offer_amount']
        if 'offer_url' in d:
            o.offer_url = d['offer_url']
        return o


