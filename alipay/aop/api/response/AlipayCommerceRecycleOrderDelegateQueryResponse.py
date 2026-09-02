#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleOrderBenefitVO import RecycleOrderBenefitVO
from alipay.aop.api.domain.RecycleStdOrderBaseVO import RecycleStdOrderBaseVO
from alipay.aop.api.domain.RecycleDeliveryVO import RecycleDeliveryVO
from alipay.aop.api.domain.RecycleOrderFundAllVO import RecycleOrderFundAllVO
from alipay.aop.api.domain.RecycleStdOrderFundSubSidyVO import RecycleStdOrderFundSubSidyVO
from alipay.aop.api.domain.RecycleStdOrderMerchantInfoVO import RecycleStdOrderMerchantInfoVO
from alipay.aop.api.domain.RecycleDeliveryVO import RecycleDeliveryVO
from alipay.aop.api.domain.RecycleDeliveryVO import RecycleDeliveryVO
from alipay.aop.api.domain.RecycleOrderTagInfoVO import RecycleOrderTagInfoVO
from alipay.aop.api.domain.RecycleOrderRelationVO import RecycleOrderRelationVO


class AlipayCommerceRecycleOrderDelegateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrderDelegateQueryResponse, self).__init__()
        self._benefits = None
        self._order_base = None
        self._order_delivery = None
        self._order_fund_all = None
        self._order_fund_subsidy = None
        self._order_merchant = None
        self._order_merchant_delivery = None
        self._order_sendback = None
        self._order_tags = None
        self._relation_infos = None

    @property
    def benefits(self):
        return self._benefits

    @benefits.setter
    def benefits(self, value):
        if isinstance(value, list):
            self._benefits = list()
            for i in value:
                if isinstance(i, RecycleOrderBenefitVO):
                    self._benefits.append(i)
                else:
                    self._benefits.append(RecycleOrderBenefitVO.from_alipay_dict(i))
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
    def order_fund_all(self):
        return self._order_fund_all

    @order_fund_all.setter
    def order_fund_all(self, value):
        if isinstance(value, RecycleOrderFundAllVO):
            self._order_fund_all = value
        else:
            self._order_fund_all = RecycleOrderFundAllVO.from_alipay_dict(value)
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
    def order_merchant_delivery(self):
        return self._order_merchant_delivery

    @order_merchant_delivery.setter
    def order_merchant_delivery(self, value):
        if isinstance(value, RecycleDeliveryVO):
            self._order_merchant_delivery = value
        else:
            self._order_merchant_delivery = RecycleDeliveryVO.from_alipay_dict(value)
    @property
    def order_sendback(self):
        return self._order_sendback

    @order_sendback.setter
    def order_sendback(self, value):
        if isinstance(value, RecycleDeliveryVO):
            self._order_sendback = value
        else:
            self._order_sendback = RecycleDeliveryVO.from_alipay_dict(value)
    @property
    def order_tags(self):
        return self._order_tags

    @order_tags.setter
    def order_tags(self, value):
        if isinstance(value, list):
            self._order_tags = list()
            for i in value:
                if isinstance(i, RecycleOrderTagInfoVO):
                    self._order_tags.append(i)
                else:
                    self._order_tags.append(RecycleOrderTagInfoVO.from_alipay_dict(i))
    @property
    def relation_infos(self):
        return self._relation_infos

    @relation_infos.setter
    def relation_infos(self, value):
        if isinstance(value, list):
            self._relation_infos = list()
            for i in value:
                if isinstance(i, RecycleOrderRelationVO):
                    self._relation_infos.append(i)
                else:
                    self._relation_infos.append(RecycleOrderRelationVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrderDelegateQueryResponse, self).parse_response_content(response_content)
        if 'benefits' in response:
            self.benefits = response['benefits']
        if 'order_base' in response:
            self.order_base = response['order_base']
        if 'order_delivery' in response:
            self.order_delivery = response['order_delivery']
        if 'order_fund_all' in response:
            self.order_fund_all = response['order_fund_all']
        if 'order_fund_subsidy' in response:
            self.order_fund_subsidy = response['order_fund_subsidy']
        if 'order_merchant' in response:
            self.order_merchant = response['order_merchant']
        if 'order_merchant_delivery' in response:
            self.order_merchant_delivery = response['order_merchant_delivery']
        if 'order_sendback' in response:
            self.order_sendback = response['order_sendback']
        if 'order_tags' in response:
            self.order_tags = response['order_tags']
        if 'relation_infos' in response:
            self.relation_infos = response['relation_infos']
