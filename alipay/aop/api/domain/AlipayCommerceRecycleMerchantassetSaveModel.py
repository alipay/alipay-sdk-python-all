#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleMerchantassetSaveModel(object):

    def __init__(self):
        self._fund_account = None
        self._out_biz_no = None
        self._seller_id_list = None
        self._subsidy_ratio = None

    @property
    def fund_account(self):
        return self._fund_account

    @fund_account.setter
    def fund_account(self, value):
        self._fund_account = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def seller_id_list(self):
        return self._seller_id_list

    @seller_id_list.setter
    def seller_id_list(self, value):
        if isinstance(value, list):
            self._seller_id_list = list()
            for i in value:
                self._seller_id_list.append(i)
    @property
    def subsidy_ratio(self):
        return self._subsidy_ratio

    @subsidy_ratio.setter
    def subsidy_ratio(self, value):
        self._subsidy_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_account:
            if hasattr(self.fund_account, 'to_alipay_dict'):
                params['fund_account'] = self.fund_account.to_alipay_dict()
            else:
                params['fund_account'] = self.fund_account
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.seller_id_list:
            if isinstance(self.seller_id_list, list):
                for i in range(0, len(self.seller_id_list)):
                    element = self.seller_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.seller_id_list[i] = element.to_alipay_dict()
            if hasattr(self.seller_id_list, 'to_alipay_dict'):
                params['seller_id_list'] = self.seller_id_list.to_alipay_dict()
            else:
                params['seller_id_list'] = self.seller_id_list
        if self.subsidy_ratio:
            if hasattr(self.subsidy_ratio, 'to_alipay_dict'):
                params['subsidy_ratio'] = self.subsidy_ratio.to_alipay_dict()
            else:
                params['subsidy_ratio'] = self.subsidy_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleMerchantassetSaveModel()
        if 'fund_account' in d:
            o.fund_account = d['fund_account']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'seller_id_list' in d:
            o.seller_id_list = d['seller_id_list']
        if 'subsidy_ratio' in d:
            o.subsidy_ratio = d['subsidy_ratio']
        return o


