#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopInfo(object):

    def __init__(self):
        self._shop_name = None
        self._shop_scene_pic = None
        self._shop_sign_board_pic = None

    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_scene_pic(self):
        return self._shop_scene_pic

    @shop_scene_pic.setter
    def shop_scene_pic(self, value):
        if isinstance(value, list):
            self._shop_scene_pic = list()
            for i in value:
                self._shop_scene_pic.append(i)
    @property
    def shop_sign_board_pic(self):
        return self._shop_sign_board_pic

    @shop_sign_board_pic.setter
    def shop_sign_board_pic(self, value):
        self._shop_sign_board_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_scene_pic:
            if isinstance(self.shop_scene_pic, list):
                for i in range(0, len(self.shop_scene_pic)):
                    element = self.shop_scene_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_scene_pic[i] = element.to_alipay_dict()
            if hasattr(self.shop_scene_pic, 'to_alipay_dict'):
                params['shop_scene_pic'] = self.shop_scene_pic.to_alipay_dict()
            else:
                params['shop_scene_pic'] = self.shop_scene_pic
        if self.shop_sign_board_pic:
            if hasattr(self.shop_sign_board_pic, 'to_alipay_dict'):
                params['shop_sign_board_pic'] = self.shop_sign_board_pic.to_alipay_dict()
            else:
                params['shop_sign_board_pic'] = self.shop_sign_board_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopInfo()
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_scene_pic' in d:
            o.shop_scene_pic = d['shop_scene_pic']
        if 'shop_sign_board_pic' in d:
            o.shop_sign_board_pic = d['shop_sign_board_pic']
        return o


