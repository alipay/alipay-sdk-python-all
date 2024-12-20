#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditInfoDTO import CreditInfoDTO
from alipay.aop.api.domain.MiniOrderDetailDTO import MiniOrderDetailDTO
from alipay.aop.api.domain.StagePayPlanDTO import StagePayPlanDTO
from alipay.aop.api.domain.SubMerchantDTO import SubMerchantDTO


class AlipayOpenAppOrderCreateModel(object):

    def __init__(self):
        self._credit_info = None
        self._merchant_biz_type = None
        self._order_detail = None
        self._out_order_id = None
        self._path = None
        self._seller_id = None
        self._service_type = None
        self._stage_pay_plans = None
        self._sub_merchant = None
        self._title = None

    @property
    def credit_info(self):
        return self._credit_info

    @credit_info.setter
    def credit_info(self, value):
        if isinstance(value, CreditInfoDTO):
            self._credit_info = value
        else:
            self._credit_info = CreditInfoDTO.from_alipay_dict(value)
    @property
    def merchant_biz_type(self):
        return self._merchant_biz_type

    @merchant_biz_type.setter
    def merchant_biz_type(self, value):
        self._merchant_biz_type = value
    @property
    def order_detail(self):
        return self._order_detail

    @order_detail.setter
    def order_detail(self, value):
        if isinstance(value, MiniOrderDetailDTO):
            self._order_detail = value
        else:
            self._order_detail = MiniOrderDetailDTO.from_alipay_dict(value)
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def stage_pay_plans(self):
        return self._stage_pay_plans

    @stage_pay_plans.setter
    def stage_pay_plans(self, value):
        if isinstance(value, StagePayPlanDTO):
            self._stage_pay_plans = value
        else:
            self._stage_pay_plans = StagePayPlanDTO.from_alipay_dict(value)
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SubMerchantDTO):
            self._sub_merchant = value
        else:
            self._sub_merchant = SubMerchantDTO.from_alipay_dict(value)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_info:
            if hasattr(self.credit_info, 'to_alipay_dict'):
                params['credit_info'] = self.credit_info.to_alipay_dict()
            else:
                params['credit_info'] = self.credit_info
        if self.merchant_biz_type:
            if hasattr(self.merchant_biz_type, 'to_alipay_dict'):
                params['merchant_biz_type'] = self.merchant_biz_type.to_alipay_dict()
            else:
                params['merchant_biz_type'] = self.merchant_biz_type
        if self.order_detail:
            if hasattr(self.order_detail, 'to_alipay_dict'):
                params['order_detail'] = self.order_detail.to_alipay_dict()
            else:
                params['order_detail'] = self.order_detail
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.stage_pay_plans:
            if hasattr(self.stage_pay_plans, 'to_alipay_dict'):
                params['stage_pay_plans'] = self.stage_pay_plans.to_alipay_dict()
            else:
                params['stage_pay_plans'] = self.stage_pay_plans
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppOrderCreateModel()
        if 'credit_info' in d:
            o.credit_info = d['credit_info']
        if 'merchant_biz_type' in d:
            o.merchant_biz_type = d['merchant_biz_type']
        if 'order_detail' in d:
            o.order_detail = d['order_detail']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'path' in d:
            o.path = d['path']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'stage_pay_plans' in d:
            o.stage_pay_plans = d['stage_pay_plans']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'title' in d:
            o.title = d['title']
        return o


