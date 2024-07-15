#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentCustomerDetail import RentCustomerDetail
from alipay.aop.api.domain.RentDeliveryDetail import RentDeliveryDetail
from alipay.aop.api.domain.RentItemDetail import RentItemDetail
from alipay.aop.api.domain.RentPriceDetail import RentPriceDetail


class AlipayCloudTraasCloudriskRentriskQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._customer_detail = None
        self._customer_id = None
        self._customer_open_id = None
        self._customer_type = None
        self._delivery_detail = None
        self._item_detail = None
        self._mobile = None
        self._out_biz_no = None
        self._price_detail = None
        self._risk_biz_scene = None
        self._source = None
        self._user_authorization = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def customer_detail(self):
        return self._customer_detail

    @customer_detail.setter
    def customer_detail(self, value):
        if isinstance(value, RentCustomerDetail):
            self._customer_detail = value
        else:
            self._customer_detail = RentCustomerDetail.from_alipay_dict(value)
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def customer_open_id(self):
        return self._customer_open_id

    @customer_open_id.setter
    def customer_open_id(self, value):
        self._customer_open_id = value
    @property
    def customer_type(self):
        return self._customer_type

    @customer_type.setter
    def customer_type(self, value):
        self._customer_type = value
    @property
    def delivery_detail(self):
        return self._delivery_detail

    @delivery_detail.setter
    def delivery_detail(self, value):
        if isinstance(value, RentDeliveryDetail):
            self._delivery_detail = value
        else:
            self._delivery_detail = RentDeliveryDetail.from_alipay_dict(value)
    @property
    def item_detail(self):
        return self._item_detail

    @item_detail.setter
    def item_detail(self, value):
        if isinstance(value, RentItemDetail):
            self._item_detail = value
        else:
            self._item_detail = RentItemDetail.from_alipay_dict(value)
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def price_detail(self):
        return self._price_detail

    @price_detail.setter
    def price_detail(self, value):
        if isinstance(value, RentPriceDetail):
            self._price_detail = value
        else:
            self._price_detail = RentPriceDetail.from_alipay_dict(value)
    @property
    def risk_biz_scene(self):
        return self._risk_biz_scene

    @risk_biz_scene.setter
    def risk_biz_scene(self, value):
        self._risk_biz_scene = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_authorization(self):
        return self._user_authorization

    @user_authorization.setter
    def user_authorization(self, value):
        self._user_authorization = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.customer_detail:
            if hasattr(self.customer_detail, 'to_alipay_dict'):
                params['customer_detail'] = self.customer_detail.to_alipay_dict()
            else:
                params['customer_detail'] = self.customer_detail
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.customer_open_id:
            if hasattr(self.customer_open_id, 'to_alipay_dict'):
                params['customer_open_id'] = self.customer_open_id.to_alipay_dict()
            else:
                params['customer_open_id'] = self.customer_open_id
        if self.customer_type:
            if hasattr(self.customer_type, 'to_alipay_dict'):
                params['customer_type'] = self.customer_type.to_alipay_dict()
            else:
                params['customer_type'] = self.customer_type
        if self.delivery_detail:
            if hasattr(self.delivery_detail, 'to_alipay_dict'):
                params['delivery_detail'] = self.delivery_detail.to_alipay_dict()
            else:
                params['delivery_detail'] = self.delivery_detail
        if self.item_detail:
            if hasattr(self.item_detail, 'to_alipay_dict'):
                params['item_detail'] = self.item_detail.to_alipay_dict()
            else:
                params['item_detail'] = self.item_detail
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.price_detail:
            if hasattr(self.price_detail, 'to_alipay_dict'):
                params['price_detail'] = self.price_detail.to_alipay_dict()
            else:
                params['price_detail'] = self.price_detail
        if self.risk_biz_scene:
            if hasattr(self.risk_biz_scene, 'to_alipay_dict'):
                params['risk_biz_scene'] = self.risk_biz_scene.to_alipay_dict()
            else:
                params['risk_biz_scene'] = self.risk_biz_scene
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_authorization:
            if hasattr(self.user_authorization, 'to_alipay_dict'):
                params['user_authorization'] = self.user_authorization.to_alipay_dict()
            else:
                params['user_authorization'] = self.user_authorization
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudTraasCloudriskRentriskQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'customer_detail' in d:
            o.customer_detail = d['customer_detail']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'customer_open_id' in d:
            o.customer_open_id = d['customer_open_id']
        if 'customer_type' in d:
            o.customer_type = d['customer_type']
        if 'delivery_detail' in d:
            o.delivery_detail = d['delivery_detail']
        if 'item_detail' in d:
            o.item_detail = d['item_detail']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'price_detail' in d:
            o.price_detail = d['price_detail']
        if 'risk_biz_scene' in d:
            o.risk_biz_scene = d['risk_biz_scene']
        if 'source' in d:
            o.source = d['source']
        if 'user_authorization' in d:
            o.user_authorization = d['user_authorization']
        return o


