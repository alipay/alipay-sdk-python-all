#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandMembercardUserinfoBatchqueryModel(object):

    def __init__(self):
        self._member_product_id = None
        self._page_num = None
        self._page_size = None

    @property
    def member_product_id(self):
        return self._member_product_id

    @member_product_id.setter
    def member_product_id(self, value):
        self._member_product_id = value
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
        if self.member_product_id:
            if hasattr(self.member_product_id, 'to_alipay_dict'):
                params['member_product_id'] = self.member_product_id.to_alipay_dict()
            else:
                params['member_product_id'] = self.member_product_id
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
        o = AntMerchantExpandMembercardUserinfoBatchqueryModel()
        if 'member_product_id' in d:
            o.member_product_id = d['member_product_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


