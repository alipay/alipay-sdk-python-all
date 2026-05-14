#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AftersaleCertificateInfo import AftersaleCertificateInfo


class AftersaleItemInfo(object):

    def __init__(self):
        self._certificate_vo_list = None
        self._item_cnt = None
        self._out_item_id = None
        self._out_sku_id = None

    @property
    def certificate_vo_list(self):
        return self._certificate_vo_list

    @certificate_vo_list.setter
    def certificate_vo_list(self, value):
        if isinstance(value, list):
            self._certificate_vo_list = list()
            for i in value:
                if isinstance(i, AftersaleCertificateInfo):
                    self._certificate_vo_list.append(i)
                else:
                    self._certificate_vo_list.append(AftersaleCertificateInfo.from_alipay_dict(i))
    @property
    def item_cnt(self):
        return self._item_cnt

    @item_cnt.setter
    def item_cnt(self, value):
        self._item_cnt = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_vo_list:
            if isinstance(self.certificate_vo_list, list):
                for i in range(0, len(self.certificate_vo_list)):
                    element = self.certificate_vo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_vo_list[i] = element.to_alipay_dict()
            if hasattr(self.certificate_vo_list, 'to_alipay_dict'):
                params['certificate_vo_list'] = self.certificate_vo_list.to_alipay_dict()
            else:
                params['certificate_vo_list'] = self.certificate_vo_list
        if self.item_cnt:
            if hasattr(self.item_cnt, 'to_alipay_dict'):
                params['item_cnt'] = self.item_cnt.to_alipay_dict()
            else:
                params['item_cnt'] = self.item_cnt
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftersaleItemInfo()
        if 'certificate_vo_list' in d:
            o.certificate_vo_list = d['certificate_vo_list']
        if 'item_cnt' in d:
            o.item_cnt = d['item_cnt']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        return o


