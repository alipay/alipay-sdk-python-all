#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MsgOrderGoodsInfoList(object):

    def __init__(self):
        self._desc = None
        self._ext_info = None
        self._goods_id = None
        self._goods_name = None
        self._goods_pic = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_pic(self):
        return self._goods_pic

    @goods_pic.setter
    def goods_pic(self, value):
        self._goods_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_pic:
            if hasattr(self.goods_pic, 'to_alipay_dict'):
                params['goods_pic'] = self.goods_pic.to_alipay_dict()
            else:
                params['goods_pic'] = self.goods_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MsgOrderGoodsInfoList()
        if 'desc' in d:
            o.desc = d['desc']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_pic' in d:
            o.goods_pic = d['goods_pic']
        return o


