#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryAgencyMerchantInfo import DeliveryAgencyMerchantInfo


class AlipayMarketingActivityDeliverychannelQueryModel(object):

    def __init__(self):
        self._belong_merchant_info = None
        self._booth_code = None
        self._page_num = None
        self._page_size = None

    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, DeliveryAgencyMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = DeliveryAgencyMerchantInfo.from_alipay_dict(value)
    @property
    def booth_code(self):
        return self._booth_code

    @booth_code.setter
    def booth_code(self, value):
        self._booth_code = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
        if self.booth_code:
            if hasattr(self.booth_code, 'to_alipay_dict'):
                params['booth_code'] = self.booth_code.to_alipay_dict()
            else:
                params['booth_code'] = self.booth_code
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityDeliverychannelQueryModel()
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'booth_code' in d:
            o.booth_code = d['booth_code']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


