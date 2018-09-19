#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsGoodsQueryModel(object):

    def __init__(self):
        self._biz_status = None
        self._category_id = None
        self._goods_code = None
        self._goods_name = None
        self._operate_context = None
        self._page_no = None
        self._page_size = None
        self._producer_id = None
        self._supplier_id = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def operate_context(self):
        return self._operate_context

    @operate_context.setter
    def operate_context(self, value):
        if isinstance(value, OperateContext):
            self._operate_context = value
        else:
            self._operate_context = OperateContext.from_alipay_dict(value)
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def producer_id(self):
        return self._producer_id

    @producer_id.setter
    def producer_id(self, value):
        self._producer_id = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.goods_code:
            if hasattr(self.goods_code, 'to_alipay_dict'):
                params['goods_code'] = self.goods_code.to_alipay_dict()
            else:
                params['goods_code'] = self.goods_code
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.producer_id:
            if hasattr(self.producer_id, 'to_alipay_dict'):
                params['producer_id'] = self.producer_id.to_alipay_dict()
            else:
                params['producer_id'] = self.producer_id
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsGoodsQueryModel()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'producer_id' in d:
            o.producer_id = d['producer_id']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


