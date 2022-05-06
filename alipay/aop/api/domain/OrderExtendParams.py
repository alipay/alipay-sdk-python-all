#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderExtendParams(object):

    def __init__(self):
        self._cashier_result_render_url = None
        self._out_scene_biz_no = None
        self._platform_scheme_ar_no = None
        self._seller_scheme_ar_no = None

    @property
    def cashier_result_render_url(self):
        return self._cashier_result_render_url

    @cashier_result_render_url.setter
    def cashier_result_render_url(self, value):
        self._cashier_result_render_url = value
    @property
    def out_scene_biz_no(self):
        return self._out_scene_biz_no

    @out_scene_biz_no.setter
    def out_scene_biz_no(self, value):
        self._out_scene_biz_no = value
    @property
    def platform_scheme_ar_no(self):
        return self._platform_scheme_ar_no

    @platform_scheme_ar_no.setter
    def platform_scheme_ar_no(self, value):
        self._platform_scheme_ar_no = value
    @property
    def seller_scheme_ar_no(self):
        return self._seller_scheme_ar_no

    @seller_scheme_ar_no.setter
    def seller_scheme_ar_no(self, value):
        self._seller_scheme_ar_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cashier_result_render_url:
            if hasattr(self.cashier_result_render_url, 'to_alipay_dict'):
                params['cashier_result_render_url'] = self.cashier_result_render_url.to_alipay_dict()
            else:
                params['cashier_result_render_url'] = self.cashier_result_render_url
        if self.out_scene_biz_no:
            if hasattr(self.out_scene_biz_no, 'to_alipay_dict'):
                params['out_scene_biz_no'] = self.out_scene_biz_no.to_alipay_dict()
            else:
                params['out_scene_biz_no'] = self.out_scene_biz_no
        if self.platform_scheme_ar_no:
            if hasattr(self.platform_scheme_ar_no, 'to_alipay_dict'):
                params['platform_scheme_ar_no'] = self.platform_scheme_ar_no.to_alipay_dict()
            else:
                params['platform_scheme_ar_no'] = self.platform_scheme_ar_no
        if self.seller_scheme_ar_no:
            if hasattr(self.seller_scheme_ar_no, 'to_alipay_dict'):
                params['seller_scheme_ar_no'] = self.seller_scheme_ar_no.to_alipay_dict()
            else:
                params['seller_scheme_ar_no'] = self.seller_scheme_ar_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderExtendParams()
        if 'cashier_result_render_url' in d:
            o.cashier_result_render_url = d['cashier_result_render_url']
        if 'out_scene_biz_no' in d:
            o.out_scene_biz_no = d['out_scene_biz_no']
        if 'platform_scheme_ar_no' in d:
            o.platform_scheme_ar_no = d['platform_scheme_ar_no']
        if 'seller_scheme_ar_no' in d:
            o.seller_scheme_ar_no = d['seller_scheme_ar_no']
        return o


