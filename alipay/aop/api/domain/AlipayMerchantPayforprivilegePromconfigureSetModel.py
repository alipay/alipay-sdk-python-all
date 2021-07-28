#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantPayforprivilegePromconfigureSetModel(object):

    def __init__(self):
        self._enabled_shop_list = None
        self._exclude_item_ids = None
        self._out_biz_no = None
        self._support_item_ids = None

    @property
    def enabled_shop_list(self):
        return self._enabled_shop_list

    @enabled_shop_list.setter
    def enabled_shop_list(self, value):
        if isinstance(value, list):
            self._enabled_shop_list = list()
            for i in value:
                self._enabled_shop_list.append(i)
    @property
    def exclude_item_ids(self):
        return self._exclude_item_ids

    @exclude_item_ids.setter
    def exclude_item_ids(self, value):
        if isinstance(value, list):
            self._exclude_item_ids = list()
            for i in value:
                self._exclude_item_ids.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def support_item_ids(self):
        return self._support_item_ids

    @support_item_ids.setter
    def support_item_ids(self, value):
        if isinstance(value, list):
            self._support_item_ids = list()
            for i in value:
                self._support_item_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.enabled_shop_list:
            if isinstance(self.enabled_shop_list, list):
                for i in range(0, len(self.enabled_shop_list)):
                    element = self.enabled_shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.enabled_shop_list[i] = element.to_alipay_dict()
            if hasattr(self.enabled_shop_list, 'to_alipay_dict'):
                params['enabled_shop_list'] = self.enabled_shop_list.to_alipay_dict()
            else:
                params['enabled_shop_list'] = self.enabled_shop_list
        if self.exclude_item_ids:
            if isinstance(self.exclude_item_ids, list):
                for i in range(0, len(self.exclude_item_ids)):
                    element = self.exclude_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.exclude_item_ids, 'to_alipay_dict'):
                params['exclude_item_ids'] = self.exclude_item_ids.to_alipay_dict()
            else:
                params['exclude_item_ids'] = self.exclude_item_ids
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.support_item_ids:
            if isinstance(self.support_item_ids, list):
                for i in range(0, len(self.support_item_ids)):
                    element = self.support_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.support_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.support_item_ids, 'to_alipay_dict'):
                params['support_item_ids'] = self.support_item_ids.to_alipay_dict()
            else:
                params['support_item_ids'] = self.support_item_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantPayforprivilegePromconfigureSetModel()
        if 'enabled_shop_list' in d:
            o.enabled_shop_list = d['enabled_shop_list']
        if 'exclude_item_ids' in d:
            o.exclude_item_ids = d['exclude_item_ids']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'support_item_ids' in d:
            o.support_item_ids = d['support_item_ids']
        return o


