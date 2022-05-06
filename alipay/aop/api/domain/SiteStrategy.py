#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SiteStrategy(object):

    def __init__(self):
        self._distance = None
        self._market_screen_biz_type = None
        self._site_num = None
        self._sn_black_list = None
        self._sn_white_list = None

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def market_screen_biz_type(self):
        return self._market_screen_biz_type

    @market_screen_biz_type.setter
    def market_screen_biz_type(self, value):
        self._market_screen_biz_type = value
    @property
    def site_num(self):
        return self._site_num

    @site_num.setter
    def site_num(self, value):
        self._site_num = value
    @property
    def sn_black_list(self):
        return self._sn_black_list

    @sn_black_list.setter
    def sn_black_list(self, value):
        if isinstance(value, list):
            self._sn_black_list = list()
            for i in value:
                self._sn_black_list.append(i)
    @property
    def sn_white_list(self):
        return self._sn_white_list

    @sn_white_list.setter
    def sn_white_list(self, value):
        if isinstance(value, list):
            self._sn_white_list = list()
            for i in value:
                self._sn_white_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.market_screen_biz_type:
            if hasattr(self.market_screen_biz_type, 'to_alipay_dict'):
                params['market_screen_biz_type'] = self.market_screen_biz_type.to_alipay_dict()
            else:
                params['market_screen_biz_type'] = self.market_screen_biz_type
        if self.site_num:
            if hasattr(self.site_num, 'to_alipay_dict'):
                params['site_num'] = self.site_num.to_alipay_dict()
            else:
                params['site_num'] = self.site_num
        if self.sn_black_list:
            if isinstance(self.sn_black_list, list):
                for i in range(0, len(self.sn_black_list)):
                    element = self.sn_black_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn_black_list[i] = element.to_alipay_dict()
            if hasattr(self.sn_black_list, 'to_alipay_dict'):
                params['sn_black_list'] = self.sn_black_list.to_alipay_dict()
            else:
                params['sn_black_list'] = self.sn_black_list
        if self.sn_white_list:
            if isinstance(self.sn_white_list, list):
                for i in range(0, len(self.sn_white_list)):
                    element = self.sn_white_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn_white_list[i] = element.to_alipay_dict()
            if hasattr(self.sn_white_list, 'to_alipay_dict'):
                params['sn_white_list'] = self.sn_white_list.to_alipay_dict()
            else:
                params['sn_white_list'] = self.sn_white_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SiteStrategy()
        if 'distance' in d:
            o.distance = d['distance']
        if 'market_screen_biz_type' in d:
            o.market_screen_biz_type = d['market_screen_biz_type']
        if 'site_num' in d:
            o.site_num = d['site_num']
        if 'sn_black_list' in d:
            o.sn_black_list = d['sn_black_list']
        if 'sn_white_list' in d:
            o.sn_white_list = d['sn_white_list']
        return o


