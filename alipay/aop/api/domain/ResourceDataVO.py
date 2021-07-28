#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResourceDataVO(object):

    def __init__(self):
        self._avg_stay_duration_per_user = None
        self._avg_stay_duration_per_vst = None
        self._clk_cnt = None
        self._clk_user_cnt = None
        self._commission = None
        self._commission_per_pv = None
        self._commission_per_uv = None
        self._expo_cnt = None
        self._expo_user_cnt = None
        self._order_gmv = None
        self._origin_name = None
        self._platform_promotion_id = None
        self._pv_rate = None
        self._report_date = None
        self._trade_cnt = None
        self._trade_gmv_per_pv = None
        self._trade_gmv_per_uv = None
        self._uv_rate = None
        self._vst_cnt = None
        self._vst_user_cnt = None

    @property
    def avg_stay_duration_per_user(self):
        return self._avg_stay_duration_per_user

    @avg_stay_duration_per_user.setter
    def avg_stay_duration_per_user(self, value):
        self._avg_stay_duration_per_user = value
    @property
    def avg_stay_duration_per_vst(self):
        return self._avg_stay_duration_per_vst

    @avg_stay_duration_per_vst.setter
    def avg_stay_duration_per_vst(self, value):
        self._avg_stay_duration_per_vst = value
    @property
    def clk_cnt(self):
        return self._clk_cnt

    @clk_cnt.setter
    def clk_cnt(self, value):
        self._clk_cnt = value
    @property
    def clk_user_cnt(self):
        return self._clk_user_cnt

    @clk_user_cnt.setter
    def clk_user_cnt(self, value):
        self._clk_user_cnt = value
    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value):
        self._commission = value
    @property
    def commission_per_pv(self):
        return self._commission_per_pv

    @commission_per_pv.setter
    def commission_per_pv(self, value):
        self._commission_per_pv = value
    @property
    def commission_per_uv(self):
        return self._commission_per_uv

    @commission_per_uv.setter
    def commission_per_uv(self, value):
        self._commission_per_uv = value
    @property
    def expo_cnt(self):
        return self._expo_cnt

    @expo_cnt.setter
    def expo_cnt(self, value):
        self._expo_cnt = value
    @property
    def expo_user_cnt(self):
        return self._expo_user_cnt

    @expo_user_cnt.setter
    def expo_user_cnt(self, value):
        self._expo_user_cnt = value
    @property
    def order_gmv(self):
        return self._order_gmv

    @order_gmv.setter
    def order_gmv(self, value):
        self._order_gmv = value
    @property
    def origin_name(self):
        return self._origin_name

    @origin_name.setter
    def origin_name(self, value):
        self._origin_name = value
    @property
    def platform_promotion_id(self):
        return self._platform_promotion_id

    @platform_promotion_id.setter
    def platform_promotion_id(self, value):
        self._platform_promotion_id = value
    @property
    def pv_rate(self):
        return self._pv_rate

    @pv_rate.setter
    def pv_rate(self, value):
        self._pv_rate = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def trade_cnt(self):
        return self._trade_cnt

    @trade_cnt.setter
    def trade_cnt(self, value):
        self._trade_cnt = value
    @property
    def trade_gmv_per_pv(self):
        return self._trade_gmv_per_pv

    @trade_gmv_per_pv.setter
    def trade_gmv_per_pv(self, value):
        self._trade_gmv_per_pv = value
    @property
    def trade_gmv_per_uv(self):
        return self._trade_gmv_per_uv

    @trade_gmv_per_uv.setter
    def trade_gmv_per_uv(self, value):
        self._trade_gmv_per_uv = value
    @property
    def uv_rate(self):
        return self._uv_rate

    @uv_rate.setter
    def uv_rate(self, value):
        self._uv_rate = value
    @property
    def vst_cnt(self):
        return self._vst_cnt

    @vst_cnt.setter
    def vst_cnt(self, value):
        self._vst_cnt = value
    @property
    def vst_user_cnt(self):
        return self._vst_user_cnt

    @vst_user_cnt.setter
    def vst_user_cnt(self, value):
        self._vst_user_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_stay_duration_per_user:
            if hasattr(self.avg_stay_duration_per_user, 'to_alipay_dict'):
                params['avg_stay_duration_per_user'] = self.avg_stay_duration_per_user.to_alipay_dict()
            else:
                params['avg_stay_duration_per_user'] = self.avg_stay_duration_per_user
        if self.avg_stay_duration_per_vst:
            if hasattr(self.avg_stay_duration_per_vst, 'to_alipay_dict'):
                params['avg_stay_duration_per_vst'] = self.avg_stay_duration_per_vst.to_alipay_dict()
            else:
                params['avg_stay_duration_per_vst'] = self.avg_stay_duration_per_vst
        if self.clk_cnt:
            if hasattr(self.clk_cnt, 'to_alipay_dict'):
                params['clk_cnt'] = self.clk_cnt.to_alipay_dict()
            else:
                params['clk_cnt'] = self.clk_cnt
        if self.clk_user_cnt:
            if hasattr(self.clk_user_cnt, 'to_alipay_dict'):
                params['clk_user_cnt'] = self.clk_user_cnt.to_alipay_dict()
            else:
                params['clk_user_cnt'] = self.clk_user_cnt
        if self.commission:
            if hasattr(self.commission, 'to_alipay_dict'):
                params['commission'] = self.commission.to_alipay_dict()
            else:
                params['commission'] = self.commission
        if self.commission_per_pv:
            if hasattr(self.commission_per_pv, 'to_alipay_dict'):
                params['commission_per_pv'] = self.commission_per_pv.to_alipay_dict()
            else:
                params['commission_per_pv'] = self.commission_per_pv
        if self.commission_per_uv:
            if hasattr(self.commission_per_uv, 'to_alipay_dict'):
                params['commission_per_uv'] = self.commission_per_uv.to_alipay_dict()
            else:
                params['commission_per_uv'] = self.commission_per_uv
        if self.expo_cnt:
            if hasattr(self.expo_cnt, 'to_alipay_dict'):
                params['expo_cnt'] = self.expo_cnt.to_alipay_dict()
            else:
                params['expo_cnt'] = self.expo_cnt
        if self.expo_user_cnt:
            if hasattr(self.expo_user_cnt, 'to_alipay_dict'):
                params['expo_user_cnt'] = self.expo_user_cnt.to_alipay_dict()
            else:
                params['expo_user_cnt'] = self.expo_user_cnt
        if self.order_gmv:
            if hasattr(self.order_gmv, 'to_alipay_dict'):
                params['order_gmv'] = self.order_gmv.to_alipay_dict()
            else:
                params['order_gmv'] = self.order_gmv
        if self.origin_name:
            if hasattr(self.origin_name, 'to_alipay_dict'):
                params['origin_name'] = self.origin_name.to_alipay_dict()
            else:
                params['origin_name'] = self.origin_name
        if self.platform_promotion_id:
            if hasattr(self.platform_promotion_id, 'to_alipay_dict'):
                params['platform_promotion_id'] = self.platform_promotion_id.to_alipay_dict()
            else:
                params['platform_promotion_id'] = self.platform_promotion_id
        if self.pv_rate:
            if hasattr(self.pv_rate, 'to_alipay_dict'):
                params['pv_rate'] = self.pv_rate.to_alipay_dict()
            else:
                params['pv_rate'] = self.pv_rate
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.trade_cnt:
            if hasattr(self.trade_cnt, 'to_alipay_dict'):
                params['trade_cnt'] = self.trade_cnt.to_alipay_dict()
            else:
                params['trade_cnt'] = self.trade_cnt
        if self.trade_gmv_per_pv:
            if hasattr(self.trade_gmv_per_pv, 'to_alipay_dict'):
                params['trade_gmv_per_pv'] = self.trade_gmv_per_pv.to_alipay_dict()
            else:
                params['trade_gmv_per_pv'] = self.trade_gmv_per_pv
        if self.trade_gmv_per_uv:
            if hasattr(self.trade_gmv_per_uv, 'to_alipay_dict'):
                params['trade_gmv_per_uv'] = self.trade_gmv_per_uv.to_alipay_dict()
            else:
                params['trade_gmv_per_uv'] = self.trade_gmv_per_uv
        if self.uv_rate:
            if hasattr(self.uv_rate, 'to_alipay_dict'):
                params['uv_rate'] = self.uv_rate.to_alipay_dict()
            else:
                params['uv_rate'] = self.uv_rate
        if self.vst_cnt:
            if hasattr(self.vst_cnt, 'to_alipay_dict'):
                params['vst_cnt'] = self.vst_cnt.to_alipay_dict()
            else:
                params['vst_cnt'] = self.vst_cnt
        if self.vst_user_cnt:
            if hasattr(self.vst_user_cnt, 'to_alipay_dict'):
                params['vst_user_cnt'] = self.vst_user_cnt.to_alipay_dict()
            else:
                params['vst_user_cnt'] = self.vst_user_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResourceDataVO()
        if 'avg_stay_duration_per_user' in d:
            o.avg_stay_duration_per_user = d['avg_stay_duration_per_user']
        if 'avg_stay_duration_per_vst' in d:
            o.avg_stay_duration_per_vst = d['avg_stay_duration_per_vst']
        if 'clk_cnt' in d:
            o.clk_cnt = d['clk_cnt']
        if 'clk_user_cnt' in d:
            o.clk_user_cnt = d['clk_user_cnt']
        if 'commission' in d:
            o.commission = d['commission']
        if 'commission_per_pv' in d:
            o.commission_per_pv = d['commission_per_pv']
        if 'commission_per_uv' in d:
            o.commission_per_uv = d['commission_per_uv']
        if 'expo_cnt' in d:
            o.expo_cnt = d['expo_cnt']
        if 'expo_user_cnt' in d:
            o.expo_user_cnt = d['expo_user_cnt']
        if 'order_gmv' in d:
            o.order_gmv = d['order_gmv']
        if 'origin_name' in d:
            o.origin_name = d['origin_name']
        if 'platform_promotion_id' in d:
            o.platform_promotion_id = d['platform_promotion_id']
        if 'pv_rate' in d:
            o.pv_rate = d['pv_rate']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'trade_cnt' in d:
            o.trade_cnt = d['trade_cnt']
        if 'trade_gmv_per_pv' in d:
            o.trade_gmv_per_pv = d['trade_gmv_per_pv']
        if 'trade_gmv_per_uv' in d:
            o.trade_gmv_per_uv = d['trade_gmv_per_uv']
        if 'uv_rate' in d:
            o.uv_rate = d['uv_rate']
        if 'vst_cnt' in d:
            o.vst_cnt = d['vst_cnt']
        if 'vst_user_cnt' in d:
            o.vst_user_cnt = d['vst_user_cnt']
        return o


