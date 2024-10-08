#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPlan import RentPlan
from alipay.aop.api.domain.RentDetail import RentDetail
from alipay.aop.api.domain.RentRoyalty import RentRoyalty


class SimpleRentInfo(object):

    def __init__(self):
        self._biz_order_id = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._buyout_price = None
        self._end_time = None
        self._out_order_id = None
        self._plan_list = None
        self._price_info = None
        self._rent_detail_list = None
        self._rent_id = None
        self._rent_status = None
        self._royalty_list = None
        self._seller_id = None
        self._smid = None
        self._start_time = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def buyout_price(self):
        return self._buyout_price

    @buyout_price.setter
    def buyout_price(self, value):
        self._buyout_price = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def plan_list(self):
        return self._plan_list

    @plan_list.setter
    def plan_list(self, value):
        if isinstance(value, list):
            self._plan_list = list()
            for i in value:
                if isinstance(i, RentPlan):
                    self._plan_list.append(i)
                else:
                    self._plan_list.append(RentPlan.from_alipay_dict(i))
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        self._price_info = value
    @property
    def rent_detail_list(self):
        return self._rent_detail_list

    @rent_detail_list.setter
    def rent_detail_list(self, value):
        if isinstance(value, list):
            self._rent_detail_list = list()
            for i in value:
                if isinstance(i, RentDetail):
                    self._rent_detail_list.append(i)
                else:
                    self._rent_detail_list.append(RentDetail.from_alipay_dict(i))
    @property
    def rent_id(self):
        return self._rent_id

    @rent_id.setter
    def rent_id(self, value):
        self._rent_id = value
    @property
    def rent_status(self):
        return self._rent_status

    @rent_status.setter
    def rent_status(self, value):
        self._rent_status = value
    @property
    def royalty_list(self):
        return self._royalty_list

    @royalty_list.setter
    def royalty_list(self, value):
        if isinstance(value, list):
            self._royalty_list = list()
            for i in value:
                if isinstance(i, RentRoyalty):
                    self._royalty_list.append(i)
                else:
                    self._royalty_list.append(RentRoyalty.from_alipay_dict(i))
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.buyout_price:
            if hasattr(self.buyout_price, 'to_alipay_dict'):
                params['buyout_price'] = self.buyout_price.to_alipay_dict()
            else:
                params['buyout_price'] = self.buyout_price
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.plan_list:
            if isinstance(self.plan_list, list):
                for i in range(0, len(self.plan_list)):
                    element = self.plan_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_list[i] = element.to_alipay_dict()
            if hasattr(self.plan_list, 'to_alipay_dict'):
                params['plan_list'] = self.plan_list.to_alipay_dict()
            else:
                params['plan_list'] = self.plan_list
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        if self.rent_detail_list:
            if isinstance(self.rent_detail_list, list):
                for i in range(0, len(self.rent_detail_list)):
                    element = self.rent_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rent_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.rent_detail_list, 'to_alipay_dict'):
                params['rent_detail_list'] = self.rent_detail_list.to_alipay_dict()
            else:
                params['rent_detail_list'] = self.rent_detail_list
        if self.rent_id:
            if hasattr(self.rent_id, 'to_alipay_dict'):
                params['rent_id'] = self.rent_id.to_alipay_dict()
            else:
                params['rent_id'] = self.rent_id
        if self.rent_status:
            if hasattr(self.rent_status, 'to_alipay_dict'):
                params['rent_status'] = self.rent_status.to_alipay_dict()
            else:
                params['rent_status'] = self.rent_status
        if self.royalty_list:
            if isinstance(self.royalty_list, list):
                for i in range(0, len(self.royalty_list)):
                    element = self.royalty_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_list[i] = element.to_alipay_dict()
            if hasattr(self.royalty_list, 'to_alipay_dict'):
                params['royalty_list'] = self.royalty_list.to_alipay_dict()
            else:
                params['royalty_list'] = self.royalty_list
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SimpleRentInfo()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'buyout_price' in d:
            o.buyout_price = d['buyout_price']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'plan_list' in d:
            o.plan_list = d['plan_list']
        if 'price_info' in d:
            o.price_info = d['price_info']
        if 'rent_detail_list' in d:
            o.rent_detail_list = d['rent_detail_list']
        if 'rent_id' in d:
            o.rent_id = d['rent_id']
        if 'rent_status' in d:
            o.rent_status = d['rent_status']
        if 'royalty_list' in d:
            o.royalty_list = d['royalty_list']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'smid' in d:
            o.smid = d['smid']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


