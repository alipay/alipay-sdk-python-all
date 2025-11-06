#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupPurchaseContactInfo import GroupPurchaseContactInfo
from alipay.aop.api.domain.GroupPurchaseShopInfo import GroupPurchaseShopInfo


class AlipayOpenSpInteopGrouppurchaseCreateModel(object):

    def __init__(self):
        self._contact_info = None
        self._inteop_order_no = None
        self._inteop_shop_info = None

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, GroupPurchaseContactInfo):
            self._contact_info = value
        else:
            self._contact_info = GroupPurchaseContactInfo.from_alipay_dict(value)
    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def inteop_shop_info(self):
        return self._inteop_shop_info

    @inteop_shop_info.setter
    def inteop_shop_info(self, value):
        if isinstance(value, GroupPurchaseShopInfo):
            self._inteop_shop_info = value
        else:
            self._inteop_shop_info = GroupPurchaseShopInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.inteop_shop_info:
            if hasattr(self.inteop_shop_info, 'to_alipay_dict'):
                params['inteop_shop_info'] = self.inteop_shop_info.to_alipay_dict()
            else:
                params['inteop_shop_info'] = self.inteop_shop_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopGrouppurchaseCreateModel()
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'inteop_shop_info' in d:
            o.inteop_shop_info = d['inteop_shop_info']
        return o


