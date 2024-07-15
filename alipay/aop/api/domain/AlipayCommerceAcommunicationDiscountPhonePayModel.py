#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationDiscountPhonePayModel(object):

    def __init__(self):
        self._client_ip = None
        self._face = None
        self._item_id = None
        self._mobile = None
        self._out_biz_no = None
        self._price = None
        self._scene = None
        self._sub_source = None

    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
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
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sub_source(self):
        return self._sub_source

    @sub_source.setter
    def sub_source(self, value):
        self._sub_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.face:
            if hasattr(self.face, 'to_alipay_dict'):
                params['face'] = self.face.to_alipay_dict()
            else:
                params['face'] = self.face
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
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
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sub_source:
            if hasattr(self.sub_source, 'to_alipay_dict'):
                params['sub_source'] = self.sub_source.to_alipay_dict()
            else:
                params['sub_source'] = self.sub_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationDiscountPhonePayModel()
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'face' in d:
            o.face = d['face']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'price' in d:
            o.price = d['price']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sub_source' in d:
            o.sub_source = d['sub_source']
        return o


