#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayItemAuditRule import AlipayItemAuditRule
from alipay.aop.api.domain.AlipayItemDescription import AlipayItemDescription
from alipay.aop.api.domain.AlipayItemOperationContext import AlipayItemOperationContext
from alipay.aop.api.domain.AlipayItemSalesRule import AlipayItemSalesRule
from alipay.aop.api.domain.AlipayItemVoucherTemplete import AlipayItemVoucherTemplete


class AlipayOfflineMarketItemCreateModel(object):

    def __init__(self):
        self._audit_rule = None
        self._cover = None
        self._descriptions = None
        self._gmt_end = None
        self._gmt_start = None
        self._inventory = None
        self._is_auto_expanded = None
        self._item_type = None
        self._operate_notify_url = None
        self._operation_context = None
        self._purchase_mode = None
        self._request_id = None
        self._sales_rule = None
        self._shop_list = None
        self._subject = None
        self._voucher_templete = None
        self._weight = None

    @property
    def audit_rule(self):
        return self._audit_rule

    @audit_rule.setter
    def audit_rule(self, value):
        if isinstance(value, AlipayItemAuditRule):
            self._audit_rule = value
        else:
            self._audit_rule = AlipayItemAuditRule.from_alipay_dict(value)
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
                if isinstance(i, AlipayItemDescription):
                    self._descriptions.append(i)
                else:
                    self._descriptions.append(AlipayItemDescription.from_alipay_dict(i))
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
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def operate_notify_url(self):
        return self._operate_notify_url

    @operate_notify_url.setter
    def operate_notify_url(self, value):
        self._operate_notify_url = value
    @property
    def operation_context(self):
        return self._operation_context

    @operation_context.setter
    def operation_context(self, value):
        if isinstance(value, AlipayItemOperationContext):
            self._operation_context = value
        else:
            self._operation_context = AlipayItemOperationContext.from_alipay_dict(value)
    @property
    def purchase_mode(self):
        return self._purchase_mode

    @purchase_mode.setter
    def purchase_mode(self, value):
        self._purchase_mode = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sales_rule(self):
        return self._sales_rule

    @sales_rule.setter
    def sales_rule(self, value):
        if isinstance(value, AlipayItemSalesRule):
            self._sales_rule = value
        else:
            self._sales_rule = AlipayItemSalesRule.from_alipay_dict(value)
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        self._shop_list = value
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
        if isinstance(value, AlipayItemVoucherTemplete):
            self._voucher_templete = value
        else:
            self._voucher_templete = AlipayItemVoucherTemplete.from_alipay_dict(value)
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_rule:
            if hasattr(self.audit_rule, 'to_alipay_dict'):
                params['audit_rule'] = self.audit_rule.to_alipay_dict()
            else:
                params['audit_rule'] = self.audit_rule
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.descriptions:
            if isinstance(self.descriptions, list):
                for i in range(0, len(self.descriptions)):
                    element = self.descriptions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.descriptions[i] = element.to_alipay_dict()
            if hasattr(self.descriptions, 'to_alipay_dict'):
                params['descriptions'] = self.descriptions.to_alipay_dict()
            else:
                params['descriptions'] = self.descriptions
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.is_auto_expanded:
            if hasattr(self.is_auto_expanded, 'to_alipay_dict'):
                params['is_auto_expanded'] = self.is_auto_expanded.to_alipay_dict()
            else:
                params['is_auto_expanded'] = self.is_auto_expanded
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.operate_notify_url:
            if hasattr(self.operate_notify_url, 'to_alipay_dict'):
                params['operate_notify_url'] = self.operate_notify_url.to_alipay_dict()
            else:
                params['operate_notify_url'] = self.operate_notify_url
        if self.operation_context:
            if hasattr(self.operation_context, 'to_alipay_dict'):
                params['operation_context'] = self.operation_context.to_alipay_dict()
            else:
                params['operation_context'] = self.operation_context
        if self.purchase_mode:
            if hasattr(self.purchase_mode, 'to_alipay_dict'):
                params['purchase_mode'] = self.purchase_mode.to_alipay_dict()
            else:
                params['purchase_mode'] = self.purchase_mode
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sales_rule:
            if hasattr(self.sales_rule, 'to_alipay_dict'):
                params['sales_rule'] = self.sales_rule.to_alipay_dict()
            else:
                params['sales_rule'] = self.sales_rule
        if self.shop_list:
            if hasattr(self.shop_list, 'to_alipay_dict'):
                params['shop_list'] = self.shop_list.to_alipay_dict()
            else:
                params['shop_list'] = self.shop_list
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.voucher_templete:
            if hasattr(self.voucher_templete, 'to_alipay_dict'):
                params['voucher_templete'] = self.voucher_templete.to_alipay_dict()
            else:
                params['voucher_templete'] = self.voucher_templete
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketItemCreateModel()
        if 'audit_rule' in d:
            o.audit_rule = d['audit_rule']
        if 'cover' in d:
            o.cover = d['cover']
        if 'descriptions' in d:
            o.descriptions = d['descriptions']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'is_auto_expanded' in d:
            o.is_auto_expanded = d['is_auto_expanded']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'operate_notify_url' in d:
            o.operate_notify_url = d['operate_notify_url']
        if 'operation_context' in d:
            o.operation_context = d['operation_context']
        if 'purchase_mode' in d:
            o.purchase_mode = d['purchase_mode']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sales_rule' in d:
            o.sales_rule = d['sales_rule']
        if 'shop_list' in d:
            o.shop_list = d['shop_list']
        if 'subject' in d:
            o.subject = d['subject']
        if 'voucher_templete' in d:
            o.voucher_templete = d['voucher_templete']
        if 'weight' in d:
            o.weight = d['weight']
        return o


