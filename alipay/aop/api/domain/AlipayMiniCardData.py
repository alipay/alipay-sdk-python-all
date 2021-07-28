#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMiniCardData(object):

    def __init__(self):
        self._action_link = None
        self._action_text = None
        self._app_name = None
        self._biz_code = None
        self._card_type = None
        self._coupon_pic = None
        self._edit_text = None
        self._item_pic = None
        self._main_text = None
        self._sub_text = None

    @property
    def action_link(self):
        return self._action_link

    @action_link.setter
    def action_link(self, value):
        self._action_link = value
    @property
    def action_text(self):
        return self._action_text

    @action_text.setter
    def action_text(self, value):
        self._action_text = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def coupon_pic(self):
        return self._coupon_pic

    @coupon_pic.setter
    def coupon_pic(self, value):
        self._coupon_pic = value
    @property
    def edit_text(self):
        return self._edit_text

    @edit_text.setter
    def edit_text(self, value):
        self._edit_text = value
    @property
    def item_pic(self):
        return self._item_pic

    @item_pic.setter
    def item_pic(self, value):
        self._item_pic = value
    @property
    def main_text(self):
        return self._main_text

    @main_text.setter
    def main_text(self, value):
        self._main_text = value
    @property
    def sub_text(self):
        return self._sub_text

    @sub_text.setter
    def sub_text(self, value):
        self._sub_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_link:
            if hasattr(self.action_link, 'to_alipay_dict'):
                params['action_link'] = self.action_link.to_alipay_dict()
            else:
                params['action_link'] = self.action_link
        if self.action_text:
            if hasattr(self.action_text, 'to_alipay_dict'):
                params['action_text'] = self.action_text.to_alipay_dict()
            else:
                params['action_text'] = self.action_text
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.coupon_pic:
            if hasattr(self.coupon_pic, 'to_alipay_dict'):
                params['coupon_pic'] = self.coupon_pic.to_alipay_dict()
            else:
                params['coupon_pic'] = self.coupon_pic
        if self.edit_text:
            if hasattr(self.edit_text, 'to_alipay_dict'):
                params['edit_text'] = self.edit_text.to_alipay_dict()
            else:
                params['edit_text'] = self.edit_text
        if self.item_pic:
            if hasattr(self.item_pic, 'to_alipay_dict'):
                params['item_pic'] = self.item_pic.to_alipay_dict()
            else:
                params['item_pic'] = self.item_pic
        if self.main_text:
            if hasattr(self.main_text, 'to_alipay_dict'):
                params['main_text'] = self.main_text.to_alipay_dict()
            else:
                params['main_text'] = self.main_text
        if self.sub_text:
            if hasattr(self.sub_text, 'to_alipay_dict'):
                params['sub_text'] = self.sub_text.to_alipay_dict()
            else:
                params['sub_text'] = self.sub_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMiniCardData()
        if 'action_link' in d:
            o.action_link = d['action_link']
        if 'action_text' in d:
            o.action_text = d['action_text']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'coupon_pic' in d:
            o.coupon_pic = d['coupon_pic']
        if 'edit_text' in d:
            o.edit_text = d['edit_text']
        if 'item_pic' in d:
            o.item_pic = d['item_pic']
        if 'main_text' in d:
            o.main_text = d['main_text']
        if 'sub_text' in d:
            o.sub_text = d['sub_text']
        return o


