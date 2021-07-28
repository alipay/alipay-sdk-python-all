#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderExt import OrderExt
from alipay.aop.api.domain.StoreOrderGood import StoreOrderGood


class AntMerchantOrderStoreCreateModel(object):

    def __init__(self):
        self._buyer_id = None
        self._contact_phone = None
        self._ext = None
        self._goods_info_list = None
        self._invalid_time = None
        self._memo = None
        self._out_biz_no = None
        self._scene = None
        self._seller_id = None
        self._shop_id = None
        self._store_open_id = None
        self._user_name = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        if isinstance(value, list):
            self._ext = list()
            for i in value:
                if isinstance(i, OrderExt):
                    self._ext.append(i)
                else:
                    self._ext.append(OrderExt.from_alipay_dict(i))
    @property
    def goods_info_list(self):
        return self._goods_info_list

    @goods_info_list.setter
    def goods_info_list(self, value):
        if isinstance(value, list):
            self._goods_info_list = list()
            for i in value:
                if isinstance(i, StoreOrderGood):
                    self._goods_info_list.append(i)
                else:
                    self._goods_info_list.append(StoreOrderGood.from_alipay_dict(i))
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_open_id(self):
        return self._store_open_id

    @store_open_id.setter
    def store_open_id(self, value):
        self._store_open_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.ext:
            if isinstance(self.ext, list):
                for i in range(0, len(self.ext)):
                    element = self.ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext[i] = element.to_alipay_dict()
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.goods_info_list:
            if isinstance(self.goods_info_list, list):
                for i in range(0, len(self.goods_info_list)):
                    element = self.goods_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_info_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_info_list, 'to_alipay_dict'):
                params['goods_info_list'] = self.goods_info_list.to_alipay_dict()
            else:
                params['goods_info_list'] = self.goods_info_list
        if self.invalid_time:
            if hasattr(self.invalid_time, 'to_alipay_dict'):
                params['invalid_time'] = self.invalid_time.to_alipay_dict()
            else:
                params['invalid_time'] = self.invalid_time
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_open_id:
            if hasattr(self.store_open_id, 'to_alipay_dict'):
                params['store_open_id'] = self.store_open_id.to_alipay_dict()
            else:
                params['store_open_id'] = self.store_open_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantOrderStoreCreateModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'ext' in d:
            o.ext = d['ext']
        if 'goods_info_list' in d:
            o.goods_info_list = d['goods_info_list']
        if 'invalid_time' in d:
            o.invalid_time = d['invalid_time']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_open_id' in d:
            o.store_open_id = d['store_open_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


