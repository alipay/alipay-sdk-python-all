#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CouponInfo import CouponInfo


class PrizeDetailInfo(object):

    def __init__(self):
        self._coupon_info = None
        self._prize_id = None
        self._prize_name = None

    @property
    def coupon_info(self):
        return self._coupon_info

    @coupon_info.setter
    def coupon_info(self, value):
        if isinstance(value, list):
            self._coupon_info = list()
            for i in value:
                if isinstance(i, CouponInfo):
                    self._coupon_info.append(i)
                else:
                    self._coupon_info.append(CouponInfo.from_alipay_dict(i))
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_info:
            if isinstance(self.coupon_info, list):
                for i in range(0, len(self.coupon_info)):
                    element = self.coupon_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coupon_info[i] = element.to_alipay_dict()
            if hasattr(self.coupon_info, 'to_alipay_dict'):
                params['coupon_info'] = self.coupon_info.to_alipay_dict()
            else:
                params['coupon_info'] = self.coupon_info
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeDetailInfo()
        if 'coupon_info' in d:
            o.coupon_info = d['coupon_info']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        return o


