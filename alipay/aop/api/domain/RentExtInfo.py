#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentBuyerExtInfo import RentBuyerExtInfo
from alipay.aop.api.domain.RentDeliveryExtInfo import RentDeliveryExtInfo
from alipay.aop.api.domain.RentFinancingExtInfo import RentFinancingExtInfo
from alipay.aop.api.domain.RentItemExtInfo import RentItemExtInfo
from alipay.aop.api.domain.RentOrderExtInfo import RentOrderExtInfo


class RentExtInfo(object):

    def __init__(self):
        self._buyer_ext_info = None
        self._delivery_ext_info = None
        self._financing_ext_info = None
        self._item_ext_info = None
        self._order_ext_info = None

    @property
    def buyer_ext_info(self):
        return self._buyer_ext_info

    @buyer_ext_info.setter
    def buyer_ext_info(self, value):
        if isinstance(value, RentBuyerExtInfo):
            self._buyer_ext_info = value
        else:
            self._buyer_ext_info = RentBuyerExtInfo.from_alipay_dict(value)
    @property
    def delivery_ext_info(self):
        return self._delivery_ext_info

    @delivery_ext_info.setter
    def delivery_ext_info(self, value):
        if isinstance(value, RentDeliveryExtInfo):
            self._delivery_ext_info = value
        else:
            self._delivery_ext_info = RentDeliveryExtInfo.from_alipay_dict(value)
    @property
    def financing_ext_info(self):
        return self._financing_ext_info

    @financing_ext_info.setter
    def financing_ext_info(self, value):
        if isinstance(value, list):
            self._financing_ext_info = list()
            for i in value:
                if isinstance(i, RentFinancingExtInfo):
                    self._financing_ext_info.append(i)
                else:
                    self._financing_ext_info.append(RentFinancingExtInfo.from_alipay_dict(i))
    @property
    def item_ext_info(self):
        return self._item_ext_info

    @item_ext_info.setter
    def item_ext_info(self, value):
        if isinstance(value, RentItemExtInfo):
            self._item_ext_info = value
        else:
            self._item_ext_info = RentItemExtInfo.from_alipay_dict(value)
    @property
    def order_ext_info(self):
        return self._order_ext_info

    @order_ext_info.setter
    def order_ext_info(self, value):
        if isinstance(value, RentOrderExtInfo):
            self._order_ext_info = value
        else:
            self._order_ext_info = RentOrderExtInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_ext_info:
            if hasattr(self.buyer_ext_info, 'to_alipay_dict'):
                params['buyer_ext_info'] = self.buyer_ext_info.to_alipay_dict()
            else:
                params['buyer_ext_info'] = self.buyer_ext_info
        if self.delivery_ext_info:
            if hasattr(self.delivery_ext_info, 'to_alipay_dict'):
                params['delivery_ext_info'] = self.delivery_ext_info.to_alipay_dict()
            else:
                params['delivery_ext_info'] = self.delivery_ext_info
        if self.financing_ext_info:
            if isinstance(self.financing_ext_info, list):
                for i in range(0, len(self.financing_ext_info)):
                    element = self.financing_ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.financing_ext_info[i] = element.to_alipay_dict()
            if hasattr(self.financing_ext_info, 'to_alipay_dict'):
                params['financing_ext_info'] = self.financing_ext_info.to_alipay_dict()
            else:
                params['financing_ext_info'] = self.financing_ext_info
        if self.item_ext_info:
            if hasattr(self.item_ext_info, 'to_alipay_dict'):
                params['item_ext_info'] = self.item_ext_info.to_alipay_dict()
            else:
                params['item_ext_info'] = self.item_ext_info
        if self.order_ext_info:
            if hasattr(self.order_ext_info, 'to_alipay_dict'):
                params['order_ext_info'] = self.order_ext_info.to_alipay_dict()
            else:
                params['order_ext_info'] = self.order_ext_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentExtInfo()
        if 'buyer_ext_info' in d:
            o.buyer_ext_info = d['buyer_ext_info']
        if 'delivery_ext_info' in d:
            o.delivery_ext_info = d['delivery_ext_info']
        if 'financing_ext_info' in d:
            o.financing_ext_info = d['financing_ext_info']
        if 'item_ext_info' in d:
            o.item_ext_info = d['item_ext_info']
        if 'order_ext_info' in d:
            o.order_ext_info = d['order_ext_info']
        return o


