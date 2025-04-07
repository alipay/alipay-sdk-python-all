#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandEcoOrderCreateModel(object):

    def __init__(self):
        self._busi_platform = None
        self._eco_code = None
        self._express_no = None
        self._order_status = None
        self._order_time = None
        self._out_order_id = None
        self._qrcode_imgs = None
        self._qrcode_tokens = None
        self._receive_time = None
        self._send_time = None
        self._shop_code = None
        self._tag_ids = None

    @property
    def busi_platform(self):
        return self._busi_platform

    @busi_platform.setter
    def busi_platform(self, value):
        self._busi_platform = value
    @property
    def eco_code(self):
        return self._eco_code

    @eco_code.setter
    def eco_code(self, value):
        self._eco_code = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def qrcode_imgs(self):
        return self._qrcode_imgs

    @qrcode_imgs.setter
    def qrcode_imgs(self, value):
        if isinstance(value, list):
            self._qrcode_imgs = list()
            for i in value:
                self._qrcode_imgs.append(i)
    @property
    def qrcode_tokens(self):
        return self._qrcode_tokens

    @qrcode_tokens.setter
    def qrcode_tokens(self, value):
        if isinstance(value, list):
            self._qrcode_tokens = list()
            for i in value:
                self._qrcode_tokens.append(i)
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value
    @property
    def tag_ids(self):
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, value):
        if isinstance(value, list):
            self._tag_ids = list()
            for i in value:
                self._tag_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.busi_platform:
            if hasattr(self.busi_platform, 'to_alipay_dict'):
                params['busi_platform'] = self.busi_platform.to_alipay_dict()
            else:
                params['busi_platform'] = self.busi_platform
        if self.eco_code:
            if hasattr(self.eco_code, 'to_alipay_dict'):
                params['eco_code'] = self.eco_code.to_alipay_dict()
            else:
                params['eco_code'] = self.eco_code
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.qrcode_imgs:
            if isinstance(self.qrcode_imgs, list):
                for i in range(0, len(self.qrcode_imgs)):
                    element = self.qrcode_imgs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qrcode_imgs[i] = element.to_alipay_dict()
            if hasattr(self.qrcode_imgs, 'to_alipay_dict'):
                params['qrcode_imgs'] = self.qrcode_imgs.to_alipay_dict()
            else:
                params['qrcode_imgs'] = self.qrcode_imgs
        if self.qrcode_tokens:
            if isinstance(self.qrcode_tokens, list):
                for i in range(0, len(self.qrcode_tokens)):
                    element = self.qrcode_tokens[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qrcode_tokens[i] = element.to_alipay_dict()
            if hasattr(self.qrcode_tokens, 'to_alipay_dict'):
                params['qrcode_tokens'] = self.qrcode_tokens.to_alipay_dict()
            else:
                params['qrcode_tokens'] = self.qrcode_tokens
        if self.receive_time:
            if hasattr(self.receive_time, 'to_alipay_dict'):
                params['receive_time'] = self.receive_time.to_alipay_dict()
            else:
                params['receive_time'] = self.receive_time
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        if self.tag_ids:
            if isinstance(self.tag_ids, list):
                for i in range(0, len(self.tag_ids)):
                    element = self.tag_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_ids[i] = element.to_alipay_dict()
            if hasattr(self.tag_ids, 'to_alipay_dict'):
                params['tag_ids'] = self.tag_ids.to_alipay_dict()
            else:
                params['tag_ids'] = self.tag_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandEcoOrderCreateModel()
        if 'busi_platform' in d:
            o.busi_platform = d['busi_platform']
        if 'eco_code' in d:
            o.eco_code = d['eco_code']
        if 'express_no' in d:
            o.express_no = d['express_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'qrcode_imgs' in d:
            o.qrcode_imgs = d['qrcode_imgs']
        if 'qrcode_tokens' in d:
            o.qrcode_tokens = d['qrcode_tokens']
        if 'receive_time' in d:
            o.receive_time = d['receive_time']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        if 'tag_ids' in d:
            o.tag_ids = d['tag_ids']
        return o


