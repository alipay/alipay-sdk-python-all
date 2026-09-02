#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleOrderPayInfoVO import RecycleOrderPayInfoVO
from alipay.aop.api.domain.RecycleOrderPayInfoVO import RecycleOrderPayInfoVO
from alipay.aop.api.domain.RecycleStdOrderFundSubSidyVO import RecycleStdOrderFundSubSidyVO
from alipay.aop.api.domain.RecycleOrderRoyaltyInfoVO import RecycleOrderRoyaltyInfoVO


class RecycleOrderFundAllVO(object):

    def __init__(self):
        self._credit_withdraw_info = None
        self._order_pay_info = None
        self._order_subsidy_info = None
        self._royalty_infos = None

    @property
    def credit_withdraw_info(self):
        return self._credit_withdraw_info

    @credit_withdraw_info.setter
    def credit_withdraw_info(self, value):
        if isinstance(value, RecycleOrderPayInfoVO):
            self._credit_withdraw_info = value
        else:
            self._credit_withdraw_info = RecycleOrderPayInfoVO.from_alipay_dict(value)
    @property
    def order_pay_info(self):
        return self._order_pay_info

    @order_pay_info.setter
    def order_pay_info(self, value):
        if isinstance(value, RecycleOrderPayInfoVO):
            self._order_pay_info = value
        else:
            self._order_pay_info = RecycleOrderPayInfoVO.from_alipay_dict(value)
    @property
    def order_subsidy_info(self):
        return self._order_subsidy_info

    @order_subsidy_info.setter
    def order_subsidy_info(self, value):
        if isinstance(value, RecycleStdOrderFundSubSidyVO):
            self._order_subsidy_info = value
        else:
            self._order_subsidy_info = RecycleStdOrderFundSubSidyVO.from_alipay_dict(value)
    @property
    def royalty_infos(self):
        return self._royalty_infos

    @royalty_infos.setter
    def royalty_infos(self, value):
        if isinstance(value, list):
            self._royalty_infos = list()
            for i in value:
                if isinstance(i, RecycleOrderRoyaltyInfoVO):
                    self._royalty_infos.append(i)
                else:
                    self._royalty_infos.append(RecycleOrderRoyaltyInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.credit_withdraw_info:
            if hasattr(self.credit_withdraw_info, 'to_alipay_dict'):
                params['credit_withdraw_info'] = self.credit_withdraw_info.to_alipay_dict()
            else:
                params['credit_withdraw_info'] = self.credit_withdraw_info
        if self.order_pay_info:
            if hasattr(self.order_pay_info, 'to_alipay_dict'):
                params['order_pay_info'] = self.order_pay_info.to_alipay_dict()
            else:
                params['order_pay_info'] = self.order_pay_info
        if self.order_subsidy_info:
            if hasattr(self.order_subsidy_info, 'to_alipay_dict'):
                params['order_subsidy_info'] = self.order_subsidy_info.to_alipay_dict()
            else:
                params['order_subsidy_info'] = self.order_subsidy_info
        if self.royalty_infos:
            if isinstance(self.royalty_infos, list):
                for i in range(0, len(self.royalty_infos)):
                    element = self.royalty_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_infos[i] = element.to_alipay_dict()
            if hasattr(self.royalty_infos, 'to_alipay_dict'):
                params['royalty_infos'] = self.royalty_infos.to_alipay_dict()
            else:
                params['royalty_infos'] = self.royalty_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleOrderFundAllVO()
        if 'credit_withdraw_info' in d:
            o.credit_withdraw_info = d['credit_withdraw_info']
        if 'order_pay_info' in d:
            o.order_pay_info = d['order_pay_info']
        if 'order_subsidy_info' in d:
            o.order_subsidy_info = d['order_subsidy_info']
        if 'royalty_infos' in d:
            o.royalty_infos = d['royalty_infos']
        return o


