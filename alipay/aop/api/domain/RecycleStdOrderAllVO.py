#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleStdOrderBaseVO import RecycleStdOrderBaseVO
from alipay.aop.api.domain.RecycleDeliveryVO import RecycleDeliveryVO
from alipay.aop.api.domain.RecycleStdOrderFundSubSidyVO import RecycleStdOrderFundSubSidyVO
from alipay.aop.api.domain.RecycleStdOrderMerchantInfoVO import RecycleStdOrderMerchantInfoVO
from alipay.aop.api.domain.RecycleDeliveryVO import RecycleDeliveryVO


class RecycleStdOrderAllVO(object):

    def __init__(self):
        self._order_base = None
        self._order_delivery = None
        self._order_fund_subsidy = None
        self._order_merchant = None
        self._order_sendback = None

    @property
    def order_base(self):
        return self._order_base

    @order_base.setter
    def order_base(self, value):
        if isinstance(value, RecycleStdOrderBaseVO):
            self._order_base = value
        else:
            self._order_base = RecycleStdOrderBaseVO.from_alipay_dict(value)
    @property
    def order_delivery(self):
        return self._order_delivery

    @order_delivery.setter
    def order_delivery(self, value):
        if isinstance(value, RecycleDeliveryVO):
            self._order_delivery = value
        else:
            self._order_delivery = RecycleDeliveryVO.from_alipay_dict(value)
    @property
    def order_fund_subsidy(self):
        return self._order_fund_subsidy

    @order_fund_subsidy.setter
    def order_fund_subsidy(self, value):
        if isinstance(value, RecycleStdOrderFundSubSidyVO):
            self._order_fund_subsidy = value
        else:
            self._order_fund_subsidy = RecycleStdOrderFundSubSidyVO.from_alipay_dict(value)
    @property
    def order_merchant(self):
        return self._order_merchant

    @order_merchant.setter
    def order_merchant(self, value):
        if isinstance(value, RecycleStdOrderMerchantInfoVO):
            self._order_merchant = value
        else:
            self._order_merchant = RecycleStdOrderMerchantInfoVO.from_alipay_dict(value)
    @property
    def order_sendback(self):
        return self._order_sendback

    @order_sendback.setter
    def order_sendback(self, value):
        if isinstance(value, RecycleDeliveryVO):
            self._order_sendback = value
        else:
            self._order_sendback = RecycleDeliveryVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.order_base:
            if hasattr(self.order_base, 'to_alipay_dict'):
                params['order_base'] = self.order_base.to_alipay_dict()
            else:
                params['order_base'] = self.order_base
        if self.order_delivery:
            if hasattr(self.order_delivery, 'to_alipay_dict'):
                params['order_delivery'] = self.order_delivery.to_alipay_dict()
            else:
                params['order_delivery'] = self.order_delivery
        if self.order_fund_subsidy:
            if hasattr(self.order_fund_subsidy, 'to_alipay_dict'):
                params['order_fund_subsidy'] = self.order_fund_subsidy.to_alipay_dict()
            else:
                params['order_fund_subsidy'] = self.order_fund_subsidy
        if self.order_merchant:
            if hasattr(self.order_merchant, 'to_alipay_dict'):
                params['order_merchant'] = self.order_merchant.to_alipay_dict()
            else:
                params['order_merchant'] = self.order_merchant
        if self.order_sendback:
            if hasattr(self.order_sendback, 'to_alipay_dict'):
                params['order_sendback'] = self.order_sendback.to_alipay_dict()
            else:
                params['order_sendback'] = self.order_sendback
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleStdOrderAllVO()
        if 'order_base' in d:
            o.order_base = d['order_base']
        if 'order_delivery' in d:
            o.order_delivery = d['order_delivery']
        if 'order_fund_subsidy' in d:
            o.order_fund_subsidy = d['order_fund_subsidy']
        if 'order_merchant' in d:
            o.order_merchant = d['order_merchant']
        if 'order_sendback' in d:
            o.order_sendback = d['order_sendback']
        return o


