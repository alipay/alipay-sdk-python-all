#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundSettleInfo import FundSettleInfo


class AlipayCommerceOperationTimescardProductApplyModel(object):

    def __init__(self):
        self._biz_from = None
        self._isv_partner_id = None
        self._out_biz_no = None
        self._partner_id = None
        self._product_code = None
        self._scene_code = None
        self._settle_info = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def isv_partner_id(self):
        return self._isv_partner_id

    @isv_partner_id.setter
    def isv_partner_id(self, value):
        self._isv_partner_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, FundSettleInfo):
            self._settle_info = value
        else:
            self._settle_info = FundSettleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.isv_partner_id:
            if hasattr(self.isv_partner_id, 'to_alipay_dict'):
                params['isv_partner_id'] = self.isv_partner_id.to_alipay_dict()
            else:
                params['isv_partner_id'] = self.isv_partner_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationTimescardProductApplyModel()
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'isv_partner_id' in d:
            o.isv_partner_id = d['isv_partner_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        return o


