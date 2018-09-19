#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CashCampaignInfo(object):

    def __init__(self):
        self._camp_status = None
        self._coupon_name = None
        self._crowd_no = None
        self._origin_crowd_no = None

    @property
    def camp_status(self):
        return self._camp_status

    @camp_status.setter
    def camp_status(self, value):
        self._camp_status = value
    @property
    def coupon_name(self):
        return self._coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self._coupon_name = value
    @property
    def crowd_no(self):
        return self._crowd_no

    @crowd_no.setter
    def crowd_no(self, value):
        self._crowd_no = value
    @property
    def origin_crowd_no(self):
        return self._origin_crowd_no

    @origin_crowd_no.setter
    def origin_crowd_no(self, value):
        self._origin_crowd_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_status:
            if hasattr(self.camp_status, 'to_alipay_dict'):
                params['camp_status'] = self.camp_status.to_alipay_dict()
            else:
                params['camp_status'] = self.camp_status
        if self.coupon_name:
            if hasattr(self.coupon_name, 'to_alipay_dict'):
                params['coupon_name'] = self.coupon_name.to_alipay_dict()
            else:
                params['coupon_name'] = self.coupon_name
        if self.crowd_no:
            if hasattr(self.crowd_no, 'to_alipay_dict'):
                params['crowd_no'] = self.crowd_no.to_alipay_dict()
            else:
                params['crowd_no'] = self.crowd_no
        if self.origin_crowd_no:
            if hasattr(self.origin_crowd_no, 'to_alipay_dict'):
                params['origin_crowd_no'] = self.origin_crowd_no.to_alipay_dict()
            else:
                params['origin_crowd_no'] = self.origin_crowd_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CashCampaignInfo()
        if 'camp_status' in d:
            o.camp_status = d['camp_status']
        if 'coupon_name' in d:
            o.coupon_name = d['coupon_name']
        if 'crowd_no' in d:
            o.crowd_no = d['crowd_no']
        if 'origin_crowd_no' in d:
            o.origin_crowd_no = d['origin_crowd_no']
        return o


