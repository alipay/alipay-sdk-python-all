#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayUserVO import CreditPayUserVO


class MybankCreditLoantradePayeeReceivableQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._need_factoring_consult = None
        self._order_list = None
        self._platform_order_list = None
        self._status_list = None
        self._sub_biz_scene = None
        self._user_info = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def need_factoring_consult(self):
        return self._need_factoring_consult

    @need_factoring_consult.setter
    def need_factoring_consult(self, value):
        self._need_factoring_consult = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                self._order_list.append(i)
    @property
    def platform_order_list(self):
        return self._platform_order_list

    @platform_order_list.setter
    def platform_order_list(self, value):
        if isinstance(value, list):
            self._platform_order_list = list()
            for i in value:
                self._platform_order_list.append(i)
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, CreditPayUserVO):
            self._user_info = value
        else:
            self._user_info = CreditPayUserVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.need_factoring_consult:
            if hasattr(self.need_factoring_consult, 'to_alipay_dict'):
                params['need_factoring_consult'] = self.need_factoring_consult.to_alipay_dict()
            else:
                params['need_factoring_consult'] = self.need_factoring_consult
        if self.order_list:
            if isinstance(self.order_list, list):
                for i in range(0, len(self.order_list)):
                    element = self.order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_list[i] = element.to_alipay_dict()
            if hasattr(self.order_list, 'to_alipay_dict'):
                params['order_list'] = self.order_list.to_alipay_dict()
            else:
                params['order_list'] = self.order_list
        if self.platform_order_list:
            if isinstance(self.platform_order_list, list):
                for i in range(0, len(self.platform_order_list)):
                    element = self.platform_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.platform_order_list[i] = element.to_alipay_dict()
            if hasattr(self.platform_order_list, 'to_alipay_dict'):
                params['platform_order_list'] = self.platform_order_list.to_alipay_dict()
            else:
                params['platform_order_list'] = self.platform_order_list
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradePayeeReceivableQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'need_factoring_consult' in d:
            o.need_factoring_consult = d['need_factoring_consult']
        if 'order_list' in d:
            o.order_list = d['order_list']
        if 'platform_order_list' in d:
            o.platform_order_list = d['platform_order_list']
        if 'status_list' in d:
            o.status_list = d['status_list']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


