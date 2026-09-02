#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExternalItemPic import ExternalItemPic
from alipay.aop.api.domain.ExternalItemPropery import ExternalItemPropery
from alipay.aop.api.domain.ExternalSaleRule import ExternalSaleRule
from alipay.aop.api.domain.ExternalSKU import ExternalSKU


class AlipayInsSceneInshealthserviceprodMallitemModifyModel(object):

    def __init__(self):
        self._item_name = None
        self._label_id_list = None
        self._pic_list = None
        self._property_list = None
        self._sale_rule_list = None
        self._ser_prod_no = None
        self._sku_list = None
        self._source_product_id = None

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def label_id_list(self):
        return self._label_id_list

    @label_id_list.setter
    def label_id_list(self, value):
        if isinstance(value, list):
            self._label_id_list = list()
            for i in value:
                self._label_id_list.append(i)
    @property
    def pic_list(self):
        return self._pic_list

    @pic_list.setter
    def pic_list(self, value):
        if isinstance(value, list):
            self._pic_list = list()
            for i in value:
                if isinstance(i, ExternalItemPic):
                    self._pic_list.append(i)
                else:
                    self._pic_list.append(ExternalItemPic.from_alipay_dict(i))
    @property
    def property_list(self):
        return self._property_list

    @property_list.setter
    def property_list(self, value):
        if isinstance(value, list):
            self._property_list = list()
            for i in value:
                if isinstance(i, ExternalItemPropery):
                    self._property_list.append(i)
                else:
                    self._property_list.append(ExternalItemPropery.from_alipay_dict(i))
    @property
    def sale_rule_list(self):
        return self._sale_rule_list

    @sale_rule_list.setter
    def sale_rule_list(self, value):
        if isinstance(value, list):
            self._sale_rule_list = list()
            for i in value:
                if isinstance(i, ExternalSaleRule):
                    self._sale_rule_list.append(i)
                else:
                    self._sale_rule_list.append(ExternalSaleRule.from_alipay_dict(i))
    @property
    def ser_prod_no(self):
        return self._ser_prod_no

    @ser_prod_no.setter
    def ser_prod_no(self, value):
        self._ser_prod_no = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, ExternalSKU):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(ExternalSKU.from_alipay_dict(i))
    @property
    def source_product_id(self):
        return self._source_product_id

    @source_product_id.setter
    def source_product_id(self, value):
        self._source_product_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.label_id_list:
            if isinstance(self.label_id_list, list):
                for i in range(0, len(self.label_id_list)):
                    element = self.label_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_id_list[i] = element.to_alipay_dict()
            if hasattr(self.label_id_list, 'to_alipay_dict'):
                params['label_id_list'] = self.label_id_list.to_alipay_dict()
            else:
                params['label_id_list'] = self.label_id_list
        if self.pic_list:
            if isinstance(self.pic_list, list):
                for i in range(0, len(self.pic_list)):
                    element = self.pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pic_list[i] = element.to_alipay_dict()
            if hasattr(self.pic_list, 'to_alipay_dict'):
                params['pic_list'] = self.pic_list.to_alipay_dict()
            else:
                params['pic_list'] = self.pic_list
        if self.property_list:
            if isinstance(self.property_list, list):
                for i in range(0, len(self.property_list)):
                    element = self.property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_list[i] = element.to_alipay_dict()
            if hasattr(self.property_list, 'to_alipay_dict'):
                params['property_list'] = self.property_list.to_alipay_dict()
            else:
                params['property_list'] = self.property_list
        if self.sale_rule_list:
            if isinstance(self.sale_rule_list, list):
                for i in range(0, len(self.sale_rule_list)):
                    element = self.sale_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sale_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.sale_rule_list, 'to_alipay_dict'):
                params['sale_rule_list'] = self.sale_rule_list.to_alipay_dict()
            else:
                params['sale_rule_list'] = self.sale_rule_list
        if self.ser_prod_no:
            if hasattr(self.ser_prod_no, 'to_alipay_dict'):
                params['ser_prod_no'] = self.ser_prod_no.to_alipay_dict()
            else:
                params['ser_prod_no'] = self.ser_prod_no
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        if self.source_product_id:
            if hasattr(self.source_product_id, 'to_alipay_dict'):
                params['source_product_id'] = self.source_product_id.to_alipay_dict()
            else:
                params['source_product_id'] = self.source_product_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInshealthserviceprodMallitemModifyModel()
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'label_id_list' in d:
            o.label_id_list = d['label_id_list']
        if 'pic_list' in d:
            o.pic_list = d['pic_list']
        if 'property_list' in d:
            o.property_list = d['property_list']
        if 'sale_rule_list' in d:
            o.sale_rule_list = d['sale_rule_list']
        if 'ser_prod_no' in d:
            o.ser_prod_no = d['ser_prod_no']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'source_product_id' in d:
            o.source_product_id = d['source_product_id']
        return o


