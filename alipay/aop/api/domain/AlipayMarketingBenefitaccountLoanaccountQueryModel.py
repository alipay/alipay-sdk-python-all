#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingBenefitaccountLoanaccountQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._end_time = None
        self._last_order_id = None
        self._page_size = None
        self._principal_user_id = None
        self._start_time = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def last_order_id(self):
        return self._last_order_id

    @last_order_id.setter
    def last_order_id(self, value):
        self._last_order_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def principal_user_id(self):
        return self._principal_user_id

    @principal_user_id.setter
    def principal_user_id(self, value):
        self._principal_user_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.last_order_id:
            if hasattr(self.last_order_id, 'to_alipay_dict'):
                params['last_order_id'] = self.last_order_id.to_alipay_dict()
            else:
                params['last_order_id'] = self.last_order_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.principal_user_id:
            if hasattr(self.principal_user_id, 'to_alipay_dict'):
                params['principal_user_id'] = self.principal_user_id.to_alipay_dict()
            else:
                params['principal_user_id'] = self.principal_user_id
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
        o = AlipayMarketingBenefitaccountLoanaccountQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'last_order_id' in d:
            o.last_order_id = d['last_order_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'principal_user_id' in d:
            o.principal_user_id = d['principal_user_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


