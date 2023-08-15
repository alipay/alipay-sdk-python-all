#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniRefundCertificateDTO import MiniRefundCertificateDTO


class MiniRefundGoodsInfoDTO(object):

    def __init__(self):
        self._certificate_info = None
        self._goods_id = None
        self._out_item_id = None
        self._out_sku_id = None
        self._refund_amount = None

    @property
    def certificate_info(self):
        return self._certificate_info

    @certificate_info.setter
    def certificate_info(self, value):
        if isinstance(value, MiniRefundCertificateDTO):
            self._certificate_info = value
        else:
            self._certificate_info = MiniRefundCertificateDTO.from_alipay_dict(value)
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_info:
            if hasattr(self.certificate_info, 'to_alipay_dict'):
                params['certificate_info'] = self.certificate_info.to_alipay_dict()
            else:
                params['certificate_info'] = self.certificate_info
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniRefundGoodsInfoDTO()
        if 'certificate_info' in d:
            o.certificate_info = d['certificate_info']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        return o


