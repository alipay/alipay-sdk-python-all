#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationMcpPhoneCreateModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._face = None
        self._final_price = None
        self._item_id = None
        self._mobile = None
        self._mobile_name = None
        self._open_id = None
        self._price = None
        self._scene = None
        self._sms_code = None
        self._source = None
        self._sub_source = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value
    @property
    def final_price(self):
        return self._final_price

    @final_price.setter
    def final_price(self, value):
        self._final_price = value
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
    def mobile_name(self):
        return self._mobile_name

    @mobile_name.setter
    def mobile_name(self, value):
        self._mobile_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_source(self):
        return self._sub_source

    @sub_source.setter
    def sub_source(self, value):
        self._sub_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.face:
            if hasattr(self.face, 'to_alipay_dict'):
                params['face'] = self.face.to_alipay_dict()
            else:
                params['face'] = self.face
        if self.final_price:
            if hasattr(self.final_price, 'to_alipay_dict'):
                params['final_price'] = self.final_price.to_alipay_dict()
            else:
                params['final_price'] = self.final_price
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
        if self.mobile_name:
            if hasattr(self.mobile_name, 'to_alipay_dict'):
                params['mobile_name'] = self.mobile_name.to_alipay_dict()
            else:
                params['mobile_name'] = self.mobile_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.sms_code:
            if hasattr(self.sms_code, 'to_alipay_dict'):
                params['sms_code'] = self.sms_code.to_alipay_dict()
            else:
                params['sms_code'] = self.sms_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayCommerceAcommunicationMcpPhoneCreateModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'face' in d:
            o.face = d['face']
        if 'final_price' in d:
            o.final_price = d['final_price']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'mobile_name' in d:
            o.mobile_name = d['mobile_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'price' in d:
            o.price = d['price']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sms_code' in d:
            o.sms_code = d['sms_code']
        if 'source' in d:
            o.source = d['source']
        if 'sub_source' in d:
            o.sub_source = d['sub_source']
        return o


