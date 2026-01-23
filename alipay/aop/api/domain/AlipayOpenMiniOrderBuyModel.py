#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderBuyDTO import OrderBuyDTO
from alipay.aop.api.domain.PromoDetailInfoDTO import PromoDetailInfoDTO


class AlipayOpenMiniOrderBuyModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_logon_id = None
        self._buyer_open_id = None
        self._mini_order_create_requests = None
        self._order_buy_no = None
        self._promo_detail_info = None
        self._source_id = None
        self._timeout_express = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def mini_order_create_requests(self):
        return self._mini_order_create_requests

    @mini_order_create_requests.setter
    def mini_order_create_requests(self, value):
        if isinstance(value, list):
            self._mini_order_create_requests = list()
            for i in value:
                if isinstance(i, OrderBuyDTO):
                    self._mini_order_create_requests.append(i)
                else:
                    self._mini_order_create_requests.append(OrderBuyDTO.from_alipay_dict(i))
    @property
    def order_buy_no(self):
        return self._order_buy_no

    @order_buy_no.setter
    def order_buy_no(self, value):
        self._order_buy_no = value
    @property
    def promo_detail_info(self):
        return self._promo_detail_info

    @promo_detail_info.setter
    def promo_detail_info(self, value):
        if isinstance(value, PromoDetailInfoDTO):
            self._promo_detail_info = value
        else:
            self._promo_detail_info = PromoDetailInfoDTO.from_alipay_dict(value)
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_logon_id:
            if hasattr(self.buyer_logon_id, 'to_alipay_dict'):
                params['buyer_logon_id'] = self.buyer_logon_id.to_alipay_dict()
            else:
                params['buyer_logon_id'] = self.buyer_logon_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.mini_order_create_requests:
            if isinstance(self.mini_order_create_requests, list):
                for i in range(0, len(self.mini_order_create_requests)):
                    element = self.mini_order_create_requests[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mini_order_create_requests[i] = element.to_alipay_dict()
            if hasattr(self.mini_order_create_requests, 'to_alipay_dict'):
                params['mini_order_create_requests'] = self.mini_order_create_requests.to_alipay_dict()
            else:
                params['mini_order_create_requests'] = self.mini_order_create_requests
        if self.order_buy_no:
            if hasattr(self.order_buy_no, 'to_alipay_dict'):
                params['order_buy_no'] = self.order_buy_no.to_alipay_dict()
            else:
                params['order_buy_no'] = self.order_buy_no
        if self.promo_detail_info:
            if hasattr(self.promo_detail_info, 'to_alipay_dict'):
                params['promo_detail_info'] = self.promo_detail_info.to_alipay_dict()
            else:
                params['promo_detail_info'] = self.promo_detail_info
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniOrderBuyModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_logon_id' in d:
            o.buyer_logon_id = d['buyer_logon_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'mini_order_create_requests' in d:
            o.mini_order_create_requests = d['mini_order_create_requests']
        if 'order_buy_no' in d:
            o.order_buy_no = d['order_buy_no']
        if 'promo_detail_info' in d:
            o.promo_detail_info = d['promo_detail_info']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        return o


