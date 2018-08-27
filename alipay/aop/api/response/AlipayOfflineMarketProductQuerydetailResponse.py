#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayDataItemDescription import AlipayDataItemDescription
from alipay.aop.api.domain.AlipayDataItemSalesRule import AlipayDataItemSalesRule
from alipay.aop.api.domain.AlipayDataItemVoucherTemplete import AlipayDataItemVoucherTemplete


class AlipayOfflineMarketProductQuerydetailResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketProductQuerydetailResponse, self).__init__()
        self._cover = None
        self._descriptions = None
        self._gmt_end = None
        self._gmt_start = None
        self._inventory = None
        self._is_auto_expanded = None
        self._item_status = None
        self._item_type = None
        self._pic_coll = None
        self._purchase_mode = None
        self._sales_rule = None
        self._shop_list = None
        self._subject = None
        self._voucher_templete = None
        self._weight = None

    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def descriptions(self):
        return self._descriptions

    @descriptions.setter
    def descriptions(self, value):
        if isinstance(value, list):
            self._descriptions = list()
            for i in value:
                if isinstance(i, AlipayDataItemDescription):
                    self._descriptions.append(i)
                else:
                    self._descriptions.append(AlipayDataItemDescription.from_alipay_dict(i))
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def is_auto_expanded(self):
        return self._is_auto_expanded

    @is_auto_expanded.setter
    def is_auto_expanded(self, value):
        self._is_auto_expanded = value
    @property
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def pic_coll(self):
        return self._pic_coll

    @pic_coll.setter
    def pic_coll(self, value):
        self._pic_coll = value
    @property
    def purchase_mode(self):
        return self._purchase_mode

    @purchase_mode.setter
    def purchase_mode(self, value):
        self._purchase_mode = value
    @property
    def sales_rule(self):
        return self._sales_rule

    @sales_rule.setter
    def sales_rule(self, value):
        if isinstance(value, AlipayDataItemSalesRule):
            self._sales_rule = value
        else:
            self._sales_rule = AlipayDataItemSalesRule.from_alipay_dict(value)
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                self._shop_list.append(i)
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def voucher_templete(self):
        return self._voucher_templete

    @voucher_templete.setter
    def voucher_templete(self, value):
        if isinstance(value, AlipayDataItemVoucherTemplete):
            self._voucher_templete = value
        else:
            self._voucher_templete = AlipayDataItemVoucherTemplete.from_alipay_dict(value)
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketProductQuerydetailResponse, self).parse_response_content(response_content)
        if 'cover' in response:
            self.cover = response['cover']
        if 'descriptions' in response:
            self.descriptions = response['descriptions']
        if 'gmt_end' in response:
            self.gmt_end = response['gmt_end']
        if 'gmt_start' in response:
            self.gmt_start = response['gmt_start']
        if 'inventory' in response:
            self.inventory = response['inventory']
        if 'is_auto_expanded' in response:
            self.is_auto_expanded = response['is_auto_expanded']
        if 'item_status' in response:
            self.item_status = response['item_status']
        if 'item_type' in response:
            self.item_type = response['item_type']
        if 'pic_coll' in response:
            self.pic_coll = response['pic_coll']
        if 'purchase_mode' in response:
            self.purchase_mode = response['purchase_mode']
        if 'sales_rule' in response:
            self.sales_rule = response['sales_rule']
        if 'shop_list' in response:
            self.shop_list = response['shop_list']
        if 'subject' in response:
            self.subject = response['subject']
        if 'voucher_templete' in response:
            self.voucher_templete = response['voucher_templete']
        if 'weight' in response:
            self.weight = response['weight']
